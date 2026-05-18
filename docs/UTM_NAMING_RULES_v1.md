# Bivision – UTM Naming Rules v1

## Purpose
UTM parameters track all campaign traffic in GA4 and Looker Studio. Every paid ad or email link must be tagged.

## Required Parameters

### utm_source
| Value | Channel |
|-------|---------|
| `facebook` | Facebook Ads |
| `instagram` | Instagram Ads |
| `linkedin` | LinkedIn Ads |
| `google` | Google Search Ads |
| `email` | Email campaigns |
| `organic` | Organic / referral |

### utm_medium
| Value | Type |
|-------|------|
| `paid_social` | FB / IG / LinkedIn Ads |
| `paid_search` | Google Search |
| `email` | Email traffic |
| `organic` | Organic / referral |

### utm_campaign — Format: `product-objective-audience-period`
- **product:** bifinance, biretail, bistock, bidebitors, biaudit, bimedical
- **objective:** demo, traffic, content, retarget
- **audience:** fd_directors, owners_smb, cfo_hospitals, ...
- **period:** 2025q1, 2025q2, 2025-03

Examples: `bifinance-demo-fd_directors-2025q1` / `biretail-demo-owners_smb-2025q2`

### utm_content (optional) — Format: `placement-asset-message-version`
- **placement:** feed, story, inbox, ln_sponsored
- **asset:** image, video, carousel
- **message:** excel_vs_results, cashflow_pain, ...
- **version:** v1, v2

## Examples

**Facebook – BiFinance demo:**
```
https://bivision.ge/saas-products/bifinance/?utm_source=facebook&utm_medium=paid_social&utm_campaign=bifinance-demo-fd_directors-2025q1&utm_content=feed-image-excel_vs_results-v1
```

**LinkedIn – BiRetail demo:**
```
https://bivision.ge/saas-products/biretail/?utm_source=linkedin&utm_medium=paid_social&utm_campaign=biretail-demo-owners_smb-2025q2&utm_content=ln_sponsored-video-inventory_control-v1
```

**Email – BiFinance newsletter:**
```
https://bivision.ge/saas-products/bifinance/?utm_source=email&utm_medium=email&utm_campaign=bifinance-demo-newsletter_clients-2025-03&utm_content=cta-button-main-v1
```

## Internal Rule
Before ANY new FB / IG / LinkedIn / Email campaign: build URL with these UTM rules.
- `utm_source` + `utm_medium` = always lowercase, no spaces, exact values above
- New month/quarter on ongoing campaign = update `period` only
