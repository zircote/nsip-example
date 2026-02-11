# Changelog

All notable changes to the Epic Pastures Demo Farm repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [0.4.0] - 2026-02-11

### Added

- **EOV Integration**: Ecological Outcome Verification framework for tracking land health
  - 4 monitoring record templates: site assessment, soil sample, water infiltration test, photo point
  - 1 action template for automated EOV analyses (seasonal summaries, site comparisons, trend reports, enrollment readiness)
  - `eov/` directory with monitoring plan, site map (12 STM + 3 LTM sites), baseline summary, and outcome goals
  - Copilot enrichment instructions (`eov.instructions.md`) with score mapping, 4 enrichment recipes, 4 action recipes, indicator glossary, and formatting rules
  - EOV enrichment workflow — auto-assigns Copilot on `record:eov-*` and `eov-action` issues
  - Quarterly seasonal reminder workflow — creates monitoring checklists on Mar 1, Jun 1, Sep 1, Dec 1
  - 4 runbooks: recording a site assessment, recording a soil sample, recording a water test, requesting an EOV analysis
  - 8 new labels: `eov`, `record:eov-site-assessment`, `record:eov-soil-sample`, `record:eov-water-test`, `record:eov-photo-point`, `eov-enriched`, `eov-action`, `verification`

### Changed

- Update `copilot-instructions.md` with EOV section, EOV labels, and link to `eov.instructions.md`
- Update weekly reminder workflow with "Land & Ecology" checklist section
- Update `USER-GUIDE.md` with `eov/` in folder table, 4 EOV runbook links, and "Tracking Land Health" section
- Update `README.md` with EOV badge, EOV section, Savory Institute links, EOV templates in record list, and `eov/` in Quick Links

## [0.3.0] - 2026-02-08

### Added

- Sale and death record templates with runbooks
- Flock rank action with reports (PR [#2](https://github.com/zircote/nsip-example/pull/2))
- Social preview image and infographic for GitHub repository

### Changed

- Rename farm from "Sunny Acres" to "Epic Pastures" across all files
- Update farm profile to 45-acre Farmville, VA operation
- Update livestock records for sheep and poultry operation
- Update crop records for market garden and pasture
- Update equipment records for small farm operation
- Update compliance records for small farm operation

### Fixed

- Align documentation with actual templates and codebase
- Align runbooks with updated farm profile

## [0.2.0] - 2026-02-07

### Added

- User guide for non-technical farm staff (`docs/USER-GUIDE.md`)
- 11 step-by-step runbooks (mating, lambing, weaning, health, sale, death, flock analysis, crop issues, equipment, finding records, weekly checklist)
- README automation section with workflows and NSIP tools

### Changed

- Update copilot instructions and labels for breeding records

## [0.1.0] - 2026-02-07

### Added

- Initial farm repository structure with `crops/`, `livestock/`, `equipment/`, `compliance/` directories
- NSIP MCP server integration (`.mcp.json`) for sheep genetic data
- 4 breeding record issue templates: mating, lambing, health, weaning
- Flock action issue template for automated analyses
- Copilot instructions with NSIP MCP tool reference and workflow recipes
- `nsip-mcp.instructions.md` with 5 enrichment recipes and EBV glossary
- Flock action workflow for Copilot auto-assignment
- Weekly farm reminder workflow (Monday at 8 AM UTC)
- Copilot setup steps workflow
- Dependabot automerge workflow
- GitHub labels for farm domains, task types, priorities, statuses, and breeding records

[Unreleased]: https://github.com/zircote/nsip-example/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/zircote/nsip-example/compare/eaa0d7b...v0.4.0
[0.3.0]: https://github.com/zircote/nsip-example/compare/1c0984a...eaa0d7b
[0.2.0]: https://github.com/zircote/nsip-example/compare/d82ea0b...1c0984a
[0.1.0]: https://github.com/zircote/nsip-example/compare/3b970f9...d82ea0b
