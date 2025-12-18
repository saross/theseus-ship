# Methodological Decisions

**Purpose**: Record scoping and methodological decisions for the paper, with rationale.

**Created**: 2025-12-18

---

## Scope Decisions

### 1. Focus on Complete Pipeline Tools Only

**Decision**: Include only tools that passed through all three research phases:
1. Discovery (LLM-assisted identification)
2. Metadata collection (structured documentation)
3. Evidence-of-life collection (lifecycle documentation)

**Rationale**:
- Ensures consistent treatment across all analysed tools
- OpenArchaeo no-DVCS tools only received evidence collection, not metadata
- Space constraints require focused analysis

**Implications**:
- Exclude 214 evidence events from OpenArchaeo no-DVCS pathway (23 tools)
- Exclude OpenArchaeo baseline comparison from paper
- Focus on 965 evidence events from Discovery pathway

**Date**: 2025-12-18

---

### 2. OpenArchaeo Exclusion

**Decision**: Do not discuss OpenArchaeo pathway in the paper.

**Rationale**:
- No OpenArchaeo-unique tools were analysed through the full pipeline
- The 20 tools that overlapped with Discovery were already covered via that pathway
- The 23 no-DVCS tools investigated for evidence only (no metadata) represent incomplete analysis
- Severe space constraints

**What OpenArchaeo contributed**:
- 513 items in export
- 375 classified as tools (372 unique after case-insensitive deduplication)
- 20 overlapped with LLM Discovery (already investigated via that pathway)
- 355 unique to OpenArchaeo — none investigated for metadata
- 23 no-DVCS tools investigated for evidence only (150 events)

**Date**: 2025-12-18

---

## Verification Decisions

### 3. Verification Status Categories (from Dec 14 session)

**Categories**:
- **CONFIRMED**: Tool exists and is correctly identified as archaeological/research software
- **MISATTRIBUTED**: Tool exists but is generic software, not research-specific
- **CONFABULATED**: Tool does not exist, OR presence in source was fabricated

**Key rules**:
- Successful metadata collection always means CONFIRMED
- Commercial software repurposed for research = CONFIRMED
- Research vs generic is deciding factor, not commercial vs non-commercial

---

## Inclusion Criteria

### 4. Tool Definition Boundaries

**Included**:
- Research-specific software (purpose-built for archaeology/research)
- Commercial software repurposed for research (e.g., Agisoft PhotoScan)
- Plugins/extensions to generic platforms when research-specific
- 3D modelling tools used for archaeological visualisation

**Excluded**:
- Generic platforms (QGIS, ArcGIS, Excel, MATLAB, R itself)
- Databases/repositories (Open Context, tDAR, ADS)
- Infrastructure/portals (HEIRPORT, national heritage systems)

---

## Notes

- This document captures decisions; see `key-quantitative-findings.md` for detailed data accounting
- See `session-handover.md` for verification workflow details
