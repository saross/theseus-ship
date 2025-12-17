# v8-OpenArchaeo-metdata (MASA product)

## Metadata
- **UUID:** `8e023561-ad16-4703-9d1a-5d52a474ccb4`
- **URL:** https://claude.ai/chat/8e023561-ad16-4703-9d1a-5d52a474ccb4
- **Date:** 2025-05-26 06:18:29

---

## Conversation

### Human (05:45:56)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (05:46:03)



I understand the task completely. I'll be collecting comprehensive metadata about research software tools used in archaeology, history, and related historical studies disciplines. I'll follow:

1. The detailed research approach outlined in the prompt
2. The writing style guide principles for Australian English 
3. The title convention format "[Tool Name]: [Primary Function] for [Application Domain]"
4. The controlled vocabulary lists and evaluation framework

I'll execute the prompt without asking follow-up questions and will handle any tool disambiguation following the guidelines provided. I'm ready to begin researching the first tool you provide.

---

### Human (05:46:09)

OpenArchaeo (semantic web platform)

---

### Assistant (05:46:16)



I'll research OpenArchaeo, the semantic web platform for archaeological data. Let me gather comprehensive information about this tool following the research approach outlined in the prompt.
```
This block is not supported on your current device yet.
```

Your OpenArchaeo platform assessment is ready. It includes analysis of this archaeological semantic web platform's federated query architecture, CIDOC CRM implementation, and technical specifications. The report evaluates its strengths in enabling cross-database searches without data migration, institutional backing through TGIR Huma-Num, and the innovative SPARNATURAL component. It also addresses limitations regarding documentation, international adoption, and comparison with alternatives like Arches.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (06:04:25)

please also produce the requested CSV

---

### Assistant (06:05:27)

Now I'll produce the comprehensive CSV following the format requested in the prompt. This CSV will contain all the metadata fields about OpenArchaeo according to the research I've conducted.

I need to ensure I follow these guidelines:
1. Present as a markdown fenced code block with quoted CSV
2. Include the header row and a single properly escaped data row
3. Format multiple values with pipe (|) separators
4. Ensure no newlines within fields
5. Use single quotes for any quoted text within fields
6. Verify the number of columns matches between header and data rows

Let me create this CSV with all the required fields:Based on my research into OpenArchaeo, I've compiled the requested metadata in the CSV format below. This assessment follows Australian English spelling conventions and academic writing standards as specified.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"OpenArchaeo","OpenArchaeo is a semantic web platform that enables federated querying of heterogeneous archaeological datasets through semantic web technologies. The current version implements the CIDOC CRM ontology and its extensions to integrate disparate archaeological databases without requiring data migration or restructuring. It provides both a technical SPARQL endpoint for machine access and a user-friendly visual query interface called SPARNATURAL, which allows archaeologists without semantic web expertise to formulate complex queries across multiple archaeological datasets. The platform focuses on preserving existing database structures while enabling cross-database searches through semantic mediation.","OpenArchaeo was developed by the MASA (Mémoire des Archéologues et des Sites Archéologiques) consortium, which was established in France in 2012 to improve digital archaeological data management. Initial development began around 2013, with conceptual architecture defined between 2013-2017. The first public presentation of the platform occurred at the ODOCH conference in Rome in June 2019, accompanied by the publication of the paper 'OpenArchaeo for Usable Semantic Interoperability'. The system has been continuously refined since then, with particular focus on the SPARNATURAL visual query interface. In 2023, the MASA consortium transitioned to MASAplus with continued support for OpenArchaeo development. Throughout its history, the platform has maintained its focus on federated querying rather than centralised data storage, aligning with European initiatives like ARIADNEplus.","The current version of OpenArchaeo employs a modular architecture built around semantic web technologies. At its core is a federated query system that connects to multiple archaeological databases through semantic mediation using the CIDOC CRM ontology and its extensions (CRMarchaeo, CRMsci, CRMba). Technically, the platform consists of several components: 1) A triple store repository (using GraphDB) that contains RDF representations of archaeological data, 2) A SPARQL endpoint providing machine-accessible query services, 3) The SPARNATURAL visual query builder (developed in TypeScript as a reusable web component), and 4) A user-friendly explorer interface specifically tailored for archaeological concepts. The backend is primarily implemented in Java (deployed as WAR files), while the frontend utilises modern JavaScript/TypeScript. Configuration is handled through SHACL specifications and Excel-based setup tools. The key technical innovation is the query federation approach - rather than requiring data migration into a centralised repository, OpenArchaeo implements semantic mappings that allow cross-database queries while preserving the original data structures. This architecture maintains database sovereignty for participating institutions while enabling semantic interoperability. The platform supports standard semantic web formats including RDF/XML, Turtle, N-Triples, and JSON-LD. The SPARNATURAL component translates user selections in the visual interface into valid SPARQL 1.1 queries, abstracting away the complexity of the query language from end users. Performance considerations include query result limitations (capped at 1000 results in the visual interface) and CORS requirements for endpoint integration.","2025-05-26","yes","OpenArchaeo meets all essential criteria for research software classification. It has a clear research-specific purpose in enabling federated querying of archaeological datasets. It directly engages with research data by transforming heterogeneous archaeological databases into semantically interoperable resources. It aligns with recognized methodologies in both archaeology and semantic web research. For supporting criteria, it excels in domain knowledge integration (implementing CIDOC CRM and archaeological vocabularies), research lifecycle support (covering data processing through publication), analytical capabilities (complex semantic queries), and visualization functions (SPARNATURAL interface). The software's documentation specifically addresses archaeological research applications, and it supports both data collection integration and dissemination of research data through semantic web standards.","https://github.com/sparna-git/Sparnatural","","","http://openarchaeo.huma-num.fr/explorateur/home","Custom licence (components vary)","Data management|Platforms and publications|Schemas and ontologies|Spatial analysis|Site mapping","semantic_web|federated_query|archaeology_database|cidoc_crm|interoperability","2019-06-01","2023-01-01","Unknown","Active","TGIR Huma-Num (CNRS, France)|MASAplus Consortium|ARIADNEplus (European project)","Olivier Marlet|Xavier Rodier|Thomas Francart|Béatrice Markhoff","Small (2-5)","Archaeology","General-purpose","Basic","OpenArchaeo is primarily used within French archaeological institutions that participate in the MASA/MASAplus consortium. No public usage statistics are available, but documented implementations include the ArSol database (Tours), HADÈS (Bordeaux Metropole), and integration with the French national archaeological thesaurus PACTOLS. The platform is referenced in European infrastructure projects, particularly ARIADNEplus. GitHub metrics for the SPARNATURAL component show modest activity with approximately 10-15 stars and fewer than 10 forks. Academic citations appear in semantic web archaeology literature, particularly in French-language publications. Community engagement occurs primarily through consortium workshops rather than open forums. The platform has limited visibility outside francophone archaeology communities despite its technical sophistication.","Data Acquisition|Processing|Analysis|Publication|Preservation and Reuse","research-specific","Stand-alone software","TypeScript|JavaScript|Java","Web (platform-independent)","","OpenArchaeo interoperates with multiple archaeological database systems through semantic mappings to CIDOC CRM. The current version supports data exchange in standard semantic web formats including RDF/XML, Turtle, N-Triples, JSON-LD, and N-Quads. Controlled vocabularies are integrated through the PACTOLS archaeological thesaurus, GeoNames for geographical references, and authority systems like VIAF and ORCID for people. The platform implements SPARQL 1.1 for queries, with RESTful APIs providing additional integration points. The federated architecture is designed to work with existing archaeological database systems without requiring data migration. Specific French archaeological databases with documented integration include ArSol (Tours), HADÈS (Bordeaux), and ArkeoGIS. For spatial data, the system supports GeoSPARQL extensions and standard OGC formats.","OpenArchaeo's primary strength is its federated architecture, which enables semantic interoperability without requiring database migration - institutions can maintain existing systems while gaining cross-database query capabilities. The current version's SPARNATURAL component provides an intuitive visual interface that translates domain concepts into SPARQL queries, making semantic web technology accessible to archaeologists without technical expertise. The platform's implementation of CIDOC CRM and its extensions ensures alignment with international standards, enhancing long-term data sustainability. Institutionally, OpenArchaeo benefits from integration with permanent French research infrastructure (TGIR Huma-Num), ensuring sustained technical support and development. The modular design allows components to be reused in other contexts, particularly the SPARNATURAL query builder which has applications beyond archaeology. The comprehensive semantic model enables complex queries across heterogeneous datasets that would be impossible with conventional database systems.","The current version of OpenArchaeo faces several limitations. Technical weaknesses include query result limitations (capped at 1000 results in the visual interface) and complex CORS requirements for endpoint integration. The federated architecture, while preserving database sovereignty, introduces performance challenges compared to centralised systems. Documentation is primarily available in French, creating a significant language barrier for international adoption. The platform requires substantial understanding of semantic web concepts for implementation, despite efforts to simplify the user interface. Institutionally, OpenArchaeo has limited visibility outside French archaeological circles, with minimal evidence of international user communities or third-party implementations. The small development team size raises concerns about response times for technical issues. While the SPARNATURAL component is open source, the complete system architecture documentation is less comprehensive than competing platforms like Arches, potentially limiting adoption by organisations without direct consortium support.","OpenArchaeo demonstrates moderate to high survivability within its primary French and European archaeological context. The platform's integration into permanent national research infrastructure (TGIR Huma-Num) provides institutional stability and sustained funding. The recent transition to the MASAplus consortium (2023) indicates continued organisational commitment. The implementation of established standards (CIDOC CRM, Semantic Web) enhances technical sustainability, while the open-source SPARNATURAL component ensures key innovations remain accessible. Participation in European digital infrastructure initiatives like ARIADNEplus further strengthens its position. However, several risk factors should be noted: the limited international visibility restricts potential growth of the user community; the relatively small development team creates potential single points of failure; and competition from more widely adopted platforms like Arches may limit broader adoption. Documentation gaps, particularly in English, may hinder new implementations outside the francophone community. Overall, OpenArchaeo appears sustainable within its current institutional context, though its global impact will likely remain limited without addressing internationalisation challenges.","Arches (Getty Conservation Institute): A comprehensive archaeological information system with global adoption that requires data migration into its platform. Offers more extensive documentation and a larger user community, but less flexibility for existing database integration. OpenAtlas (Austrian Academy of Sciences): A CIDOC CRM-native database system focused on historical and archaeological research with strong spatial capabilities and prosopographical data handling. Offers direct data modelling but smaller user base than OpenArchaeo. ARK (Archaeological Recording Kit): Established excavation recording system with web-based interfaces, but less semantic web integration than OpenArchaeo. Uses traditional LAMP stack rather than semantic technologies. ResearchSpace (British Museum): Enterprise-scale semantic web platform with sophisticated knowledge representation capabilities, but more complex implementation requirements than OpenArchaeo. Excellent for museum collections but less field-oriented. Heurist (University of Sydney): Research-focused database platform with archaeological capabilities and flexible schema design. More straightforward than semantic web approaches but less powerful for heterogeneous data integration."
```

---
