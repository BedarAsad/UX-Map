# Example: non-commercial public data map (anonymized)

A free public map of about 2,300 industrial sites in one country, each with a harm rating. No signup, pricing or checkout. Goal confirmed with the user: **find the sites in an area and understand their harm**. Walked logged out at desktop width and at 375 px (phone); only filters, rows and dialogs used.

## Personas
| Persona | Role | Wants | Blocked by |
| --- | --- | --- | --- |
| Resident | Lives near a site, on a phone, may read only the local language | "Is the site near me harmful?" | English-only UI; codes; phone row tap leaves the site |
| Journalist / researcher | Reports, papers | Evidence to cite and share | No result count, share link or download |
| Regulator / policymaker | Environment agency, local government | Where to act first | No area summary; harm number has no scale |

## Flow 1 (desktop): boxes used
Homepage [amber: spinner about 9 s while all sites and ~2 MB of boundaries load] → Location filters (multi-select with search; map zooms) → Site table [amber: ID and type codes not explained] → Map popup [amber: "Harm Rate: 2.59" with no scale] → Get directions [accent: opens an external maps app]. Side: explanatory note (PDFs in two languages, in a dialog). Gaps [dashed red]: no result count (504 sites in the chosen region, not stated); numbers vs words (legend uses 5 words, table uses numbers); nothing to share.

## Flow 2 (phone): boxes used
Homepage on a phone (filters and table; map hidden) → Site table [amber: says "Click a row to locate on the map"] → Tap a row: directions dialog [amber] → Gap: leaves the site (harm level never shown). Branch: separate map page [amber: only "Back to Home" and "Reset View"] → Gap: no legend or filters.

## Findings (top of the table)
| Priority | Finding | Fix | Effort |
| --- | --- | --- | --- |
| 1 | Harm rate is a bare number; legend and filter use 5 words; nothing links them | Level word beside every number; score ranges in the legend | Low |
| 2 | On phones, tapping a row labelled "locate on the map" opens external directions | Tap shows site details on the map; directions as a button | Medium |
| 3 | Phone map page has no legend or filters | Add the legend; keep the chosen area in the link | Medium |
| 4 | UI is English only; the local language exists only as a PDF | Local-language interface toggle | Medium |

What made this walk work: using the tool rather than only reading links (real clicks on custom dropdowns, counting table rows), repeating the path at phone width (where the worst finding was), and checking the PDFs with a HEAD fetch before calling them broken.
