# v8-iDig-metadata

## Metadata
- **UUID:** `439ed426-9534-4379-8788-778312082634`
- **URL:** https://claude.ai/chat/439ed426-9534-4379-8788-778312082634
- **Date:** 2025-05-08 13:15:09

---

## Conversation

### Human (12:33:30)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (12:33:40)



I understand your requirements completely. I'll follow the detailed metadata collection guidelines to research archaeological software tools based on the names/acronyms you provide. I'll apply the Writing Style Guide with its academic tone, active voice with strategic variation, and other specifications, including Australian spelling.

For each tool, I'll produce a comprehensive report following the format "[Tool Name]: [Primary Function] for [Application Domain]" and provide a properly formatted CSV with all the required fields, ensuring thorough and accurate information collection.

I'm ready to begin researching the first tool whenever you provide its name or acronym.

---

### Human (13:00:47)

iDig

---

### Assistant (13:00:58)



I'll research iDig software for archaeological research now. This appears to be a tool used in archaeological fieldwork, but to ensure I'm researching the correct software, I'll launch a comprehensive research process to gather all relevant information according to your metadata collection guidelines.
```
This block is not supported on your current device yet.
```

Your archaeological field recording software analysis is ready. It examines iDig's development from 2012-2024, core functionality for real-time excavation documentation, technical architecture, institutional adoption across 12 Mediterranean sites, comparative advantages against alternatives like FAIMS and ARK, and recent evolution into WebDig. The report evaluates how this iPad-based system transforms archaeological recording through visualization capabilities and total station integration.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (13:11:59)

please also produce the requested CSV

---

### Assistant (13:12:50)



Based on my research about iDig, I've compiled the comprehensive data you requested. Here's the CSV with metadata about this archaeological research software tool:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"iDig","iDig is a specialised iPad-based software application designed for archaeological field recording. Developed by Bruce Hartzler at the American School of Classical Studies at Athens (ASCSA), it enables real-time digital documentation of excavation contexts, features, and finds. The current version allows archaeologists to wirelessly connect to total stations for precise spatial measurements, synchronise data across multiple iPads, instantly visualise stratigraphic relationships, and integrate with previous excavation records. A distinctive feature nicknamed 'Camping it' (after Agora excavation director John Camp) allows users to trace areas on screen to see previously recorded contexts at that location, effectively creating a virtual time machine through the stratigraphic layers. Recently evolved into WebDig (2023/2024), extending functionality beyond iOS devices.","iDig's development history reflects a methodical evolution from early digital experimentation to a sophisticated recording system. In 1998, Bruce Hartzler joined the American School of Classical Studies at Athens as staff for the Athenian Agora excavations. During the 2000s, Hartzler began digitising 80+ years of Agora excavation records and experimenting with mobile recording using Palm Pilots synchronised with total stations. Following the 2010 release of the iPad, the first version of iDig was created in 2011 and initially implemented at the Athenian Agora excavations in 2012. By 2016, the software had reached version 5.0.2, as documented in a published review by Martin Uildriks. Training sessions were conducted through 2021, indicating continued development. The most significant recent development occurred in late 2023/early 2024 with the evolution into WebDig, a web-based application with expanded capabilities that addresses the iOS platform limitation while maintaining core functionality and visualisation strengths.","iDig is built as a native iOS application, likely developed initially in Objective-C with possibly later components in Swift as Apple shifted programming paradigms. The software employs a multi-tier architecture with: 1) Mobile Application Layer (iPad client) handling user interface, data entry, and visualisation; 2) Sync/Collaboration Layer managing 'Trenchmates' functionality for iPad synchronisation and total station connectivity; and 3) Optional External Server Component ('iDig Server' application) for enterprise-level data management using Git repositories. The application's data model is specifically tailored to archaeological excavation workflows, supporting entity types like contexts, features, objects, and lots – each with specialised fields and relationship types reflecting archaeological thinking (such as 'is above', 'is below', 'is after'). Technical requirements include iOS 9.3 or later, iPad devices with minimum 10.6 MB free space, Wi-Fi for synchronisation between devices, and optional Leica Total Station integration. Data storage uses a structured on-device approach with periodic snapshots for backup. The primary export format is UTF-8 tab-delimited text files, which can be processed for use in spreadsheets, databases, and GIS software. The current WebDig implementation leverages web technologies to provide similar functionality through a browser interface, allowing for broader platform compatibility while maintaining the core visualisation capabilities that distinguished the original iOS application.","2024-05-08","yes","iDig meets all essential criteria for research software tools as it has a clear research-specific purpose (archaeological recording), directly engages with research data (spatial measurements and context documentation), and aligns with established archaeological methodologies. It also satisfies numerous supporting criteria: it integrates domain knowledge through its archaeological terminology and classification system; supports multiple research lifecycle stages (data acquisition, processing, analysis); transforms data between field recordings and analytical formats; provides analytical capabilities through relationships between contexts; offers specialised visualisation of stratigraphic relationships; includes documentation specifically addressing archaeological research applications; supports field data collection with total station integration; and enables data dissemination through its export functions. The software was purposefully designed by an archaeologist for archaeological research, further confirming its classification as research software.","","","","https://idig.tips/","Proprietary","Data collection|Spatial analysis|Site mapping|3D modelling|Data management","Archaeological recording|Stratigraphic visualisation|Field documentation|Spatial data|Real-time collaboration","2011","2023","WebDig (2023/2024)","Active","American School of Classical Studies at Athens (ASCSA)|Packard Humanities Institute","Bruce Hartzler","Small (2-5)","Archaeology","Project-specific","Comprehensive","iDig has been adopted by at least 12 major archaeological projects in the Mediterranean region, including the Athenian Agora Excavations (primary development site), American/Greek excavations at the Ismenion sanctuary (Thebes), Belgian/Dutch fieldwork at Thorikos, British excavations at Keros, Casa della Regina Carolina Project at Pompeii, Eastern Boeotia Archaeological Project at Eleon, Greek underwater survey in the Argo-Saronic Gulf, Lechaion Harbor and Settlement Land Project, Molyvoti Thrace Archaeological Project (MTAP), Teos Excavation Project, Swiss excavations at Eretria and Amarynthos, and Northwest Bolsena Archaeological Project. The most significant implementation beyond the Agora has been the MTAP project, which adopted iDig in 2019 and later evolved it into WebDig. Beyond project adoption, usage indicators include training sessions conducted through 2021 and documented use in publications reviewing archaeological field recording methods.","Data Acquisition|Processing|Analysis|Interpretation","research-specific","Stand-alone software","Objective-C|Swift","iOS (iPad)|Web (WebDig)","","iDig primarily uses UTF-8 tab-delimited text files as its export format, enabling integration with spreadsheets, databases, and GIS software. The current version supports connection with Leica Total Stations for precise spatial measurements. Import capabilities include georeferenced scanned drawings and previous seasons' data. The recently developed WebDig extends interoperability beyond the iOS ecosystem. The software uses a structured data model with well-defined relationships between archaeological contexts, features, objects, and lots, facilitating data integration with other archaeological recording systems.","iDig offers several notable strengths that have driven its adoption across Mediterranean archaeological projects: 1) Visual interface - Unlike text-heavy alternatives, iDig provides strong visualisation of spatial relationships through multiple perspectives including top plan views, cross-sections, and matrix layouts; 2) Real-time integration - Wireless connectivity to total stations and synchronisation across multiple iPads enables collaborative field recording; 3) Historical context - Immediate access to previous excavation data while in the field provides crucial contextual information for interpretation; 4) Animation features - The 'Camping it' functionality helps visualise changes in archaeological contexts through time; 5) Data protection - Multiple safeguards against data loss including trash recovery and periodic snapshots; and 6) Intuitive design - Developed by an archaeologist for archaeologists, with streamlined field recording workflows aligned with excavation practices. The current WebDig version maintains these core strengths while expanding platform accessibility beyond iOS.","Despite its strengths, iDig presents several limitations: 1) Platform limitation - The original version is exclusive to Apple's iOS ecosystem, requiring iPad devices, though the recent WebDig development addresses this constraint; 2) Hardware dependencies - The software is optimised for expensive Leica Total Stations, potentially limiting accessibility for projects with limited budgets; 3) Limited customisation - The software is closely tied to Athenian Agora recording methodology, which may not align with all archaeological recording systems; 4) Documentation gaps - Reviews note insufficient explanation of some status settings and fields; 5) Export limitations - Primary export to tab-delimited text requires post-processing for integration with some analysis tools; and 6) Specialised focus - Primarily designed for excavation, with limited support for survey or other archaeological methods. While WebDig addresses the platform limitation, other weaknesses likely persist in the newer implementation.","iDig shows strong indicators of long-term survivability. The evolution into WebDig in late 2023/early 2024 demonstrates ongoing development commitment and adaptation to changing technology landscapes. Continued institutional support from established organisations like the American School of Classical Studies at Athens and the Packard Humanities Institute provides stable backing. The software's adoption by at least 12 major archaeological projects across the Mediterranean indicates a user base sufficient to justify continued development. Training sessions as recently as 2021 show active community engagement. The transition to a web-based platform addresses previous platform limitations and suggests forward-thinking adaptation. Integration capabilities with standard archaeological tools and formats ensure continued relevance. While the proprietary nature of the software could limit community contributions to development, the strong institutional backing and proven track record of responsive development mitigate this concern. These factors collectively suggest high survivability potential for the foreseeable future.","The primary alternatives to iDig in archaeological field recording include: FAIMS (Field Acquired Information Management Systems) - An Android-based open-source platform with extensive customisation capabilities but less emphasis on visual representation. While more adaptable to different project types, it requires significant technical expertise to configure and deploy. ARK (Archaeological Recording Kit) - A web-based system usable on any device with a browser. It offers greater customisation possibilities and is more text-oriented but lacks the immediate visual feedback that distinguishes iDig. OpenDig - Uses a three-tiered approach (field recording, expedition editing, web application) and works with limited internet connectivity. More adaptable to different project types but with a different development approach. Traditional paper-based recording with post-excavation digitisation - While lacking real-time benefits, still used by many projects. Compared to these alternatives, iDig's distinctive advantages remain its intuitive visual interface, real-time synchronisation capabilities, and total station integration, while WebDig now addresses the platform limitation that previously restricted adoption."
```

Would you like me to analyze any particular aspect of this metadata in more detail or research any other archaeological software tools?

---
