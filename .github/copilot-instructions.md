# Copilot Instructions for Epic Pastures Demo Farm

This repository manages farm operations for a 320-acre diversified
Midwest agricultural operation.

## Farm Profile

- **Location:** Midwest United States
- **Size:** 320 acres
- **Primary Crops:** Corn, soybeans, wheat, alfalfa
- **Livestock:** 45 beef cattle, 12 dairy cows, 28 sheep, 3 horses
- **Key Equipment:** John Deere 6120M tractor, Case IH combine,
  center-pivot irrigation

## Writing Style

When drafting Issues or documentation:

- Use plain, practical language (avoid jargon)
- Be specific about locations (field names, barn sections)
- Include relevant dates and timeframes
- Mention equipment by name when applicable
- Consider weather and seasonal factors

## Common Tasks

- Equipment maintenance and repair tracking
- Crop planting and harvest scheduling
- Livestock health records and feeding schedules
- Compliance documentation (grants, certifications)
- Seasonal planning and task prioritization
- Breeding record keeping (mating, lambing, health, weaning)
- Flock genetic analysis and sire selection

## NSIP MCP Tools

This repository is configured with the NSIP MCP server (`.mcp.json`), which
provides access to the National Sheep Improvement Program database of 400,000+
sheep with estimated breeding values (EBVs).

Available tools: `search`, `details`, `lineage`, `progeny`, `profile`,
`breed_groups`, `trait_ranges`, `compare`, `rank`, `inbreeding_check`,
`mating_recommendations`, `flock_summary`, `database_status`.

See `.github/instructions/nsip-mcp.instructions.md` for full tool reference,
workflow recipes, and formatting rules.

### Breeding Records

Issues with `record:*` labels are structured breeding observations. When a
breeding record issue is opened, enrich it with NSIP data by calling the
appropriate MCP tools and posting a formatted comment. See
`docs/BREEDING-EVENT-LOG.md` for the full enrichment workflow.

### Flock Actions

Issues with the `flock-action` label request automated analyses. Parse the
issue form fields, call the appropriate MCP tools, and produce a report PR
in `reports/`. See `.github/instructions/flock-action.instructions.md`.

## Labels

Use these categories when suggesting labels:

- Domain: crops, livestock, equipment, compliance
- Type: maintenance, repair, inspection, planning, health
- Priority: urgent, routine, seasonal
- Status: waiting-on-parts, waiting-on-weather, waiting-on-vet
- Breeding records: record:mating, record:lambing, record:health, record:weaning, record:sale, record:death
- Flock actions: flock-action
- Agent status: enriched
