# v8-STELLAR-metadata (clarified)

## Metadata
- **UUID:** `2a23ca97-46f3-4632-8020-4a30892183f9`
- **URL:** https://claude.ai/chat/2a23ca97-46f3-4632-8020-4a30892183f9
- **Date:** 2025-05-31 07:38:00

---

## Conversation

### Human (07:02:36)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (07:02:40)



I understand the task completely. I'll be collecting detailed metadata about research software tools used in archaeology, history, and related historical studies disciplines. I'll follow:

1. The detailed research approach in the prompt
2. The Australian English writing style guide provided
3. The title convention format "[Tool Name]: [Primary Function] for [Application Domain]"

I'll conduct thorough research on each tool you specify, evaluating whether it qualifies as research software according to the criteria provided. The output will include a comprehensive CSV with all required fields and follow the specific formatting requirements (pipe separators, proper escaping, etc.).

I'm ready to begin research on the first tool you name. Please provide the name or acronym of the tool you'd like me to investigate.

---

### Human (07:03:27)

STELLAR (Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources)

---

### Assistant (07:03:34)



Let me research STELLAR (Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources) thoroughly to provide you with comprehensive metadata according to your requirements.

I'll launch a detailed research process to gather all the necessary information about STELLAR, including its purpose, technical implementation, development history, and application in archaeological research.
```
This block is not supported on your current device yet.
```

Your STELLAR archaeological data management analysis is ready. It covers the software's functionality for converting datasets to CIDOC CRM-EH linked data, its development history (2010-2011), technical implementation in C#/.NET, and template-based conversion system. The report examines archaeological applications, interoperability with heritage standards, strengths/weaknesses, and comparisons with alternative tools like ARIADNEplus, Open Context, and Arches.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (07:34:17)

please also generate the requested csv

---

### Assistant (07:35:27)

I need to create a CSV with the metadata for STELLAR based on my research. I'll follow the format requested in the prompt, ensuring I include all the required fields with appropriate data.

The CSV should contain a single row with all the metadata about STELLAR, with the header row matching exactly what was specified in the prompt.

Let me organize the data for each field:

1. Tool: STELLAR (Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources)
2. Description: A comprehensive overview focused on its purpose of converting archaeological datasets to linked data
3. History: Chronological development including the AHRC-funded project, timeline, and relationship to other projects
4. Technical-discussion: Detailed explanation of how it works technically
5. Access-date: Today's date (2025-05-31)
6. Tool-status: "yes" (based on the research software evaluation criteria)
7. Tool-status-reasoning: Explanation of why it meets the criteria
8. DVCS-repo: GitHub link if available, otherwise empty
9. CRAN: Empty (not an R package)
10. PyPi: Empty (not a Python package)
11. Other-URL: Primary homepage or documentation URL
12. License: The license info I found
13. Tags: Appropriate tags from the controlled vocabulary
14. AI-tags: Five tags I'll generate to characterize STELLAR
15. First-release-date: The initial release date
16. Last-update-date: The most recent update date
17. Current-version: Most recent version identifier (if available)
18. Development-status: From the controlled list (Abandoned)
19. Institutional-backing: The supporting organizations
20. Authors: The main contributors
21. Development-team-size: Size category based on what I found
22. Original-discipline: Archaeology
23. Original-purpose: From controlled list
24. Documentation-quality: Based on my assessment
25. Usage-indicators: Usage metrics paragraph
26. Lifecycle-stage: Stages it supports from the controlled list
27. Type: "research-specific"
28. Category: From the controlled list
29. Language: C#/.NET
30. Platform: Windows, with Mono for Linux/macOS
31. Open-Archaeo-Platform: Empty (not a package/library for another platform)
32. Interoperability: Data formats and exchange capabilities
33. Strengths: Evidence-based assessment of advantages
34. Weaknesses: Evidence-based assessment of limitations
35. Survivability: Long-term viability assessment
36. Alternatives: Similar tools comparison

Now I'll create the CSV following the format requirements, ensuring proper escaping, using pipe (|) separators for multiple values, and making sure no newlines or citations within fields.# STELLAR: Semantic Data Conversion for Archaeological Resources

Based on thorough research, I've compiled comprehensive metadata about STELLAR (Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources), a specialized tool for converting archaeological datasets into linked semantic data.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"STELLAR","STELLAR (Semantic Technologies Enhancing Links and Linked Data for Archaeological Resources) is a toolkit designed to enable archaeologists and data managers without semantic web expertise to convert archaeological datasets into linked data conforming to the CIDOC CRM-EH ontology. The current version provides three core applications: STELLAR.Console (command-line utility), STELLAR.Web (browser interface), and STELLAR.Testing (validation tool). These applications allow users to import structured data (CSV/TAB), manipulate it via SQL queries, and apply predefined templates to convert archaeological records to RDF/XML format. STELLAR was specifically developed to bridge the gap between excavation data management and semantic web technologies, making linked data creation accessible to archaeological practitioners without requiring expertise in ontology modelling.","STELLAR emerged from a £110,000 Arts and Humanities Research Council (AHRC) funded project running from March 2010 to March 2011. It was developed at the University of Glamorgan (now University of South Wales) by Professor Douglas Tudhope and Research Fellow Ceri Binding, in collaboration with the Archaeology Data Service and English Heritage. The project built upon previous semantic web initiatives: the FACET project (EPSRC-funded) pioneered thesaurus-based search techniques, followed by the 3-year STAR project (2007-2010) that developed core semantic technologies for archaeological reporting. STELLAR represented the culmination of this research progression, focusing on practical tools for archaeological data managers. The software was publicly released in 2011, with case studies demonstrating applications with major UK archaeological datasets. While active development concluded with the project's completion in 2011, STELLAR's approach influenced subsequent projects including SENESCHAL (2013-2014) for vocabulary services and contributed to the European ARIADNEplus infrastructure. No version numbering system was implemented beyond the initial release.","The STELLAR toolkit's technical implementation centers on a template-based approach to data transformation. The current version is built in C# on the .NET Framework, with core dependencies including ANTLR for template parsing, FileHelpers for structured text processing, and the SemWeb library for RDF operations. The system architecture follows a three-stage workflow: 1) Data Preparation - STELLAR.Console imports CSV/TAB files into an internal SQLite database, allowing users to consolidate data using SQL queries before conversion; 2) Template Application - Predefined templates express relationships between archaeological data fields and CRM entities/properties (templates contain variables that match column headings from the source data, with conditional logic and loops for handling complex mappings); 3) RDF Generation - The system produces RDF/XML output with consistent URI patterns for archaeological entities. The technical innovation lies in the template mechanism, which abstracts semantic web complexity through pattern-based transformation rules. Templates encapsulate the complex entity-relationship mapping between archaeological concepts and the CIDOC CRM-EH ontology. For example, a context record template might create a 'EHE0007.ContextFind' entity with properties linking to context and find entities, handling relationship cardinality and identifier generation automatically. The software implements W3C standards for RDF/XML output, generates consistent URIs for entities, and manages namespaces for linked data publication. Memory management was optimized for large datasets through stream-based processing rather than loading entire datasets. Previous versions during development featured more limited template capabilities and lacked the SQL preparation stage that was added to handle real-world archaeological data complexity.","2025-05-31","yes","STELLAR fully satisfies all essential criteria for research software. It was specifically designed to support archaeological research (Research-Specific Purpose) by transforming excavation datasets into semantic linked data (Research Data Engagement). Its template-based approach aligns with established methodologies for archaeological data integration (Methodological Alignment). For supporting criteria, STELLAR meets 5 out of the 8: it incorporates domain knowledge through CIDOC CRM-EH ontology integration (Domain Knowledge Integration); supports the data processing and analysis stages of research (Research Lifecycle Support); transforms between CSV/TAB formats and RDF/XML (Data Transformation); performs complex entity-relationship mappings (Analytical Capabilities); and provides documentation specifically addressing archaeological applications (Documentation Focus). Its primary function of enabling semantic web integration for archaeological datasets demonstrates clear research-specific purpose beyond general database capabilities.","https://github.com/cbinding/stellar","","","http://hypermedia.research.southwales.ac.uk/kos/STELLAR","Creative Commons Attribution 3.0","Data management|Schemas and ontologies|API interfaces and web scrapers|Platforms and publications|Data collection","semantic_web|archaeological_databases|data_transformation|ontology_mapping|rdf_generation","2010-03-01","2011-03-31","1.0","Abandoned","University of Glamorgan (now University of South Wales)|Archaeology Data Service|English Heritage","Douglas Tudhope|Ceri Binding","Small (2-5)","Archaeology","Project-specific","Comprehensive","STELLAR was initially used to process 5+ major UK excavation archives, including the Channel Tunnel Rail Link Section 1, Hartshill ironworking site, Wellington Quarry, and St Peter's Church data. It produced 10+ academic publications and influenced at least 4 subsequent projects (SENESCHAL, ARIADNE, ARIADNEplus, STELETO). International adoption included the German ArcheoInf project and the German Archaeological Institute creating thesauri for DARIAH. While precise download statistics are unavailable, the software was distributed through university channels. Academic impact continues with citations in digital archaeology literature through 2024, particularly in semantic archaeological data management research. Conference presentations at CAA (Computer Applications in Archaeology) events from 2008-2014 disseminated findings internationally. The relatively small user base reflects its specialized nature as a research tool rather than commercial software, though its conceptual approach has been widely influential in the field.","Processing|Analysis|Preservation and Reuse","research-specific","Stand-alone software","C#","Windows|Linux|macOS","","STELLAR supports input formats including CSV, TAB-delimited, and fixed-width text files, producing output in RDF/XML and N-Triples formats compliant with W3C standards. The current version implements CIDOC CRM (ISO 21127) and its archaeological extension CRM-EH, along with SKOS for controlled vocabularies. This standards-based approach ensures interoperability with semantic web infrastructure and archaeological data repositories. The system generates consistent URIs for entities and manages namespaces for linked data publication. Integration points include compatibility with the Archaeology Data Service's linked data repository and the broader archaeological semantic web ecosystem through standards compliance. The transformation templates provide a flexible mechanism for mapping various archaeological database schemas to the standardized CIDOC CRM-EH model, supporting interoperability across diverse excavation recording systems.","STELLAR's primary strength is its accessibility for non-specialists, providing guided workflows and predefined templates that reduce barriers to semantic technology adoption in archaeology. The current version's template-based approach successfully abstracts complex ontological relationships, allowing archaeologists to create valid RDF/XML without deep knowledge of semantic web technologies. Its standards-based implementation using established cultural heritage ontologies (CIDOC CRM-EH) ensures long-term compatibility with emerging archaeological information systems. Practical validation with real commercial archaeological datasets demonstrates genuine utility beyond theoretical exercises. The free availability and relatively straightforward installation process made it accessible for budget-conscious archaeological projects. Documentation was comprehensive, including detailed mapping guidelines, user manuals, and examples drawn from actual archaeological datasets. The project's close collaboration with major institutions (English Heritage, Archaeology Data Service) ensured alignment with practical needs of the archaeological community. The toolkit successfully addressed the critical need for semantic interoperability in archaeological data, particularly for legacy datasets from completed excavations.","Several limitations affect STELLAR's practical application. Template modification complexity required rebuilding the application to implement new patterns, creating a technical barrier for advanced users. The current version's reliance on manual mapping processes poses scalability challenges for large-scale data integration projects, lacking automated schema matching capabilities found in newer systems. Initial versions offered limited vocabulary control, often mapping free text rather than controlled terms, which reduced semantic precision. Technical dependencies on specific software environments (.NET Framework) created deployment hurdles for some archaeological organizations. Documentation gaps exist for advanced usage scenarios, requiring expertise to extend beyond provided templates. The workflow separation between data preparation and transformation increases learning complexity compared to integrated platforms. Performance optimization for very large datasets (>100,000 records) remains unaddressed in current implementations. The lack of visual mapping tools makes relationship comprehension difficult for complex archaeological schemas. Maintenance challenges emerged after project funding concluded, with limited community resources for ongoing development. These weaknesses reflect STELLAR's origin as a research project rather than commercial software, with emphasis on conceptual innovation over production-grade implementation.","STELLAR's long-term viability as a standalone tool appears limited, as the software has not been actively maintained since the project's completion in 2011. However, its conceptual framework and approach have demonstrated remarkable sustainability through integration into successor projects and operational services. The software's intellectual foundation continues to influence archaeological linked data initiatives globally. Several factors contribute to its mixed survivability profile: 1) The CIDOC CRM standard remains actively maintained and widely adopted, ensuring continued relevance of STELLAR's core approach; 2) Modern alternatives have incorporated and extended STELLAR's template-based mapping concepts while addressing technical limitations; 3) Documentation remains accessible through academic repositories, allowing knowledge transfer despite limited software maintenance; 4) The code base is available under permissive licensing, enabling reuse of components in newer systems; 5) Technical dependencies on older .NET frameworks create increasing compatibility challenges on modern systems. While the original software may become increasingly difficult to deploy, STELLAR's conceptual contributions to archaeological data integration continue to demonstrate significant impact through derivative systems and services, particularly in the European archaeological data infrastructure landscape.","Alternative tools for archaeological data semantic conversion and management have evolved significantly since STELLAR's development. ARIADNEplus represents the closest conceptual successor, implementing STELLAR's vision at continental scale with over 3.5 million resources and advanced Virtual Research Environments. Unlike STELLAR's standalone approach, ARIADNEplus provides a comprehensive infrastructure with automated mapping services. Open Context shares STELLAR's semantic web focus but emphasizes peer-reviewed data publication over mapping tools, with stronger support for field data collection and integration with external repositories. tDAR (The Digital Archaeological Record) prioritizes long-term preservation and broad accessibility without STELLAR's semantic emphasis, offering more comprehensive file format support but less ontological integration. For practical heritage management, Arches provides enterprise-level capabilities with optional CIDOC CRM compliance, superior visualization features, and active maintenance. Heurist offers flexible humanities database design with less semantic integration but greater customization for project-specific needs. FAIMS focuses on mobile field data collection, integrating with backend systems for semantic processing. Migration from STELLAR remains feasible due to standard RDF output formats, though newer systems offer improved workflow integration and user interfaces. Current community preferences favor larger, well-funded platforms with proven sustainability and comprehensive feature sets."
```

Based on my research, STELLAR qualifies as research software under the evaluation criteria. It was specifically designed for archaeological data transformation and supports semantic data integration using established ontologies. Despite being no longer actively maintained, its conceptual approach continues to influence archaeological data management through successor projects like ARIADNEplus.

---
