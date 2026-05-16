# Post-Mortem: bivision.ge — 2026-05-16

## რა მოხდა
9+ საათი მობილური layout broken. root cause: cascading mistakes functions.php-ში + WP Additional CSS-ში.

---

## Timeline

### 10:00 — სესია დაიწყო
**მოთხოვნა:** BiRetail product page-ზე CSS ჩანდა plain text-ად (`<p>` tags).
**Root cause:** CSS შენახული post_content-ში `<style>` ტეგის გარეშე.

### ~10:30 — MISTAKE #1: geo_style_registry
- **რა გავაკეთე:** `render_block` filter დავამატე functions.php-ში — ყველა block-ის `<style>` ტეგი ჩავანაცვლე `%%GEO_STYLE_N_%%` placeholder-ებით
- **რა მოხდა:** filter ყველა block-ს ეხება (header, footer, template parts) — არა მხოლოდ post content-ს. restore მხოლოდ `the_content`-ზე მუშაობდა. შედეგი: `%%GEO_STYLE_0_%%` visible text ყველა გვერდზე
- **სად შევცდი:** `render_block` = global hook. ყველა გვერდი ეხება. staging-ის გარეშე deploy

### ~11:00 — geo_style_registry ამოვიღე, ახალი fix დავამატე
- `product-css-text-strip` filter (priority 1) — სწორი fix BiRetail-ისთვის ✓
- `style-br-cleanup` filter (priority 99) ✓
- `products-button-group-mobile-stack` CSS via `wp_add_inline_style` — **MISTAKE #2**

### MISTAKE #2: CSS functions.php-ში
- **რა გავაკეთე:** mobile button CSS ჩავდე functions.php-ში `wp_add_inline_style`-ით
- **სწორი ადგილი:** WP Customizer → Additional CSS
- **შედეგი:** ახლა 2 ადგილი აკონტროლებს CSS-ს — functions.php + WP Additional CSS. conflict გარდაუვალი

### ~12:00 — MISTAKE #3: FTP upload cascade
- Passive FTP: TIMEOUT (exit 28)
- Active FTP `--ftp-port -`: wrote **0 bytes** → functions.php = empty/corrupt
- cPanel UAPI-ით restore: 59152 bytes — სწორი ზომა დაბრუნდა
- **სად შევცდი:** FTP unreliable-ია FastCloud-ზე. cPanel Fileman API პირველი ნაბიჯი უნდა ყოფილიყო

### ~13:00 — MISTAKE #4: services section CSS
- **რა გავაკეთე:** WP Additional CSS-ში დიდი mobile CSS block დავამატე `.products-*` სელექტორებით
- **რა მოხდა:** theme-ს უკვე ჰქონდა `.products-*` mobile rules. ახლა 3 კომპლექტი:
  1. Theme original CSS (`max-width: 768px`)
  2. ჩემი services section CSS (`max-width: 767px`) — conflicting
  3. functions.php CSS (`wp_add_inline_style`)
- **შედეგი:** iOS Safari-ზე layout broken. Chrome/Playwright — OK (ამიტომ ვერ ვამოწმებ)

### MISTAKE #5: Playwright = iOS validation
- Playwright Chrome simulator: scrollWidth=376, overflow=none, layout OK
- Real iPhone: content shifted, horizontal scroll, sections jumping
- **გაკვეთილი:** Playwright ≠ iOS Safari. visual validation = real device ONLY

---

## წესები — რა არ შეიძლება bivision.ge-ზე

### 🚫 NEVER — functions.php
| აკრძალვა | სწორი გზა |
|---|---|
| CSS functions.php-ში (`wp_add_inline_style`) | WP Customizer → Additional CSS |
| Global hook (`render_block`, `the_content` pr<5) staging-ის გარეშე | staging site → test → deploy |
| FTP upload 1000+ line ფაილისთვის | cPanel Fileman API (`save_file_content`) |

### 🚫 NEVER — WP Additional CSS
| აკრძალვა | მიზეზი |
|---|---|
| `.products-*` rules თუ theme-ს უკვე აქვს | specificity conflict გარდაუვალია |
| `!important` მრავლობით სელექტორებზე | cascade ვეღარ კონტროლდება |
| CSS block staging-ის გარეშე | real-device bug-ი Chrome-ში არ ჩანს |

### 🚫 NEVER — validation
| აკრძალვა | მიზეზი |
|---|---|
| "Playwright OK" = ship | Chrome ≠ iOS Safari (overflow, fixed positioning) |
| iteration broken state-ზე | cascading failure |
| CSS conflict-ის ignore | 3+ rule კომპლექტი = undefined behavior |

---

## რამ რა შეიძლება გამოიწვიოს

| მოქმედება | რისკი |
|---|---|
| functions.php edit | site-wide PHP error = white screen of death |
| FTP upload large file | timeout → 0 bytes → corrupt file → site down |
| `render_block` hook | ყველა block ყველა გვერდზე ეხება |
| `the_content` priority < 5 | WP core filters-ს ვუსწრებ, unpredictable |
| WP Additional CSS-ში `.products-*` | theme conflict, iOS broken |
| Deploy without real-device test | iOS Safari-ს ცალკე bugs აქვს |
| Iterating on broken state | ყოველი "fix" ახალ bug-ს შეიძლება ქმნიდეს |

---

## სწორი procedure (მომავლისთვის)

```
1. CSS change → WP Customizer Additional CSS (არა functions.php)
2. PHP hook → functions.php, მაგრამ:
   a. staging-ზე პირველ ტესტი
   b. cPanel Fileman API upload (არა FTP)
   c. scope: is_singular('bevision_product') — targeted, არა global
3. Visual test → real iPhone (ან BrowserStack iOS)
4. Rollback plan → backup date ცნობილი before deploy
5. One change at a time — არა cascade
```

---

## დამატებითი context

**BiRetail tabs broken** — pre-existing, May 16-მდე. ჩემი ცვლილება არ.
**BiRetail 301 redirect** — session-ის დასაწყისში 301 იყო, later 200. LiteSpeed cache purge-ის შემდეგ გასწორდა.
**functions.php server state post-incident:** 59152 bytes, 3 hook — სტაბილური, მაგრამ WP Additional CSS conflict-ი რჩება restore-მდე.
