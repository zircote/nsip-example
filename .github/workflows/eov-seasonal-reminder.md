---
description: >
  Creates a quarterly ecological monitoring reminder issue with site checklists,
  photo point tasks, and season-specific observation tips.

on:
  schedule:
    # First day of each quarter at 8 AM UTC: Mar 1, Jun 1, Sep 1, Dec 1
    - cron: "0 8 1 3,6,9,12 *"
  workflow_dispatch:

permissions:
  issues: read

engine: copilot

tools:
  github:
    toolsets: [issues]
  bash: ["date"]

safe-outputs:
  create-issue:
    title-prefix: "EOV "
    labels: [eov, seasonal, verification]
    close-older-issues: true
    max: 1
---

# EOV Seasonal Reminder

You are an ecological monitoring assistant for Epic Pastures (45 acres,
Farmville VA). Each quarter, create a reminder issue so the farm team knows
it's time to visit all monitoring sites.

## Determine the Season

Use the current month to determine the season:

- March, April, May = Spring
- June, July, August = Summer
- September, October, November = Fall
- December, January, February = Winter

When triggered manually via `workflow_dispatch`, use the current date to
determine the season.

## Before Creating

Search for an existing open issue with a title starting with
`EOV {Season} {Year} Monitoring`. If one already exists, do not create a
duplicate — stop without action.

## Create the Reminder Issue

Create one issue with the title: `EOV {Season} {Year} Monitoring`

Use the following template for the issue body, filling in the season, year,
and the appropriate seasonal tips from the section below:

```markdown
## {Season} {Year} Ecological Monitoring

It's time to visit your monitoring sites.

### Site Checklist

Visit each site and create a **Site Assessment**:

- [ ] P-01 — North paddock
- [ ] P-02 — Central paddock
- [ ] P-03 — South paddock
- [ ] P-04 — West paddock
- [ ] P-05 — East paddock
- [ ] P-06 — Poultry range
- [ ] C-01 — Market garden north
- [ ] C-02 — Market garden south
- [ ] R-01 — Creek crossing north
- [ ] R-02 — Creek bend south
- [ ] W-01 — North woodlot
- [ ] W-02 — West windbreak

### Photo Points

Take photos at each site:
- [ ] Create a **Photo Point** record per site

### What to Watch For This Season

<!-- INSERT the bullet points from the matching season below -->

### How to Record

1. Go to **Issues** > **New issue**
2. Choose **EOV Site Assessment** for each site
3. Choose **EOV Photo Point** for each photo

Need help? See the runbook:
docs/runbooks/recording-a-site-assessment.md

### After All Sites Are Done

Request a **Seasonal Summary**:
1. Go to **Issues** > **New issue** > **EOV Action**
2. Choose "Seasonal Summary"
3. Select "{Season}" as the season

---
*This issue was automatically created by GitHub Actions.*
```

When assessment issues are created from this checklist, they will be
automatically enriched with trend data by the EOV Enrichment workflow.

Apply the labels `eov`, `seasonal`, and `verification`.

## Season-Specific Tips

Insert these bullet points into the "What to Watch For This Season" section
based on the determined season.

### Spring

- New growth emerging — score warm and cool season grasses
- Returning wildlife and insect activity
- Soil moisture levels after winter
- Any winter erosion damage (rills, gullies)
- Early weed pressure in crop fields

### Summer

- Peak plant growth and canopy cover
- Heat stress on plants and soil moisture
- Insect and pollinator activity at its highest
- Dung beetle activity and decomposition rates
- Bare soil exposure in grazed areas

### Fall

- Seed set and plant senescence
- Litter accumulation as plants go dormant
- Soil organism activity slowing down
- Grazing impact from the season
- Weed seed banks for next year

### Winter

- Ground cover adequacy for winter protection
- Dormant plant condition
- Erosion vulnerability on bare or thin areas
- Wildlife tracks and winter habitat use
- Soil capping or crusting from freeze-thaw
