# v8-FAIMS-metadata and prompt improvement

## Metadata
- **UUID:** `e58947d8-f5b1-4e05-bcac-ce2b1bfc5117`
- **URL:** https://claude.ai/chat/e58947d8-f5b1-4e05-bcac-ce2b1bfc5117
- **Date:** 2025-05-04 19:43:37

---

## Conversation

### Human (19:12:27)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
Note that a 'Writing Style Guide' is attached to this Project, please apply it to your report and the CSV.

---

### Assistant (19:12:34)



I understand your request perfectly. You'd like me to collect and organize detailed metadata about research software tools used in archaeology, history, and related historical disciplines. I'll follow the comprehensive guidelines provided in the paste.txt document and apply the writing style from the Writing Style Guide to ensure academic clarity with direct assertions, balanced authority, and appropriate technical precision.

The guidelines provide an excellent framework for evaluating and documenting software tools, including their core purpose, technical details, development history, strengths and weaknesses, and long-term viability. I'll present my findings in a properly formatted CSV within a markdown code block as specified.

I'm ready to begin researching the first tool you'd like me to investigate. Please provide the name or acronym of the software tool, and I'll start the research process.

---

### Human (19:12:41)

FAIMS

---

### Assistant (19:12:48)



Thank you for providing the first tool for me to research. I'll investigate FAIMS (Field Acquired Information Management Systems) thoroughly following the detailed methodology outlined in your guidelines.

I'll need to gather comprehensive information about this archaeological software tool, including its purpose, technical implementation, development history, usage metrics, and much more. I'll be starting an in-depth research process to ensure I provide accurate, evidence-based information formatted according to your writing style guide.

Just to confirm, is there any specific aspect of FAIMS you'd like me to emphasize in my research, or should I proceed with a comprehensive investigation covering all the metadata fields specified?

I'll start my research right away!
```
This block is not supported on your current device yet.
```

Your FAIMS archaeological fieldwork report is ready. It explores the evolution of this open-source mobile platform for offline data collection, highlighting its technical architecture, worldwide adoption across 40+ projects, key strengths for archaeological workflows, and limitations affecting broader adoption. The report also examines alternatives and evaluates how FAIMS supports FAIR data principles in archaeological research.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (19:22:36)

Please generate the requested CSV

---

### Assistant (19:23:30)



I'll generate the CSV containing the metadata for FAIMS according to your guidelines. Based on my research, here's the complete metadata:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"FAIMS","FAIMS (Field Acquired Information Management Systems) is an open-source platform for collecting digital field data in offline environments. Originally designed for archaeological fieldwork, it enables researchers to create customised data collection workflows with comprehensive recording capabilities including structured data, free text, geospatial information, and multimedia. The system offers robust offline functionality with multi-user synchronisation and version tracking, essential for remote fieldwork locations without internet connectivity. FAIMS supports rigorous data collection through controlled vocabularies, data validation, and complete provenance tracking. The platform has evolved from an Android-only application to a cross-platform system (rebranded as Fieldmark in 2023) with implementations across archaeological projects worldwide.","FAIMS began in 2012 when Australian archaeologists, led by Shawn Ross and Adela Sobotkova, secured National eResearch Collaboration Tools and Resources (NeCTAR) funding to create specialised field data collection software. The initial version was released in 2014 as an Android-only application focused on offline functionality. After relocating to Macquarie University in 2015, the project received substantial funding through an Australian Research Council Linkage Infrastructure Equipment and Facilities (LIEF) grant valued at AUD $945,000 and a NSW Research Attraction and Acceleration Program (RAAP) grant. FAIMS 2.x followed, enhancing the original functionality. A significant transformation occurred in 2020-2022 with Australian Research Data Commons (ARDC) funding, resulting in FAIMS3, released in December 2022 and rebranded as Fieldmark™ in June 2023. This latest iteration features a cross-platform architecture supporting Android, iOS, and desktop systems. A commercial entity, Electronic Field Notebooks Pty Ltd, was established in 2023 to provide hosting services and ensure sustainability.","FAIMS's technical architecture directly addresses archaeological fieldwork challenges, particularly the need to operate in remote locations without internet connectivity. The earliest versions (1.0 and 2.x) used a Java-based Android client with a Ruby server, utilising SQLite in a domain-key normal form (DKNF) for data storage. This ensured complete offline functionality with eventual synchronisation when connectivity became available. A defining feature is the append-only datastore that preserves the complete history of all records and changes, crucial for maintaining archaeological data provenance. Every modification is tracked by timestamp and user, fundamental to archaeological record integrity. FAIMS3/Fieldmark represents a significant technical evolution, shifting to a modern web technology stack (TypeScript/JavaScript, React, Capacitor) with CouchDB for improved synchronisation capabilities while maintaining the core offline functionality. The system employs a modular architecture where data collection forms ('modules') can be customised for specific project needs. These modules define the UI, data validation rules, and relationships between different record types. Key technical capabilities include comprehensive data collection support (structured data, free text, geospatial information, multimedia), lightweight GIS functionality for field mapping, multi-user synchronisation with conflict resolution, external sensor integration (GPS, digital calipers), and customisable export in various formats (CSV, shapefile, etc.).","2025-05-04","yes","FAIMS clearly qualifies as research software based on all essential criteria and multiple supporting criteria. It has a specific research purpose (archaeological fieldwork data collection), directly engages with research data (capturing, validating, and managing field observations), and aligns with archaeological methodologies. It incorporates domain knowledge through customisable modules with archaeological terminology and classifications, supports multiple research lifecycle stages (planning, data acquisition, processing), enables data transformation through validation and export capabilities, provides analytical capabilities through spatial data handling, and offers visualisation functions for mapping. The academic literature consistently recognises FAIMS as a significant contribution to digital archaeological methods, with multiple peer-reviewed publications analysing its implementation and impact.","https://github.com/FAIMS","","","https://faims.edu.au/","Apache License 2.0","Data collection|Spatial analysis|Site mapping|Data management","archaeological-data-collection|offline-fieldwork-tool|digital-archaeology-platform|structured-recording-system|field-research-software","2014","2023-06","Fieldmark (formerly FAIMS3)","Active","Macquarie University|Electronic Field Notebooks Pty Ltd","Shawn Ross|Adela Sobotkova|Penny Crook|Brian Ballsun-Stanton","Medium (6-20)","Archaeology","General-purpose","Comprehensive","FAIMS has been implemented in over 40 archaeological projects worldwide with nearly 70 distinct research workflows. Notable implementations include the Perachora Peninsula Archaeological Project (Greece), Willandra Lakes World Heritage Area survey (Australia), Malawi Earlier Middle Stone Age Project, Boncuklu Project (Turkey), and Proyecto Arqueológico Zaña Colonial (Peru). While precise download metrics are not publicly available, FAIMS has seen adoption across multiple continents and various archaeological subdisciplines. Its application extends beyond archaeology to other field sciences including ecology, geochemistry, and oral history. The project has generated multiple peer-reviewed publications and presentations at major archaeological computing conferences.","Planning|Data Acquisition|Processing|Analysis|Preservation and Reuse","research-specific","Stand-alone software","Java|Ruby|JavaScript|TypeScript|React","Android|iOS|Web","","FAIMS supports comprehensive data import/export capabilities with formats including CSV, shapefile, KML, GeoJSON, and SQLite databases. The system can integrate with external sensors (GPS, digital calipers) and includes APIs for connecting with other systems. Export functions allow data to be transferred to GIS software (QGIS, ArcGIS), statistical packages, and other analysis tools. The modular architecture enables customisation for different data models and recording systems, supporting interoperability with existing archaeological recording methodologies and data standards.","FAIMS offers several significant advantages for archaeological fieldwork: (1) Unmatched offline functionality allows complete operation in remote locations without internet connectivity, addressing a fundamental requirement of archaeological fieldwork; (2) Data integrity through versioning ensures no information is ever lost or overwritten, with all changes tracked by user and timestamp—critical for maintaining the integrity of the archaeological record; (3) Extensive customisability allows adaptation to specific methodological approaches, reflecting the diversity of archaeological recording systems worldwide; (4) Built-in data quality controls including controlled vocabularies, validation rules, and certainty indicators help ensure consistent recording across large field teams; (5) Immediate digital data availability eliminates weeks or months of post-excavation digitisation, allowing faster analysis and publication. The system also implements FAIR data principles (Findable, Accessible, Interoperable, Reusable) from the moment of collection.","Despite its strengths, FAIMS faces several limitations that have constrained broader adoption: (1) Technical complexity requires significant setup time and expertise, especially for earlier versions. Creating customised modules often demanded programming knowledge or direct support from the FAIMS team; (2) The DKNF append-only datastore, while excellent for data integrity, creates performance issues with large datasets, particularly during search and read operations; (3) Earlier versions were limited to Android devices, restricting usage for teams with iOS devices; (4) Sociotechnical barriers exist around adoption, with many archaeologists finding it difficult to allocate time at the project start to save time later; (5) Resource requirements for hardware, technical expertise, and training can be prohibitive for smaller projects without substantial technical support. These limitations have confined most successful FAIMS implementations to well-funded academic projects with dedicated technical assistance.","FAIMS demonstrates strong long-term viability through several factors: (1) Sustained institutional support from Macquarie University and consistent funding success across multiple national grant schemes; (2) The establishment of Electronic Field Notebooks Pty Ltd in 2023 represents a significant step toward financial sustainability through a commercial service model; (3) The transition to modern web technologies with FAIMS3/Fieldmark makes the platform more accessible and maintainable; (4) A dedicated core development team has maintained continuity throughout multiple project phases; (5) Strong integration with archaeological research workflows and documented efficiency improvements create ongoing demand; (6) The open-source nature ensures code availability even if institutional support changes. The major risk factors include continued reliance on grant funding cycles and the technical complexity that may limit adoption without dedicated support. Overall, the project has demonstrated remarkable resilience and adaptability over its decade-long existence.","Several alternatives to FAIMS exist in the archaeological digital recording ecosystem: (1) KoboToolbox offers simpler setup and a more user-friendly interface but provides less specialised archaeological functionality and weaker offline synchronisation capabilities; (2) Arches excels at heritage inventory management with strong geospatial capabilities and built-in cultural heritage ontologies but focuses less on field data collection; (3) QFIELD integrates directly with QGIS for stronger spatial data handling but offers less structured data collection for archaeological contexts; (4) ODK (Open Data Kit) provides a flexible framework for mobile data collection but requires significant customisation for archaeological use; (5) Paper-based methods with digital post-processing remain common, accepting the inefficiencies of later digitisation to avoid technical complexity and hardware dependence. The optimal choice depends on project-specific factors including technical capabilities, recording methodology, team size, funding, and fieldwork location."
```

---

### Human (19:25:47)

Claude, this is excellent, the only refinement I'd still like to see is absolutely consistent distinction between the current version and older versions in descriptive and evaluabive (e.g., description, technical-discussion, interoperability, strenths, weaknesses, survivability). At present this distinction is not always respected.

---

### Assistant (19:26:35)



You're absolutely right. Maintaining a clear distinction between current and older versions is crucial for accuracy. I'll refine the CSV to ensure consistent differentiation between FAIMS3/Fieldmark (current version) and previous iterations throughout all descriptive and evaluative fields. 

Let me update the CSV with this improvement:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"FAIMS","FAIMS (Field Acquired Information Management Systems) is an open-source platform for collecting digital field data in offline environments. The current version, rebranded as Fieldmark in 2023, offers cross-platform support for Android, iOS, and desktop systems. Fieldmark enables researchers to create customised data collection workflows with comprehensive recording capabilities including structured data, free text, geospatial information, and multimedia. The system provides robust offline functionality with multi-user synchronisation and version tracking, essential for remote fieldwork locations without internet connectivity. Fieldmark supports rigorous data collection through controlled vocabularies, data validation, and complete provenance tracking. Since its inception, FAIMS has evolved from an Android-only application to the current cross-platform system with implementations across archaeological projects worldwide.","FAIMS began in 2012 when Australian archaeologists, led by Shawn Ross and Adela Sobotkova, secured National eResearch Collaboration Tools and Resources (NeCTAR) funding to create specialised field data collection software. The initial version was released in 2014 as an Android-only application focused on offline functionality. After relocating to Macquarie University in 2015, the project received substantial funding through an Australian Research Council Linkage Infrastructure Equipment and Facilities (LIEF) grant valued at AUD $945,000 and a NSW Research Attraction and Acceleration Program (RAAP) grant. FAIMS 2.x followed, enhancing the original functionality. A significant transformation occurred in 2020-2022 with Australian Research Data Commons (ARDC) funding, resulting in FAIMS3, released in December 2022 and rebranded as Fieldmark™ in June 2023. This latest iteration features a cross-platform architecture supporting Android, iOS, and desktop systems. A commercial entity, Electronic Field Notebooks Pty Ltd, was established in 2023 to provide hosting services and ensure sustainability.","The current Fieldmark (formerly FAIMS3) platform employs a modern web technology stack based on TypeScript/JavaScript, React, and Capacitor with CouchDB for data management and synchronisation. This architecture enables true cross-platform functionality while maintaining the core offline capabilities essential for archaeological fieldwork. Early FAIMS versions (1.0 and 2.x) used a Java-based Android client with a Ruby server and SQLite in domain-key normal form (DKNF) for data storage. Across all versions, a defining feature is the append-only datastore that preserves the complete history of all records and changes, crucial for maintaining archaeological data provenance. In Fieldmark, every modification is tracked by timestamp and user, fundamental to archaeological record integrity. The system employs a modular architecture where data collection forms ('modules') can be customised for specific project needs. These modules define the UI, data validation rules, and relationships between different record types. Fieldmark's key technical capabilities include comprehensive data collection support (structured data, free text, geospatial information, multimedia), lightweight GIS functionality for field mapping, multi-user synchronisation with conflict resolution, external sensor integration, and customisable export in various formats.","2025-05-04","yes","FAIMS clearly qualifies as research software based on all essential criteria and multiple supporting criteria. It has a specific research purpose (archaeological fieldwork data collection), directly engages with research data (capturing, validating, and managing field observations), and aligns with archaeological methodologies. It incorporates domain knowledge through customisable modules with archaeological terminology and classifications, supports multiple research lifecycle stages (planning, data acquisition, processing), enables data transformation through validation and export capabilities, provides analytical capabilities through spatial data handling, and offers visualisation functions for mapping. The academic literature consistently recognises FAIMS as a significant contribution to digital archaeological methods, with multiple peer-reviewed publications analysing its implementation and impact.","https://github.com/FAIMS","","","https://faims.edu.au/","Apache License 2.0","Data collection|Spatial analysis|Site mapping|Data management","archaeological-data-collection|offline-fieldwork-tool|digital-archaeology-platform|structured-recording-system|field-research-software","2014","2023-06","Fieldmark (formerly FAIMS3)","Active","Macquarie University|Electronic Field Notebooks Pty Ltd","Shawn Ross|Adela Sobotkova|Penny Crook|Brian Ballsun-Stanton","Medium (6-20)","Archaeology","General-purpose","Comprehensive","FAIMS has been implemented in over 40 archaeological projects worldwide with nearly 70 distinct research workflows. Notable implementations include the Perachora Peninsula Archaeological Project (Greece), Willandra Lakes World Heritage Area survey (Australia), Malawi Earlier Middle Stone Age Project, Boncuklu Project (Turkey), and Proyecto Arqueológico Zaña Colonial (Peru). While precise download metrics are not publicly available, FAIMS has seen adoption across multiple continents and various archaeological subdisciplines. Its application extends beyond archaeology to other field sciences including ecology, geochemistry, and oral history. The project has generated multiple peer-reviewed publications and presentations at major archaeological computing conferences.","Planning|Data Acquisition|Processing|Analysis|Preservation and Reuse","research-specific","Stand-alone software","Java|Ruby|JavaScript|TypeScript|React","Android|iOS|Web","","The current Fieldmark platform supports comprehensive data import/export capabilities with formats including CSV, shapefile, KML, GeoJSON, and SQLite databases. Fieldmark can integrate with external sensors and includes APIs for connecting with other systems. Export functions allow data to be transferred to GIS software (QGIS, ArcGIS), statistical packages, and other analysis tools. The modular architecture enables customisation for different data models and recording systems, supporting interoperability with existing archaeological recording methodologies and data standards. Previous FAIMS versions offered similar capabilities but with more limited platform compatibility and synchronisation options.","Fieldmark (the current FAIMS version) offers several significant advantages for archaeological fieldwork: (1) Cross-platform support (Android, iOS, desktop) with unmatched offline functionality allows complete operation in remote locations without internet connectivity; (2) Data integrity through versioning ensures no information is ever lost or overwritten, with all changes tracked by user and timestamp—critical for maintaining archaeological record integrity; (3) Extensive customisability allows adaptation to specific methodological approaches, reflecting the diversity of archaeological recording systems; (4) Built-in data quality controls including controlled vocabularies, validation rules, and certainty indicators help ensure consistent recording across field teams; (5) Immediate digital data availability eliminates post-excavation digitisation, allowing faster analysis and publication. Fieldmark implements FAIR data principles (Findable, Accessible, Interoperable, Reusable) from the moment of collection, a significant improvement over previous versions.","Despite its strengths, the current Fieldmark platform faces several adoption challenges: (1) Technical complexity requires significant setup time and expertise. Creating customised modules often demands programming knowledge or direct support from the development team; (2) Resource requirements for hardware, technical expertise, and training can be prohibitive for smaller projects without substantial technical support; (3) Sociotechnical barriers exist around adoption, with many archaeologists finding it difficult to allocate time at the project start to save time later. Previous FAIMS versions had additional limitations that have been partially addressed in Fieldmark: the DKNF append-only datastore created performance issues with large datasets, and earlier versions were limited to Android devices. While the current version has improved cross-platform support and performance, these historical limitations continue to affect perception and adoption rates.","Fieldmark (current FAIMS version) demonstrates strong long-term viability through several factors: (1) Sustained institutional support from Macquarie University and consistent funding success across multiple national grant schemes; (2) The 2023 establishment of Electronic Field Notebooks Pty Ltd represents a significant step toward financial sustainability through a commercial service model; (3) The transition to modern web technologies makes the platform more accessible and maintainable than previous versions; (4) A dedicated core development team has maintained continuity throughout multiple project phases; (5) Strong integration with archaeological research workflows and documented efficiency improvements create ongoing demand; (6) The open-source nature ensures code availability even if institutional support changes. The major risk factors include continued reliance on grant funding cycles and the technical complexity that may limit adoption without dedicated support. Overall, Fieldmark has built upon the decade-long resilience of the FAIMS project while addressing several previous limitations.","Several alternatives to Fieldmark (current FAIMS version) exist in the archaeological digital recording ecosystem: (1) KoboToolbox offers simpler setup and a more user-friendly interface but provides less specialised archaeological functionality and weaker offline synchronisation capabilities compared to Fieldmark; (2) Arches excels at heritage inventory management with strong geospatial capabilities and built-in cultural heritage ontologies but focuses less on field data collection; (3) QFIELD integrates directly with QGIS for stronger spatial data handling but offers less structured data collection for archaeological contexts; (4) ODK (Open Data Kit) provides a flexible framework for mobile data collection but requires significant customisation for archaeological use and lacks the built-in archaeological features of Fieldmark; (5) Paper-based methods with digital post-processing remain common, accepting the inefficiencies of later digitisation to avoid technical complexity and hardware dependence. The optimal choice depends on project-specific factors including technical capabilities, recording methodology, team size, funding, and fieldwork location."
```

---

### Human (19:29:04)

That's much better - how can I modify the prompt to get this kind of consistency?

---

### Assistant (19:29:19)


The user is asking for advice on how to modify the prompt to ensure consistent distinction between current and older versions in software metadata collection. I should analyze what changes I made to improve the consistency and suggest specific modifications to the prompt instructions.

Key improvements I made in the revised CSV:
1. Explicitly identified the current version by name (Fieldmark) in the Description field
2. Added clear temporal markers (e.g., "current version," "previous versions")
3. Separated descriptions of features by version
4. Made consistent distinctions in all evaluative fields (strengths, weaknesses, interoperability, survivability)
5. Used precise version references instead of generic references to "FAIMS"
6. Added comparative statements where relevant (e.g., "a significant improvement over previous versions")

To formalize these improvements into prompt modifications, I should suggest adding specific instructions about version clarity in the Column Specifications section of their prompt, particularly for fields dealing with software descriptions and evaluation.

Based on my revisions, here are specific modifications you could make to your prompt to ensure consistent version distinction in software metadata:

Add a new section under "Content Guidelines" specifically addressing version clarity:

```
## Version Clarity Guidelines
- **Current vs. Previous Versions**: Always maintain clear distinction between the current version and previous versions in all descriptive and evaluative fields. 
- **Name Specificity**: Use the specific version name/number rather than the generic tool name when describing version-specific features.
- **Temporal Markers**: Consistently use phrases like "current version," "previous versions," or "earlier iterations" as signposts for readers.
- **Description Field**: Begin with the current version's capabilities, then acknowledge evolution from previous versions.
- **Technical-discussion**: Clearly identify which architecture/technologies belong to which version, with current version presented first.
- **Evaluative Fields**: For strengths, weaknesses, interoperability, and survivability, explicitly state which version(s) each point refers to.
- **Comparative Statements**: Where relevant, include how the current version has improved upon or addresses limitations of previous versions.
```

You could also modify the specific column instructions for relevant fields. For example:

```
- **Description**: 5-7 sentence overview prioritizing the current version's purpose and functionality, with clear identification of the current version by name. If describing historical versions, explicitly note them as previous or earlier versions.

- **Technical-discussion**: Begin with the current version's technical implementation, clearly labeled as such, followed by relevant information about previous versions with explicit version identification.

- **Interoperability/Strengths/Weaknesses/Survivability**: Always specify which version(s) each capability or limitation applies to, beginning with the current version before discussing previous versions.
```

These additions would help ensure that anyone following your prompt maintains consistent distinction between software versions throughout their metadata collection.

---

### Human (19:30:40)

In keeping with our attempt to make the prompt as consice as possible while still maintaining output quality, can we shorten the 'version clarity guidelines' without compromising efficacy? If the answer is 'no', that's fine, otherwise suggest a more consice wording.


```
## Version Clarity Guidelines
- **Current vs. Previous Versions**: Always maintain clear distinction between the current version and previous versions in all descriptive and evaluative fields. 
- **Name Specificity**: Use the specific version name/number rather than the generic tool name when describing version-specific features.
- **Temporal Markers**: Consistently use phrases like "current version," "previous versions," or "earlier iterations" as signposts for readers.
- **Description Field**: Begin with the current version's capabilities, then acknowledge evolution from previous versions.
- **Technical-discussion**: Clearly identify which architecture/technologies belong to which version, with current version presented first.
- **Evaluative Fields**: For strengths, weaknesses, interoperability, and survivability, explicitly state which version(s) each point refers to.
- **Comparative Statements**: Where relevant, include how the current version has improved upon or addresses limitations of previous versions.
```

---

### Assistant (19:30:47)


The person is asking me to shorten the "Version Clarity Guidelines" section while maintaining its effectiveness. I need to create a more concise version that still captures all the essential guidance about maintaining clear distinction between current and previous software versions throughout metadata descriptions.

Looking at the original guidelines, I notice:
1. Some points could be combined
2. Some wording is redundant
3. The core message could be distilled more effectively

Let me create a more concise version that maintains the key requirements:

I can definitely make these guidelines more concise while maintaining their effectiveness. Here's a streamlined version:

```
## Version Clarity
- **Explicit Version Identification**: Always specify which version is being described (use version names/numbers) in all fields.
- **Current Version Priority**: Begin descriptions with current version capabilities before discussing previous versions.
- **Consistent Signposting**: Use clear markers ("current version," "previous versions") throughout all evaluative fields.
- **Comparative Context**: Where relevant, note how current versions improve upon or address limitations of earlier iterations.
```

This shorter version consolidates the key principles while removing redundancy. It still maintains the core requirements of clear version identification, prioritizing current version information, using consistent language markers, and providing comparative context where helpful. The concise format should be easier for researchers to reference while still ensuring high-quality, consistent version differentiation.

---
