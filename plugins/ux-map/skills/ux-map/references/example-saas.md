# Example: commercial SaaS (anonymized)

A research-tools SaaS with four products, a free tier (1 project, 1 form), a $49/month Pro plan and hosted servers from $79/month. Walked logged out (homepage, signup, product and pricing pages, pricing buttons) and logged in on a free account (dashboard, core editor, both checkout pages, an empty "servers" page). The dashboard item count was 0 before and after — nothing created. Not tested: the AI generation step (would use the one free item), the free-limit screen, the payment processor page.

## Personas
| Persona | Role | Wants | Blocked by |
| --- | --- | --- | --- |
| The doer | Research assistant / analyst | Get the form built fast, no server work | Can't spend money |
| The approver | Principal investigator / project manager | Reliable data, controlled budget | Needs proof and an invoice |
| Procurement | Finance / IT | Invoices, security answers | Card-only payment |

## Flow 1 (public): boxes used
Homepage → 4 product entries (each with its price or "free") → Signup [amber: same generic heading on every path; chosen plan not shown] → Free workspace (1 project, 1 form) | Checkout (plan carried in the `next=` link) → Hits the free limit [amber] → Paid [accent]. Gaps [dashed red]: org/approver buyer ("Talk to Sales" is a mailto only); lost plan (a logged-out `/checkout` link redirects to `/login` without the plan).

## Flow 2 (logged in): boxes used
Dashboard (onboarding checklist 2 of 5, starter prompt chips) → Core editor [amber: blank spreadsheet, prompts not shown here] / Upgrade button (sidebar, every page) / Create server → Preview and download [amber: checklist ends here] → Gap: dead end [dashed red: no nudge to publish or upgrade]; Upgrade + Create server → One-page checkout (bundle discount; name required) → Card payment [amber: no invoice, bank transfer or quote] → Paid.

## Findings (top of the table)
| Priority | Finding | Fix | Effort |
| --- | --- | --- | --- |
| 1 | Onboarding checklist ends at "Download your form"; nothing points to the paid product | Add a final step that leads to it (e.g. "Publish to your own server") | Low |
| 2 | "Talk to Sales" is a mailto; checkout is card only | "Share with my manager" quote PDF; invoice option | Medium |
| 3 | The editor opens on a blank sheet; helpful prompt chips stay on the dashboard | Show the prompts in the empty editor | Low |
| 4 | Signup copy identical on every path; plan hidden | Path-specific heading + plan summary | Low |
| 5 | Logged-out `/checkout` redirects to `/login` without `next=` | Keep `next=` on the redirect | Low |

What made these good: each names the exact screen, quotes the site, and ties to a purchase-path consequence. Cosmetic items (e.g. "Page 1 of 0" on an empty table) go at the bottom.
