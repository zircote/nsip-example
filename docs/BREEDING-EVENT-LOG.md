# Breeding Event Log

Using GitHub Issues as a structured breeding record-keeping system for sheep flocks,
enriched with NSIP genetic data.

## Overview

Each breeding observation -- mating, lambing, health event, weaning, sale, or death --
is captured as a GitHub Issue with a `record:*` label. An AI agent monitors new issues,
extracts animal identifiers (LPN IDs), queries the NSIP MCP server for genetic data, and
posts an enrichment comment with EBVs, lineage, and breeding analysis.

Over time, issues compile into a chronological event log that tracks flock performance
across seasons.

### Label Taxonomy

| Label | Description |
|---|---|
| `record:mating` | Planned or completed mating |
| `record:lambing` | Lambing event with birth details |
| `record:health` | Health observation or treatment |
| `record:weaning` | Weaning weights and dates |
| `record:sale` | Animal sale or transfer |
| `record:death` | Death or culling record |
| `enriched` | Agent has added NSIP data |

## Record Types

### Mating Record (`record:mating`)

Records a planned or completed mating between a sire and dam.

**Required fields:**
- Sire LPN ID
- Dam LPN ID
- Mating date (YYYY-MM-DD)
- Breeding method (Natural, AI, Embryo Transfer)

**Optional fields:**
- Notes (synchronization protocol, repeat mating, etc.)

**Agent enrichment:**
1. Runs `inbreeding_check` on the sire/dam pair to report the coefficient of inbreeding (COI)
   for predicted offspring and flags high-risk matings.
2. Calls `details` for both sire and dam to retrieve current EBVs.
3. Calls `compare` on the pair to show trait complementarity across key indexes
   (MP+, DP+, FP+) and individual EBVs (BWT, WWT, YWT, NLB, NLW, WEC).
4. Calls `mating_recommendations` for the dam to show how this sire ranks among
   recommended mates.
5. Posts a formatted comment with COI assessment, EBV comparison table, and
   index predictions for offspring.

### Lambing Record (`record:lambing`)

Records a lambing event with birth details for each lamb.

**Required fields:**
- Dam LPN ID
- Lambing date (YYYY-MM-DD)
- Number born
- Number born alive

**Optional fields:**
- Birth weights (kg) per lamb
- Sex of each lamb (Ram, Ewe, Wether)
- Sire LPN ID (if known)
- Lambing ease score (1-5)
- Notes (assistance required, presentation, fostering)

**Agent enrichment:**
1. Calls `details` for the dam to retrieve her NLB (Number of Lambs Born) and
   NLW (Number of Lambs Weaned) EBVs.
2. Calls `trait_ranges` for NLB and NLW to show where the dam sits relative to
   breed percentile bands.
3. If sire is provided, calls `lineage` on both parents for pedigree context.
4. Posts a comment comparing actual litter size against the dam's NLB EBV and
   breed average, with a historical lambing summary if prior records exist.

### Health Record (`record:health`)

Records a health observation, diagnosis, or treatment.

**Required fields:**
- Animal LPN ID
- Date (YYYY-MM-DD)
- Condition or diagnosis

**Optional fields:**
- Treatment administered
- Veterinarian notes
- Follow-up date
- Body condition score (1-5)

**Agent enrichment:**
1. Calls `details` for the animal to pull its current EBV profile.
2. For parasite-related conditions (worms, fluke, barber pole), highlights the
   animal's WEC (Worm Egg Count) and PWEC (Post-Weaning WEC) EBVs and calls
   `trait_ranges` to show breed-relative standing.
3. Calls `lineage` to flag whether susceptibility patterns appear in the pedigree.
4. Posts a comment with the animal's health-related EBVs and any pedigree patterns.

### Weaning Record (`record:weaning`)

Records weaning weights for a group of lambs.

**Required fields:**
- Weaning date (YYYY-MM-DD)
- Animal LPN IDs and weights (one per line, format: `LPN_ID: weight_kg`)

**Optional fields:**
- Age at weaning (days)
- Management group
- Notes

**Agent enrichment:**
1. Calls `details` for each animal to retrieve WWT (Weaning Weight) EBVs.
2. Calls `compare` across the weaning group to rank animals by WWT EBV and
   actual weight.
3. Calls `trait_ranges` for WWT to show breed percentile context.
4. For each lamb, calls `details` on the dam to show her PEMD (Post-Weaning
   Eye Muscle Depth) and PFAT (Post-Weaning Fat) maternal contribution.
5. Posts a ranked weaning summary table with actual weights, WWT EBVs, and
   breed percentile bands.

### Sale Record (`record:sale`)

Records an animal leaving the flock through sale or transfer.

**Required fields:**
- Animal LPN ID
- Sale date (YYYY-MM-DD)

**Optional fields:**
- Buyer name
- Sale price
- Destination flock
- Sale type (private treaty, auction, stud sale)
- Notes

**Agent enrichment:**
1. Calls `profile` to generate a comprehensive animal summary with all EBVs
   and index values.
2. Calls `lineage` for complete pedigree information.
3. Posts a formatted animal profile card suitable for record-keeping, including
   key indexes (MP+, DP+, FP+) and trait EBVs.

### Death/Cull Record (`record:death`)

Records an animal death or culling decision.

**Required fields:**
- Animal LPN ID
- Date (YYYY-MM-DD)
- Cause (disease, predation, age, culled -- structural, culled -- performance, other)

**Optional fields:**
- Age at death
- Notes

**Agent enrichment:**
1. Calls `profile` to archive the animal's complete genetic record.
2. Calls `progeny` to list any living offspring in the flock.
3. Posts a final profile comment for permanent record-keeping, noting any
   active progeny that carry the animal's genetics.

## Agent Workflow

The AI agent (GitHub Copilot or a custom GitHub Actions bot) processes breeding
records through the following pipeline:

```
1. Issue created with `record:*` label
       |
2. Agent triggers on issue event
       |
3. Agent reads issue body
       |
4. Agent extracts LPN IDs from form fields
       |
5. Agent calls NSIP MCP tools:
       - details / profile    -- animal data
       - lineage              -- pedigree context
       - inbreeding_check     -- COI for matings
       - trait_ranges          -- breed percentiles
       - compare              -- multi-animal analysis
       - mating_recommendations -- sire rankings
       - progeny              -- offspring lookup
       |
6. Agent formats enrichment comment
       |
7. Agent posts comment on the issue
       |
8. Agent adds `enriched` label
```

### Enrichment Comment Format

Each enrichment comment follows a consistent structure:

```markdown
## NSIP Enrichment

### Animal: [Name] (LPN: [ID])
**Breed:** [breed] | **Flock:** [flock] | **DOB:** [date]

### Key Indexes
| Index | Value | Percentile |
|-------|-------|------------|
| MP+   | 152.3 | Top 20%    |
| DP+   | 148.7 | Top 25%    |

### Selected EBVs
| Trait | EBV   | Accuracy | Breed Avg |
|-------|-------|----------|-----------|
| BWT   | 0.32  | 68%      | 0.28      |
| WWT   | 2.45  | 72%      | 1.90      |
| YWT   | 4.10  | 65%      | 3.50      |

### Analysis
[Context-specific analysis based on record type]
```

## Event Log Compilation

A scheduled GitHub Actions workflow compiles breeding records into a
periodic summary.

### Weekly Digest Workflow

The workflow runs on a weekly schedule and:

1. Queries all issues with `record:*` labels from the past week.
2. Sorts events chronologically by the date field in each record.
3. Creates a summary issue (`event-log:weekly`) with:
   - Timeline of events grouped by day
   - Counts by record type (matings, lambings, health events, etc.)
   - Any flagged concerns (high COI matings, health clusters)

### Seasonal Summary

At the end of each lambing or mating season, a manual workflow trigger
generates a season report:

- **Mating season:** Number of matings planned, sires used, average COI
- **Lambing season:** Total lambs born, born alive, mortality rate, average
  birth weight, sex ratio
- **Weaning:** Average weaning weight, top/bottom performers by WWT EBV
- **Trait trends:** Flock-average EBV movement compared to prior seasons

The summary is posted as a milestone issue or committed as a markdown file
in `docs/seasons/`.

## NSIP MCP Tools Reference

The following NSIP MCP server tools power the enrichment pipeline:

| Tool | Purpose | Used By |
|---|---|---|
| `details` | Retrieve individual animal EBVs and identification | All record types |
| `profile` | Comprehensive animal summary with indexes | Sale, Death records |
| `lineage` | Sire/dam/grandparent pedigree tree | Mating, Lambing, Health |
| `inbreeding_check` | COI calculation for a sire/dam pair | Mating records |
| `mating_recommendations` | Ranked sire suggestions for a dam | Mating records |
| `trait_ranges` | Breed percentile bands for a trait | Lambing, Weaning, Health |
| `compare` | Side-by-side EBV comparison of multiple animals | Mating, Weaning |
| `progeny` | List offspring of an animal | Death records |
| `search` | Find animals by name, ID, or flock | All (ID resolution) |
| `rank` | Rank animals within a flock by trait or index | Seasonal summaries |
| `flock_summary` | Aggregate flock statistics | Seasonal summaries |

## Getting Started

1. **Create labels.** Add the `record:*` labels and `enriched` label to your
   repository. Use consistent colors (e.g., green for `record:mating`,
   blue for `record:lambing`, red for `record:health`).

2. **Enable issue templates.** The templates in `.github/ISSUE_TEMPLATE/` provide
   structured forms for each record type.

3. **Configure the agent.** Set up GitHub Copilot coding agent or a GitHub Actions
   workflow that triggers on `issues.opened` and `issues.labeled` events, with
   access to the NSIP MCP server.

4. **Start recording.** Create issues using the templates. The agent will
   automatically enrich each record within minutes.

5. **Review and close.** After reviewing the enrichment, close the issue to mark
   the record as complete. Closed issues remain searchable and contribute to
   season summaries.
