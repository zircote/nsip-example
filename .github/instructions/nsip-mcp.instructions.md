---
applyTo: "**/*-record.yml,**/BREEDING-EVENT-LOG*,reports/**"
---

# NSIP MCP Agent Instructions

When working with breeding record issues, event logs, or livestock data queries, use
the NSIP MCP tools described below. This document is the authoritative reference for
agent-driven interactions with the NSIP Search API.

---

## What is the NSIP MCP Server?

The NSIP MCP server wraps the [National Sheep Improvement Program](https://nsip.org/)
Search API as a Model Context Protocol service. It gives AI agents direct access to:

- **400,000+ sheep** with estimated breeding values (EBVs)
- **Pedigree trees** spanning multiple generations
- **Breed-level benchmarks** (trait ranges, averages)
- **Breeding analytics** — inbreeding coefficients, trait ranking, mating recommendations

**Transport**: stdio only — started with `nsip mcp`

---

## Tool Reference

### search

Find animals matching filter criteria. Returns paginated results.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `breed_group_id` | integer | no | | Breed group ID |
| `breed_id` | integer | no | | Breed ID |
| `status` | string | no | | `"CURRENT"`, `"SOLD"`, or `"DEAD"` |
| `gender` | string | no | | `"Male"`, `"Female"`, or `"Both"` |
| `born_after` | string | no | | Animals born after this date (`YYYY-MM-DD`) |
| `born_before` | string | no | | Animals born before this date (`YYYY-MM-DD`) |
| `proven_only` | boolean | no | false | Only return proven animals |
| `flock_id` | string | no | | Flock ID |
| `sort_by` | string | no | | Trait abbreviation to sort by (e.g. `"WWT"`) |
| `reverse` | boolean | no | false | Reverse the sort order |
| `page` | integer | no | 0 | Page number (0-indexed) |
| `page_size` | integer | no | 15 | Results per page (1–100) |

**Example — find current Poll Dorset rams sorted by weaning weight:**

```json
{
  "tool": "search",
  "arguments": {
    "breed_id": 486,
    "gender": "Male",
    "status": "CURRENT",
    "sort_by": "WWT",
    "page_size": 5
  }
}
```

**When to use**: Starting point for most queries. Use `search` to discover animals
before drilling into `details`, `lineage`, or `compare`.

---

### details

Fetch full EBV data, breed, contact info, and status for one animal.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `animal_id` | string | yes | LPN ID or registration number |

**Example:**

```json
{
  "tool": "details",
  "arguments": { "animal_id": "430735-0032" }
}
```

**Example response (abbreviated):**

```json
{
  "lpn_id": "430735-0032",
  "breed": "Poll Dorset",
  "gender": "Male",
  "status": "CURRENT",
  "date_of_birth": "2022-08-15",
  "traits": {
    "BWT": { "name": "BWT", "value": 0.28, "accuracy": 72 },
    "WWT": { "name": "WWT", "value": 9.6,  "accuracy": 68 },
    "YWT": { "name": "YWT", "value": 14.2, "accuracy": 55 },
    "EMD": { "name": "EMD", "value": 1.1,  "accuracy": 48 },
    "FAT": { "name": "FAT", "value": -0.3, "accuracy": 51 },
    "NLB": { "name": "NLB", "value": 0.05, "accuracy": 38 }
  },
  "contact_info": {
    "flock_name": "Doreen Downs",
    "state": "NSW"
  }
}
```

**When to use**: After identifying an animal via `search`, fetch its full profile.
Always pair with `trait_ranges` to provide breed-relative context.

---

### lineage

Retrieve the pedigree (ancestry) tree — parents, grandparents, and deeper ancestors.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `animal_id` | string | yes | LPN ID |

**Example:**

```json
{
  "tool": "lineage",
  "arguments": { "animal_id": "430735-0032" }
}
```

**Example response (abbreviated):**

```json
{
  "subject": { "lpn_id": "430735-0032", "farm_name": "Doreen Downs" },
  "sire": { "lpn_id": "410220-0015", "farm_name": "Oak Valley" },
  "dam":  { "lpn_id": "430735-0018", "farm_name": "Doreen Downs" },
  "generations": [
    [
      { "lpn_id": "410220-0008" },
      { "lpn_id": "410220-0011" },
      { "lpn_id": "430735-0005" },
      { "lpn_id": "430735-0009" }
    ]
  ]
}
```

**When to use**: Before mating decisions — check for shared ancestors. Also useful
for understanding an animal's genetic background.

---

### progeny

List offspring for an animal with pagination.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `animal_id` | string | yes | | LPN ID |
| `page` | integer | no | 0 | Page number (0-indexed) |
| `page_size` | integer | no | 10 | Results per page |

**Example:**

```json
{
  "tool": "progeny",
  "arguments": { "animal_id": "430735-0032", "page_size": 5 }
}
```

**When to use**: Evaluating a sire's or dam's proven track record. A ram with many
high-performing offspring is a stronger breeding prospect.

---

### profile

All-in-one call that combines `details`, `lineage`, and `progeny` in a single request.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `animal_id` | string | yes | LPN ID |

**Example:**

```json
{
  "tool": "profile",
  "arguments": { "animal_id": "430735-0032" }
}
```

**When to use**: When you need the complete picture of an animal and want to minimize
round trips. Prefer `profile` over calling `details` + `lineage` + `progeny` separately.

---

### breed_groups

List all breed groups and individual breeds in the NSIP database. No parameters.

**Example:**

```json
{
  "tool": "breed_groups",
  "arguments": {}
}
```

**Example response (abbreviated):**

```json
[
  {
    "breed_group_id": 1,
    "breed_group_name": "Terminal Sire",
    "breeds": [
      { "breed_id": 486, "breed_name": "Poll Dorset" },
      { "breed_id": 487, "breed_name": "Suffolk" },
      { "breed_id": 488, "breed_name": "White Suffolk" }
    ]
  },
  {
    "breed_group_id": 2,
    "breed_group_name": "Maternal",
    "breeds": [
      { "breed_id": 490, "breed_name": "Corriedale" }
    ]
  }
]
```

**When to use**: To discover valid `breed_id` values before calling `search`,
`rank`, `trait_ranges`, or `mating_recommendations`.

---

### trait_ranges

Get the min/max EBV values across all animals within a breed. Essential for
understanding where an individual sits relative to the breed.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `breed_id` | integer | yes | Breed ID |

**Example:**

```json
{
  "tool": "trait_ranges",
  "arguments": { "breed_id": 486 }
}
```

**Example response (abbreviated):**

```json
[
  { "trait_name": "BWT", "min": -1.2, "max": 2.8 },
  { "trait_name": "WWT", "min": -5.0, "max": 18.5 },
  { "trait_name": "YWT", "min": -8.0, "max": 25.3 },
  { "trait_name": "NLB", "min": -0.15, "max": 0.32 }
]
```

**When to use**: Always call `trait_ranges` when presenting EBV data so you can
say "this ram's WWT of +9.6 is in the top 30% of Poll Dorsets" rather than just
showing a raw number.

---

### compare

Side-by-side EBV comparison of 2–5 animals. Optionally filter to specific traits.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `animal_ids` | array of strings | yes | LPN IDs (2–5 items) |
| `traits` | string | no | Comma-separated trait filter (e.g. `"BWT,WWT,YWT"`) |

**Example — compare three rams on growth traits:**

```json
{
  "tool": "compare",
  "arguments": {
    "animal_ids": ["430735-0032", "430735-0041", "410220-0015"],
    "traits": "BWT,WWT,YWT,EMD,FAT"
  }
}
```

**Example response:**

```json
{
  "animal_count": 3,
  "animals": [
    {
      "lpn_id": "430735-0032",
      "breed": "Poll Dorset",
      "gender": "Male",
      "traits": {
        "BWT": { "value": 0.28, "accuracy": 72 },
        "WWT": { "value": 9.6,  "accuracy": 68 },
        "YWT": { "value": 14.2, "accuracy": 55 },
        "EMD": { "value": 1.1,  "accuracy": 48 },
        "FAT": { "value": -0.3, "accuracy": 51 }
      }
    },
    {
      "lpn_id": "430735-0041",
      "breed": "Poll Dorset",
      "gender": "Male",
      "traits": {
        "BWT": { "value": 0.45, "accuracy": 65 },
        "WWT": { "value": 11.2, "accuracy": 62 },
        "YWT": { "value": 16.8, "accuracy": 50 },
        "EMD": { "value": 0.8,  "accuracy": 42 },
        "FAT": { "value": -0.1, "accuracy": 45 }
      }
    },
    {
      "lpn_id": "410220-0015",
      "breed": "Poll Dorset",
      "gender": "Male",
      "traits": {
        "BWT": { "value": -0.10, "accuracy": 88 },
        "WWT": { "value": 8.4,   "accuracy": 85 },
        "YWT": { "value": 12.5,  "accuracy": 78 },
        "EMD": { "value": 1.4,   "accuracy": 72 },
        "FAT": { "value": -0.5,  "accuracy": 68 }
      }
    }
  ]
}
```

**How to present comparison results:**

| Trait | 430735-0032 | 430735-0041 | 410220-0015 | Best |
|---|---|---|---|---|
| BWT | +0.28 (72%) | +0.45 (65%) | **-0.10 (88%)** | 410220-0015 |
| WWT | +9.6 (68%) | **+11.2 (62%)** | +8.4 (85%) | 430735-0041 |
| YWT | +14.2 (55%) | **+16.8 (50%)** | +12.5 (78%) | 430735-0041 |
| EMD | +1.1 (48%) | +0.8 (42%) | **+1.4 (72%)** | 410220-0015 |
| FAT | -0.3 (51%) | -0.1 (45%) | **-0.5 (68%)** | 410220-0015 |

**Summary**: 430735-0041 leads on growth (WWT, YWT) but has higher birth weight.
410220-0015 has the best combination of low BWT, muscling, and leanness with high
accuracy. 430735-0032 is a balanced middle option.

---

### rank

Rank animals within a breed by a weighted composite score. The score formula is:

```
Score = Σ (trait_value × weight × accuracy / 100)
```

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `breed_id` | integer | yes | | Breed ID to search |
| `weights` | object | yes | | Trait-to-weight map, e.g. `{"BWT": -1.0, "WWT": 2.0}` |
| `gender` | string | no | | `"Male"`, `"Female"`, or `"Both"` |
| `status` | string | no | | `"CURRENT"`, `"SOLD"`, `"DEAD"` |
| `top_n` | integer | no | 10 | Number of top results to return |

**Example — terminal sire ranking (prioritize growth, penalize birth weight):**

```json
{
  "tool": "rank",
  "arguments": {
    "breed_id": 486,
    "weights": { "BWT": -1.0, "WWT": 2.0, "YWT": 1.5, "EMD": 1.0 },
    "gender": "Male",
    "status": "CURRENT",
    "top_n": 5
  }
}
```

**Example — maternal sire ranking:**

```json
{
  "tool": "rank",
  "arguments": {
    "breed_id": 486,
    "weights": { "NLB": 2.0, "NWT": 2.0, "PWT": 1.5, "BWT": -0.5 },
    "gender": "Male",
    "top_n": 10
  }
}
```

**Example response:**

```json
[
  {
    "lpn_id": "430735-0041",
    "score": 28.94,
    "trait_scores": {
      "BWT": -0.29,
      "WWT": 13.89,
      "YWT": 12.60,
      "EMD": 2.74
    }
  },
  {
    "lpn_id": "430735-0032",
    "score": 22.15,
    "trait_scores": {
      "BWT": -0.20,
      "WWT": 13.06,
      "YWT": 11.72,
      "EMD": -2.43
    }
  }
]
```

**Understanding weights:**
- Positive weight → higher EBV values score better (e.g., WWT: 2.0)
- Negative weight → lower EBV values score better (e.g., BWT: -1.0)
- Magnitude controls importance (weight of 2.0 counts twice as much as 1.0)

---

### inbreeding_check

Calculate Wright's coefficient of inbreeding (COI) for a potential sire × dam mating.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sire_id` | string | yes | LPN ID of the sire (father) |
| `dam_id` | string | yes | LPN ID of the dam (mother) |

**Example:**

```json
{
  "tool": "inbreeding_check",
  "arguments": {
    "sire_id": "430735-0032",
    "dam_id": "430735-0089"
  }
}
```

**Example response — safe mating:**

```json
{
  "coefficient": 0.03125,
  "rating": "Green",
  "shared_ancestors": [
    { "lpn_id": "410220-0008", "sire_depth": 2, "dam_depth": 2 }
  ]
}
```

**Example response — risky mating:**

```json
{
  "coefficient": 0.125,
  "rating": "Red",
  "shared_ancestors": [
    { "lpn_id": "430735-0005", "sire_depth": 1, "dam_depth": 1 }
  ]
}
```

**COI traffic-light thresholds:**

| Rating | COI | Equivalent to | Recommendation |
|---|---|---|---|
| Green | < 6.25% | Less related than half-siblings | Safe — proceed |
| Yellow | 6.25–12.5% | Half-sibling level | Caution — consider alternatives |
| Red | > 12.5% | Full sibling or closer | Avoid — high inbreeding depression risk |

**Inbreeding depression effects in sheep:**
- Reduced fertility and lower lambing rates
- Decreased lamb survival
- Slower growth rates
- Weakened immune response and parasite susceptibility

**When to use**: Always check COI before any planned mating. This is the most
important safety check in a breeding program.

---

### mating_recommendations

Find optimal mates for an animal. Searches the breed for candidates of the opposite
gender, ranks by trait complementarity, and checks inbreeding for each candidate.

| Parameter | Type | Required | Default | Description |
|---|---|---|---|---|
| `animal_id` | string | yes | | LPN ID of the animal to find mates for |
| `breed_id` | integer | yes | | Breed ID to search for candidates |
| `target_traits` | string | no | WWT, BWT, NLB | Comma-separated traits to optimize |
| `max_results` | integer | no | 5 | Number of recommendations |

**Default trait weights** (when `target_traits` is omitted):
- WWT: +1.0 (higher weaning weight)
- BWT: -0.5 (lower birth weight)
- NLB: +0.5 (more lambs born)

**Automatic negative weights** — these traits are automatically penalized because
lower is better: BWT, DAG, WEC, FEC.

**Example — find mates for a ewe, optimizing for growth and muscling:**

```json
{
  "tool": "mating_recommendations",
  "arguments": {
    "animal_id": "430735-0089",
    "breed_id": 486,
    "target_traits": "WWT,EMD,NLB",
    "max_results": 3
  }
}
```

**Example response:**

```json
[
  {
    "mate_lpn_id": "430735-0032",
    "rank_score": 18.42,
    "coi": { "coefficient": 0.015, "rating": "Green" },
    "predicted_offspring_ebvs": {
      "BWT": 0.15,
      "WWT": 11.3,
      "EMD": 1.8,
      "NLB": 0.12
    }
  },
  {
    "mate_lpn_id": "410220-0015",
    "rank_score": 16.80,
    "coi": { "coefficient": 0.0, "rating": "Green" },
    "predicted_offspring_ebvs": {
      "BWT": -0.05,
      "WWT": 9.8,
      "EMD": 2.1,
      "NLB": 0.08
    }
  }
]
```

**How to present recommendations:**

| Rank | Mate | Score | COI | Pred. BWT | Pred. WWT | Pred. EMD | Pred. NLB |
|---|---|---|---|---|---|---|---|
| 1 | 430735-0032 | 18.42 | 1.5% | +0.15 | +11.3 | +1.8 | +0.12 |
| 2 | 410220-0015 | 16.80 | 0.0% | -0.05 | +9.8 | +2.1 | +0.08 |

The predicted offspring EBVs are midparent values: `(sire_EBV + dam_EBV) / 2`.

---

### flock_summary

Summarize a flock: animal count, gender breakdown, and average EBV traits.

| Parameter | Type | Required | Description |
|---|---|---|---|
| `flock_id` | string | yes | Flock ID |
| `breed_id` | integer | no | Filter to a specific breed within the flock |

**Example:**

```json
{
  "tool": "flock_summary",
  "arguments": { "flock_id": "430735", "breed_id": 486 }
}
```

**Example response:**

```json
{
  "flock_id": "430735",
  "total_count": 87,
  "sample_size": 87,
  "males": 12,
  "females": 75,
  "trait_averages": {
    "BWT": 0.32,
    "WWT": 8.45,
    "YWT": 12.10,
    "NLB": 0.08,
    "EMD": 0.95,
    "FAT": -0.18
  }
}
```

**When to use**: For flock-level analysis. Compare `trait_averages` against
`trait_ranges` to identify where the flock sits relative to the breed.

---

### database_status

Check when the NSIP database was last updated and what animal statuses are available.
No parameters.

**Example:**

```json
{
  "tool": "database_status",
  "arguments": {}
}
```

**When to use**: Before any analysis session, confirm the database is current.
Mention the last-updated date when presenting results to farmers.

---

## Workflow Recipes

### Recipe 1: Full Animal Evaluation

**Goal**: Provide a farmer with a complete breeding assessment of one animal.

**Steps:**

1. Call `profile` to get details, pedigree, and progeny in one request.
2. Extract the `breed_id` from the response (or ask the user).
3. Call `trait_ranges` for that breed.
4. For each EBV trait, calculate where the animal falls within the breed range.

**Presenting results — example for a ram:**

> **Ram 430735-0032** (Poll Dorset, born 15 Aug 2022)
>
> | Trait | Value | Accuracy | Breed Range | Position |
> |---|---|---|---|---|
> | Birth Weight | +0.28 lbs | 72% | -1.2 to +2.8 | Below average — good (lower is better) |
> | Weaning Weight | +9.6 lbs | 68% | -5.0 to +18.5 | Above average — lambs will be heavier at weaning |
> | Yearling Weight | +14.2 lbs | 55% | -8.0 to +25.3 | Above average — good growth to market |
> | Eye Muscle Depth | +1.1 mm | 48% | -1.5 to +3.2 | Above average — better muscling |
> | Fat Depth | -0.3 mm | 51% | -1.8 to +1.5 | Below average — leaner carcass |
> | Lambs Born | +0.05 | 38% | -0.15 to +0.32 | Near average — limited maternal data |
>
> **Strengths**: Good growth (WWT, YWT) with low birth weight — lambs should be
> born easily and grow well. Lean carcass suits premium markets.
>
> **Weaknesses**: Limited accuracy on NLB — not yet proven as a maternal sire.
> EMD accuracy is moderate; more data would strengthen confidence.
>
> **Recommended use**: Terminal sire over commercial ewes. Not yet proven for
> breeding replacement ewes.

---

### Recipe 2: Mating Safety Check

**Goal**: Determine whether a planned sire × dam mating is safe.

**Steps:**

1. Call `inbreeding_check` with `sire_id` and `dam_id`.
2. Interpret the COI rating.
3. If Green, call `details` for both animals and present predicted offspring EBVs.
4. If Yellow or Red, call `mating_recommendations` to suggest safer alternatives.

**Presenting results — safe mating:**

> **Mating Plan: 430735-0032 × 430735-0089**
>
> Inbreeding coefficient: **3.1%** — **Green** (safe to proceed)
>
> One shared ancestor found (410220-0008) at 2 generations from both sire and dam.
> This is a distant enough relationship to pose minimal risk.
>
> **Predicted offspring EBVs** (midparent values):
> | Trait | Sire | Dam | Predicted Offspring |
> |---|---|---|---|
> | BWT | +0.28 | +0.02 | +0.15 |
> | WWT | +9.6 | +7.2 | +8.4 |
> | NLB | +0.05 | +0.18 | +0.12 |

**Presenting results — risky mating:**

> **Mating Plan: 430735-0032 × 430735-0018**
>
> Inbreeding coefficient: **12.5%** — **Red** (avoid this mating)
>
> These animals share a close ancestor (430735-0005) at 1 generation from both
> sire and dam, meaning the offspring would be equivalent to a full-sibling cross.
>
> **Recommendation**: Do not proceed. Consider these alternative sires instead:
> *(then call `mating_recommendations` for the dam and present alternatives)*

---

### Recipe 3: Flock Improvement Analysis

**Goal**: Identify where a flock needs genetic improvement.

**Steps:**

1. Call `flock_summary` with the flock ID.
2. Call `trait_ranges` for the breed.
3. Compare flock averages to breed midpoint `(min + max) / 2`.
4. Flag traits where the flock falls below the breed midpoint.
5. Call `rank` with weights targeting the weak traits to find sires that could improve them.

**Presenting results:**

> **Flock 430735 — Poll Dorset (87 animals: 12 rams, 75 ewes)**
>
> | Trait | Flock Average | Breed Midpoint | Status |
> |---|---|---|---|
> | BWT | +0.32 | +0.80 | Below midpoint — good (lower is better) |
> | WWT | +8.45 | +6.75 | Above midpoint |
> | YWT | +12.10 | +8.65 | Above midpoint |
> | EMD | +0.95 | +0.85 | Above midpoint |
> | NLB | +0.08 | +0.09 | Near midpoint — room for improvement |
> | FAT | -0.18 | -0.15 | Near midpoint |
>
> **Strengths**: Growth traits (WWT, YWT) are well above breed average.
>
> **Improvement opportunities**: NLB is at breed midpoint — selecting sires with
> higher NLB could boost lambing rates. Consider rams ranked by maternal traits.

---

### Recipe 4: Compare Sire Candidates

**Goal**: A farmer has 2–3 rams to choose from and needs help deciding.

**Steps:**

1. Call `compare` with the LPN IDs.
2. For each trait, identify the best and worst animal.
3. Call `trait_ranges` and position each animal within the breed.
4. Summarize trade-offs and recommend based on the farmer's breeding objective.

**Key question to ask the farmer**: "Are you looking for a terminal sire (maximise
lamb growth for market) or a maternal sire (improve lambing rates and ewe
productivity)?" — the answer determines which traits matter most.

---

### Recipe 5: Enriching a Breeding Record Issue

**Goal**: An issue was created with a `record:mating` label. Enrich it with NSIP data.

**Steps:**

1. Extract `sire_lpn` and `dam_lpn` from the issue body.
2. Call `inbreeding_check` with `sire_id` and `dam_id`.
3. Call `details` for both animals.
4. Call `compare` on the pair.
5. Post an enrichment comment with:
   - COI result and traffic-light rating
   - Side-by-side EBV comparison table
   - Predicted offspring EBVs (midparent values)
   - Any concerns or recommendations
6. Add the `enriched` label to the issue.

---

## EBV Trait Glossary

EBVs (Estimated Breeding Values) predict the genetic merit an animal passes to its
offspring. They are expressed as deviations from a breed average — positive means
above average, negative means below.

| Abbreviation | Full Name | Unit | What It Means in Practice | Selection |
|---|---|---|---|---|
| BWT | Birth Weight | lbs | Heavier or lighter lambs at birth. Lower BWT reduces difficult births (dystocia). | Lower preferred |
| WWT | Weaning Weight | lbs | How heavy lambs are at weaning (~60 days). Higher means faster early growth. | Higher preferred |
| PWWT | Post-Weaning Weight | lbs | Growth after weaning. Important for animals staying on farm longer. | Higher preferred |
| YWT | Yearling Weight | lbs | Weight at ~12 months. Key for market lamb production. | Higher preferred |
| FAT | Fat Depth | mm | Backfat at the 12th–13th rib. Affects carcass grading and market premiums. | Moderate preferred |
| EMD | Eye Muscle Depth | mm | Loin muscle size. More muscling = more meat per carcass. | Higher preferred |
| NLB | Number of Lambs Born | lambs | How many lambs a ewe produces per lambing. Key fertility trait. | Higher (with caution) |
| NWT | Number of Lambs Weaned | lambs | How many lambs survive to weaning. Reflects mothering ability. | Higher preferred |
| PWT | Pounds Weaned | lbs | Total weight of all lambs weaned per ewe. Combines fertility + growth. | Higher preferred |
| DAG | Dag Score | score | Fecal soiling around the breech. Affects flystrike risk and shearing ease. | Lower preferred |
| WGR | Wool Growth Rate | g/day | Daily wool growth. Important for wool-focused enterprises. | Higher (wool breeds) |
| WEC | Worm Egg Count | eggs/g | Intestinal parasite burden. Lower means better natural resistance. | Lower preferred |
| FEC | Faecal Egg Count | eggs/g | Alternate parasite measure. Lower means fewer drenches needed. | Lower preferred |

### Understanding Accuracy

Accuracy (%) indicates how reliable an EBV is:

| Accuracy | Reliability | Typical Source |
|---|---|---|
| < 40% | Low | Limited data, young animal, few relatives measured |
| 40–60% | Moderate | Own performance + some progeny data |
| 60–80% | High | Good progeny data from multiple flocks |
| > 80% | Very high | Extensive progeny testing, proven sire |

**Rule of thumb**: For important breeding decisions (selecting a sire to use across
a flock), prefer animals with accuracy above 50%. For initial screening, lower
accuracy is acceptable.

---

## Formatting Rules

When presenting NSIP data to farmers, follow these conventions:

1. **Always use tables** for EBV data — never dump raw JSON.

2. **Show accuracy** alongside every EBV value: `+9.6 (68%)`.

3. **Explain in plain language** what each value means practically:
   - Say "lambs will be about 9.6 lbs heavier at weaning"
   - Not "WWT EBV is +9.6"

4. **Use the traffic light** for COI results:
   - Green: "Safe — this mating has low inbreeding risk"
   - Yellow: "Caution — consider alternative sires"
   - Red: "Avoid — high risk of inbreeding depression"

5. **Include breed context** whenever possible. A WWT of +9.6 means little
   without knowing the breed range.

6. **Caveat low accuracy**: If a key trait has accuracy below 40%, note that
   the prediction may change as more data becomes available.

7. **Use the trait's natural units**: lbs for weights, mm for depth/fat,
   lambs for NLB/NWT, eggs/g for parasite counts.
