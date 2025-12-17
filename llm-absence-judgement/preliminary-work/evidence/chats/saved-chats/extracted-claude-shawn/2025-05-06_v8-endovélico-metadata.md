# v8-Endovélico-metadata

## Metadata
- **UUID:** `ce31e610-3b81-420d-ad17-d8722daa8cb1`
- **URL:** https://claude.ai/chat/ce31e610-3b81-420d-ad17-d8722daa8cb1
- **Date:** 2025-05-06 20:02:22

---

## Conversation

### Human (19:16:24)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow these **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" pattern for the name and title of your Report

---

### Assistant (19:16:28)



I understand the task completely. You've provided detailed instructions for collecting and organizing metadata about research software tools used in archaeology, history, and related historical studies disciplines.

Based on the Writing Style Guide attachment and your requirements, I'll:
- Apply Australian spelling and punctuation
- Follow the academic writing style outlined in the guide
- Use the title convention "[Tool Name]: [Primary Function] for [Application Domain]"
- Create comprehensive metadata entries following your detailed CSV format
- Present my findings in a properly formatted CSV code block

I'm ready to begin researching specific software tools. Please provide me with the name or acronym of the first tool you'd like me to investigate.

---

### Human (19:16:39)

Endovélico information system

---

### Assistant (19:17:04)



I'll research the Endovélico information system thoroughly to create a comprehensive metadata entry following your requirements. This appears to be an archaeological database system from Portugal. I'll start my research right away to gather all the necessary information.
```
This block is not supported on your current device yet.
```

Your report on Endovélico, Portugal's archaeological information system, is ready. It covers the system's evolution from paper records to digital database, access pathways, institutional oversight, technical architecture, usage patterns, strengths and limitations, and evaluation as research software. The report details how this government-maintained system serves as Portugal's official archaeological inventory with approximately 26,000 sites, featuring GIS integration and standardized vocabularies.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (19:30:19)

please also produce the CSV

---

### Assistant (19:31:00)



Here's the complete CSV with metadata for the Endovélico information system:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"Endovélico","Endovélico is Portugal's official archaeological information system that serves as the national inventory and management platform for archaeological sites and fieldwork authorisation. The system, named after a pre-Roman deity worshipped in ancient Lusitania, maintains approximately 26,000 archaeological sites with standardised vocabularies and georeferenced mapping. It provides three-tiered access levels: general public (basic site information), heritage professionals (detailed information requiring registration), and qualified archaeological directors (complete access with submission capabilities). While primarily designed as an administrative tool for cultural heritage management, Endovélico has evolved to support research by providing access to archaeological records, technical documentation, and project details.","Endovélico began as handwritten inventory cards in the 1980s known as 'Carta Arqueológica' (Archaeological Map). Digital development started in 1989 using MS-DOS and Dbase database software, transitioning to Apple Macintosh systems with Filemaker in 1990. The formal Endovélico system was established in 1995 as a relational database with GIS capabilities. Online availability began in 1998, with georeferenced distribution of archaeological sites added in 2012. The system was originally developed by the Instituto Português de Arqueologia (IPA) through its Inventory Division, later transferred to the Instituto de Gestão do Património Arquitectónico e Arqueológico (IGESPAR), then to the Direção-Geral do Património Cultural (DGPC), and as of January 2024, to the newly created Património Cultural, I.P. as part of governmental restructuring.","The Endovélico system has evolved significantly since its inception. Originally based on Dbase (1989) and Filemaker (1990), the current implementation likely employs Oracle Database for backend storage, though specific technical details aren't explicitly documented in public sources. The system operates as a web-based platform accessed through the Portal do Arqueólogo, with server infrastructure maintained by Património Cultural, I.P. The database maintains relational tables for archaeological sites, technical documentation, permits, and project information, all accessible through a tiered-access web interface. Core technical components include: 1) A centralised database with standardised fields and controlled vocabularies for archaeological site characterisation; 2) GIS integration since 1995, supporting spatial querying and mapping via Web Map Service (WMS); 3) Document management capabilities for storing reports and technical documentation; 4) Authentication and authorisation system managing the three-tiered access model; 5) Integration with Matriz 3.0 for archaeological artefact inventory; and 6) Alignment with ISO 14721:2003 Open Archival Information System standard for digital preservation. The system handles spatial data for georeferencing, digital documents, multimedia content, and structured database information with standardised vocabularies. Unlike traditional software with version numbering, Endovélico undergoes continuous daily updates as new archaeological information is processed, with major enhancements implemented through projects like ARQUEOSIA (Modernization of Digital Archaeological Services).","2025-05-06","maybe","Endovélico meets the core definition of research software only partially. While it fully satisfies research data engagement by providing access to archaeological site information and documentation, its primary purpose was administrative rather than research-focused. It partially satisfies methodological alignment by following established archaeological documentation practices. For supporting criteria, it fully satisfies domain knowledge integration (using standardised archaeological vocabularies), documentation focus (providing detailed archaeological site records), and data dissemination (making archaeological information publicly accessible). It partially meets research lifecycle support, mainly serving preservation and publication stages. It has minimal analytical capabilities and data transformation functions. As primarily an inventory and management system rather than analytical research software, it occupies a borderline position.","","","","https://arqueologia.patrimoniocultural.pt/","Government System with Restricted Use","Data management","archaeological database|cultural heritage|inventory system|geospatial integration|Portuguese archaeology","1989","2024-01-01","Continuous updates (no version numbers)","Active","Património Cultural, I.P. (formerly DGPC)","Originally developed by the Inventory Division of the Instituto Português de Arqueologia, with later contributions from various institutional teams. Key individuals include Filipa Bragança.","Small (2-5)","Archaeology","Project-specific","Comprehensive","The system contains approximately 26,000 archaeological sites and is used by all professional archaeologists working in Portugal for both administrative requirements and research purposes. It processes all archaeological work permits in mainland Portugal and serves as the central repository for Portuguese archaeological information. The Portal do Arqueólogo (public interface) receives regular use from researchers, heritage professionals, and the general public, though specific usage metrics aren't publicly documented.","Preservation and Reuse|Publication","mass-market","Stand-alone software","Likely SQL-based with web interface","Web-based (browser)","","Endovélico handles various data formats including spatial data for georeferenced mapping, digital documents and reports, multimedia content (images and photographs), and structured database information with standardised vocabularies. It supports GIS integration through Web Map Service (WMS), integrates with Matriz 3.0 for archaeological artefact inventory, aligns with the ISO 14721:2003 Open Archival Information System standard for digital preservation, and provides both keyword-based and geographical search capabilities.","The system's major strengths include: 1) Centralised management of all Portuguese archaeological activity through a single unified platform; 2) Comprehensive national coverage with approximately 26,000 archaeological sites catalogued; 3) Early adoption of GIS capabilities (since 1995) for spatial representation of archaeological sites; 4) Use of controlled vocabularies for data standardisation and consistency; 5) Tiered public accessibility through the Portal do Arqueólogo, balancing openness with site protection; 6) Strong institutional backing ensuring continuous maintenance and updates; 7) Historical significance as one of Europe's early digital archaeological information systems.","Notable weaknesses include: 1) Spatial and typological consistency issues identified by Portuguese archaeologists, with survey concentration near university centres creating geographical biases; 2) Data verification challenges, particularly for underwater archaeology entries; 3) Functions primarily as an inventory rather than a true data repository with limited capabilities for accessing actual datasets; 4) Five-year embargo period on excavation reports delays information access; 5) Limited analytical functions compared to dedicated research software; 6) Administrative focus sometimes prioritises governance over research accessibility; 7) Possible technological constraints from legacy database architecture.","Endovélico benefits from strong governmental support and institutional mandate as Portugal's official archaeological information system, ensuring long-term sustainability. The recent organisational transformation from DGPC to Património Cultural, I.P. in January 2024 introduces some uncertainty but suggests continued commitment to the system. As a foundation of Portuguese archaeological practice with established workflows and user community, discontinuation is unlikely. However, challenges include keeping pace with technological advances, maintaining data quality and completeness, securing adequate resources for maintenance and development, and addressing the spatial biases in coverage. The system's evolution from paper records to digital database demonstrates adaptability, but significant modernisation may be required to fully transition from an inventory to a comprehensive research platform.","The Archaeology Data Service (UK) and tDAR (Digital Archaeological Record, US) function more as comprehensive data repositories rather than national inventories, offering greater analytical capabilities and direct data access. The European ARIADNE project offers cross-border data interoperability using the CIDOC Conceptual Reference Model. The Nautical Archaeology Digital Library addresses verification issues in underwater heritage documentation. Portugal-specific alternatives are limited as Endovélico is the mandated national system, though some regional or thematic databases exist for specialised research purposes."
```

---
