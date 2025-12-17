# v8-StratiGraf-metadata

## Metadata
- **UUID:** `ebe3af96-5184-4e8f-bc98-7f13e2986f9a`
- **URL:** https://claude.ai/chat/ebe3af96-5184-4e8f-bc98-7f13e2986f9a
- **Date:** 2025-05-31 09:02:20

---

## Conversation

### Human (08:11:47)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (08:11:51)



I understand your requirements completely. I'll follow the detailed prompt to collect metadata about research software tools for archaeology, history, and other historical studies disciplines. I'll adhere to the Writing Style Guide provided, applying Australian spelling and punctuation throughout.

For report titles, I'll use the specified format: "[Tool Name]: [Primary Function] for [Application Domain]"

I won't ask follow-up questions and will focus on executing the prompt thoroughly. If there's any ambiguity about which tool to investigate, I'll consult the 'Tool disambiguation' section and prioritise the software most relevant to archaeological/historical research.

I'm ready to begin the research process as soon as you provide the name or acronym of the first tool.

---

### Human (08:11:55)

Stratigraph

---

### Assistant (08:12:02)



I'll begin researching Stratigraph for the metadata collection. This appears to be a tool relevant to archaeological research, likely relating to stratigraphic analysis or visualization. I'll launch a comprehensive research process to gather all the required metadata according to your specifications.
```
This block is not supported on your current device yet.
```

Your StratiGraf software analysis is ready. It covers this archaeological documentation system's development history, technical specifications, and critical limitations. The report details why this Windows-based program from Proleg DPC (Spain) failed to gain traction despite ambitious goals, identifies its proprietary database format as a fatal flaw, and notes its apparent discontinuation around 2011. Modern archaeological software alternatives are also discussed.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (08:59:54)

please also produce the requested csv

---

### Assistant (09:00:49)

I'll now produce the CSV format with the metadata about StratiGraf according to the specifications in the prompt. I'll make sure to follow all the requirements:

1. Create a properly escaped CSV with header row and a single data row
2. Include all fields specified in the prompt, even if empty
3. Format multiple values with pipe (|) separators
4. Use single quotes for quoted text within fields
5. Ensure the number of columns in the data row matches the number in the header row

I'll organize the information from my research into the required CSV format:

Tool: StratiGraf
Description: A comprehensive commercial archaeological documentation system developed by Proleg DPC (Spain) that integrates stratigraphic recording, Harris Matrix generation, and database management. The software organizes archaeological data in a hierarchical structure from Site to Materials, allowing users to maintain relationships between different levels of recording.
History: Developed by Proleg DPC in Spain, with version 1.1 released around 2000. Development continued through versions 3.5 and 3.6, but appears to have ceased around 2011 with no evidence of ongoing maintenance.
Technical-discussion: StratiGraf was a Windows-only desktop application using proprietary database technology. The earliest documented version required Windows NT/95/98, with minimum hardware specifications of a Pentium II 266 MHz processor and 32 MB RAM. The software employed a proprietary database format that became one of its most significant limitations, preventing data import or export to other systems. This design decision effectively isolated user data within the StratiGraf ecosystem, making integration with other archaeological tools impossible. The software was distributed as an executable installer and offered in three languages: English, Spanish, and Catalan.
Access-date: 2025-05-31
Tool-status: yes
Tool-status-reasoning: StratiGraf meets all essential criteria as research software: it has a research-specific purpose (archaeological documentation), engages directly with research data (stratigraphic units and relationships), and aligns with established methodologies (Harris Matrix). It also satisfies multiple supporting criteria: it incorporates domain-specific terminology, supports multiple research lifecycle stages, transforms data between representations, provides analytical capabilities for stratigraphic relationships, visualizes data through Harris Matrix generation, includes documentation focused on research applications, and supports data collection in field settings.
DVCS-repo: 
CRAN: 
PyPi: 
Other-URL: 
License: Commercial/Proprietary
Tags: Harrix matrix|Site mapping|Data management|Data collection
AI-tags: Archaeological documentation|Stratigraphic analysis|Harris Matrix generation|Excavation recording|Legacy software
First-release-date: 2000
Last-update-date: ~2011
Current-version: 3.6
Development-status: Abandoned
Institutional-backing: Proleg DPC (Pròleg d.p.c. S.L.)
Authors: Albert Franquesa (Technical Contact)
Development-team-size: Small (2-5)
Original-discipline: Archaeology
Original-purpose: Project-specific
Documentation-quality: Basic
Usage-indicators: Limited information is available about actual usage. The software used a commercial licensing model with tiered pricing: €560 for the first license, €94 for additional licenses, and €14 for educational institutions. A critical review in Internet Archaeology (2000) by M. Rains noted significant limitations that likely hampered widespread adoption. No evidence of continued usage or community support exists after approximately 2011.
Lifecycle-stage: Data Acquisition|Processing|Analysis
Type: research-specific
Category: Stand-alone software
Language: Unknown (likely C++ or Visual Basic)
Platform: Windows
Open-Archaeo-Platform: 
Interoperability: Very limited. The software used a proprietary database format with no import/export capabilities, creating a closed system that couldn't interface with other archaeological tools, GIS software, or analytical packages. This was identified as a critical weakness in contemporary reviews.
Strengths: StratiGraf provided an ambitious integrated environment for archaeological recording rather than focusing on a single task. The hierarchical data structure (Site → Excavation → Section → Grid Square → Stratigraphic Unit → Materials) reflected genuine archaeological workflows. The software offered multilingual support (English, Spanish, Catalan) and tiered pricing for educational institutions. Its structured environment for data entry, with a three-category system (Identification, Situation, Documentation), provided a framework for comprehensive recording that could effectively manage the full recording process for small excavations.
Weaknesses: The proprietary database format with no import/export capabilities represented a fundamental design flaw that violated basic principles of scientific data management. Users could neither migrate existing data into StratiGraf nor extract their data for use in other analytical tools. Scalability problems emerged with larger datasets, with reports of display issues and crashes when handling excavations with more than 1,000 contexts. The limited document management capabilities, restricted to linking simple image files, failed to accommodate diverse digital documentation increasingly common in archaeological practice. The Windows-only platform limitation and lack of ongoing development meant the software couldn't adapt to changing technological landscapes.
Survivability: Low survivability. The software appears to have been discontinued around 2011, with no evidence of ongoing development or support. Its proprietary data format creates significant risks for long-term data accessibility, as files created in StratiGraf cannot be easily migrated to modern systems. The Windows-only implementation further limits its viability on contemporary operating systems. The commercial licensing model without an open-source transition plan means there is no path for community maintenance. Archaeological projects using StratiGraf face substantial data loss risks without significant effort to extract information from its proprietary format.
Alternatives: Several superior alternatives exist: ArchEd (free, focused solely on Harris Matrix generation), Harris Matrix Composer (commercial, with modern interface and better visualization), ARK (Archaeological Recording Kit, open-source web-based system), FAIMS/Fieldmark (open-source mobile-first field recording), and Intrasis (comprehensive commercial system). Modern systems typically offer better interoperability, adherence to data standards, multi-platform support, and integration with spatial recording tools that StratiGraf lacked.

Now I'll format this as the requested CSV with proper escaping:Based on the comprehensive research I've conducted, I'll now provide the metadata for StratiGraf in the requested CSV format.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"StratiGraf","StratiGraf is a commercial archaeological documentation and interpretation software that combines stratigraphic recording, Harris Matrix generation, and comprehensive database management in a single integrated system. Developed by Proleg DPC of Spain, the software organises archaeological data in a hierarchical structure progressing from Site → Excavation → Section → Grid Square → Stratigraphic Unit (SU) → Materials, allowing researchers to maintain relationships between different levels of archaeological recording. The database capabilities record information under three main headings: Identification, Situation, and Documentation, theoretically providing comprehensive coverage of excavation data requirements. It was available in English, Spanish, and Catalan.","Developed by Proleg DPC (Pròleg d.p.c. S.L.) based in Balaguer, Spain, in the late 1990s. The company registered the domain proleg.com in August 1998 and released version 1.1 by 2000. Development progressed through several versions, with 3.5 and 3.6 representing the most recent documented iterations. The software used a tiered commercial licensing model: €560 for the first license, €94 for additional licenses, and €14 for educational institutions. A demonstration version limited to 30 stratigraphic units allowed potential users to evaluate the software before purchase. Development appears to have ceased around 2011, based on the last update to domain registration information and absence from contemporary archaeological software surveys.","StratiGraf was developed as a Windows-only desktop application using proprietary database technology. The earliest documented version (1.1, circa 2000) required Windows NT, 95, or 98, with minimum hardware specifications of a Pentium II 266 MHz processor, 32 MB RAM, and SVGA resolution. The software employed a proprietary database format that became one of its most significant limitations. Unlike contemporary archaeological software that supported standard formats like CSV, XML, or established archaeological data standards, StratiGraf's closed format prevented data import or export to other systems. This design decision effectively isolated user data within the StratiGraf ecosystem, making it impossible to integrate with GIS software, statistical analysis packages, or other archaeological tools commonly used in research workflows. The software was distributed as an executable installer (stratigraf.exe) and offered in three languages: English, Spanish, and Catalan. Platform support remained limited to Windows throughout the software's lifecycle, with no evidence of ports to macOS, Linux, or web-based platforms. This Windows-centric approach, combined with the proprietary data format, positioned StratiGraf poorly for the emerging trends in archaeological computing toward open standards and cross-platform compatibility.","2025-05-31","yes","StratiGraf meets all essential criteria as research software: it has a research-specific purpose (archaeological documentation), engages directly with research data (stratigraphic units and relationships), and aligns with established methodologies (Harris Matrix). It also satisfies multiple supporting criteria: it incorporates domain-specific terminology, supports multiple research lifecycle stages, transforms data between representations, provides analytical capabilities for stratigraphic relationships, visualises data through Harris Matrix generation, includes documentation focused on research applications, and supports data collection in field settings.","","","","","Commercial/Proprietary","Harrix matrix|Site mapping|Data management|Data collection","Archaeological documentation|Stratigraphic analysis|Harris Matrix generation|Excavation recording|Legacy software","2000","~2011","3.6","Abandoned","Proleg DPC (Pròleg d.p.c. S.L.)","Albert Franquesa (Technical Contact)","Small (2-5)","Archaeology","Project-specific","Basic","Limited information is available about actual usage. The software used a commercial licensing model with tiered pricing: €560 for the first license, €94 for additional licenses, and €14 for educational institutions. A critical review in Internet Archaeology (2000) by M. Rains noted significant limitations that likely hampered widespread adoption. No evidence of continued usage or community support exists after approximately 2011.","Data Acquisition|Processing|Analysis","research-specific","Stand-alone software","Unknown (likely C++ or Visual Basic)","Windows","","Very limited. The software used a proprietary database format with no import/export capabilities, creating a closed system that couldn't interface with other archaeological tools, GIS software, or analytical packages. This was identified as a critical weakness in contemporary reviews.","StratiGraf provided an ambitious integrated environment for archaeological recording rather than focusing on a single task. The hierarchical data structure (Site → Excavation → Section → Grid Square → Stratigraphic Unit → Materials) reflected genuine archaeological workflows. The software offered multilingual support (English, Spanish, Catalan) and tiered pricing for educational institutions. Its structured environment for data entry, with a three-category system (Identification, Situation, Documentation), provided a framework for comprehensive recording that could effectively manage the full recording process for small excavations.","The proprietary database format with no import/export capabilities represented a fundamental design flaw that violated basic principles of scientific data management. Users could neither migrate existing data into StratiGraf nor extract their data for use in other analytical tools. Scalability problems emerged with larger datasets, with reports of display issues and crashes when handling excavations with more than 1,000 contexts. The limited document management capabilities, restricted to linking simple image files, failed to accommodate diverse digital documentation increasingly common in archaeological practice. The Windows-only platform limitation and lack of ongoing development meant the software couldn't adapt to changing technological landscapes.","Low survivability. The software appears to have been discontinued around 2011, with no evidence of ongoing development or support. Its proprietary data format creates significant risks for long-term data accessibility, as files created in StratiGraf cannot be easily migrated to modern systems. The Windows-only implementation further limits its viability on contemporary operating systems. The commercial licensing model without an open-source transition plan means there is no path for community maintenance. Archaeological projects using StratiGraf face substantial data loss risks without significant effort to extract information from its proprietary format.","Several superior alternatives exist: ArchEd (free, focused solely on Harris Matrix generation), Harris Matrix Composer (commercial, with modern interface and better visualisation), ARK (Archaeological Recording Kit, open-source web-based system), FAIMS/Fieldmark (open-source mobile-first field recording), and Intrasis (comprehensive commercial system). Modern systems typically offer better interoperability, adherence to data standards, multi-platform support, and integration with spatial recording tools that StratiGraf lacked."
```

---
