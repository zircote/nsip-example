---
applyTo: "reports/**"
---

# Flock Action Instructions

When assigned a `flock-action` issue, follow this workflow to produce a
structured breeding report.

## 1. Parse the Issue

Extract these fields from the issue body:

| Field | Location | Required |
|---|---|---|
| Action | `action` dropdown | yes |
| LPN IDs | `lpn_ids` textarea (one per line) | yes |
| Trait Weights | `trait_weights` textarea (`TRAIT:weight` per line) | only for Rank |
| Sort Trait | `sort_trait` input | only for Compare |
| Notes | `notes` textarea | no |

## 2. Call MCP Tools by Action

### Mating Recommendations
For each LPN ID (assumed to be ewes):
1. Call `details` to get the animal's breed.
2. Call `mating_recommendations` with the animal's LPN ID and breed ID.
3. For each recommended mate, call `inbreeding_check`.

### Evaluate Flock
1. Call `details` for every LPN ID.
2. Extract the breed ID from the first animal.
3. Call `trait_ranges` for that breed.
4. For each animal, calculate breed-relative position per trait.

### Compare Animals
1. Call `compare` with all LPN IDs.
2. If a sort trait is provided, sort the results by that trait.
3. Call `trait_ranges` to add breed context.

### Rank Animals
1. Parse trait weights from the issue (format: `TRAIT:weight`).
2. Call `details` for each LPN ID.
3. Compute a weighted score: `score = sum(trait_value * weight * accuracy / 100)`.
4. Sort animals by score descending.
5. Call `trait_ranges` for breed context.

### Inbreeding Matrix
1. For every unique pair of LPN IDs, call `inbreeding_check`.
2. Build a matrix of COI values with traffic-light ratings.

### Flock Profile
1. Call `details` for each LPN ID.
2. Compute aggregate statistics: count, gender split, trait averages.
3. Call `trait_ranges` for breed context.
4. Compare flock averages against breed midpoints.

## 3. Produce Artifacts

Create output in `reports/{YYYY-MM-DD}-{action-slug}/` where:
- `{YYYY-MM-DD}` is today's date
- `{action-slug}` is the action in kebab-case (e.g., `mating-recommendations`)

### report.md

Formatted markdown with:
- Header linking back to the issue (`Closes #N`)
- Summary of the action and animals analyzed
- Data tables with EBV values, accuracies, and breed-relative context
- Recommendations or analysis conclusions
- Trait glossary footnote for non-obvious abbreviations

### data.csv

Machine-readable export with columns appropriate to the action:
- **Mating Recommendations**: `ewe_lpn,recommended_sire_lpn,rank_score,coi,predicted_bwt,predicted_wwt,...`
- **Evaluate Flock**: `lpn_id,breed,gender,bwt,bwt_acc,wwt,wwt_acc,...`
- **Compare Animals**: `lpn_id,trait,value,accuracy`
- **Rank Animals**: `lpn_id,score,trait1_contribution,trait2_contribution,...`
- **Inbreeding Matrix**: `sire_lpn,dam_lpn,coi,rating`
- **Flock Profile**: `metric,value`

## 4. Open a Pull Request

Create a PR with:
- **Title**: `[Flock Action] {Action Name} — {N} animals`
- **Body**:
  - Summary of findings
  - Link to the issue: `Closes #{issue_number}`
  - List of artifacts produced
- **Branch**: `flock-action/{issue_number}-{action-slug}`

## Formatting Rules

- Use markdown tables for all EBV data — never dump raw JSON.
- Show accuracy alongside every EBV: `+9.6 (68%)`.
- Use traffic-light indicators for COI: Green, Yellow, Red.
- Include breed ranges for context when presenting individual values.
- Round EBV values to 2 decimal places.
- Use the trait's natural units (lbs, mm, lambs, eggs/g).
