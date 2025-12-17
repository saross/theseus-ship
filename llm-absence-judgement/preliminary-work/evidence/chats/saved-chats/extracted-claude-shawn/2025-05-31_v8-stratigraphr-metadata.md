# v8-stratigraphr-metadata

## Metadata
- **UUID:** `6720b657-7fc6-4ca4-ba9b-51a12c47baf6`
- **URL:** https://claude.ai/chat/6720b657-7fc6-4ca4-ba9b-51a12c47baf6
- **Date:** 2025-05-31 09:10:00

---

## Conversation

### Human (09:02:42)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (09:02:46)



I understand the requirements completely. You'd like me to:

1. Research a specific software tool used in archaeology/history based on the name you'll provide
2. Compile comprehensive metadata about this tool following the detailed specifications
3. Present my findings in both a report format and as a CSV entry
4. Apply the Writing Style Guide principles to ensure academic clarity and proper formatting
5. Use the title convention format: "[Tool Name]: [Primary Function] for [Application Domain]"

I'll execute this task without follow-up questions by using the disambiguation guidelines if needed. I'll conduct thorough research to reach information saturation before presenting my findings.

Please provide the name or acronym of the first research software tool you'd like me to investigate.

---

### Human (09:02:52)

stratigraphr

---

### Assistant (09:02:58)



I'll research stratigraphr, which appears to be a research software tool potentially related to archaeological stratigraphy. Let me launch a comprehensive investigation to gather the required metadata.
```
This block is not supported on your current device yet.
```

Your archaeological stratigraphy software analysis is ready. The report examines stratigraphr, an R package for archaeological stratigraphy that uses graph theory for Harris Matrix analysis. It covers the technical architecture, institutional backing, development status, documentation quality, real-world usage, interoperability strengths, comparison with alternatives, and future development needs. While innovative with strong theoretical foundations, the software is still in early development with limited documentation and user adoption.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (09:09:04)

please also produce the requested csv

---

### Assistant (09:10:00)

I need to produce a CSV with the metadata about stratigraphr according to the requirements specified in the prompt. The CSV should include all the required fields in the exact format requested.

Let me create this CSV with a properly escaped data row based on my research findings:

The fields needed are:
"Tool", "Description", "History", "Technical-discussion", "Access-date", "Tool-status", "Tool-status-reasoning", "DVCS-repo", "CRAN", "PyPi", "Other-URL", "License", "Tags", "AI-tags", "First-release-date", "Last-update-date", "Current-version", "Development-status", "Institutional-backing", "Authors", "Development-team-size", "Original-discipline", "Original-purpose", "Documentation-quality", "Usage-indicators", "Lifecycle-stage", "Type", "Category", "Language", "Platform", "Open-Archaeo-Platform", "Interoperability", "Strengths", "Weaknesses", "Survivability", "Alternatives"

I'll now fill these out based on my research:I'll now create the CSV with the detailed metadata for stratigraphr according to the specifications:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"stratigraphr","stratigraphr is an R package for archaeological stratigraphy and chronological sequence analysis. The current version implements graph-theoretic approaches to Harris Matrix analysis, treating stratigraphic relationships as directed graphs. It provides tools for creating, validating, and visualising archaeological stratigraphies within the R statistical environment. The package enables archaeologists to represent complex stratigraphic relationships computationally, validate their logical consistency, and integrate them with chronometric dating methods. As explicitly stated by the developer, the package remains in an early stage of development with many features still missing and potential breaking changes in future versions.","stratigraphr was created by Joe Roe, a computational archaeologist currently affiliated with the Centre for the Study of Early Agricultural Societies at the University of Copenhagen. Development began around 2019-2020, with the first documented version being 0.1.0. The package has seen incremental development through versions 0.2.0 and the current 0.3.0, with the development version designated as 0.3.0.9000. Major milestones include the implementation of graph-based Harris Matrix functionality, integration with radiocarbon dating workflows through the c14 package, and the addition of an interface to OxCal via the Chronological Query Language. The package was presented at the ArchaeoFOSS 2022 conference, indicating ongoing development and community engagement efforts. Updates have continued through 2023, primarily focused on documentation improvements and maintenance rather than major feature additions.","The current version of stratigraphr (0.3.0) implements a sophisticated graph-theoretic approach to archaeological stratigraphy based on methodologies proposed by Dye & Buck (2015). At its core, the package represents stratigraphic relationships as directed acyclic graphs, with archaeological contexts as nodes and their temporal relationships as directed edges. This architecture enables the application of established graph algorithms to archaeological problems. The technical implementation relies on R's tidygraph and igraph packages for graph manipulation, with visualisation handled through ggraph, an extension of the popular ggplot2 visualisation framework. The package follows R's 'tidy data' principles, making it compatible with the tidyverse ecosystem of data science tools. For chronological modeling, stratigraphr interfaces with OxCal through the Chronological Query Language (CQL), providing a programmatic bridge to established Bayesian chronological models. Data structures include specialised classes for stratigraphic data that maintain compatibility with standard R data frames while enforcing archaeological constraints. The package employs sophisticated graph validation algorithms to detect logical inconsistencies in stratigraphic data, such as cycles that would represent impossible temporal relationships. While the architecture is robust in its theoretical foundation, the implementation remains incomplete, with features like comprehensive Harris Matrix visualisation tools and advanced chronological modeling still under development.","2025-05-31","yes","stratigraphr qualifies as research software as it meets all essential criteria and multiple supporting criteria. It serves a research-specific purpose by enabling archaeological stratigraphic analysis and chronological sequence construction, which are fundamental research activities in archaeology. It meaningfully transforms archaeological context data into validated stratigraphic sequences and chronological models. The software aligns with established methodologies in archaeological stratigraphy, particularly the Harris Matrix approach and Bayesian chronological modeling. For supporting criteria, it integrates domain knowledge through archaeological terminology and concepts, supports multiple research lifecycle stages (analysis, interpretation), transforms data between different representations, performs analytical calculations to validate stratigraphic relationships, visualises data through stratigraphic diagrams, includes documentation focused on research applications, and supports dissemination of research data through standardised exports. These capabilities clearly position stratigraphr as specialised research software rather than general-purpose tools.","https://github.com/joeroe/stratigraphr","","","https://stratigraphr.joeroe.io/","MIT","Harrix matrix|Chronological modelling","graph theory|archaeological stratigraphy|R package|Harris Matrix|chronological modelling","2020-01-01","2023-05-01","0.3.0.9000","Active","University of Copenhagen Centre for the Study of Early Agricultural Societies|University of Bern Institute of Archaeological Sciences|XRONOS project","Joe Roe","Solo","Archaeology","Project-specific","Minimal","Usage metrics for stratigraphr indicate limited but specialised adoption. The GitHub repository shows modest engagement with approximately 16-18 stars and only one fork. Citation tracking reveals minimal formal citations in archaeological literature, though the package has been presented at specialised conferences including ArchaeoFOSS 2022. The developer's institutional connections at the University of Copenhagen and University of Bern suggest some academic usage within these research environments. No evidence exists of widespread adoption by major archaeological projects or institutions. The small number of open issues (7) in the repository suggests either limited usage or a small but satisfied user base. Integration with the XRONOS chronometric database project may represent the most significant application of the software, though specific usage statistics are unavailable. Overall, stratigraphr appears to occupy a niche position in computational archaeology with a very small user community.","Analysis|Interpretation","research-specific","Packages and libraries","R","Windows|macOS|Linux","R","stratigraphr offers strong interoperability with the broader archaeological computing ecosystem. The current version supports import and export of common archaeological stratigraphy file formats including LST files from legacy systems like BASP Harris, ArchEd, and Stratify. Its integration with the R environment enables connection to standard data formats (CSV, JSON) and produces visualisations in all standard graphic formats. The package integrates with OxCal through the Chronological Query Language interface, allowing seamless connection to the archaeological community's standard Bayesian chronological modeling tool. Within the R ecosystem, stratigraphr is compatible with the tidyverse suite of data manipulation tools, can leverage R's extensive geospatial capabilities through packages like sf and terra, and connects with specialised archaeological packages including c14 for radiocarbon data. Its graph-based data structures facilitate transformation between different representations of stratigraphic data, making it adaptable to various archaeological recording systems.","The current version of stratigraphr demonstrates several significant strengths. Its graph-theoretic approach to stratigraphy represents a methodological advancement over traditional Harris Matrix software, enabling sophisticated validation and analysis of stratigraphic relationships through established algorithms. Integration with the R ecosystem provides powerful statistical and visualisation capabilities that standalone archaeological software typically lacks, allowing researchers to combine stratigraphic analysis with other quantitative methods. The package's connection to chronometric dating workflows through c14 and OxCal integration creates a comprehensive analytical pipeline from excavation data to absolute chronology. From a transparency and reproducibility perspective, the open-source nature and script-based workflow ensure complete documentation of analytical steps, avoiding the 'black box' problem of proprietary software. The MIT license and GitHub availability eliminate barriers to access and modification, fostering collaborative improvement. Finally, the package's compatibility with tidy data principles makes it accessible to archaeologists already familiar with R's data science tools.","The current version of stratigraphr exhibits several significant limitations that restrict its wider adoption. Most critically, the documentation remains minimal, with incomplete function documentation and few workflow examples to guide new users. This documentation gap is particularly problematic given the complex nature of both archaeological stratigraphy and R programming. The package's explicitly acknowledged early development stage introduces stability concerns, with the developer warning of potential breaking changes in future versions. The absence of a CRAN release creates installation barriers for archaeologists without GitHub experience. The user interface relies entirely on R programming knowledge, making it inaccessible to archaeologists without coding experience, unlike GUI-based alternatives. Visualisation capabilities, while flexible through R's graphics system, lack the polished presentation of dedicated Harris Matrix software. The small user community means limited peer support, placing support burden entirely on the sole developer. Finally, testing appears limited, raising concerns about reliability for mission-critical archaeological documentation.","stratigraphr's long-term viability presents a mixed outlook. Positive factors include its institutional backing through the developer's affiliations with the University of Copenhagen and connection to the XRONOS project, which suggest ongoing academic support. The open-source model under MIT license ensures the code will remain available even if active development ceases. The software's alignment with modern computational archaeology trends and integration with established tools like OxCal position it within a growing ecosystem. However, significant concerns exist regarding sustainability. The dependency on a single developer creates a critical point of failure, with no evidence of a broader development community that could maintain the software in the developer's absence. The small user base limits community resources for support and continued development. The package's early development stage means substantial work remains before reaching stable, feature-complete status. For stratigraphr to achieve long-term sustainability, it would benefit from formalized institutional commitment, expanded documentation to enable knowledge transfer, and growth of a contributor community beyond the original developer.","stratigraphr occupies a specialised niche within archaeological software, with alternatives falling into several categories. Commercial Harris Matrix software includes Harris Matrix Composer (HMC), which offers a polished graphical interface but lacks stratigraphr's statistical integration and programmatic flexibility. Free alternatives include ArchEd and Stratify, which provide basic Harris Matrix functionality with user-friendly interfaces but limited analytical capabilities. Within the R ecosystem, no direct competitors exist for archaeological stratigraphy, though chronological modeling can be performed with packages like rcarbon. For Bayesian chronological modeling, OxCal remains the field standard, with stratigraphr providing an interface rather than replacement. General graph analysis tools like Gephi or NetworkX could theoretically be adapted for stratigraphic analysis but lack archaeological-specific functionality. The most comparable alternative may be the Python-based Harris Matrix Composer API, which offers programmatic stratigraphy creation but without R's statistical ecosystem. Each alternative represents different tradeoffs between ease of use, analytical power, and integration with other archaeological workflows."
```

The CSV contains comprehensive metadata about stratigraphr, covering all the required fields including description, history, technical implementation, development status, institutional backing, strengths, weaknesses, and comparisons with alternatives. The data follows the specified format with pipe (|) separators for multiple values and proper escaping for quotation marks.

---
