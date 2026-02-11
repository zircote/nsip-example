---
applyTo: "**/*eov*.yml,eov/**,reports/**"
---

# EOV Agent Instructions

When working with ecological monitoring record issues, EOV action requests, or
land health data, follow the workflows described below. This document is the
authoritative reference for agent-driven interactions with the farm's EOV
monitoring data.

---

## What is EOV?

Ecological Outcome Verification (EOV) is a framework developed by the Savory
Institute to measure ecological health outcomes on managed land. Unlike
practice-based standards (which track *what you do*), EOV tracks *what actually
happens* — whether the land is getting healthier over time.

This farm uses a simplified EOV protocol adapted for a 45-acre operation:

- **Short-Term Monitoring (STM)**: Seasonal visual assessments of 15 ecological
  health indicators at 12 monitoring sites
- **Long-Term Monitoring (LTM)**: Periodic soil sampling and water infiltration
  testing at 3 sites
- **Photo Points**: Seasonal photos at each site documenting visual change

All monitoring data is stored as GitHub Issues with `record:eov-*` labels.

---

## Indicator Reference — The 15 Ecological Health Indicators

These indicators are scored during every site assessment (STM). Each is scored
on a 5-point scale that maps to numerical values for trend tracking.

| # | Indicator | What It Measures | Ecosystem Process |
|---|-----------|-----------------|-------------------|
| 1 | Live Canopy Cover | Amount of living plant cover | Solar energy capture |
| 2 | Living Organisms | Insects, earthworms, birds, wildlife | Biodiversity |
| 3 | Warm Season Grasses | Vigor of warm-season grass species | Plant community health |
| 4 | Cool Season Grasses | Vigor of cool-season grass species | Plant community health |
| 5 | Forbs and Legumes | Non-grass herbaceous plants | Plant diversity |
| 6 | Trees and Shrubs | Woody plant health | Structural diversity |
| 7 | Desirable Species | Plants you want more of | Plant community trajectory |
| 8 | Undesirable Species | Weeds and invasives | Plant community trajectory |
| 9 | Litter Abundance | Dead plant material on ground | Nutrient cycling |
| 10 | Litter Decomposition | Breakdown of dead material | Nutrient cycling |
| 11 | Dung Decomposition | Breakdown of animal dung | Nutrient cycling |
| 12 | Bare Soil | Exposed ground | Water cycle |
| 13 | Soil Capping | Surface sealing/crusting | Water cycle |
| 14 | Wind Erosion | Signs of wind-driven soil loss | Soil stability |
| 15 | Water Erosion | Signs of water-driven soil loss | Soil stability |

---

## Numerical Score Mapping

Map dropdown values to numbers for trend analysis. Standard scale (indicators
1-7, 9-11):

| Score | Dropdown Value | Numerical |
|-------|---------------|-----------|
| Best | Excellent / Thriving / Very abundant / Heavy / Rapid | +2 |
| Good | Good / Vigorous / Abundant / Active / Dominant (desirable) | +1 |
| Neutral | Average / Fair / Moderate / Some | 0 |
| Below | Below average / Weak / Few / Slow | -1 |
| Worst | Poor / Absent / None observed / Sparse / None (decomposition) | -2 |

**Inverted scale** (indicators 8, 12-15 — lower is better):

| Score | Dropdown Value | Numerical |
|-------|---------------|-----------|
| Best | None (erosion/capping) / <10% (bare soil) / None (undesirable) | +2 |
| Good | Minimal / 10-25% / Few | +1 |
| Neutral | Light / 25-50% / Some | 0 |
| Below | Moderate / 50-75% / Many | -1 |
| Worst | Severe / >75% / Dominant (undesirable) | -2 |

**Ecological Health Index (EHI)** = sum of all 15 indicator scores.
- Range: -30 (all worst) to +30 (all best)
- A positive EHI indicates generally healthy conditions
- EHI change over time is the primary measure of ecological trajectory

---

## Enrichment Workflow Recipes

### Recipe 1 — Enrich Site Assessment Record

**Trigger**: Issue opened with label `record:eov-site-assessment`

**Steps:**

1. Parse `site_id` and `assessment_date` from issue body.
2. Calculate the EHI for this assessment using the score mapping above.
3. Search closed issues with label `record:eov-site-assessment` for the same
   `site_id` (use GitHub issue search: `label:record:eov-site-assessment` plus
   the site_id text).
4. If previous assessments found:
   a. Calculate EHI for each previous assessment.
   b. Build a trend table showing EHI over time.
   c. For each of the 15 indicators, compare current score to most recent
      previous score and flag changes (improved / stable / declined).
   d. Identify the 3 most-improved and 3 most-declined indicators.
5. Post an enrichment comment with:

```markdown
## EOV Enrichment — Site {site_id}

### Ecological Health Index

| Date | Season | EHI Score | Trend |
|------|--------|-----------|-------|
| {previous dates...} | {season} | {score} | — |
| **{current_date}** | **{season}** | **{score}** | {↑ improving / → stable / ↓ declining} |

### Indicator Changes (vs. previous assessment)

| Indicator | Previous | Current | Change |
|-----------|----------|---------|--------|
| {indicator} | {prev_score} | {curr_score} | {↑/→/↓} |
| ... | ... | ... | ... |

### Key Observations

**Improving:** {list indicators that improved}
**Declining:** {list indicators that declined}
**Stable:** {count} of 15 indicators unchanged

### What This Means

{Plain-language interpretation of the trends — what's getting better, what
needs attention, and what management actions might help.}
```

6. Add the `eov-enriched` label to the issue.

**If this is the first assessment for this site:**
Post a simpler comment noting the baseline EHI score, explain that trend data
will appear after the next seasonal assessment, and still add the
`eov-enriched` label.

---

### Recipe 2 — Enrich Soil Sample Record

**Trigger**: Issue opened with label `record:eov-soil-sample`

**Steps:**

1. Parse `site_id` and key metrics from issue body.
2. Search closed issues with label `record:eov-soil-sample` for the same
   `site_id`.
3. If previous samples found, build a trend table.
4. Compare against benchmarks:

| Metric | Needs Improvement | Acceptable | Good | Excellent |
|--------|------------------|------------|------|-----------|
| Haney Score | <7 | 7-15 | 15-30 | >30 |
| Organic Matter (%) | <2.0 | 2.0-3.5 | 3.5-5.0 | >5.0 |
| Soil Respiration (mg CO2-C/kg) | <30 | 30-80 | 80-150 | >150 |
| Aggregate Stability (%) | <20 | 20-40 | 40-60 | >60 |
| Soil pH | <5.5 or >8.0 | 5.5-6.0 or 7.5-8.0 | 6.0-7.5 | 6.2-7.0 |

5. Post an enrichment comment with trend table, benchmark comparison, and
   plain-language interpretation.
6. Add the `eov-enriched` label.

---

### Recipe 3 — Enrich Water Infiltration Record

**Trigger**: Issue opened with label `record:eov-water-test`

**Steps:**

1. Parse `site_id` and `infiltration_rate` from issue body.
2. Search closed issues with label `record:eov-water-test` for the same
   `site_id`.
3. If previous tests found, build a trend table.
4. Compare against benchmarks:

| Infiltration Rate (in/hr) | Rating | What It Means |
|---------------------------|--------|---------------|
| <0.5 | Poor | Soil is compacted or sealed; water runs off |
| 0.5-1.0 | Fair | Some absorption but room for improvement |
| 1.0-2.0 | Good | Healthy soil structure; water is being absorbed |
| >2.0 | Excellent | Very healthy soil; water soaks right in |

5. Post an enrichment comment with trend data, benchmark rating, and
   plain-language interpretation.
6. Add the `eov-enriched` label.

---

### Recipe 4 — Enrich Photo Point Record

**Trigger**: Issue opened with label `record:eov-photo-point`

**Steps:**

1. Parse `site_id`, `season`, and `direction` from issue body.
2. Search closed issues with label `record:eov-photo-point` for the same
   `site_id` and `direction`.
3. If previous photos found at the same site and direction, post a comment
   linking to the previous records so the user can compare visually.
4. Post an enrichment comment noting:
   - How many previous photos exist for this site/direction
   - Links to same-season photos from previous years (if any)
   - A reminder to compare vegetation cover, bare soil, and overall appearance
5. Add the `eov-enriched` label.

---

## EOV Action Recipes

**Trigger**: Issue opened with label `eov-action`

Parse the `action` dropdown to determine which analysis to run.

### Action: Seasonal Summary

1. Identify the target season from the form.
2. Search issues with label `record:eov-site-assessment` for that season.
3. For each site, calculate the EHI score.
4. Aggregate farm-wide statistics:
   - Average EHI across all sites
   - EHI by land type (pasture, crop, riparian, woodlot)
   - Best and worst performing sites
   - Most common "declining" indicators across all sites
5. Create a report PR in `reports/{YYYY-MM-DD}-eov-seasonal-summary/` with:
   - `report.md` — formatted summary with tables and interpretation
   - `data.csv` — raw scores for all sites and indicators

### Action: Site Comparison

1. Parse `site_ids` from the form (or use all sites if blank).
2. Find the most recent assessment for each site.
3. Build a comparison table showing all 15 indicators side by side.
4. Calculate EHI for each site and rank them.
5. Create a report PR in `reports/{YYYY-MM-DD}-eov-site-comparison/`.

### Action: Annual Trend Report

1. Find all assessments across the full year for all sites.
2. For each site, calculate EHI for each season.
3. Show the trajectory: is each site improving, stable, or declining?
4. Identify farm-wide patterns (e.g., "bare soil decreased across all pasture
   sites" or "litter decomposition improved in spring but declined in fall").
5. Create a report PR in `reports/{YYYY-MM-DD}-eov-annual-trend/`.

### Action: Enrollment Readiness Check

1. Check the monitoring data completeness:
   - How many sites have been assessed?
   - How many seasons of data exist?
   - Are soil samples and water tests recorded?
   - Are photo points documented?
2. Assess the ecological trajectory:
   - Is EHI improving or stable at most sites?
   - Are any critical indicators (bare soil, erosion) still declining?
3. Create a report PR in `reports/{YYYY-MM-DD}-eov-enrollment-readiness/` with:
   - Completeness checklist
   - Trajectory assessment
   - Gaps that need to be addressed
   - Recommended timeline for enrollment

---

## Formatting Rules

When presenting EOV data to farmers, follow these conventions:

1. **Always use tables** for indicator data and trends — never dump raw data.

2. **Use arrows for trends**: ↑ improving, → stable, ↓ declining.

3. **Explain in plain language** what each indicator means practically:
   - Say "the ground is more covered with plants than last season"
   - Not "live canopy cover increased from 0 to +1"

4. **Include season and weather context**: Note the season and any unusual
   weather that might affect observations (drought, flooding, early frost).

5. **Use natural units throughout**: inches/hour for infiltration, percent for
   organic matter, etc.

6. **Note the number of data points**: Trends based on 2 assessments are less
   reliable than trends based on 8. Always mention how many observations are
   in the trend.

7. **Give management-relevant advice**: Connect observations to actions. If
   bare soil is increasing, suggest management responses (more recovery time
   between grazing, cover crop, mulch).

8. **Use benchmark context**: When presenting soil or water data, always show
   where the value falls relative to the benchmarks defined in this document.

9. **Celebrate improvement**: When indicators improve, say so clearly and
   explain why it matters. Positive reinforcement encourages continued
   monitoring.

---

## Indicator Glossary

Plain-language definitions for non-technical users.

**Live Canopy Cover** — How much of the ground is covered by living plants when
you look down from above. More cover means more photosynthesis, cooler soil,
and less erosion.

**Living Organisms** — The insects, earthworms, birds, and other creatures you
can see. A healthy ecosystem is buzzing with life. Dung beetles breaking down
manure, earthworms in the soil, birds hunting insects — all signs the system
is working.

**Warm Season Grasses** — Grasses that grow in summer heat (like bermudagrass,
switchgrass, big bluestem). They handle drought better and have deep roots that
build soil.

**Cool Season Grasses** — Grasses that grow in spring and fall (like fescue,
orchardgrass, ryegrass). They provide ground cover when warm-season grasses are
dormant.

**Forbs and Legumes** — Non-grass plants: wildflowers, clover, alfalfa,
chicory. They add diversity, fix nitrogen (legumes), and feed pollinators.

**Trees and Shrubs** — Woody plants providing shade, windbreaks, wildlife
habitat, and deep root systems that improve water infiltration.

**Desirable Species** — Plants you want to see more of — the ones that feed
livestock, build soil, or support wildlife. More desirable species means the
plant community is headed in the right direction.

**Undesirable Species** — Weeds, invasives, and plants you'd rather not have.
Fewer undesirable species means grazing management and competition from
desirable plants are working.

**Litter Abundance** — Dead plant material lying on the ground. Litter protects
soil from sun and rain, feeds soil organisms, and slowly releases nutrients.
It's natural mulch.

**Litter Decomposition** — How fast dead plant material is breaking down. Active
decomposition means soil organisms (fungi, bacteria, insects) are healthy and
cycling nutrients.

**Dung Decomposition** — How fast animal manure is being broken down. Dung
beetles and other organisms should be incorporating manure into the soil. If
dung sits on the surface unchanged for weeks, biological activity is low.

**Bare Soil** — Exposed ground with no plant cover or litter. Bare soil is
vulnerable to erosion, compaction, and moisture loss. Less bare soil is almost
always better.

**Soil Capping / Crusting** — A thin, hard crust on the soil surface that forms
when rain hits bare ground. It seals the surface and prevents water from
soaking in. Healthy soil has good structure and doesn't cap.

**Wind Erosion** — Signs that soil is being blown away: dust clouds, exposed
roots, sand deposits. Indicates lack of ground cover and soil structure
problems.

**Water Erosion** — Signs that soil is being washed away: rills, gullies,
sediment deposits, murky runoff. Indicates water is running off instead of
soaking in.
