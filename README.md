# Epic Pastures Demo Farm

<!-- Social Preview -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/social-preview-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/social-preview.svg">
  <img alt="Epic Pastures Demo Farm — happy farm animals on a green field" src=".github/social-preview.svg" width="100%">
</picture>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/zircote/nsip-example?label=Records&color=blue)](https://github.com/zircote/nsip-example/issues)
[![NSIP Integration](https://img.shields.io/badge/NSIP-Integrated-2E7D32)](https://nsip.org)
[![GitHub Actions](https://img.shields.io/badge/Automation-GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/zircote/nsip-example/actions)

Welcome to the Epic Pastures farm repository — your digital barn for all farm information.

This repository does two things:

1. **Organizes farm records** into easy-to-browse folders (crops, livestock, equipment, compliance)
2. **Tracks sheep breeding** through a record-keeping system powered by the [National Sheep Improvement Program (NSIP)](https://nsip.org) genetic database

When you create a breeding record (mating, lambing, health, weaning), the system automatically looks up the animal's genetics and adds useful information like growth potential, inbreeding risk, and trait comparisons.

---

## Quick Links

| Section | What You'll Find |
|---------|-----------------|
| [Crops](./crops/) | Planting schedule, crop rotation, soil tests |
| [Livestock](./livestock/) | Health records, feeding schedule, vet log |
| [Equipment](./equipment/) | Maintenance log, safety inspections, inventory |
| [Compliance](./compliance/) | Grant tracking, certifications |

### Guides

| Guide | Description |
|-------|-------------|
| [User Guide](./docs/USER-GUIDE.md) | Start here — how to use this system (written for non-technical users) |
| [Runbooks](./docs/runbooks/) | Step-by-step instructions for common tasks |
| [Breeding Event Log](./docs/BREEDING-EVENT-LOG.md) | How the NSIP breeding record system works |

### Creating Records

Click the **Issues** tab above, then **New issue** to create a record. Available forms:

- **Mating Record** — Log a breeding pairing (auto-checks inbreeding risk)
- **Lambing Record** — Log a birth event
- **Health Record** — Log a health observation or treatment
- **Weaning Record** — Log weaning weights
- **Flock Action** — Request an automated flock analysis (compare, rank, mating recommendations)
- **Crop Issue Report** — Report a field problem
- **Equipment Maintenance** — Report an equipment issue

---

## How It Works

<picture>
  <img alt="How Epic Pastures Works — Create records, get automatic genetic enrichment, search your history" src=".github/readme-infographic.svg" width="100%">
</picture>

---

## Automation

This repository uses [GitHub Actions](https://github.com/zircote/nsip-example/actions) workflows and the [NSIP MCP server](https://github.com/zircote/nsip) to automate farm operations.

### Workflows

| Workflow | Trigger | What It Does |
|----------|---------|--------------|
| **Flock Action** | Issue opened with `flock-action` label | Auto-assigns [Copilot coding agent](https://docs.github.com/en/copilot) to run the requested flock analysis and produce a report |
| **Weekly Farm Reminder** | Every Monday at 8:00 AM UTC | Creates a checklist issue with equipment, livestock, crop, and administrative tasks for the week |
| **Copilot Setup** | Manual (on-demand) | Installs the `nsip` CLI binary and pulls the NSIP Docker image for the Copilot agent environment |
| **Dependabot Auto-Merge** | Dependabot PR opened | Automatically approves and merges dependency update PRs after CI passes |

### NSIP MCP Server

The [`.mcp.json`](.mcp.json) file configures a Docker-based [MCP](https://modelcontextprotocol.io) server that connects to the National Sheep Improvement Program database (400,000+ sheep). When a breeding record issue is created, the Copilot agent calls NSIP tools to enrich the record with genetic data:

| Tool | Purpose |
|------|---------|
| `search` | Find animals by name, ID, or flock |
| `details` / `profile` | Retrieve individual animal EBVs and indexes |
| `lineage` / `progeny` | Pedigree and offspring lookup |
| `compare` / `rank` | Side-by-side comparison or weighted ranking |
| `inbreeding_check` | Calculate coefficient of inbreeding for a pairing |
| `mating_recommendations` | Find optimal sires for a given dam |
| `trait_ranges` / `flock_summary` | Breed percentiles and aggregate flock statistics |

See [`.github/instructions/nsip-mcp.instructions.md`](.github/instructions/nsip-mcp.instructions.md) for the full tool reference.

---

## About This Farm

Epic Pastures is a 45-acre farm in Farmville, VA. We raise Katahdin hair sheep, chickens, ducks, and turkeys, and sell market garden produce and eggs seasonally.

**Contact:** hello@epicpastures.com

---

*This is a demo repository for [GitHub4Farms](https://github.com) training. All data is fictional.*
