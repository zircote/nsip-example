# Copilot Instructions for Epic Pastures Demo Farm

This repository manages farm operations for a 45-acre farm
in Farmville, VA.

## Farm Profile

- **Location:** Farmville, VA
- **Size:** 45 acres
- **Primary Products:** Market garden (seasonal), eggs (seasonal)
- **Livestock:** Katahdin hair sheep, chickens, ducks, turkeys
- **Key Equipment:** John Deere 6120M tractor, Kubota ZD1211 mower

## Writing Style

When drafting Issues or documentation:

- Use plain, practical language (avoid jargon)
- Be specific about locations (field names, barn sections)
- Include relevant dates and timeframes
- Mention equipment by name when applicable
- Consider weather and seasonal factors

## Common Tasks

- Equipment maintenance and repair tracking
- Market garden planting and harvest scheduling
- Livestock health records and feeding schedules
- Egg production and seasonal sales tracking
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

### EOV (Ecological Outcome Verification)

This farm tracks ecological health using the Savory Institute's EOV framework.
Monitoring covers pastures, crop fields, riparian zones, and woodlots.

#### EOV Records

Issues with `record:eov-*` labels are ecological monitoring records. When an
EOV record is opened, enrich it by:
1. Comparing current scores to previous assessments at the same site
2. Calculating trend direction (improving / stable / declining)
3. Flagging any indicators that have dropped significantly
4. Posting a formatted enrichment comment

See `.github/instructions/eov.instructions.md` for the full enrichment
workflow, indicator glossary, and formatting rules.

#### EOV Actions

Issues with the `eov-action` label request automated EOV analyses (seasonal
summaries, site comparisons, trend reports). Parse the issue form fields,
analyze the data, and produce a report PR in `reports/`.

## Labels

Use these categories when suggesting labels:

- Domain: crops, livestock, equipment, compliance, eov
- Type: maintenance, repair, inspection, planning, health, field-observation, verification
- Priority: urgent, routine, seasonal
- Status: waiting-on-parts, waiting-on-weather, waiting-on-vet
- Breeding records: record:mating, record:lambing, record:health, record:weaning, record:sale, record:death
- EOV records: record:eov-site-assessment, record:eov-soil-sample, record:eov-water-test, record:eov-photo-point
- Flock actions: flock-action
- EOV actions: eov-action
- Agent status: enriched, eov-enriched
