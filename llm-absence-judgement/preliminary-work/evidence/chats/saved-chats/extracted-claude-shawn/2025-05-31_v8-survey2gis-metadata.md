# v8-Survey2GIS-metadata

## Metadata
- **UUID:** `c60890c6-4f5a-4e22-b765-30a7ac7b9dbd`
- **URL:** https://claude.ai/chat/c60890c6-4f5a-4e22-b765-30a7ac7b9dbd
- **Date:** 2025-05-31 09:19:37

---

## Conversation

### Human (09:11:04)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (09:11:07)



I understand the task completely. I'll follow the detailed prompt to collect metadata about research software tools in archaeology, history, and other historical studies disciplines. I'll apply the Writing Style Guide to my report and CSV output, and follow the specified title conventions for the report.

I won't ask follow-up questions and will execute the prompt as specified. If there's any ambiguity about which tool I'm investigating, I'll consult the 'Tool disambiguation' section in the prompt.

I'm ready to begin - please provide the name or acronym of the first tool you'd like me to research.

---

### Human (09:11:13)

Survey2GIS

---

### Assistant (09:11:20)



I'll research Survey2GIS thoroughly and prepare a comprehensive metadata report following the guidelines provided. Starting my research process now!
```
This block is not supported on your current device yet.
```

Your Survey2GIS archaeological software analysis is ready. It covers the tool's role in converting field survey data to GIS formats, technical architecture, development history, and active maintenance despite its small community. The report examines Dr. Benjamin Ducke's leadership, documentation quality, institutional adoption patterns, and how Survey2GIS compares to alternatives like QGIS. It highlights the software's strengths in specialized archaeological workflows and institutional backing from German heritage agencies.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (09:18:38)

please also produce the requested csv

---

### Assistant (09:19:37)

I need to produce a CSV based on my research findings about Survey2GIS. This needs to follow the specific format mentioned in the prompt, with all the required fields. Let me create that now.

From my research, I can compile the following information for the CSV:

Tool: Survey2GIS
Description: Survey2GIS is a specialized open-source software tool that converts field survey data from total stations and GPS devices into GIS-ready formats. It serves as a critical bridge in archaeological documentation workflows, transforming coded coordinate files into topologically correct geometrical objects suitable for GIS analysis. The current version (1.5.2) supports various data formats, automated topological cleaning, and vertical section processing.
History: Initially developed in 2011-2012 by the Cultural Heritage Authority of Baden-Württemberg, Germany. Version 1.1 was the first public release, followed by incremental improvements. Version 1.3.3 (2017) marked transition to production use. Version 1.5.0 introduced spatial reference system transformation and vertical section support. Current stable version 1.5.2 was released in 2024, with active maintenance continuing.
Technical-discussion: Built primarily in C programming language with a minimalist approach prioritizing portability and flexibility. Runs as a portable application across Windows, Linux, and macOS platforms without installation (though Mac requires additional dependencies). The architecture centers on a flexible parser system using ASCII-encoded text files to describe input and output structures, allowing users to define custom parsing schemes for different survey equipment. Provides both GUI and CLI versions, with CLI enabling batch processing. Outputs include ESRI Shapefile (2D/3D), GeoJSON, and KML. Performs automated 2D topological corrections and validation, though 3D topology functions are limited. Features multi-language support with automatic OS language detection.
Access-date: 2025-05-31
Tool-status: yes
Tool-status-reasoning: Survey2GIS meets all essential criteria for research software: it has a research-specific purpose supporting archaeological fieldwork, it meaningfully transforms research data (survey coordinates into GIS formats), and aligns with recognized archaeological methodologies. It also satisfies multiple supporting criteria: it incorporates domain knowledge (archaeological survey standards), supports the research lifecycle (data processing stage), transforms data between formats, and provides documentation focused on research applications.
DVCS-repo: https://github.com/survey2gis/survey-tools
CRAN: 
PyPi: 
Other-URL: https://www.survey-tools.org/
License: GPL-3.0
Tags: Data management|Site mapping|Spatial analysis|Geophysical survey|Data collection
AI-tags: Archaeological survey processing|Total station data conversion|GIS format transformation|Field data digitization|Topological correction
First-release-date: 2012
Last-update-date: 2024-07-31
Current-version: 1.5.2
Development-status: Active
Institutional-backing: Cultural Heritage Authority of Baden-Württemberg, German Archaeological Institute (DAI), NFDI4Objects
Authors: Dr. Benjamin Ducke
Development-team-size: Small (2-5)
Original-discipline: Archaeology
Original-purpose: Project-specific
Documentation-quality: Comprehensive
Usage-indicators: Adoption metrics show a niche but committed user base primarily in European archaeological institutions. GitHub repository shows modest statistics (3 stars, 2 forks, 1 follower) but has documented institutional adoption by German heritage agencies (Baden-Württemberg, Bavaria) and Oxford Archaeology (UK). The software has been presented at Computer Applications and Quantitative Methods in Archaeology (CAA) conferences since 2018. Community support centers around an official mailing list at survey2gis@groups.io.
Lifecycle-stage: Processing
Type: research-specific
Category: Stand-alone software
Language: C
Platform: Windows|Linux|macOS
Open-Archaeo-Platform: 
Interoperability: Inputs include data from various total station and GPS devices through configurable parser files. Outputs in standard GIS formats including ESRI Shapefile (2D/3D), GeoJSON, and KML, ensuring compatibility with major GIS platforms. Supports automated 2D topological corrections and on-the-fly coordinate system transformations since version 1.5.0.
Strengths: Survey2GIS addresses a specific workflow gap with a lightweight, portable solution requiring no complex installation. Its flexible parser system adapts to various survey equipment and project requirements. Institutional backing from German heritage agencies provides stability and legitimacy. Its open-source nature (GPL 3.0) ensures long-term accessibility and prevents vendor lock-in—critical for archaeological data preservation. Automated topological validation and cleaning addresses common data quality issues in field survey data. The program provides both GUI and command-line interfaces, enabling batch processing for larger datasets.
Weaknesses: The small development team (essentially one lead developer with institutional support) creates sustainability risks. Limited community size restricts peer support and third-party development. Documentation, while academically rigorous, lacks user-friendly tutorial resources. Technical limitations include primarily 2D-focused topology operations and platform-specific issues like additional dependencies for macOS. The specialized nature limits broader adoption potential. The software lacks mobile integration, cloud synchronization, and real-time collaboration features found in newer alternatives.
Survivability: Survey2GIS demonstrates ongoing viability through continued institutional support and recent development activity. The last GitHub commit was July 31, 2024, indicating active maintenance. Integration with the NFDI4Objects national research infrastructure project provides funding stability. However, the project's dependence on a single lead developer represents a sustainability risk despite institutional backing. Future plans include a QGIS plugin, which could expand the user base while maintaining specialized functionality within a larger ecosystem.
Alternatives: QGIS with QField offers broader functionality and massive community support but requires more complex setup for survey-specific workflows. Commercial alternatives like ESRI's ArcGIS Suite with Survey123 provide comprehensive solutions at substantial cost (annual licenses $100-$7,000+). gvSIG-CE represents the closest alternative, sharing development philosophy with Survey2GIS. Specialized archaeological tools like Arches and ARK serve different workflow niches. Mobile-first solutions including KoBo Toolbox and ODK provide easier field data collection but lack Survey2GIS's specific total station integration and topological processing capabilities.

Now I'll format this as CSV following the required format:Based on my comprehensive research of Survey2GIS, I'll now provide the metadata in the required CSV format:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"Survey2GIS","Survey2GIS is a specialized open-source software tool that converts field survey data from total stations and GPS devices into GIS-ready formats. It serves as a critical bridge in archaeological documentation workflows, transforming coded coordinate files into topologically correct geometrical objects suitable for GIS analysis. The current version (1.5.2) supports various data formats, automated topological cleaning, and vertical section processing. European archaeological institutions have integrated the software into their standard workflows, with documented usage across Germany's state heritage agencies and Oxford Archaeology in the UK. Since version 1.5.0, it supports vertical section processing through Y/Z-axis switching, enabling archaeologists to document stratigraphic profiles—a feature particularly valuable for excavation documentation.","Initially developed in 2011-2012 by the Cultural Heritage Authority of Baden-Württemberg, Germany. Version 1.1 was the first public release, followed by incremental improvements. Version 1.3.3 (2017) marked transition to production use across Baden-Württemberg. Version 1.5.0 introduced significant features including on-the-fly spatial reference system transformation and vertical section support, addressing key archaeological requirements. The current stable version 1.5.2 was released in 2024. Development activity remains consistent if modest, with the GitHub repository showing the last commit on July 31, 2024. Future development includes a planned QGIS plugin as part of the NFDI4Objects (National Research Data Infrastructure) initiative, signalling continued institutional commitment to the tool's evolution.","Built primarily in C programming language with a minimalist approach prioritizing portability and flexibility. The software requires no installation, running as a portable application across Windows, Linux, and macOS platforms, though Mac users need additional dependencies. This design choice reflects its field-oriented purpose, allowing archaeologists to run the software directly from USB drives on field computers. The architecture centres on a flexible parser system using ASCII-encoded text files to describe input and output structures. This allows users to define custom parsing schemes for different survey equipment and data formats—a critical feature given the variety of total stations and GPS devices used in archaeology. The software provides both graphical user interface (GUI) and command-line interface (CLI) versions, with the CLI enabling batch processing and workflow automation. Output formats include industry-standard ESRI Shapefile (supporting both 2D and 3D geometries), GeoJSON, and KML, ensuring compatibility with major GIS platforms. The software performs automated 2D topological corrections and validation, though 3D topology functions remain limited. Multi-language support with automatic OS language detection demonstrates consideration for international usage, though documentation is primarily in German and English.","2025-05-31","yes","Survey2GIS meets all essential criteria for research software: it has a research-specific purpose supporting archaeological fieldwork, it meaningfully transforms research data (survey coordinates into GIS formats), and aligns with recognized archaeological methodologies. It also satisfies multiple supporting criteria: it incorporates domain knowledge (archaeological survey standards), supports the research lifecycle (data processing stage), transforms data between formats, performs analytical operations (topological validation), and provides documentation focused on research applications.","https://github.com/survey2gis/survey-tools","","","https://www.survey-tools.org/","GPL-3.0","Data management|Site mapping|Spatial analysis|Geophysical survey|Data collection","Archaeological survey processing|Total station data conversion|GIS format transformation|Field data digitization|Topological correction","2012","2024-07-31","1.5.2","Active","Cultural Heritage Authority of Baden-Württemberg|German Archaeological Institute (DAI)|NFDI4Objects","Dr. Benjamin Ducke","Small (2-5)","Archaeology","Project-specific","Comprehensive","Adoption metrics show a niche but committed user base primarily in European archaeological institutions. GitHub repository shows modest statistics (3 stars, 2 forks, 1 follower) but has documented institutional adoption by German heritage agencies (Baden-Württemberg, Bavaria) and Oxford Archaeology (UK). The software has been presented at Computer Applications and Quantitative Methods in Archaeology (CAA) conferences since 2018. Academic citations cluster in European archaeological computing literature, with the core Bibby & Ducke (2017) publication serving as the primary reference point. Community support centres around an official mailing list at survey2gis@groups.io.","Processing","research-specific","Stand-alone software","C","Windows|Linux|macOS","","Inputs include data from various total station and GPS devices through configurable parser files. Outputs in standard GIS formats including ESRI Shapefile (2D/3D), GeoJSON, and KML, ensuring compatibility with major GIS platforms. Supports automated 2D topological corrections and on-the-fly coordinate system transformations since version 1.5.0.","Survey2GIS addresses a specific workflow gap with a lightweight, portable solution requiring no complex installation. Its flexible parser system adapts to various survey equipment and project requirements. Institutional backing from German heritage agencies provides stability and legitimacy. Its open-source nature (GPL 3.0) ensures long-term accessibility and prevents vendor lock-in—critical for archaeological data preservation. Automated topological validation and cleaning addresses common data quality issues in field survey data. The program provides both GUI and command-line interfaces, enabling batch processing for larger datasets. Integration with established GIS platforms (gvSIG-CE, planned QGIS plugin) leverages existing ecosystems rather than attempting to replace them.","The small development team (essentially one lead developer with institutional support) creates sustainability risks. Limited community size restricts peer support and third-party development. Documentation, while academically rigorous, lacks user-friendly tutorial resources. Technical limitations include primarily 2D-focused topology operations and platform-specific issues like additional dependencies for macOS. The specialized nature limits broader adoption potential. The software lacks mobile integration, cloud synchronization, and real-time collaboration features found in newer alternatives. The parser system documentation, while thorough, requires significant technical understanding, reflecting the tool's positioning for users with existing GIS knowledge.","Survey2GIS demonstrates ongoing viability through continued institutional support and recent development activity. The last GitHub commit was July 31, 2024, indicating active maintenance. Integration with the NFDI4Objects national research infrastructure project provides funding stability. However, the project's dependence on a single lead developer represents a sustainability risk despite institutional backing. Future plans include a QGIS plugin, which could expand the user base while maintaining specialized functionality within a larger ecosystem. The software's production use across Baden-Württemberg validates its reliability for professional archaeological work, suggesting continued institutional support.","QGIS with QField offers broader functionality and massive community support but requires more complex setup for survey-specific workflows. Commercial alternatives like ESRI's ArcGIS Suite with Survey123 provide comprehensive solutions at substantial cost (annual licenses $100-$7,000+). gvSIG-CE represents the closest alternative, sharing development philosophy with Survey2GIS. Specialized archaeological tools like Arches and ARK serve different workflow niches. Mobile-first solutions including KoBo Toolbox and ODK provide easier field data collection but lack Survey2GIS's specific total station integration and topological processing capabilities. The planned Survey2GIS plugin for QGIS suggests recognition of QGIS's dominant position in the GIS landscape."
```

---
