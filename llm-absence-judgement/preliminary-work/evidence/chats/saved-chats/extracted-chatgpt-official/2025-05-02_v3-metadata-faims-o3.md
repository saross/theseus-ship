# v3-Metadata-FAIMS-o3

## Metadata
- **Conversation ID:** `6815259d-c5d4-800c-b22d-3a3e44d4da58`
- **Created:** 2025-05-02 22:05:49
- **Updated:** 2025-12-07 21:39:09
- **Default Model:** `o3`
- **Project ID:** `g-p-682fbda4eb1c819180b176f6de9d9cd8`
- **Source:** Official ChatGPT Export

---

## Conversation

### Human (22:05:45)

we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.

# Archaeological Research Software Tools Metadata Collection

## Ground Rules
- ACCURACY FIRST: Do not make claims without supporting evidence. If uncertain, clearly indicate uncertainty. Double-check your work even if that requires more time.
- THOROUGH RESEARCH: Conduct comprehensive research using all available sources including repositories, scholarly literature, official documentation, and reliable mentions, even if it takes more time.
- METHODICAL APPROACH: Follow a systematic research process and document findings carefully.
- RECENCY FOCUS: All metadata must reflect the most recent version of the software as of the access date, unless specifically noted.
- CONTROLLED VOCABULARY: Strictly adhere to the provided controlled lists for compatibility with the Open-Archaeo project.

## Research Methodology
1. Begin with official sources (project website, documentation, repositories)
2. Expand to scholarly literature discussing the tool
3. Consider community resources and discussions
4. Synthesize findings with careful attention to recency and reliability
5. For subjective assessments (strengths, weaknesses, survivability), base conclusions on evidence rather than speculation


## Research Standards and Data Quality
When researching a tool, examine at least the first 20 search results, the tool's official documentation, its source code repositories, and any scholarly articles mentioning it. Prioritize official documentation and peer-reviewed publications over third-party blogs or forums.

For fields where information is unavailable after thorough research, use the following conventions:
- For URLs and other web addresses: leave field empty (do not use "N/A" or placeholder text)
- For categorical fields with controlled vocabulary: leave empty rather than guessing
- For open text fields requiring subjective assessment: provide your best assessment based on available evidence, but clearly indicate limitations (e.g., "Based on limited available information...")
- When sources conflict: prioritize official documentation, then peer-reviewed publications, then community consensus


## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "History", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"


## Column Specifications

### Version and Currency Determination
To identify the current version:
- Check release dates on repositories and official sites
- Look for "latest release" or "current version" indicators
- If version history is unclear, use the most recently documented version with evidence of being publicly available
- Note in the "Description" if the tool appears abandoned or unmaintained

### Essential Information
- **Tool**: Exact name as provided in the prompt
- **Description**: Clear, detailed overview (3-5 sentences) of the CURRENT version's purpose and functionality
- **History**: Chronological account of the tool's development, including major versions, significant updates, and evolution over time
- **Access-date**: Today's date in YYYY-MM-DD format, representing when this research was conducted
- **Tool-status**: One of three values based on the Research Software Tool Definition:
  * "yes" - clearly meets all essential criteria and sufficient supporting criteria
  * "maybe" - meets some criteria but with uncertainties or borderline characteristics 
  * "no" - clearly fails to meet essential criteria
- **Tool-status-reasoning**: Detailed explanation of classification decision referencing specific criteria from the framework; for "maybe" classifications, explicitly describe uncertainties or borderline aspects that prevent a definitive determination
- **DVCS-repo**: Primary repository URL (GitHub, GitLab, etc.) if available
- **CRAN**: URL if available
- **PyPi**: URL if available
- **Other-URL**: Primary project homepage or documentation site
- **Category**: Select one value from the Category controlled list below, using only the category name
- **Language**: Programming language(s) of CURRENT version, separated by pipes (|)
- **Platform**: Operating systems/environments supported by CURRENT version
- **Open-Archaeo-Platform**: Only if "Category" is "Packages and libraries", otherwise leave empty. When applicable, select from the Open-Archaeo-Platform controlled list below.

### Technical Characteristics (CURRENT VERSION ONLY)
- **License**: Most recent license, verified from official sources
- **Lifecycle-stage**: Research stages supported, selected from the Lifecycle-stage controlled list below. Multiple values should be pipe-separated.
- **Type**: Either "mass-market" or "research-specific"
- **Interoperability**: Focus on data input/output formats and exchange capabilities in the CURRENT version

### Assessment Criteria (CURRENT VERSION ONLY)
- **Strengths**: Evidence-based assessment of key advantages and research opportunities enabled
- **Weaknesses**: Evidence-based assessment of limitations, challenges, or potential risks
- **Survivability**: Assessment of long-term viability based on development activity, support, user community, and technical aspects
- **Alternatives**: Similar tools serving comparable functions
- **Authors**: Individual contributors (not organizations) separated by pipes
- **Tags**: Applicable terms selected from the Tags controlled list below, pipe-separated
- **AI-tags**: Five descriptive tags summarizing key aspects of the tool

## Controlled Vocabulary Lists

### Category Controlled List
- **Packages and libraries**: Sets of functions assembled with clear purpose, and made accessible using standards established by an underlying platform.
- **Stand-alone software**: Software that may be operated without needing to first access an underlying platform.
- **Scripts**: Sets of pragmatically assembled mutable functions, often lacking complete documentation or adherence to protocols that would otherwise facilitate secondary use outside their original contexts of creation.

### Open-Archaeo-Platform Controlled List
ArcGIS
AutoCAD
JavaScript
LibreOffice Calc
Lisp
Meshlab
Microsoft Excel
Nextflow
Open Data Kit
Piwigo
Python
QGIS
R
Stellarium

### Lifecycle-stage Controlled List
Planning
Data Acquisition
Processing
Analysis
Interpretation
Publication
Preservation and Reuse

### Tags Controlled List
Statistical analysis
Spatial analysis
Viewshed analysis
Site mapping
Harrix matrix
Chronological modelling
Seriation
Zooarchaeology
Palaeobotany
Artefact morphology
Literary analysis and epigraphy
Iconography
Shape recognition
3D modelling
Photogrammetry
Virtual reality
Augmented reality
Drones
Aerial and satellite imagery
Luminescence dating
X-Ray Fluorescence
Instrumental Neutron activation analysis
Radiocarbon dating, calibration and sequencing
Geophysical survey
Data management
Data collection
Lithic analysis
API interfaces and web scrapers
Datasets
Diagrams and visualizations
Platforms and publications
Schemas and ontologies
Templates
Drivers and IO
Educational resources and practical guides
Public archaeology
Public policy and civic action
Games
Writing
Lists
LiDAR
Museums
Bibliography
Archaeogenetics
Bits and bobs
Biological anthropology
Archaeoastronomy
Dendrochronology
Photography
Cultural evolution
Ethics and professional development
Simulation
Stable isotope analysis
Network analysis
Geoarchaeology
Machine learning
Palaeoclimate modelling
Ceramic analysis

## Research Software Tool Definition and Evaluation Framework

### Core Definition
A research software tool is specialized software that supports historical and archaeological research by facilitating data collection, processing, analysis, visualization, or dissemination in ways that contribute to scholarly inquiry beyond basic storage or display functions.

### Essential Criteria (Must Meet ALL)
1. **Research-Specific Purpose**: Primary function supports research activities rather than exclusively serving general computing tasks
2. **Research Data Engagement**: Collects, transforms, analyzes, visualizes, or facilitates sharing of research materials in discipline-relevant ways
3. **Methodological Alignment**: Functions in ways compatible with recognized research methodologies from historical disciplines, even if this alignment is implicit rather than explicitly stated

### Supporting Criteria (Must Meet at Least TWO)
1. **Domain Knowledge Integration**: Incorporates terminology, classifications, or procedures relevant to historical disciplines
2. **Research Lifecycle Support**: Addresses one or more research stages (planning, acquisition, processing, analysis, interpretation, publication, preservation)
3. **Data Transformation**: Converts between formats or representations relevant to historical research
4. **Analytical Capabilities**: Performs calculations, comparisons, or pattern recognition on historical data
5. **Visualization Functions**: Renders historical or archaeological data in meaningful visual formats
6. **Documentation Focus**: Contains documentation addressing research applications
7. **Data Collection**: Specifically designed for gathering research data in field or laboratory settings
8. **Data Dissemination**: Actively supports sharing, publication, or reuse of research data beyond simple storage

### Consideration Factors (Not Exclusionary, But Informative)
1. **Generic Functionality**: Degree to which functions extend beyond general-purpose software
2. **Passive Repository**: Extent of processing capabilities beyond storage
3. **Display-Only**: Presence of analytical or transformative functions beyond display
4. **Commercial Origin**: Despite commercial development, extent of significant research applications or adaptations

### Confidence Assessment
Based on available evidence, classify the tool as:
1. **Yes**: Clearly meets all essential criteria and sufficient supporting criteria
2. **Maybe**: Meets some criteria but with uncertainties, limitations, or borderline characteristics
3. **No**: Clearly fails to meet essential criteria

### Evaluation Process
1. Identify primary functions and intended use cases
2. Check against all Essential Criteria
3. Evaluate against Supporting Criteria
4. Consider the Consideration Factors
5. Determine appropriate classification, using "Maybe" when genuine uncertainty exists

### Classification Examples
- "Yes" example: A tool that specifically implements archaeological seriation algorithms, provides data visualization capabilities for archaeological contexts, and has documentation focused on research use cases
- "Maybe" example: A commercial GIS system with some archaeology-specific extensions but primarily designed for general geospatial work
- "No" example: A general-purpose database with no specific adaptations for historical research


## Output Delivery
- Present findings in a markdown fenced code block with quoted CSV
- Include header row and single data row
- Format multiple values within cells with pipe (|) separators
- Ensure CSV is properly escaped and formatted as a single continuous line
- Do not include any inline citations or references in the CSV itself

### For CSV formatting:
- Double quotes within fields must be escaped as two double quotes ("") 
- Ensure no newlines appear within any field
- For fields containing commas, ensure the entire field is properly quoted

## Example Output Format

"Tool","Description","History","Access-date","Tool-status",...
"ToolName","This tool currently provides...","Initially developed in 2010, the tool underwent major revisions in 2015 and 2022...","2025-05-02","maybe",...

---

### Assistant (22:05:49) [Model: o3]

Understood. I will follow the specified research methodology, controlled vocabularies, formatting rules, and quality standards, and will supply a single-row, quoted CSV inside a fenced code block for each tool. Please let me know the name or acronym of the first software tool to profile.

---

### Human (22:06:27)

FAIMS

---

### Assistant (22:07:47) [Model: o3]

```csv
"Tool","Description","History","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","Category","Language","Platform","Open-Archaeo-Platform","License","Lifecycle-stage","Type","Interoperability","Strengths","Weaknesses","Survivability","Alternatives","Authors","Tags","AI-tags"
"FAIMS","FAIMS3 (v1.0.0, released 2024-12-16) is the current generation of the Field Acquired Information Management System: an open-source, cross-platform electronic field-notebook and data-capture suite that operates offline on Android, iOS, the web and desktop. Users design custom notebooks, collect structured multimedia records in the field, and synchronise them through CouchDB/PouchDB when connectivity is available. The platform emphasises FAIR and reproducible data workflows and provides authentication, role-based access and export utilities.","Initiated in 2012 at Macquarie University, FAIMS launched its first Android-only mobile platform in 2014. Between 2020 and 2022 the codebase was completely rewritten as FAIMS3 with TypeScript and Ionic Capacitor to support Android, iOS, web and desktop. Iterative beta releases culminated in stable version 1.0.0 on 2024-12-16, merging the mobile app, Conductor server and Designer into a single monorepo; active development continues in 2025.","2025-05-02","yes","Meets all essential criteria (research-specific purpose, research-data engagement, methodological alignment) and multiple supporting criteria (domain knowledge integration, lifecycle support, data transformation, visualisation and documentation).","https://github.com/FAIMS/FAIMS3","","","https://faims.edu.au","Stand-alone software","TypeScript|JavaScript","Android|iOS|Web|Desktop","","Apache-2.0","Data Acquisition|Processing|Preservation and Reuse","research-specific","JSON documents stored in CouchDB with PouchDB offline replicas; RESTful API; exports CSV, GeoJSON and other formats; supports multimedia attachments and geospatial coordinates.","Offline-first; highly customisable; cross-platform; FAIR-aligned metadata; permissive licence and active development.","Complex server setup; CouchDB dependency; limited built-in analytics; comparatively small user community.","Apache licence, institutional stewardship, ARDC funding and frequent commits (May 2025) suggest high survivability.","Open Data Kit|KoboToolbox|ArcGIS Field Maps|QField","Shawn Ross|Brian Ballsun-Stanton|Steve Cassidy|Penny Crook|James Tocknell|Aidan Farrell","Data collection|Data management|Templates","mobile-field-data|offline-first|FAIR|custom-notebooks|cross-platform"
```

Sources used: citeturn7view0turn3view0turn9search1turn12view0turn13view0

---
