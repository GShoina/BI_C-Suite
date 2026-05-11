"""
Meta Ads Creative Creator — Bivision UTM Integration
Meta Marketing API v22.0

UTM schema (url_tags field, creative-level only):
  utm_source=facebook
  &utm_medium=paid_social
  &utm_campaign={{campaign.name}}
  &utm_content={{ad.name}}
  &utm_term={{adset.name}}
  &utm_id={{campaign.id}}

Rules enforced:
  1. url_tags set ONLY at creative creation — existing creatives immutable in v22
  2. Meta dynamic placeholders only — no hardcoded campaign names
  3. Calendly-direct ads: url_tags handles UTM append (Meta appends to ANY destination URL,
     including Calendly). Do NOT embed {{placeholders}} in link URL — Meta only resolves them
     in url_tags, not in link_data.link. Embedding causes literal "{{campaign.name}}" in analytics.
  4. account-level / adset-level url_tags = phantom fields — NOT used
"""

import json
import os

import requests

API_VERSION = "v22.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"

CALENDLY_BASE = "https://calendly.com/bivision/courtest-meeting"

UTM_TAGS = (
    "utm_source=facebook"
    "&utm_medium=paid_social"
    "&utm_campaign={{campaign.name}}"
    "&utm_content={{ad.name}}"
    "&utm_term={{adset.name}}"
    "&utm_id={{campaign.id}}"
)


def _credentials() -> tuple[str, str]:
    token = os.environ.get("META_ACCESS_TOKEN")
    account = os.environ.get("META_AD_ACCOUNT_ID")  # format: act_XXXXXXXXX
    if not token:
        raise EnvironmentError("META_ACCESS_TOKEN not set")
    if not account:
        raise EnvironmentError("META_AD_ACCOUNT_ID not set")
    return token, account


def create_creative(name: str, object_story_spec: dict) -> dict:
    """
    Create a new Meta ad creative with UTM url_tags injected.

    Works for ALL destination types (bivision.ge, Calendly, etc.) — url_tags is appended
    by Meta to the final click URL at serve time, regardless of destination domain.

    Args:
        name:              Creative name (resolves as {{ad.name}} in UTM params)
        object_story_spec: Meta API object_story_spec dict (must include page_id)

    Returns:
        API response dict containing 'id' of the new creative
    """
    token, account = _credentials()

    resp = requests.post(
        f"{BASE_URL}/{account}/adcreatives",
        params={"access_token": token},
        data={
            "name": name,
            "object_story_spec": json.dumps(object_story_spec),
            "url_tags": UTM_TAGS,
        },
        timeout=30,
    )

    if not resp.ok:
        raise RuntimeError(f"Meta API {resp.status_code}: {resp.text}")

    return resp.json()


def verify_creative_utm(creative_id: str) -> dict:
    """Fetch creative and confirm url_tags field is set correctly."""
    token, _ = _credentials()
    resp = requests.get(
        f"{BASE_URL}/{creative_id}",
        params={
            "fields": "id,name,url_tags,object_story_spec",
            "access_token": token,
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("url_tags") != UTM_TAGS:
        raise AssertionError(
            f"url_tags mismatch on creative {creative_id}:\n"
            f"  expected: {UTM_TAGS}\n"
            f"  got:      {data.get('url_tags')}"
        )
    return data


# ---------------------------------------------------------------------------
# Usage
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    PAGE_ID = "YOUR_PAGE_ID"

    # Standard creative — link to bivision.ge
    r1 = create_creative(
        name="Bivision_PowerBI_May_Desktop_v1",
        object_story_spec={
            "page_id": PAGE_ID,
            "link_data": {
                "link": "https://bivision.ge/",
                "message": "Power BI dashboard — 3 კვირაში. ₾0 სალიცენზიო გადასახადი.",
                "image_hash": "YOUR_IMAGE_HASH",
                "call_to_action": {"type": "LEARN_MORE"},
            },
        },
    )
    print("Standard creative:", json.dumps(r1, indent=2))
    verify_creative_utm(r1["id"])

    # Calendly-direct creative — same API call, url_tags appends UTM to Calendly URL
    r2 = create_creative(
        name="Bivision_Demo_Calendly_May_v1",
        object_story_spec={
            "page_id": PAGE_ID,
            "link_data": {
                "link": CALENDLY_BASE,
                "message": "უფასო 30-წუთიანი კონსულტაცია — Bivision BI-ზე.",
                "image_hash": "YOUR_IMAGE_HASH",
                "call_to_action": {"type": "SIGN_UP"},
            },
        },
    )
    print("Calendly creative:", json.dumps(r2, indent=2))
    verify_creative_utm(r2["id"])
    print("Both UTMs verified ✓")
