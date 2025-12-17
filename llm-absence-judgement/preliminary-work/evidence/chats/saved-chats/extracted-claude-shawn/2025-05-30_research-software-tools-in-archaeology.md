# Research Software Tools in Archaeology

## Metadata
- **UUID:** `b3d79951-864c-4aee-9d2e-1cf89123a68e`
- **URL:** https://claude.ai/chat/b3d79951-864c-4aee-9d2e-1cf89123a68e
- **Date:** 2025-05-30 12:49:53

---

## Conversation

### Human (12:29:02)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (12:29:07)



I understand completely. I'll follow the detailed prompt to research and collect metadata about research software tools used in archaeology and historical studies. I'll apply the Writing Style Guide to ensure proper formatting and adhere to the Title Conventions for my report.

I won't ask follow-up questions and will execute the prompt as directed. I'll consult the Tool disambiguation section if I have any questions about the exact tool I'm investigating.

I'm ready to begin researching the first tool. Please provide me with the name or acronym.

---

### Human (12:31:17)

Zooniverse Project Builder

---

### Assistant (12:31:24)



I'll research the Zooniverse Project Builder and compile comprehensive metadata according to the guidelines provided. Starting my research now!
```
This block is not supported on your current device yet.
```

Your report on the Zooniverse Project Builder is ready. It covers the platform's functionality for archaeological and historical citizen science, technical infrastructure, development history, and institutional support. The analysis includes comparisons with alternatives like FromThePage and PYBOSSA, highlighting Zooniverse's strengths in task types (classification, annotation, transcription), scalability (2.6M+ volunteers), and open-source sustainability for humanities research.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (12:48:50)

please also build the requested csv

---

### Assistant (12:49:53)

I'll now create the CSV output format requested in the prompt, following the structure and controlled vocabulary lists provided. I'll compile all the information I've researched about Zooniverse Project Builder into a single CSV row with the appropriate columns.

Let me structure this carefully based on the specifications:

1. I need to ensure I have all the columns in the correct order
2. Each field should be properly quoted
3. Multiple values should use pipe (|) separators
4. I need to ensure the CSV row aligns with the headers

Let me work through each column systematically:I'll create the CSV output for the Zooniverse Project Builder following the specified format:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"Zooniverse Project Builder","The Zooniverse Project Builder is a free, web-based platform that enables researchers to create citizen science projects without programming expertise. The platform specialises in three main task types: classification (identifying objects in images), annotation (marking specific elements), and transcription (converting handwritten or printed text to digital format). In archaeological contexts, it has been used for site detection in LiDAR data, classifying artefacts, and mapping features in satellite imagery. For historical research, it excels at manuscript transcription, photograph analysis, and extracting data from archival documents. The current version uses a three-tier architecture where projects contain workflows (task sequences) that process subject sets (collections of images or documents).","The Zooniverse platform originated in 2007 with Galaxy Zoo, an astronomy project that revolutionised citizen science by engaging volunteers in galaxy classification. Early projects required months of professional development using the 'Ouroboros' platform, limiting launches to 3-5 projects annually. The pivotal transformation came in 2015 with the release of the Panoptes platform and Project Builder, which democratised project creation by providing self-service tools. Key milestones include: 2011 - Ancient Lives launches, pioneering humanities applications; 2015 - Panoptes platform and Project Builder release; 2016 - Python client introduces programmatic access; 2017 - ALICE transcription aggregation tool development begins; 2019 - Frontend modernisation with React; 2022 - NASA partnership renewal; 2025 - Python client v1.7.0 released with enhanced features. This evolution reflects a philosophy of thoughtful improvements based on researcher needs rather than disruptive changes.","The Zooniverse Project Builder runs on a sophisticated three-tier architecture optimised for global-scale citizen science. The current version's backend is built on Ruby on Rails with PostgreSQL databases, while the frontend uses React and Next.js frameworks for responsive user interfaces. Authentication employs OAuth 2.0 with JWT tokens. The platform comprises several key components: (1) Panoptes API - a RESTful JSON API providing programmatic access to all platform features; (2) Client Libraries - official SDKs in Python, Ruby, and JavaScript; (3) Background Processing - Celery for distributed task scheduling; (4) Cloud Storage - media storage with CDN distribution. The system architecture prioritises horizontal scalability to handle millions of concurrent classifications. The platform supports a range of task interfaces including point/line/polygon drawing tools (critical for archaeological site mapping), hierarchical classifications via dropdown menus, and specialised transcription interfaces with the ALICE aggregation tool. Data aggregation algorithms apply statistical methods to combine multiple volunteer contributions into consensus results. Technical requirements for end users are minimal - just modern web browsers with HTTPS support. Developers can run local instances using Docker containers with Kubernetes orchestration. The internationalization framework enables multilingual deployment, supporting global research communities. Performance optimization includes intelligent subject retirement based on agreement thresholds, ensuring efficient volunteer effort allocation.","2025-05-30","yes","The Zooniverse Project Builder fully satisfies all essential research software criteria. It has a clear research-specific purpose facilitating citizen science for scholarly inquiry. It directly engages with research data through classification, annotation and transcription workflows. It aligns perfectly with recognised methodologies in digital humanities and archaeology. It satisfies multiple supporting criteria: it incorporates domain knowledge through specialised workflows for humanities research; supports multiple research lifecycle stages from data collection through analysis; transforms data between formats; provides analytical capabilities through consensus algorithms; visualises results through project dashboards; and extensively documents research applications through case studies.","https://github.com/zooniverse/panoptes","","https://pypi.org/project/panoptes-client/","https://www.zooniverse.org/","Apache License 2.0","Data collection|Platforms and publications|Transcription|Archaeological|Cultural evolution|3D modelling|LiDAR|Museums|API interfaces and web scrapers|Aerial and satellite imagery","citizen science|crowdsourcing|volunteer transcription|archaeological classification|humanities research platform","2015-06-23","2025-03-07","1.7.0 (Python client)","Active","University of Oxford|Adler Planetarium|University of Minnesota-Twin Cities|Citizen Science Alliance","Chris Lintott|Laura Trouille|Lucy Fortson|Brooke Simmons|Grant Miller","Medium (6-20)","Astronomy","General-purpose","Excellent","The Zooniverse Project Builder has attracted over 2.6 million registered volunteers who have contributed to more than 450 research projects since 2007. The platform processes approximately 100,000 classifications daily across 90+ active projects. Notable archaeological projects include Ancient Lives (250,000+ volunteers transcribing Greek papyri) and various LiDAR analysis initiatives. The platform has enabled research resulting in 200+ peer-reviewed publications across disciplines. GitHub metrics show strong development activity with 1,000+ stars, 500+ forks and 100+ contributors across repositories. The Python client has 50,000+ PyPI downloads monthly. Educational adoption includes integration into university curricula and K-12 classroom activities.","Planning|Data Acquisition|Processing|Analysis|Interpretation|Publication","research-specific","Stand-alone software","Ruby|JavaScript|Python|R","Web|Mobile","","The platform provides comprehensive data interoperability through multiple export formats including CSV for statistical analysis, JSON for complex data structures, and TEI (Text Encoding Initiative) for transcription projects. The data schema captures classification data (user information, timestamps, versions), subject metadata (filenames, custom fields), and workflow configuration (task definitions, retirement rules). IIIF (International Image Interoperability Framework) compliance enables integration with digital library systems. The RESTful API supports real-time data access and custom analytical pipelines. The platform follows FAIR data principles: findable through the public project directory, accessible via open data exports, interoperable through standard formats, and reusable with clear licensing.","The Zooniverse Project Builder offers several significant strengths for archaeological and historical research: (1) Democratised access - researchers can launch sophisticated projects without programming skills or technical infrastructure funding; (2) Massive volunteer community - 2.6+ million registered users enable rapid project completion; (3) Scalability - handles datasets from hundreds to millions of items efficiently; (4) Statistical validation - multiple volunteer consensus algorithms ensure research integrity; (5) Specialised humanities tools - ALICE transcription aggregation provides capabilities unavailable elsewhere; (6) Educational integration - supports classroom adoption with teaching resources; (7) Community features - Talk boards foster volunteer engagement and knowledge sharing; (8) Zero cost - completely free for researchers unlike commercial alternatives; (9) Institutional backing - sustained by major research universities ensuring long-term viability; (10) Open-source flexibility - allows customisation for specific research needs.","Despite its versatility, the current version of the Zooniverse Project Builder has several limitations: (1) Task complexity ceiling - best suited for tasks reducible to simple, repeatable actions rather than complex interpretive work; (2) Survey limitations - not designed for opinion-based research or complex branching surveys; (3) Upload constraints - 10,000 subject limit per user upload (though waivable upon request); (4) Customisation boundaries - projects requiring features beyond the builder interface need custom development; (5) Learning curve - building optimal workflows requires understanding volunteer behaviour and platform capabilities; (6) Limited direct integration with GIS software for archaeological applications; (7) Mobile responsiveness varies - complex annotation tasks work better on desktop; (8) Data export requires statistical knowledge for proper interpretation; (9) No built-in machine learning assistance for classification (though external integration is possible); (10) Volunteer recruitment responsibility falls on researchers, with success varying by project topic appeal.","The Zooniverse Project Builder demonstrates excellent long-term viability through several key factors: (1) Diversified funding from multiple federal agencies (NSF, NASA, IMLS, NIH, NEH), private foundations, and institutional commitments; (2) Multi-institutional governance through the Citizen Science Alliance, providing resilience against organisational changes; (3) Active development with regular updates and feature additions; (4) Growing volunteer base indicating sustained public interest; (5) Strong publication record establishing legitimacy in academic contexts; (6) Apache 2.0 open-source licensing ensuring code availability regardless of institutional changes; (7) Containerised deployment enabling flexible hosting options; (8) Educational adoption creating stakeholder commitment; (9) 17+ year operational history demonstrating sustainability; (10) Recent achievements like the 2024 White House 'Champions of Open Science' award indicating continued relevance. These factors collectively suggest the platform will remain viable for the foreseeable future, making it a safe investment for long-term research projects.","Several alternative platforms exist for citizen science in humanities research, though none match Zooniverse's comprehensive features and community size: (1) FromThePage - excels at manuscript transcription with specialised paleography tools but requires paid subscriptions and lacks image analysis capabilities; (2) PYBOSSA - offers maximum customisation as an open-source framework but demands significant technical expertise and lacks hosted options since CrowdCrafting's discontinuation; (3) CitSci.org - provides excellent community governance features but lacks sophisticated humanities tools; (4) SPOTTERON - offers polished, branded experiences but at substantial cost (€3,000+ setup plus maintenance); (5) Transkribus - powerful for document transcription with AI assistance but limited to text rather than multi-modal research. For archaeological projects combining multiple task types, Zooniverse remains unmatched in capabilities and accessibility."
```

---
