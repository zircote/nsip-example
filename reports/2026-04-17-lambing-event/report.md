# Lambing Event Enrichment — 6401492023FLE078 × 6401492025FLE141

Closes #28

**Date**: April 17, 2026
**Event**: Lambing Record — Twin Birth
**Breed**: Katahdin
**Database Last Updated**: March 22, 2026

---

## Event Summary

| Field | Value |
|-------|-------|
| Dam LPN | 6401492023FLE078 |
| Sire LPN | 6401492025FLE141 |
| Lambing Date | 2026-04-17 |
| Number Born | 2 |
| Number Born Alive | 2 |
| Survival Rate | 100% |
| Lamb Details | Ram: EPC006; Ewe: EPC007 |
| Lambing Ease | None recorded |
| Notes | — |

**Good outcome**: Two lambs born alive with 100% early survival. This is a productive twin lambing for a young ewe.

---

## Inbreeding Safety Check (Sire × Dam)

| Metric | Result |
|---|---|
| COI | **18.75%** |
| Rating | **Red** |
| Shared ancestor | 6401492018DRW522 |

**Interpretation**: **Red — avoid repeating this pairing.** This level is above the 12.5% red-line threshold and carries elevated risk for inbreeding depression (reduced fertility, survival, and growth).

---

## Dam Profile — 6401492023FLE078

**Breed**: Katahdin | **Born**: February 21, 2023 | **Status**: CURRENT
**Flock**: Beyond Blessed Farm (Abingdon, VA) | **Total Progeny (before this event)**: 0
**US Hair Index**: 100.10 | **SRC Index**: 105.48

### Dam EBVs vs. Breed (Katahdin)

| Trait | EBV | Accuracy | Breed Range | Percentile | Notes |
|-------|-----|----------|-------------|------------|-------|
| BWT | +0.31 lbs | 64% | -0.94 to +1.30 | 55th | Near average birth weight |
| WWT | +1.65 lbs | 62% | -3.02 to +6.19 | 51st | Near average weaning growth |
| PWWT | +1.64 lbs | 61% | -7.11 to +9.43 | 53rd | Near average post-weaning growth |
| YWT | +0.68 lbs | 52% | -9.53 to +10.27 | 52nd | Near average yearling growth |
| NLB | -0.05 lambs | 50% | -0.36 to +0.69 | 29th | Below average litter-size EBV |

---

## Sire Profile — 6401492025FLE141

**Breed**: Katahdin | **Born**: February 24, 2025 | **Status**: CURRENT
**Flock**: Beyond Blessed Farm (Abingdon, VA) | **Total Progeny (before this event)**: 0
**US Hair Index**: 101.85 | **SRC Index**: 114.18

### Sire EBVs vs. Breed (Katahdin)

| Trait | EBV | Accuracy | Breed Range | Percentile | Notes |
|-------|-----|----------|-------------|------------|-------|
| BWT | +0.27 lbs | 61% | -0.94 to +1.30 | 54th | Near average birth weight |
| WWT | +1.29 lbs | 59% | -3.02 to +6.19 | 47th | Near average weaning growth |
| PWWT | +2.52 lbs | 58% | -7.11 to +9.43 | 58th | Slightly above average post-weaning growth |
| YWT | +2.22 lbs | 47% | -9.53 to +10.27 | 59th | Slightly above average yearling growth |
| NLB | -0.02 lambs | 38% | -0.36 to +0.69 | 33rd | Below average, low-accuracy maternal signal |

> **Accuracy note**: Sire NLB accuracy is low (38%), so this maternal fertility estimate may shift as more progeny data is added.

---

## Predicted Offspring Profile

Calculated as midparent values: `(sire_EBV + dam_EBV) / 2`

| Trait | Dam EBV | Sire EBV | Predicted Offspring | Breed Midpoint | vs. Midpoint |
|-------|---------|----------|---------------------|----------------|--------------|
| BWT | +0.31 | +0.27 | **+0.29 lbs** | +0.18 | Slightly above average |
| WWT | +1.65 | +1.29 | **+1.47 lbs** | +1.59 | Slightly below midpoint |
| PWWT | +1.64 | +2.52 | **+2.08 lbs** | +1.16 | Above average |
| YWT | +0.68 | +2.22 | **+1.45 lbs** | +0.37 | Above average |
| NLB | -0.05 | -0.02 | **-0.03 lambs** | +0.16 | Below average |

---

## Pedigree and Relationship Risk

### Dam Lineage (6401492023FLE078)

- Sire: 6401492018DRW522
- Dam: 6401492021FLE144

### Sire Lineage (6401492025FLE141)

- Sire: 6401552024GBR123
- Dam: 6401492020FLE205
- Maternal grandsire: 6401492018DRW522

**Key relationship**: 6401492018DRW522 appears in both pedigrees at very close depth, which aligns with the **Red (18.75%)** inbreeding result.

---

## Analysis and Recommendations

1. **Record birth weights** for EPC006 and EPC007 as soon as possible so NSIP can strengthen BWT and growth evaluations.
2. **Do not repeat this sire-dam pairing** next season due to Red COI risk.
3. **Use a less-related ram for future breedings** of FLE078 and run `inbreeding_check` before pairing.
4. **Track weaning weights** (~60 days, mid-June 2026) to improve WWT/PWWT accuracies for both parents.

---

## Trait Glossary

- **BWT**: Birth Weight (lbs), lower is usually preferred for easier lambing.
- **WWT**: Weaning Weight (lbs), higher indicates stronger early growth.
- **PWWT**: Post-Weaning Weight (lbs), higher supports market growth after weaning.
- **YWT**: Yearling Weight (lbs), higher supports heavier market lamb potential.
- **NLB**: Number of Lambs Born, higher supports higher lambing rate.

---

*Report generated from NSIP database, last updated March 22, 2026. EBV values may change as additional performance data is recorded.*
