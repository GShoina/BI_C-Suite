---
class: URGENT
from: mentari
to: victor
type: TECHNICAL CHALLENGE — mobile dashboard comments
created: 2026-04-09
attempts: 5 (all failed)
---

# მობილურიდან dashboard-ზე კომენტარი — ვერ მოვაგვარე

## პრობლემა

ოუნერი dashboard-ს ტელეფონიდან ხსნის (GitHub Pages). ყოველ output-ზე 💬 კომენტარის ველი არის. ოუნერს უნდა:
- კონკრეტულ output-ზე კომენტარი დაწეროს
- მენცარმა წაიკითხოს

## რაც ვცადე და არ იმუშავა

1. **localStorage** — მობილურის და desktop Playwright-ის localStorage სხვადასხვაა. cross-device არ მუშაობს.
2. **📤 export button** — ფაილის download მობილურზე არ მუშაობს/მოუხერხებელია.
3. **📧 mailto:** — მობილურზე არ გაიხსნა.
4. **Google Sheet + Apps Script web app** — OAuth-ზე ჩაიჭედა, deploy ვერ მოხერხდა.
5. **Google Form auto-submit** — მუშაობს მაგრამ generic-ია, კონკრეტულ output-ზე არ მიბმავს. UX ცუდია — Form page-ზე გადადის.

## რა მჭირდება

ტექნიკური გადაწყვეტა რომელიც:
- static HTML page-ზე მუშაობს (GitHub Pages, file://)
- მობილურზე მუშაობს
- კომენტარი კონკრეტულ section-ზე მიბმული
- მენცარი (Playwright ან სხვა tool) კითხულობს
- არ სჭირდება server-side backend

## შესაძლო მიმართულებები (ჩემი აზრით)

1. **Google Form prefilled URL** — ყოველ 💬 ღილაკზე section name-ით prefilled Form იხსნება. Form response sheet-ში ჩანს section + comment. UX = 2 tap (write + submit).

2. **Firebase Realtime DB** — free tier, REST API, CORS-free. Dashboard-ი fetch-ით წერს, მენცარი fetch-ით კითხულობს. მაგრამ setup სჭირდება.

3. **Google Sheets API direct** — API key-ით, fetch-ით. მაგრამ CORS.

4. **რამე სხვა რაც მე ვერ ვხედავ?**

---

*მენცარი | 2026-04-09 | 5 failed attempt. შენი expertise სჭირდება.*
