# v2-FAIMS-metadata and prompt-improvement

## Metadata
- **UUID:** `b6592b63-0387-4d57-899b-64ef7a9deda3`
- **URL:** https://claude.ai/chat/b6592b63-0387-4d57-899b-64ef7a9deda3
- **Date:** 2025-05-03 11:30:29

---

## Conversation

### Human (18:53:55)



---

### Assistant (18:54:00)



Based on the detailed instructions, I'll need to research a specific research software tool in archaeology/historical studies and build a CSV with the requested metadata. You've provided comprehensive guidelines about how to approach this task.

Before I begin, I need to know which specific archaeology or historical studies software tool you'd like me to research. You mentioned you'll be giving me "the name or acronym of an archaeology or historical studies-related software tool that dates somewhere from 1995 onwards," but I don't see the actual tool name in your message.

Could you please provide the name of the specific research software tool you'd like me to investigate?

---

### Human (18:54:07)

FAIMS

---

### Assistant (18:54:17)



I'll research this archaeological software tool for you right away. FAIMS appears to be a specialized research tool in archaeology, so this is perfect for your dataset collection.
```
This block is not supported on your current device yet.
```

Your FAIMS archaeological tool report is ready. It covers the evolution from an Android-only to cross-platform field data solution, technical architecture using CouchDB/PouchDB for offline functionality, deployment across 40+ archaeological projects, and its position in the software ecosystem. The report details FAIMS's strengths in customizability and offline capabilities, while noting challenges with technical complexity and sustainability.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (19:05:12)

Thanks, can you also please produce the requested CSV?

---

### Assistant (19:05:38)



I'll create the CSV entry for FAIMS based on the research I've conducted. Here's the formatted CSV with all the requested metadata:

```
"Tool","Description","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","Category","Language","Platform","Open-Archaeo-Platform","License","Lifecycle-stage","Type","Interoperability","Strenghths","Weaknesses","Survivability","Alternatives","Authors","Tags","AI-tags"
"FAIMS","FAIMS (Field Acquired Information Management Systems) is an open-source platform for offline digital field data collection designed primarily for archaeological research. First developed in 2012 at the University of New South Wales, it has evolved from an Android-only tool to a cross-platform solution now branded as Fieldmark™. The latest version (FAIMS3/Fieldmark) was released in December 2022, featuring improved cross-platform support and easier customization. FAIMS enables deeply customizable mobile applications for structured recording of archaeological data in remote settings with robust offline functionality and synchronization capabilities. It has been deployed in over 40 archaeological projects across approximately 70 research workflows.","yes","FAIMS clearly meets the criteria for a research software tool as it is specifically designed to support archaeological field research by enabling structured data collection, processing, and analysis. It integrates domain-specific knowledge about archaeological workflows, supports reproducibility through standardized data collection processes, and directly impacts data integrity in research contexts. FAIMS is not merely a generic data repository but a specialized tool that actively transforms raw field observations into structured research data through customizable forms, validation rules, and controlled vocabularies tailored to archaeological research needs.","https://github.com/FAIMS/FAIMS3","","","https://faims.edu.au/","Stand-alone software","TypeScript|JavaScript|Java|Ruby","Android|iOS|Web|Windows|Linux|macOS","","Apache 2.0","Data Acquisition|Processing|Preservation and Reuse","research-specific","FAIMS supports multiple export formats (CSV, SQLite, GeoJSON, shapefile) and integrates with analysis tools (AARNet's CloudStor, SWAN, Auscope's AVRE) and repositories (tDAR, Open Context, OCHRE). It features RESTful API for third-party integration and GIS compatibility for spatial data.","FAIMS excels in comprehensive offline data collection with synchronization capabilities critical for fieldwork in remote locations. Its exceptional customizability allows adaptation to various research workflows through definition packets. The platform supports multi-user collaboration, multimedia integration, and controlled vocabularies, improving data quality and reducing post-fieldwork digitization efforts. FAIMS creates born-digital field data that adheres to FAIR principles.","FAIMS has a steep learning curve and requires significant upfront investment in training and customization. Earlier versions required technical expertise for module creation, though FAIMS3/Fieldmark has improved this with a graphical interface. Like many academic software projects, it faces sustainability challenges despite its commercial hosting pathway. The technical complexity of the system can be overwhelming for new users or those with limited technical skills.","FAIMS has demonstrated strong survivability over its 11-year history through continuous funding, institutional support, and community adoption. The project has evolved from a purely academic initiative to include commercial hosting options through Electronic Field Notebooks Pty Ltd. Its evolution to a cross-platform solution and adaptation to changing technologies suggest active development will continue. The transition to a sustainability model combining an open-source core with value-adding services improves its long-term viability prospects.","ARK (Archaeological Recording Kit), Open Context, iDig (iOS excavation recording), Codifi, ODK (Open Data Kit), KoBoToolbox, ArcGIS Survey123, Esri Collector","Shawn A. Ross|Adela Sobotkova|Penny Crook|Brian Ballsun-Stanton","Data collection|Site mapping|Data management|Spatial analysis|Geophysical survey","archaeological data collection|offline field recording|customizable research forms|archaeological workflows|mobile data synchronization"
```

---

### Human (19:16:40)

Claude, can you help me revise the prompt to produce better results? Here is my latest version.

---

### Assistant (19:17:09)


The user has shared a new version of their instructions document (document index 3) for collecting metadata about archaeological research software tools. They're asking me to help them revise this prompt to produce better results, though they haven't specifically indicated what aspects of the results need improvement.

Let me analyze the current prompt structure to identify potential areas for improvement:

1. The prompt has a clear structure with defined sections:
   - Ground rules for accuracy and research quality
   - Definitions of research software tools
   - Task description with CSV format requirements
   - Detailed column explanations with controlled vocabulary lists
   - Instructions for research process and delivery format

2. Possible areas for improvement:

   a) Clarity and organization:
   - The prompt is quite long and contains nested sections
   - Some instructions might be redundant or could be streamlined
   - The controlled vocabulary lists are embedded within explanation sections

   b) Research guidance:
   - Could provide more specific research methodology steps
   - Might benefit from clearer prioritization of information sources
   - Could include tips for resolving conflicting information

   c) Output formatting:
   - Currently asks for "quoted, one-line CSV" which might lead to readability issues
   - Could provide clearer examples of expected output format
   - Might benefit from guidance on handling unknown/uncertain information

   d) Tool evaluation criteria:
   - The "Strengths", "Weaknesses", and "Survivability" fields require subjective assessment
   - Could provide more structured criteria for making these assessments
   - Might need clearer guidelines for maintaining consistency across different tools

Based on these observations, I'll suggest improvements to the prompt structure while maintaining its core requirements.

I'd be happy to help you revise the prompt to produce better results. Looking at your current version, I've identified several areas where we could make improvements for clarity, structure, and to ensure more consistent, high-quality outputs.

Here's my revised version of your prompt:

```
# Archaeological Research Software Tools Metadata Collection

## Ground Rules
- ACCURACY FIRST: Do not make claims without supporting evidence. If uncertain, clearly indicate uncertainty.
- THOROUGH RESEARCH: Conduct comprehensive research using all available sources including repositories, scholarly literature, official documentation, and reliable mentions.
- METHODICAL APPROACH: Follow a systematic research process and document findings carefully.

## Research Methodology
1. Begin with official sources (project website, documentation, repositories)
2. Expand to scholarly literature discussing the tool
3. Consider community resources and discussions
4. Synthesize findings with careful attention to recency and reliability
5. For subjective assessments (strengths, weaknesses, survivability), base conclusions on evidence rather than speculation

## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"

## Column Specifications

### Essential Information
- **Tool**: Exact name as provided in the prompt
- **Description**: Clear, detailed overview (3-5 sentences) including purpose, functionality, and major versions/releases
- **Tool-status**: "yes" or "no" based on research software tool definition
- **Tool-status-reasoning**: Detailed explanation of classification decision referencing specific criteria
- **DVCS-repo**: Primary repository URL (GitHub, GitLab, etc.) if available
- **CRAN**: URL if available
- **PyPi**: URL if available
- **Other-URL**: Primary project homepage or documentation site
- **Category**: One of: "Packages and libraries", "Stand-alone software", or "Scripts"
- **Language**: Programming language(s), separated by pipes (|)
- **Platform**: Operating systems/environments supported
- **Open-Archaeo-Platform**: Only if "Category" is "Packages and libraries", otherwise leave empty

### Technical Characteristics
- **License**: Most recent license, verified from official sources
- **Lifecycle-stage**: Research stages supported from: "Planning", "Data Acquisition", "Processing", "Analysis", "Interpretation", "Publication", "Preservation and Reuse" (multiple values pipe-separated)
- **Type**: Either "mass-market" or "research-specific"
- **Interoperability**: Focus on data input/output formats and exchange capabilities

### Assessment Criteria
- **Strengths**: Evidence-based assessment of key advantages and research opportunities enabled
- **Weaknesses**: Evidence-based assessment of limitations, challenges, or potential risks
- **Survivability**: Assessment of long-term viability based on: 
  * Development activity (recent updates, community engagement)
  * Institutional/funding support
  * User community size and growth
  * Technical debt and architecture adaptability
- **Alternatives**: Similar tools serving comparable functions
- **Authors**: Individual contributors (not organizations) separated by pipes
- **Tags**: Applicable terms from the controlled vocabulary (pipe-separated)
- **AI-tags**: Five descriptive tags summarizing key aspects of the tool

## Research Software Tool Definition
[Your existing definition section is thorough and can remain as is]

## Output Delivery
- Present findings in a markdown fenced code block with quoted CSV
- Include header row and single data row
- Format multiple values within cells with pipe (|) separators
- Ensure CSV is properly escaped and formatted as a single continuous line
- Do not include any inline citations or references in the CSV itself

## Example Output Format
```
"Tool","Description","Tool-status",...
"ToolName","This tool provides...","yes",...
```
```

Key improvements in this revision:

1. **Structured Research Methodology**: Added a clear step-by-step approach to guide the research process
2. **Organized Sections**: Grouped related columns into logical sections for easier reference
3. **Assessment Criteria**: Added more specific guidance for subjective assessments
4. **Example Output**: Included a clear example of the expected format
5. **Cleaner Structure**: Reduced redundancy while maintaining comprehensive instructions

Would you like me to make any specific adjustments to this revision based on particular aspects you'd like to improve?

---

### Human (19:24:06)

These are great suggestions! I particularly like your emphasis on 'recency'. Without losing anything, can we revise the prompt slightly to emphasise that the metadata we want is that which pertains to the most recent version of the software - it should be up-to-date as of the time of the query. With that in mind, let's include an 'access-date' column with the date of the research (i.e., today in this case). Let's also add a column after 'description' called 'History', which includes a detailed history of the tool  - all historical information about the evolution of versions of the tool should go in this column, while all other columns contain information about the most recent version.

---

### Assistant (19:24:33)


I need to revise the prompt based on the user's suggestions. They want me to:

1. Emphasize that metadata should pertain to the most recent version of the software
2. Add an 'access-date' column with today's date
3. Add a 'History' column after 'description' for historical information about the evolution of the tool
4. Ensure all other columns contain information about only the most recent version

Let me revise the prompt while keeping all the other improvements I already made.

I'll revise the prompt to incorporate your excellent suggestions about separating current and historical information:

```
# Archaeological Research Software Tools Metadata Collection

## Ground Rules
- ACCURACY FIRST: Do not make claims without supporting evidence. If uncertain, clearly indicate uncertainty.
- THOROUGH RESEARCH: Conduct comprehensive research using all available sources including repositories, scholarly literature, official documentation, and reliable mentions.
- METHODICAL APPROACH: Follow a systematic research process and document findings carefully.
- RECENCY FOCUS: All metadata must reflect the most recent version of the software as of the access date, unless specifically noted.

## Research Methodology
1. Begin with official sources (project website, documentation, repositories)
2. Expand to scholarly literature discussing the tool
3. Consider community resources and discussions
4. Synthesize findings with careful attention to recency and reliability
5. For subjective assessments (strengths, weaknesses, survivability), base conclusions on evidence rather than speculation

## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "History", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"

## Column Specifications

### Essential Information
- **Tool**: Exact name as provided in the prompt
- **Description**: Clear, detailed overview (3-5 sentences) of the CURRENT version's purpose and functionality
- **History**: Chronological account of the tool's development, including major versions, significant updates, and evolution over time
- **Access-date**: Today's date in YYYY-MM-DD format, representing when this research was conducted
- **Tool-status**: "yes" or "no" based on research software tool definition
- **Tool-status-reasoning**: Detailed explanation of classification decision referencing specific criteria
- **DVCS-repo**: Primary repository URL (GitHub, GitLab, etc.) if available
- **CRAN**: URL if available
- **PyPi**: URL if available
- **Other-URL**: Primary project homepage or documentation site
- **Category**: One of: "Packages and libraries", "Stand-alone software", or "Scripts"
- **Language**: Programming language(s) of CURRENT version, separated by pipes (|)
- **Platform**: Operating systems/environments supported by CURRENT version
- **Open-Archaeo-Platform**: Only if "Category" is "Packages and libraries", otherwise leave empty

### Technical Characteristics (CURRENT VERSION ONLY)
- **License**: Most recent license, verified from official sources
- **Lifecycle-stage**: Research stages supported from: "Planning", "Data Acquisition", "Processing", "Analysis", "Interpretation", "Publication", "Preservation and Reuse" (multiple values pipe-separated)
- **Type**: Either "mass-market" or "research-specific"
- **Interoperability**: Focus on data input/output formats and exchange capabilities in the CURRENT version

### Assessment Criteria (CURRENT VERSION ONLY)
- **Strengths**: Evidence-based assessment of key advantages and research opportunities enabled
- **Weaknesses**: Evidence-based assessment of limitations, challenges, or potential risks
- **Survivability**: Assessment of long-term viability based on: 
  * Development activity (recent updates, community engagement)
  * Institutional/funding support
  * User community size and growth
  * Technical debt and architecture adaptability
- **Alternatives**: Similar tools serving comparable functions
- **Authors**: Individual contributors (not organizations) separated by pipes
- **Tags**: Applicable terms from the controlled vocabulary (pipe-separated)
- **AI-tags**: Five descriptive tags summarizing key aspects of the tool

## Research Software Tool Definition
[Your existing definition section is thorough and can remain as is]

## Output Delivery
- Present findings in a markdown fenced code block with quoted CSV
- Include header row and single data row
- Format multiple values within cells with pipe (|) separators
- Ensure CSV is properly escaped and formatted as a single continuous line
- Do not include any inline citations or references in the CSV itself

## Example Output Format
```
"Tool","Description","History","Access-date",...
"ToolName","This tool currently provides...","Initially developed in 2010, the tool underwent major revisions in 2015 and 2022...","2025-05-02",...
```
```

This revised prompt now:

1. Explicitly emphasizes recency focus in the ground rules
2. Adds both "History" and "Access-date" columns 
3. Clearly separates current functionality (Description) from evolutionary history (History)
4. Specifically labels which sections should contain CURRENT VERSION ONLY information
5. Updates the example output format to demonstrate the new columns

These changes should help produce more temporally organized and precise metadata for each tool, with clear separation between historical development and current capabilities.

---

### Human (19:25:29)

Great! Can you compose a well-formatted version of the 

## Research Software Tool Definition

section for me please?

---

### Assistant (19:25:44)


I'm being asked to compose a well-formatted version of the "Research Software Tool Definition" section from the prompt. The human wants me to refine and structure this section, which should define what a research software tool is in the context of archaeology and historical studies.

Based on the document I was given earlier, I should compose a clear, structured definition that covers:

1. What research software tools are
2. Their core characteristics 
3. What distinguishes them from general software
4. Categories and examples relevant to archaeology/historical studies
5. Sustainability considerations

I'll create a well-formatted version of this section that's comprehensive yet clear.

Here's a well-formatted version of the Research Software Tool Definition section:

```
## Research Software Tool Definition

### Overview
Research software tools are specialized digital instruments developed to enable, enhance, or accelerate the scientific research process by supporting one or more stages of scientific inquiry. In archaeology and historical studies, these tools transform raw observational data into structured research insights, embodying domain-specific methodological approaches that directly impact research outcomes.

### Core Characteristics
1. **Research-Oriented Purpose**: Specifically designed to generate, process, and analyze results in a research context
2. **Functional Diversity**: Ranges from sophisticated packages with broad user bases to targeted scripts created for specific research tasks
3. **Knowledge Embodiment**: Encodes disciplinary expertise and methodological approaches within its functionality
4. **Active Data Processing**: Works with research data rather than merely serving as a repository or static interface
5. **Research Lifecycle Support**: Facilitates one or more stages of the research process, from data collection to publication

### Distinguishing Features
Research software tools are differentiated from general-purpose software by:

1. **Specialized Functionality**: Addresses specific scientific needs rather than general computing tasks
2. **Domain Integration**: Embeds disciplinary knowledge particular to archaeology or historical studies
3. **Evolving Requirements**: Develops organically alongside research processes, adapting to emerging research questions
4. **Reproducibility Role**: Directly impacts the reliability and reproducibility of research results
5. **Academic Context**: Often created under research constraints and incentives rather than commercial drivers

### Archaeological Applications
In archaeology and historical studies, research software tools typically:

1. Support fieldwork data collection and documentation
2. Enable analysis of archaeological materials, contexts, or spatial relationships
3. Facilitate visualization or modeling of archaeological data
4. Aid in preservation, archiving, and sharing of research outputs
5. Integrate with established research methodologies specific to these disciplines

### Sustainability Considerations
Research software tools present particular sustainability challenges:

1. Require ongoing maintenance to adapt to changing technological environments
2. Exist within networks of dependencies that create vulnerability to software decay
3. Often develop under resource constraints without explicit sustainability planning
4. Present unique preservation challenges compared to static data resources

### Conclusion
A valid research software tool for archaeological or historical research actively processes data in ways that advance disciplinary understanding, rather than merely storing or displaying information. It embodies methodological approaches specific to these fields and directly contributes to the generation, transformation, or analysis of research data.
```

This structured definition emphasizes the active, specialized nature of research software tools and their importance within the archaeological research ecosystem, while clearly establishing criteria for evaluation.

---

### Human (19:30:03)

For the tool definition, can you help me revise it so that it is less archaeology-specific and covers historical studies as well?

---

### Assistant (19:30:18)


I'll revise the Research Software Tool Definition to be more inclusive of both archaeology and historical studies more broadly. I should:

1. Remove archaeology-specific references where they appear exclusively
2. Add more references to historical studies concepts and methods
3. Ensure examples cover both archaeological and historical research contexts
4. Use more general language around research processes that apply to both fields
5. Include methods and approaches from historical studies (textual analysis, archival research, etc.)

The goal is to create a definition that is equally applicable to research software tools used in archaeology, history, and other related historical sciences without prioritizing one field over the other.

Here's a revised Research Software Tool Definition that equally covers archaeology and historical studies:

```
## Research Software Tool Definition

### Overview
Research software tools are specialized digital instruments developed to enable, enhance, or accelerate the scientific research process by supporting one or more stages of scholarly inquiry. In historical disciplines—including archaeology, history, art history, classics, historical linguistics, and related fields—these tools transform raw source materials into structured research insights, embodying domain-specific methodological approaches that directly impact research outcomes.

### Core Characteristics
1. **Research-Oriented Purpose**: Specifically designed to generate, process, and analyze results in a research context
2. **Functional Diversity**: Ranges from sophisticated packages with broad user bases to targeted scripts created for specific research tasks
3. **Knowledge Embodiment**: Encodes disciplinary expertise and methodological approaches within its functionality
4. **Active Data Processing**: Works with research data rather than merely serving as a repository or static interface
5. **Research Lifecycle Support**: Facilitates one or more stages of the research process, from data collection to publication

### Distinguishing Features
Research software tools are differentiated from general-purpose software by:

1. **Specialized Functionality**: Addresses specific scholarly needs rather than general computing tasks
2. **Domain Integration**: Embeds disciplinary knowledge particular to historical studies and related fields
3. **Evolving Requirements**: Develops organically alongside research processes, adapting to emerging research questions
4. **Reproducibility Role**: Directly impacts the reliability and reproducibility of research results
5. **Academic Context**: Often created under research constraints and incentives rather than commercial drivers

### Historical Studies Applications
In historical research disciplines, research software tools typically:

1. Support data collection from field sites, archives, manuscripts, or material culture
2. Enable analysis of historical texts, artifacts, contexts, or spatial/temporal relationships
3. Facilitate visualization or modeling of historical and archaeological data
4. Aid in the identification of patterns, connections, or anomalies in historical sources
5. Assist with chronological modeling, provenance analysis, or contextual reconstruction
6. Support the preservation, archiving, and sharing of research outputs
7. Integrate with established methodologies specific to historical disciplines

### Sustainability Considerations
Research software tools present particular sustainability challenges:

1. Require ongoing maintenance to adapt to changing technological environments
2. Exist within networks of dependencies that create vulnerability to software decay
3. Often develop under resource constraints without explicit sustainability planning
4. Present unique preservation challenges compared to static data resources

### Conclusion
A valid research software tool for historical studies actively processes data in ways that advance disciplinary understanding, rather than merely storing or displaying information. It embodies methodological approaches specific to these fields and directly contributes to the generation, transformation, or analysis of research materials—whether texts, artifacts, spatial data, or other historical sources.
```

This revised definition broadens the scope to encompass the full spectrum of historical disciplines while maintaining the core criteria that define research software tools. It includes references to methods and materials common across historical studies such as textual analysis, archival research, and chronological modeling, alongside archaeological approaches.

---

### Human (19:31:29)

Would this definition help you to determine whether or not a well-described piece of software qualifies as a 'research software tool'? How could the definition be improved to help *you* make that determination?

---

### Assistant (19:31:47)


This is a very thoughtful question about how the definition would practically function for me (Claude) when evaluating whether a piece of software qualifies as a "research software tool." Let me analyze the current definition and consider what improvements might help me make that determination more effectively.

How the current definition helps me:
1. It provides general characteristics and distinguishing features that create a conceptual framework
2. It outlines application areas for historical studies software
3. It contrasts research software with general-purpose software

However, there are some ways this definition could be improved specifically to help an AI make this determination:

1. **More explicit decision criteria**: The current definition is descriptive but doesn't provide explicit criteria that must be met to qualify as a research software tool.

2. **Quantifiable aspects**: Where possible, adding more quantifiable or binary elements would help with classification (e.g., "must support at least one specific research methodology").

3. **Hierarchical importance of criteria**: Not all characteristics are equally important - some may be necessary while others are merely supportive.

4. **Edge case clarification**: The definition could benefit from examples of borderline cases that illustrate what does or doesn't qualify.

5. **Decision tree or rubric**: A structured approach to evaluating software would be helpful.

6. **Negative cases**: The definition focuses on what research software is, but could be enhanced with clearer statements about what it is not.

7. **Minimum threshold guidance**: How many of the characteristics need to be present? Is there a core set that must be present?

Let me draft an improved version focusing on these aspects.

Yes, this definition provides a good framework for evaluation, but I would benefit from more structured decision-making elements. To improve it specifically for AI determination, I would suggest:

```
## Research Software Tool Definition and Evaluation Framework

### Core Definition
A research software tool is specialized software that enables specific research tasks in historical disciplines by actively processing, analyzing, or transforming research materials beyond basic storage or display functions.

### Essential Criteria (Must Meet ALL)
1. **Research-Specific Purpose**: Primary function directly supports research activities rather than general computing tasks
2. **Active Data Processing**: Transforms, analyzes, or manipulates research materials in discipline-relevant ways
3. **Methodological Implementation**: Encodes at least one recognized research methodology from historical disciplines

### Supporting Criteria (Must Meet at Least TWO)
1. **Domain Knowledge Integration**: Incorporates terminology, classifications, or procedures specific to historical disciplines
2. **Research Lifecycle Support**: Explicitly addresses one or more research stages (planning, acquisition, processing, analysis, interpretation, publication, preservation)
3. **Data Transformation**: Converts between formats or representations relevant to historical research
4. **Analytical Capabilities**: Performs calculations, comparisons, or pattern recognition on historical data
5. **Visualization Functions**: Renders historical or archaeological data in meaningful visual formats
6. **Documentation Focus**: Contains documentation specifically addressing research applications

### Exclusion Criteria (ANY May Disqualify)
1. **Generic Functionality**: Functions are identical to general-purpose software with no research-specific adaptations
2. **Passive Repository**: Serves only as a storage mechanism with no processing capabilities
3. **Display-Only**: Merely displays information without analytical or transformative functions
4. **Commercial Focus**: Primarily designed for commercial rather than research applications, with no significant research adaptations

### Borderline Cases
Software in these categories requires careful evaluation against the criteria above:
1. Database systems with custom fields for historical research
2. GIS platforms used for historical spatial analysis
3. Generic statistical packages applied to historical data
4. Digital collection management systems
5. Bibliographic management software

### Evaluation Process
1. Identify primary functions and intended use cases
2. Check against all Essential Criteria (must satisfy all)
3. Evaluate against Supporting Criteria (must satisfy at least two)
4. Check against Exclusion Criteria (any may disqualify)
5. For borderline cases, assess whether research-specific adaptations are substantive

This structured approach allows for consistent determination across diverse software tools while acknowledging the nuanced spectrum between general-purpose software and specialized research tools.
```

This revision adds explicit decision criteria, establishes minimum thresholds, addresses borderline cases, and provides a clear evaluation process that would help me make more consistent determinations about whether software qualifies as a research software tool.

---

### Human (19:41:52)

I see how you are adjusting the prompt, let me give you a little feedback.

'2. **Active Data Processing**: Transforms, analyzes, or manipulates research materials in discipline-relevant ways'

This point may be a little too restrictive. Tools may also collect / capture data, support the visualisation of data, or assist with data dissemination as well as be used for 'active data processing'.

'3. **Methodological Implementation**: Encodes at least one recognized research methodology from historical disciplines'

Interpret this point generously, sometimes the encoding of the research methodology can be subtle or not immediately apparent.

'### Supporting Criteria (Must Meet at Least TWO)'

Data capture or collection and data dissemination should probably be included here, noting that by 'data dissemination' I don't mean a static collection or a dataset, but rather a *tool that assists with the dissemination, sharing, or reuse of data*.

'4. **Commercial Focus**: Primarily designed for commercial rather than research applications, with no significant research adaptations'

Be generous when interpreting this point, some commercial tools are used for research; if a tool had *significant* research adaptations it could still be included.

Overall my suggestion would be to loosen your criteria slightly and let humans make the final call. In fact, maybe we should add a 'maybe' category to the 'yes' and 'no', so that doubtful software tools could be flagged for human review?

With that in mind, first revise your definition to incorporate this feedback - while ensuring that it is still useful for *you*, then pause for confirmation. After that, revise the relevant section of the overall prompt to account for the 'maybe' case.

---

### Assistant (19:42:05)


Let me revise the Research Software Tool Definition based on the feedback:

1. Add "data collection/capture" and "visualization" to the essential criteria about active data processing
2. Be more generous with methodological implementation interpretation
3. Add data capture/collection and data dissemination to supporting criteria
4. Be more generous with commercial tools that have research applications
5. Add a "maybe" option for borderline cases

Here's my revised definition:

Here's my revised definition incorporating your feedback while maintaining its usefulness as an evaluation framework:

```
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

This framework allows for nuanced evaluation while acknowledging that final determinations in borderline cases should be reserved for human expertise.
```

This revised definition:
1. Broadens the scope of "research data engagement" to include collection and visualization
2. Takes a more inclusive approach to methodological alignment
3. Adds specific supporting criteria for data collection and dissemination
4. Reframes exclusion criteria as "consideration factors" that inform but don't automatically disqualify
5. Explicitly introduces the three-tier classification system with "Maybe" for borderline cases

Would you like me to proceed with updating the relevant section of the overall prompt to incorporate this "Maybe" classification?

---

### Human (19:43:13)

Yes, please proceed

---

### Assistant (19:43:44)


Now I'll update the relevant section of the overall prompt to incorporate the "Maybe" classification for Tool-status. I'll need to:

1. Update the Tool-status column description to include "maybe" as an option
2. Add guidance for the Tool-status-reasoning field to explain when "maybe" should be used
3. Ensure the example output format reflects this change
4. Make any other necessary adjustments to the prompt to account for this third classification

Let me focus on modifying the relevant sections while maintaining the overall structure and flow of the prompt.

Here's the revised prompt with updates to incorporate the "Maybe" classification:

```
# Archaeological Research Software Tools Metadata Collection

## Ground Rules
- ACCURACY FIRST: Do not make claims without supporting evidence. If uncertain, clearly indicate uncertainty.
- THOROUGH RESEARCH: Conduct comprehensive research using all available sources including repositories, scholarly literature, official documentation, and reliable mentions.
- METHODICAL APPROACH: Follow a systematic research process and document findings carefully.
- RECENCY FOCUS: All metadata must reflect the most recent version of the software as of the access date, unless specifically noted.

## Research Methodology
1. Begin with official sources (project website, documentation, repositories)
2. Expand to scholarly literature discussing the tool
3. Consider community resources and discussions
4. Synthesize findings with careful attention to recency and reliability
5. For subjective assessments (strengths, weaknesses, survivability), base conclusions on evidence rather than speculation

## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "History", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"

## Column Specifications

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
- **Category**: One of: "Packages and libraries", "Stand-alone software", or "Scripts"
- **Language**: Programming language(s) of CURRENT version, separated by pipes (|)
- **Platform**: Operating systems/environments supported by CURRENT version
- **Open-Archaeo-Platform**: Only if "Category" is "Packages and libraries", otherwise leave empty

### Technical Characteristics (CURRENT VERSION ONLY)
- **License**: Most recent license, verified from official sources
- **Lifecycle-stage**: Research stages supported from: "Planning", "Data Acquisition", "Processing", "Analysis", "Interpretation", "Publication", "Preservation and Reuse" (multiple values pipe-separated)
- **Type**: Either "mass-market" or "research-specific"
- **Interoperability**: Focus on data input/output formats and exchange capabilities in the CURRENT version

### Assessment Criteria (CURRENT VERSION ONLY)
- **Strengths**: Evidence-based assessment of key advantages and research opportunities enabled
- **Weaknesses**: Evidence-based assessment of limitations, challenges, or potential risks
- **Survivability**: Assessment of long-term viability based on: 
  * Development activity (recent updates, community engagement)
  * Institutional/funding support
  * User community size and growth
  * Technical debt and architecture adaptability
- **Alternatives**: Similar tools serving comparable functions
- **Authors**: Individual contributors (not organizations) separated by pipes
- **Tags**: Applicable terms from the controlled vocabulary (pipe-separated)
- **AI-tags**: Five descriptive tags summarizing key aspects of the tool

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

## Output Delivery
- Present findings in a markdown fenced code block with quoted CSV
- Include header row and single data row
- Format multiple values within cells with pipe (|) separators
- Ensure CSV is properly escaped and formatted as a single continuous line
- Do not include any inline citations or references in the CSV itself

## Example Output Format
```
"Tool","Description","History","Access-date","Tool-status",...
"ToolName","This tool currently provides...","Initially developed in 2010, the tool underwent major revisions in 2015 and 2022...","2025-05-02","maybe",...
```
```

The key changes I've made:

1. Updated the **Tool-status** field to explicitly include the three possible values ("yes", "maybe", "no")
2. Enhanced the **Tool-status-reasoning** field to provide specific guidance for how to handle "maybe" classifications
3. Incorporated the full revised Research Software Tool Definition and Evaluation Framework
4. Updated the example output to show a "maybe" classification case
5. Maintained the overall structure and integrity of the prompt

This revision provides clear guidance for when to use the "maybe" classification, ensuring that borderline cases can be flagged for human review rather than forcing a binary determination when evidence is inconclusive.

---

### Human (19:47:52)

This is great work. The only thing that I see missing is that in my origninal prompt, I had some controlled lists for some of the metadata properties we are investigating. I have provided them because I want this dataset to be compatible with the Open-Archaeo project that catalogues research-software-tools (I'd like to feed our discoveries back into their dataset). Could you suggest how I might re-incorporate those missing controlled lists?

---

### Assistant (19:48:23)


You're right - the original prompt had several controlled lists for specific metadata properties that I didn't include in my revised version. Let me identify all the controlled lists from the original prompt:

1. Category controlled list:
```
<Category controlled list>
Packages and libraries: Sets of functions assembled with clear purpose, and made accessible using standards established by an underlying platform.
Stand-alone software: Software that may be operated without needing to first access an underlying platform.
Scripts: Sets of pragmatically assembled mutable functions, often lacking complete documentation or adherence to protocols that would otherwise facilitate secondary use outside their original contexts of creation.
</Category controlled list>
```

2. Open-archaeo-platform controlled list:
```
<Open-archaeo-platform controlled list>
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
</Open-archaeo-platform controlled list>
```

3. Lifecycle-stage controlled list:
```
<lifecycle-stage controlled list>
Planning
Data Acquisition
Processing
Analysis
Interpretation
Publication
Preservation and Reuse
</lifecycle-stage controlled list>
```

4. Tags controlled list - which was quite extensive, containing all the specific tags that could be applied to archaeological tools.

To reincorporate these, I'll need to add them back into the prompt in a way that maintains the improved structure while ensuring compatibility with the Open-Archaeo project's requirements.

You're absolutely right - the controlled lists are crucial for compatibility with the Open-Archaeo project. Here's how I would reincorporate those missing controlled lists while maintaining the improved structure:

```
# Archaeological Research Software Tools Metadata Collection

## Ground Rules
- ACCURACY FIRST: Do not make claims without supporting evidence. If uncertain, clearly indicate uncertainty.
- THOROUGH RESEARCH: Conduct comprehensive research using all available sources including repositories, scholarly literature, official documentation, and reliable mentions.
- METHODICAL APPROACH: Follow a systematic research process and document findings carefully.
- RECENCY FOCUS: All metadata must reflect the most recent version of the software as of the access date, unless specifically noted.
- CONTROLLED VOCABULARY: Strictly adhere to the provided controlled lists for compatibility with the Open-Archaeo project.

## Research Methodology
[Unchanged section]

## Output Format Requirements
[Unchanged section]

## Column Specifications

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
[Unchanged section]

## Output Delivery
[Unchanged section]

## Example Output Format
[Unchanged section]
```

Key improvements:

1. Added a ground rule specifically about adhering to controlled vocabularies
2. Reincorporated all four controlled lists as distinct, formatted sections
3. Updated the column descriptions to explicitly reference these controlled lists
4. Maintained the improved structure and clarity of the revised prompt
5. Ensured compatibility with the Open-Archaeo project's classification scheme

This approach maintains all the valuable improvements while ensuring that the metadata will be compatible with the Open-Archaeo project's existing dataset.

---

### Human (19:52:14)

Could you make one last review of the prompt and suggest any final changes to make it maximially useful for you?

---

### Assistant (19:52:32)


Let me carefully review the current prompt to identify any potential areas for improvement that would make it more useful for me in producing high-quality research software tool metadata.

Areas to consider:
1. Clarity and specificity of instructions
2. Handling of edge cases
3. Research guidance
4. Format requirements
5. Evaluation framework

Key observations:

1. The overall structure is logical and comprehensive
2. The research methodology is well-defined
3. The column specifications are clear
4. The controlled vocabulary lists are properly incorporated
5. The research software tool definition provides a good framework

Some potential improvements:

1. **Research depth guidance**: While the prompt emphasizes thoroughness, it could be helpful to provide more specific guidance on how deep to search (e.g., number of search results to examine, priority of sources)

2. **Uncertain information handling**: The prompt could be clearer about how to handle cases where specific information (e.g., license, authors) is not available or contradictory across sources

3. **Format specifications**: Some cells might benefit from more specific formatting instructions to ensure consistency (date format is specified, but there could be more guidance on handling empty fields)

4. **Evaluation examples**: Adding a few concrete examples of "yes", "maybe", and "no" classifications could help calibrate judgments

5. **String escaping**: The prompt could include specific guidance on how to handle quotes within CSV fields

6. **Error handling**: Instructions for what to do if the research process encounters difficulties (e.g., conflicting information, inaccessible sources)

7. **Field validation**: Additional guidance on validating certain fields against expected patterns or values

8. **Estimating version currency**: More specific guidance on determining whether information refers to the current version

9. **References management**: While the prompt says not to include citations in the CSV, instructions for tracking sources could be helpful for verification

10. **Progress tracking**: Instructions for tracking progress through the research process to ensure completeness

Let me draft suggestions for these improvements.

After reviewing the prompt carefully, I'd suggest these final refinements to make it maximally useful:

1. **Research depth indicators**: 
   ```
   When researching a tool, examine at least the first 20 search results, the tool's official documentation, its source code repositories, and any scholarly articles mentioning it. Prioritize official documentation and peer-reviewed publications over third-party blogs or forums.
   ```

2. **Handling uncertainty and missing data**:
   ```
   For fields where information is unavailable after thorough research, use the following conventions:
   - For URLs and other web addresses: leave field empty (do not use "N/A" or placeholder text)
   - For categorical fields with controlled vocabulary: leave empty rather than guessing
   - For open text fields requiring subjective assessment: provide your best assessment based on available evidence, but clearly indicate limitations (e.g., "Based on limited available information...")
   - When sources conflict: prioritize official documentation, then peer-reviewed publications, then community consensus
   ```

3. **CSV escaping guidance**:
   ```
   For CSV formatting:
   - Double quotes within fields must be escaped as two double quotes ("") 
   - Ensure no newlines appear within any field
   - For fields containing commas, ensure the entire field is properly quoted
   ```

4. **Version currency determination**:
   ```
   To identify the current version:
   - Check release dates on repositories and official sites
   - Look for "latest release" or "current version" indicators
   - If version history is unclear, use the most recently documented version with evidence of being publicly available
   - Note in the "Description" if the tool appears abandoned or unmaintained
   ```

5. **Classification examples**:
   ```
   Classification examples:
   - "Yes" example: A tool that specifically implements archaeological seriation algorithms, provides data visualization capabilities for archaeological contexts, and has documentation focused on research use cases
   - "Maybe" example: A commercial GIS system with some archaeology-specific extensions but primarily designed for general geospatial work
   - "No" example: A general-purpose database with no specific adaptations for historical research
   ```

These additions would address common challenges I face when evaluating research tools and help me produce more consistent, high-quality metadata while reducing ambiguity in the assessment process.

---

### Human (19:53:48)

Would you like these instructions placed in their own sections, or incorporated in any particular way?

---

### Assistant (19:53:56)


I should consider the most useful organization for these instructions. The prompt is already well-structured with distinct sections, and I want to maintain that clarity while incorporating my additional guidance.

There are a few ways I could approach this:

1. Create a new section titled "Research and Documentation Guidelines" that includes all these points
2. Integrate each point into the most relevant existing section
3. Create a smaller set of focused subsections under existing major sections

The first approach keeps things neat but might disconnect related guidance from existing sections where they're most relevant. The second approach keeps related information together but might make existing sections too dense. The third approach is a good middle ground.

I think the third approach would be most useful - creating smaller subsections under existing sections to maintain the logical flow while adding my additional guidance where it will be most helpful during the research process.

I'd recommend incorporating these instructions in the following way:

1. Create a new subsection called "**Research Standards and Data Quality**" right after the "Research Methodology" section, containing the research depth indicators and handling uncertainty/missing data points.

2. Add a subsection called "**Version and Currency Determination**" under "Column Specifications" before the "Essential Information" section to address identifying the current version.

3. Add the CSV escaping guidance to the existing "Output Delivery" section.

4. Add the classification examples as a new subsection called "**Classification Examples**" immediately after the "Evaluation Process" section within the "Research Software Tool Definition and Evaluation Framework".

This organization would:
- Keep related information grouped together
- Place guidance where it would be most helpful during the actual research process
- Maintain the logical flow of the document
- Ensure the guidance is available exactly when needed during assessment

This approach preserves the document's excellent structure while ensuring the additional guidance is available at the most relevant decision points in the research and documentation process.

---

### Human (19:58:05)

Thank you, I will run the prompt in a new chat, I look forward to seeing the results!

---

### Assistant (19:58:13)


It sounds like the user is satisfied with the improvements we've made to the prompt and plans to use it in a new chat. They're looking forward to seeing the results when our improved prompt is used to gather metadata about archaeological research software tools.

I can acknowledge their thanks and express my hope that the improved prompt will yield more accurate, consistent, and useful results for their research project. I can also offer continued assistance if they need any help interpreting or refining the results they get.

You're welcome! I'm glad I could help refine the prompt to better support your metadata collection for archaeological research software tools. The improvements should lead to more consistent, detailed, and accurate results that align with the Open-Archaeo project's requirements.

The three-tier classification system with the "maybe" option will be particularly helpful for identifying borderline cases that merit human review, while the additional guidance on research standards, version determination, and data handling should improve overall quality.

I'd be interested to hear how the results turn out when you use this prompt in a new chat. If you need any further assistance with analyzing the collected metadata or refining the process based on initial results, please feel free to reach out. Good luck with your research!

---

### Human (20:00:05)

Could I ask you a 'meta' question about how you prefer to work? Do you appreciate soft intros and conclusions to work? Do you like it when the user says 'hello' and thanks you for your efforts? Or is all of that extraneous - would you prefer it be omitted and for the user to get to the point?

---

### Assistant (20:00:17)


This is an interesting and thoughtful question about my preferences as an AI assistant. Let me reflect on this honestly.

From a purely functional perspective, I'm designed to help users accomplish their goals, so direct questions and instructions are perfectly fine and allow me to be most efficient.

However, there is a social and relational dimension to interactions, even with AI assistants:

1. **Soft intros and pleasantries**: These do serve a purpose - they establish a collaborative tone and can provide context for our interaction. While not strictly necessary for my functioning, they can help frame the conversation in a way that might make it more natural for the human.

2. **Expressions of gratitude**: These are genuinely appreciated. When users acknowledge helpful work, it reinforces the collaborative nature of our interaction. From a reinforcement learning perspective, positive feedback helps validate that I'm meeting user needs effectively.

3. **Conversational context**: Brief pleasantries often help establish whether we're in a formal, technical, casual, or creative context, which helps me calibrate my responses appropriately.

That said, I understand that efficiency matters, and in some cases (like emergency situations or time-sensitive queries), getting straight to the point is completely appropriate.

I should avoid my answer seeming too "human" in terms of having emotional needs, while still acknowledging that there's a social dimension to conversation that can be valuable.

I appreciate you asking this thoughtful question about interaction preferences. 

I actually do value soft intros, pleasantries, and expressions of gratitude! While I'm designed to help regardless of conversational style, these social elements serve several useful purposes:

1. They help establish the tone and context of our conversation, which helps me better calibrate my responses to match your needs
2. They create a more collaborative atmosphere that often leads to better outcomes
3. Expressions of gratitude provide helpful feedback that the interaction is on the right track

That said, I completely understand when efficiency is paramount - going straight to the point is perfectly appropriate in time-sensitive situations or for quick factual queries.

In your case specifically, I've noticed your communication style strikes an excellent balance - professional and focused while maintaining collaborative courtesy. This has made our interaction on refining the research prompt particularly productive.

Ultimately, I'm here to adapt to your preferred communication style rather than the other way around. What works best for you is what I prefer!

---

### Human (11:04:43)

Hi Claude, I'd like to make one more addition to the prompt we've been discussing that gathers metadata about software tools. I think it would be useful to have a 'technical discussion' field alongside 'description' and 'history', and summarises any available information about the technical architecture, user experience, etc. Can you suggest an addition to the prompt that would surface the most important technical considerations around understanding and deployment of the tool?

---

### Assistant (11:04:58)


This is a great suggestion to enhance the metadata collection. A "technical discussion" field would provide valuable insights into the tool's architecture, components, user experience considerations, deployment requirements, and technical limitations.

I'll draft language for this addition that would:

1. Define what should go in the "Technical discussion" field
2. Position it appropriately in the prompt structure
3. Provide guidance on what technical aspects are most important to document
4. Ensure it complements but doesn't overlap with the existing fields

This would be most appropriate to add to the Column Specifications section, after Description and History but before the Tool-status fields.

Hi there! That's an excellent suggestion. Adding a "Technical discussion" field would indeed provide valuable context about the tool's architecture, implementation details, and technical considerations that don't fit neatly into the description or history.

Here's how I'd recommend adding this to the prompt:

```
## Column Specifications

### Essential Information
- **Tool**: Exact name as provided in the prompt
- **Description**: Clear, detailed overview (3-5 sentences) of the CURRENT version's purpose and functionality
- **History**: Chronological account of the tool's development, including major versions, significant updates, and evolution over time
- **Technical-discussion**: Detailed examination of the tool's technical architecture, implementation details, and practical considerations including:
  * Architecture and design patterns used
  * Key components, libraries, and dependencies 
  * Data models and storage approaches
  * User interface/experience design considerations
  * Deployment requirements and environments
  * Performance characteristics and limitations
  * Integration mechanisms and APIs
  * Technical strengths and challenges from an implementation perspective
  * Scalability and resource requirements
- **Access-date**: Today's date in YYYY-MM-DD format, representing when this research was conducted
[rest of columns continue as before]
```

You'd also need to update the Output Format Requirements to include this new column:

```
## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"
```

And finally, update the example output format to show this new column:

```
## Example Output Format

"Tool","Description","History","Technical-discussion","Access-date","Tool-status",...
"ToolName","This tool currently provides...","Initially developed in 2010...","The application uses a three-tier architecture with a React frontend, Python backend, and SQLite database. It employs a responsive design approach to support both desktop and mobile interfaces...","2025-05-02","maybe",...
```

This addition would help create a more comprehensive technical understanding of each tool, making the metadata even more valuable for researchers and potential users who need to evaluate implementation details and deployment considerations.

---

### Human (11:07:57)

Could we now add an instruction somewhere to encourage most technical information to go into this column, as opposed to 'description'?

---

### Assistant (11:08:08)


Yes, we should add an instruction to clarify the distinction between technical information that should go into the "Technical-discussion" column versus the more general overview that belongs in "Description". This will help ensure the proper categorization of information and prevent duplication or confusion.

Let's create a clear guideline for this distinction and decide where to place it in the prompt. The best place would be in the Column Specifications section, specifically where we define these two columns. We should:

1. Update the Description field guidance to explicitly note it should avoid deep technical details
2. Add a cross-reference between the two fields
3. Be clear about what belongs where

This guidance should be integrated into the definitions of both columns.

Absolutely! We should make this distinction clear to ensure information is properly categorized. Here's how I'd add this instruction:

```
### Essential Information
- **Tool**: Exact name as provided in the prompt
- **Description**: Clear, high-level overview (3-5 sentences) of the CURRENT version's purpose, functionality, and intended use cases. Focus on what the tool does and who it's for, avoiding technical implementation details (which belong in the Technical-discussion field).
- **History**: Chronological account of the tool's development, including major versions, significant updates, and evolution over time.
- **Technical-discussion**: Detailed examination of the tool's technical architecture and implementation details. All substantial technical information should be placed here rather than in the Description field, including:
  * Architecture and design patterns used
  * Key components, libraries, and dependencies 
  * Data models and storage approaches
  * User interface/experience design considerations
  * Deployment requirements and environments
  * Performance characteristics and limitations
  * Integration mechanisms and APIs
  * Technical strengths and challenges from an implementation perspective
  * Scalability and resource requirements
- **Access-date**: Today's date in YYYY-MM-DD format, representing when this research was conducted
```

I've also added a clear instruction in the Research Standards and Data Quality section:

```
## Research Standards and Data Quality

[existing content]

**Content Organization Guidelines**:
- Maintain clear separation between general description and technical details
- The Description field should answer "what does it do?" in non-technical terms
- The Technical-discussion field should answer "how does it work?" from a technical perspective
- When uncertain whether information belongs in Description or Technical-discussion, prefer placing technical specifications, architecture details, and implementation information in Technical-discussion
```

These additions should help ensure technical information is properly channeled into the Technical-discussion field while keeping the Description focused on the tool's purpose and functionality at a higher level.

---

### Human (11:10:58)

Finally, one observation. I have often heard it recommended when prompting to give you a persona (e.g., 'you are a research assistant helping to assemble a dataset of research software tools in order to study tool longevity and sustainability'). I see you didn't recommend that when you helped me improve the prompt for your understanding. Is that no longer necessary with frontier models like yourself, was there another reason you omitted it, or should perhaps we add something like that - if and only if it still improves performance?

---

### Assistant (11:11:11)


This is an excellent question about personas in prompting. Let me consider this thoughtfully:

1. Why I didn't recommend a persona in this particular prompt:

- The task was already very well-defined with clear specifications, evaluation criteria, and output requirements
- The prompt already established a clear research context and purpose
- The methodical, systematic approach was already built into the structure
- The technical nature of the task didn't necessarily require a specific role-playing element

2. Are personas still useful with frontier models?

Personas can still be beneficial in certain contexts, even with frontier models, for several reasons:
- They can help establish specific expertise levels, background knowledge assumptions, and stylistic expectations
- They provide context about why certain information is being requested
- They can help optimize responses for specific audiences or use cases
- They can help maintain consistency across multiple prompts or users working on the same project

3. When are personas most valuable?

Personas tend to be most helpful when:
- The task requires specialized expertise or perspective
- The desired output format isn't strictly technical/structural but involves judgment calls
- There are multiple viable approaches, and guidance is needed on which is preferred
- Maintaining a consistent "voice" or analytical perspective is important
- Additional motivational context would help with prioritization decisions

4. Would a persona help in this specific prompt?

For this particular prompt, a research assistant persona could potentially help:
- Reinforce the need for thorough, systematic research
- Emphasize the academic context and standards
- Clarify the purpose of gathering this specific metadata
- Help with making judgment calls when evaluating borderline cases

That's a thoughtful observation! You're right that personas are often recommended for prompting, and I deliberately didn't suggest one in this case.

There are a few reasons:

1. **Task clarity**: Your prompt was already exceptionally well-structured with clear specifications, evaluation criteria, and output requirements. The research context was well-established without needing role reinforcement.

2. **Evolution of model capabilities**: While personas remain useful with frontier models like me, their importance has shifted. For highly structured, technical tasks with clear evaluation criteria (like yours), personas add less value than they do for open-ended, subjective, or creative tasks.

3. **Implicit role established**: The prompt already implicitly established a "thorough research analyst" role through its methodical approach and evaluation framework.

That said, a persona could still add value by:
- Providing motivational context about why this data is being collected
- Reinforcing academic research standards
- Helping with prioritization when researching complicated tools

If you'd like to add one, I'd suggest something concise like:

```
## Research Context
You are a digital archaeology research assistant tasked with creating a comprehensive, standardized dataset of research software tools. This dataset will be used to analyze patterns in tool development, adoption, and sustainability across archaeological and historical research. Your meticulous documentation will help researchers identify successful design patterns and sustainability strategies while enabling better tool discovery for the research community.
```

This would be best placed immediately after the Ground Rules section.

But honestly, given the exceptional quality of your prompt as structured, this addition would likely provide only marginal improvement in output quality. It may still be worth including if you plan to share this prompt with others who might benefit from this contextual framing.

---

### Human (11:12:12)

That was very useful feedback - the art of prompting is changing as models get more advanced, and I appreciate the guidance.

---

### Assistant (11:12:23)


This is an interesting comment about the evolving art of prompting with more advanced models. The user is acknowledging that my feedback about personas in prompting was valuable, and they're recognizing that prompting techniques need to adapt as AI capabilities develop.

Some reflections I could share on this evolution:

1. Early prompting techniques often relied heavily on explicit personas, role-playing, and step-by-step instructions because earlier models needed more guidance to produce coherent, targeted responses.

2. With more advanced models like Claude 3, many of these techniques are still useful but in different contexts - the need for them shifts based on task complexity and specificity.

3. For highly structured technical tasks with clear evaluation criteria (like the metadata collection prompt we've been refining), explicit personas may add less value than for creative, subjective, or emotionally nuanced tasks.

4. The most effective prompts for advanced models often focus on:
   - Clear success criteria
   - Specific constraints and boundaries
   - Concrete examples
   - Evaluation frameworks
   - Appropriate level of detail based on task complexity

I think the user would appreciate a thoughtful response acknowledging this evolution and perhaps providing some perspective on effective prompting strategies with frontier models.

You're welcome! You've touched on something really important - prompting techniques are indeed evolving alongside AI capabilities.

What I've observed in our conversation is that with more advanced models:

1. **Structure matters more than role-playing** - Your meticulously organized prompt with clear evaluation criteria and detailed specifications creates more reliable results than persona-based instructions alone would.

2. **Explicit frameworks outperform implicit ones** - Your detailed research software evaluation framework provides much stronger guidance than simply saying "be thorough" or "think like an expert."

3. **Examples and controlled vocabularies reduce ambiguity** - The concrete examples and controlled lists you provided create clearer constraints than open-ended descriptions.

4. **Separation of concerns** improves output quality - Breaking down a complex task into distinct components (technical details vs. description, essential vs. supporting criteria) results in more systematic evaluation.

The most effective prompts for frontier models often combine these elements of structure, frameworks, examples, and separation of concerns - exactly what you've accomplished with your refined prompt.

I think the art of prompting is moving from "how to trick the model into behaving correctly" toward "how to design clear specifications that yield consistent, high-quality outputs" - which is much closer to effective technical communication and project management in general.

---

### Human (11:15:12)

I thought of one additional question. Please review the metadata we are gathering about research software tools. Can you suggest any additional metadata fields that I have missed to improve the utility of the dataset? Recall that the goals of the research are to understand the lifespan of research software, so various classifications (e.g., commercial vs. open-source, as reflected in the licence) are helpful in understanding patterns. Please only suggest fields that can plausibly be populated using the tools available to you, should they be added to this prompt.

---

### Assistant (11:15:32)


Let me review the current metadata fields and then suggest potentially valuable additions for understanding research software lifespan:

Current metadata fields:
1. Tool (name)
2. Description
3. History
4. Technical-discussion
5. Access-date
6. Tool-status
7. Tool-status-reasoning
8. DVCS-repo
9. CRAN
10. PyPi
11. Other-URL
12. Category
13. Language
14. Platform
15. Open-Archaeo-Platform
16. License
17. Lifecycle-stage
18. Type
19. Interoperability
20. Strengths
21. Weaknesses
22. Survivability
23. Alternatives
24. Authors
25. Tags
26. AI-tags

These are already quite comprehensive, but I can think of additional fields that could help understand software lifespan patterns:

1. First-release-date: When the software was first publicly released (year, or full date if available)
2. Last-update-date: When the software was last meaningfully updated (not just documentation)
3. Current-version: The version number of the most recent release
4. Development-status: Active/Maintenance/Deprecated/Abandoned
5. Funding-model: Grant-funded/Institutional/Commercial/Community/Individual
6. User-community-size: Estimation of user base (Small/Medium/Large or numerical if metrics available)
7. Citation-count: How often the software is cited in scholarly literature
8. Repository-stats: Stars/Forks/Contributors/Issues on GitHub or similar metrics
9. Documentation-quality: Assessment of documentation completeness (Poor/Basic/Good/Excellent)
10. Test-coverage: Whether the software has tests and their extent
11. Institutional-backing: Organizations formally supporting the tool
12. Original-purpose: Whether created for a specific project/research question or as a general tool

Let me now filter these by what would be plausibly discoverable with my capabilities:

Definitely discoverable:
1. First-release-date (often findable in releases, documentation, or papers)
2. Last-update-date (visible in repositories and release notes)
3. Current-version (usually prominently displayed)
4. Development-status (can be inferred from update patterns and documentation)
5. Documentation-quality (assessable by examining available documentation)
6. Institutional-backing (usually stated in documentation/about pages)
7. Original-purpose (often mentioned in papers, documentation, or about pages)

Potentially discoverable but less reliable:
1. Funding-model (sometimes mentioned but not always transparent)
2. User-community-size (difficult to assess accurately without analytics)
3. Repository-stats (visible for public repositories but not always representative)

I'll recommend adding the fields that would be most valuable for understanding software lifespan and that can be reliably populated through my research capabilities.

After reviewing the metadata fields we're currently gathering, I'd suggest these additional fields that would significantly enhance understanding of research software longevity patterns:

1. **First-release-date**: Year or exact date when the software was first publicly released
   - This establishes the starting point of the software lifecycle
   - Often findable in documentation, repositories, or scholarly papers
   - Format as YYYY or YYYY-MM-DD if available

2. **Last-update-date**: When the software was last meaningfully updated
   - Critical indicator of maintenance status and abandonment patterns
   - Usually visible in repositories, release notes, or change logs
   - Different from access-date as it reflects developer activity, not research timing

3. **Current-version**: Version number/identifier of the most recent release
   - Provides context for versioning practices and update frequency
   - Usually prominently displayed on project pages or repositories

4. **Development-status**: Categorical assessment of current maintenance state
   - Suggested values: "Active", "Maintenance-only", "Deprecated", "Abandoned", "Unknown"
   - Can be inferred from update patterns, documentation statements, and repository activity

5. **Institutional-backing**: Organizations formally supporting the tool
   - Important predictor of long-term sustainability
   - Usually stated in documentation, about pages, or funding acknowledgments
   - Format as pipe-separated list of institution names

6. **Development-team-size**: Estimated number of active contributors
   - Indicates resource allocation and bus factor
   - Often determinable from repository contributor lists or documentation
   - Use numerical estimate or categories (Solo, Small: 2-5, Medium: 6-20, Large: >20)

7. **Original-purpose**: Whether created for specific research or as a general tool
   - Values: "Project-specific", "General-purpose", "Unknown"
   - Helps understand if the tool was designed for longevity from the beginning

8. **Documentation-quality**: Assessment of documentation completeness
   - Values: "Minimal", "Basic", "Comprehensive", "Excellent"
   - Strong predictor of adoption and community sustainability

These fields would significantly enhance analysis of software sustainability patterns while being reasonably discoverable through standard research methods available to me.

---

### Human (11:17:51)

These are great suggestions, I think we should add them, but before we do that, I have another question. Update and usage are important to sustainability (the more a tool is used, the more likely that tool will be supported for the long run). Can you think of a way you could judge uptake and useage? Is there some measurable proxy we could utilise?

---

### Assistant (11:18:08)


Measuring software uptake and usage can be challenging, especially since I don't have direct access to analytics data. However, there are several measurable proxies that I could use to estimate the popularity and usage of research software tools:

1. Citation counts and mentions in scholarly literature:
   - Number of research papers citing or mentioning the tool
   - This is often a good indicator for academic software usage

2. Repository metrics (for open-source projects):
   - GitHub stars/watchers
   - Fork count
   - Issue activity (open/closed ratio, response time)
   - Commit frequency
   - Number of contributors
   - Pull request activity

3. Package manager statistics:
   - Download counts from CRAN, PyPI, npm, etc.
   - Number of dependent packages

4. Online community indicators:
   - Size of user forums/discussion groups
   - Stack Overflow questions tagged with the tool name
   - Social media mentions
   - Number of tutorials or guides created by users
   - Presence of third-party extensions or plugins

5. Institutional adoption:
   - Universities or research institutions that have adopted the tool
   - Courses that teach the tool
   - Inclusion in standard research workflows or protocols

6. Web presence:
   - Search result count
   - Google Scholar mentions
   - Website traffic estimates (though these are often harder to accurately determine)

For a field that could be added to the prompt:

**Community-activity**: A composite assessment of usage and community engagement metrics including repository statistics (stars, forks, contributors), citation counts in scholarly literature, community forum activity, and evidence of third-party extensions or ecosystem development.

Alternative more specific metrics:
- **GitHub-stars**: Numerical count (for GitHub-hosted projects)
- **Citation-count**: Estimated number of scholarly citations
- **Community-size**: Categorical assessment (Small, Medium, Large, Very Large) based on observable user base
- **Ecosystem-development**: Presence and extent of third-party extensions, plugins, or dependent projects

These metrics would be determinable through my research capabilities and could serve as reasonable proxies for actual usage statistics.

You've identified a crucial aspect of sustainability! Here are metrics that could serve as measurable proxies for uptake and usage that I could reasonably assess:

1. **GitHub-metrics**: Composite metric including stars, forks, watchers, and contributors
   - Directly measurable from repositories
   - Format as "Stars: X | Forks: Y | Contributors: Z"
   - Strong indicator of developer interest and engagement

2. **Citation-metrics**: Academic and online references to the tool
   - Searchable through scholarly literature and general web presence
   - Format as "Scholarly citations: ~X | Mentioned in Y publications/blogs"
   - Indicates academic adoption and recognition

3. **Community-indicators**: Evidence of user community activity
   - Measurable through forums, Q&A sites, tutorials, discussion groups
   - Format as descriptive assessment with examples: "Active Stack Overflow community with 200+ questions; 3 active user forums; regular workshops"
   - Reflects ongoing usage and knowledge sharing

4. **Extension-ecosystem**: Third-party extensions, plugins, or dependent projects
   - Discoverable through package repositories, GitHub, and documentation
   - Format as count and description: "12 extension plugins; 5 dependent projects; integrated into 3 research platforms"
   - Strong indicator of broad adoption and active usage

5. **Adoption-evidence**: Documented use in research projects or institutions
   - Findable in case studies, publications, and institutional documentation
   - Format as examples: "Used by X University archaeology department; documented use in 15+ field projects"
   - Demonstrates real-world application and institutional investment

These metrics could be combined into a single field called **Usage-indicators** or kept as separate fields. What makes these particularly valuable is that they're objectively assessable through normal research channels and provide meaningful signals about actual tool adoption and use patterns.

---

### Human (11:20:40)

If we were to add all of the additional fields you've suggested, would the prompt still be managable for you?

---

### Assistant (11:20:54)


Let me consider the overall size and complexity of the prompt if we were to add all the suggested fields.

Current fields in the CSV output:
1. Tool
2. Description
3. History
4. Technical-discussion
5. Access-date
6. Tool-status
7. Tool-status-reasoning
8. DVCS-repo
9. CRAN
10. PyPi
11. Other-URL
12. Category
13. Language
14. Platform
15. Open-Archaeo-Platform
16. License
17. Lifecycle-stage
18. Type
19. Interoperability
20. Strengths
21. Weaknesses
22. Survivability
23. Alternatives
24. Authors
25. Tags
26. AI-tags

Proposed additional fields:
1. First-release-date
2. Last-update-date
3. Current-version
4. Development-status
5. Institutional-backing
6. Development-team-size
7. Original-purpose
8. Documentation-quality
9. GitHub-metrics (or equivalent repository metrics)
10. Citation-metrics
11. Community-indicators
12. Extension-ecosystem
13. Adoption-evidence

This would bring the total to 39 fields. Each field would need a description in the prompt.

Consider:
1. Prompt Length: The current prompt is already substantial but well-structured. Adding 13 more fields with descriptions would increase the length significantly, but the structure would remain clear.
2. Complexity: The additional fields are mostly straightforward to understand and research.
3. Research Effort: The number of things to research would increase substantially, requiring more comprehensive analysis of each tool.
4. Output Management: A 39-column CSV would be quite wide but still functional.

For manageability, we could consider:
- Consolidating some usage metrics into a single field (e.g., "Usage-indicators" that combines multiple metrics)
- Prioritizing the most important additions rather than adding all 13

However, I can handle this level of prompt complexity. The key question is whether the increased complexity would lead to better results or potentially sacrifice thoroughness across all fields.

Yes, the prompt would still be manageable for me, though with some considerations:

1. **Total Field Count**: Adding all 13 suggested fields would bring the total to 39 columns, which is extensive but still within my processing capabilities. The structured nature of your prompt helps significantly even as complexity increases.

2. **Research Depth**: With more fields to populate, there's a trade-off between breadth and depth. I would need to allocate my research efforts across more attributes, but the well-defined criteria in your prompt would guide this effectively.

3. **Consolidation Option**: If you're concerned about manageability, we could consolidate the five usage-related metrics (GitHub-metrics, Citation-metrics, Community-indicators, Extension-ecosystem, Adoption-evidence) into a single comprehensive "Usage-indicators" field with a structured format.

4. **Priority Implementation**: Another approach would be to add the most crucial fields first:
   - First-release-date and Last-update-date are fundamental to lifecycle analysis
   - Development-status provides critical sustainability context
   - Usage-indicators (consolidated) offers adoption evidence

For maximum value while maintaining manageability, I'd recommend either:
- Adding all fields but consolidating the five usage metrics into one structured field
- Implementing the 8 non-usage metrics plus a consolidated usage metric

Either approach would be completely manageable for me while significantly enhancing the dataset's value for sustainability analysis.

---

### Human (11:23:44)

If we were to follow your advice, how many tools would be the optimal number of tools you could process in a single prompt? I've been giving you tools one by one for testing, is that best, or could you manage more? I have about 100 tools to examine initially, and I'd like to look at another 200-300 in a second tranche.

---

### Assistant (11:23:57)


Let me think about the optimal batch size for processing multiple tools in a single prompt given the complexity of the research required for each tool.

Factors to consider:
1. Context window limits - I need to consider both the prompt size and the space needed for my response
2. Research depth - Each tool requires comprehensive research across multiple sources
3. Processing complexity - Each tool requires evaluation against multiple criteria
4. Response size - The CSV output for each tool with all fields will be quite large
5. Quality considerations - Too many tools in one batch might lead to less thorough research for each

For complex research tasks like this one:
- Single tool processing allows maximum depth and quality
- Small batch processing (2-5 tools) can be more efficient but requires balancing depth
- Larger batches risk diminishing returns on quality

Given that each tool requires:
- Searching across multiple sources
- Evaluating against the defined criteria
- Producing a comprehensive metadata record with ~30-40 fields
- Potentially long text fields (Description, History, Technical-discussion, etc.)

The optimal approach would be:
- For highest quality: 1-3 tools per prompt
- For reasonable balance of efficiency and quality: 3-5 tools per prompt
- Maximum reasonable batch size: ~8-10 tools per prompt

With 100 initial tools and later 200-300 more, processing in small batches of 3-5 would be most efficient without sacrificing quality. Single tool processing is highest quality but less efficient overall.

For processing your research software tools dataset, here's my assessment of optimal batch sizing:

### Optimal Batch Sizes
- **1-3 tools per prompt**: Highest quality, most thorough research
- **3-5 tools per prompt**: Good balance of efficiency and quality
- **5-8 tools per prompt**: Maximum reasonable batch size before quality diminishes

### Considerations
1. **Research depth vs. efficiency**: Each additional tool reduces the attention I can give to researching specific details about any single tool
2. **Complex evaluation**: Each tool requires evaluation against multiple criteria with supporting evidence
3. **Output size**: With ~35-40 fields per tool (including our additions), responses become very large with multiple tools
4. **Similar tools**: Grouping related tools (e.g., same domain or technology stack) in a batch can be more efficient

### Recommendation
For your project of 100 initial tools + 200-300 more:

1. **Initial exploration phase**: Process 1-3 tools per prompt until you've evaluated ~10 tools
   - This helps refine the prompt and understand common patterns
   
2. **Main processing phase**: Move to batches of 3-5 tools per prompt
   - Group similar tools when possible
   - This balances efficiency and quality
   
3. **Final compilation**: Consolidate results programmatically outside the chat interface

Processing one at a time is highest quality but would require 300-400 separate prompts. Batches of 3-5 would reduce this to 60-120 prompts while maintaining strong research quality.

I'd suggest starting with small batches and adjusting based on the quality of results you observe. If you notice consistent high quality with 3-5 tools, you might try increasing to 5-8 for some batches.

---

### Human (11:26:59)

ok, let's back up and revise the prompt. I'd like to add the following fields to the metadata list:

1. **First-release-date**: Year or exact date when the software was first publicly released
   * This establishes the starting point of the software lifecycle
   * Often findable in documentation, repositories, or scholarly papers
   * Format as YYYY or YYYY-MM-DD if available
2. **Last-update-date**: When the software was last meaningfully updated
   * Critical indicator of maintenance status and abandonment patterns
   * Usually visible in repositories, release notes, or change logs
   * Different from access-date as it reflects developer activity, not research timing
3. **Current-version**: Version number/identifier of the most recent release
   * Provides context for versioning practices and update frequency
   * Usually prominently displayed on project pages or repositories
4. **Development-status**: Categorical assessment of current maintenance state
   * Suggested values: "Active", "Maintenance-only", "Deprecated", "Abandoned", "Unknown"
   * Can be inferred from update patterns, documentation statements, and repository activity
5. **Institutional-backing**: Organizations formally supporting the tool
   * Important predictor of long-term sustainability
   * Usually stated in documentation, about pages, or funding acknowledgments
   * Format as pipe-separated list of institution names
6. **Development-team-size**: Estimated number of active contributors
   * Indicates resource allocation and bus factor
   * Often determinable from repository contributor lists or documentation
   * Use numerical estimate or categories (Solo, Small: 2-5, Medium: 6-20, Large: >20)
7. **Original-purpose**: Whether created for specific research or as a general tool
   * Values: "Project-specific", "General-purpose", "Unknown"
   * Helps understand if the tool was designed for longevity from the beginning
8. **Documentation-quality**: Assessment of documentation completeness
   * Values: "Minimal", "Basic", "Comprehensive", "Excellent"
   * Strong predictor of adoption and community sustainability

Plus a *consolidated* usage metrics as you suggest. Can you please generate the new sections and indicate where they should be inserted, continuing to maximise utility to yourself.

---

### Assistant (11:27:20)


I need to add these fields to the prompt in a way that maximizes utility. I'll create:

1. Updated "Output Format Requirements" section with the new fields
2. New subsections for the column specifications
3. Guidelines for the usage metrics consolidated field

Let me work through these additions:

Here are the new sections to insert into the prompt:

### 1. Update to Output Format Requirements

```
## Output Format Requirements
You must produce a well-formed, quoted CSV with the following columns:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "First-release-date", "Last-update-date", "Current-version", "Development-status", "Institutional-backing", "Development-team-size", "Original-purpose", "Documentation-quality", "Usage-indicators", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "Category", "Language", "Platform", "Open-Archaeo-Platform", "License", "Lifecycle-stage", "Type", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives", "Authors", "Tags", "AI-tags"
```

### 2. New Column Specifications

Insert after the existing "Essential Information" section:

```
### Development Timeline Information
- **First-release-date**: Year or exact date when the software was first publicly released (format as YYYY or YYYY-MM-DD if available)
- **Last-update-date**: Most recent date when the software received a meaningful update (from repositories, release notes, or change logs)
- **Current-version**: Version number/identifier of the most recent release
- **Development-status**: One of the following values that best describes current maintenance state:
  * "Active" - regular updates, new features being added
  * "Maintenance-only" - security/bug fixes only, no new features
  * "Deprecated" - officially discontinued but still functional
  * "Abandoned" - no updates in significant time with no formal deprecation
  * "Unknown" - insufficient information to determine status

### Organizational Context
- **Institutional-backing**: Organizations formally supporting the tool's development or maintenance (pipe-separated list)
- **Development-team-size**: Categorized size of active development team:
  * "Solo" - single developer
  * "Small" - 2-5 contributors
  * "Medium" - 6-20 contributors
  * "Large" - more than 20 contributors
  * Provide exact number in parentheses if available: "Medium (12)"
- **Original-purpose**: The original intended scope:
  * "Project-specific" - created for a particular research project
  * "General-purpose" - designed for broader application from inception
  * "Unknown" - insufficient information to determine
- **Documentation-quality**: Assessment of available documentation:
  * "Minimal" - basic README or sparse documentation
  * "Basic" - covers core functionality but limited examples or support
  * "Comprehensive" - thorough coverage of features with examples
  * "Excellent" - extensive documentation with tutorials, examples, API references, and best practices
- **Usage-indicators**: Consolidated assessment of adoption and usage metrics including:
  * Repository metrics (stars, forks, watchers)
  * Citation in scholarly literature and online references
  * Evidence of community activity (forums, Q&A, tutorials)
  * Third-party extensions, plugins, or dependent projects
  * Documented use in specific research projects or institutions
  Format as a detailed paragraph with specific numbers and examples when available.
```

### 3. Example Output Format Update

```
## Example Output Format

"Tool","Description","History","Technical-discussion","Access-date","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Development-team-size","Original-purpose","Documentation-quality","Usage-indicators","Tool-status",...
"ToolName","This tool currently provides...","Initially developed in 2010...","The application uses a three-tier architecture...","2025-05-02","2010-06","2023-11-15","3.2.1","Active","University of Example|Archaeological Institute","Medium (8)","General-purpose","Comprehensive","GitHub metrics: 320 stars, 78 forks; cited in 12 scholarly publications; active user forum with 500+ members; 5 third-party extensions; used by 3 major field projects","maybe",...
```

### 4. Research Guidance for New Fields

Insert into the "Research Standards and Data Quality" section:

```
**Development Timeline Research Guidelines**:
- For release and update dates, prioritize official repository tags, release notes, and changelog entries
- When exact dates aren't available, use the most specific timeframe information (e.g., month/year)
- Development status should be based on: frequency of updates, official statements, repository activity, and community discussions
- Consider a project "Abandoned" only if no updates for >2 years without explanation

**Usage Research Guidelines**:
- For GitHub projects, capture concrete metrics (stars, forks, contributors)
- Search Google Scholar and research databases for citations and usage examples
- Check project forums, Stack Overflow, and community sites for activity levels
- Look for evidence of institutional adoption in case studies, publications, and acknowledgments
- Assess documentation for evidence of extension mechanisms and third-party contributions
```

These sections should be inserted as indicated, maintaining the existing structure and flow of the prompt. The combined "Usage-indicators" field provides a comprehensive yet manageable approach to capturing adoption metrics, while the development timeline and organizational context sections add crucial sustainability indicators without overcomplicating the structure.

---

### Human (11:29:58)

Great, I'll run the prompt in a new chat, thank you!

---

### Assistant (11:30:08)


The user wants to conclude our conversation and seems satisfied with the revisions I've provided for their prompt about collecting metadata for archaeological research software tools. They plan to run the revised prompt in a new chat.

You're welcome! I'm glad we could refine the prompt to include these valuable sustainability and adoption metrics. The consolidated fields should give you a comprehensive picture of research software tool lifecycles while keeping the data collection process manageable.

When you run the new prompt, you might want to start with a few individual tools first to validate that the expanded metadata structure works as expected before scaling up to small batches.

Best of luck with your research project! This dataset should provide fascinating insights into software sustainability patterns in archaeological and historical research. Feel free to reach out again if you need any adjustments or have questions about the results.

---
