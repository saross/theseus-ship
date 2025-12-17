# v8-VirtualArch-metadata

## Metadata
- **UUID:** `ed7c4b4a-39ea-4cec-89a6-173e4866e2a0`
- **URL:** https://claude.ai/chat/ed7c4b4a-39ea-4cec-89a6-173e4866e2a0
- **Date:** 2025-05-31 13:58:36

---

## Conversation

### Human (13:46:10)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. 

A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 

Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt. Consult the 'Tool disambiguation' section in particular if you have questions about the exact tool you are investigating.

Confirm that you understand, then I will provide you with the name or acronym of the first tool.

---

### Assistant (13:46:15)



I understand your requirements completely. I'll collect metadata about research software tools in archaeology, history, and other historical studies disciplines, following the detailed prompt provided. I'll apply the Writing Style Guide to both the report and CSV output, using the specified title convention format of "[Tool Name]: [Primary Function] for [Application Domain]".

I'll execute the prompt without asking follow-up questions and will consult the 'Tool disambiguation' section if there are any questions about the exact tool being investigated.

I'm ready to begin researching the first tool as soon as you provide its name or acronym.

---

### Human (13:46:17)

VirtualArch

---

### Assistant (13:46:24)



I'll start researching VirtualArch to collect comprehensive metadata following the research approach outlined in your instructions.

Time to dive into some detailed research about VirtualArch and its applications in archaeological contexts!
```
This block is not supported on your current device yet.
```

Your VirtualArch research report is ready. It clarifies that VirtualArch was an EU-funded project (2017-2020) that created multiple VR/AR applications for archaeological sites across Central Europe, not standalone software. The report covers the project's €2.1M budget, pilot implementations across 8 sites, technical approaches, institutional partners, research outputs, and limitations as research software. It includes analysis of alternatives and evaluation against sustainability criteria.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (13:57:38)

please also generate the requested csv

---

### Assistant (13:58:36)

I need to create a CSV output for VirtualArch based on the research I've conducted. The CSV should follow the structure specified in the instructions, with appropriate values for each field. Let me work through each required field:

### Essential Information
- **Tool**: "VirtualArch"
- **Description**: Brief overview of VirtualArch as a project rather than standalone software
- **History**: Chronological development from 2017-2020
- **Technical-discussion**: Technical implementation details 
- **Access-date**: Today's date (2025-05-31)
- **Tool-status**: "no" (based on the evaluation criteria - it's not sustainable research software)
- **Tool-status-reasoning**: Explanation of why it doesn't qualify as research software
- **DVCS-repo/CRAN/PyPi**: Empty as there's no repository
- **Other-URL**: Project website or documentation
- **License**: Not specified/Unknown
- **Tags**: Relevant tags from the controlled list
- **AI-tags**: 5 custom tags characterizing the tool

### Development and Organization
- **First-release/Last-update-date**: 2017 / 2020
- **Current-version**: N/A
- **Development-status**: "Deprecated" 
- **Institutional-backing**: The archaeological organizations involved
- **Authors**: Key project contributors
- **Development-team-size**: "Medium (6-20)" based on the number of partners
- **Original-discipline**: "Archaeology"
- **Original-purpose**: "Project-specific"
- **Documentation-quality**: "Minimal"
- **Usage-indicators**: Usage metrics paragraph

### Technical and Assessment 
- **Lifecycle-stage**: Relevant research stages
- **Type**: "research-specific"
- **Category**: Likely "Stand-alone software" (though this is borderline)
- **Language**: Programming languages used (if known)
- **Platform**: Operating systems supported
- **Open-Archaeo-Platform**: N/A
- **Interoperability**: Data formats and exchange
- **Strengths/Weaknesses**: Evidence-based assessment
- **Survivability**: Assessment of long-term viability
- **Alternatives**: Similar tools for comparison

Let me create the CSV entry with this information.Now I'll generate the requested CSV data following the specified format:

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"VirtualArch","VirtualArch was an EU-funded research project (2017-2020) that developed multiple virtual and augmented reality applications for visualising hidden archaeological heritage across Central Europe. The project focused on making underground, underwater, and otherwise inaccessible archaeological sites visible to the public through digital visualisation technologies. It was not developed as a standalone software tool but rather as a series of site-specific digital applications implemented at eight pilot locations, including Bronze Age salt mines in Austria, medieval silver mines in Germany, and Roman harbour remains in Croatia. The project sought to enhance heritage conservation, education, and tourism through innovative visualisation approaches.","VirtualArch was conceived and funded as an Interreg Central Europe initiative under the European Regional Development Fund, running from July 2017 to June 2020. The project was led by the Archaeological Heritage Office of Saxony (Germany) in partnership with 10 full partner institutions and 17 associate organisations across 8 Central European countries. The project operated with a total budget of €2,093,771.25, with €1,730,429.76 from EU funding sources. Development proceeded through coordinated transnational activities with regular partner meetings and milestone deliverables. The project officially launched with a kickoff meeting in 2017, developed and implemented pilot applications at eight archaeological sites between 2018-2019, and concluded with final reports and an international conference in 2020. No development activities continued beyond the project's official end date of 30 June 2020.","The technical implementation of VirtualArch varied across the eight pilot sites, as each location required customised solutions appropriate to its specific archaeological context. The project did not develop a unified software platform but instead created multiple applications using existing tools and technologies. For underground mining sites in Germany and Austria, the team employed 3D laser scanning combined with photogrammetry to document spaces, creating VR experiences viewable through HTC Vive headsets and mobile AR applications like 'Medieval MinesAR' for Android. Urban archaeological sites in Slovakia and the Czech Republic utilised LiDAR scanning for landscape documentation, with progressive web applications providing offline functionality through service workers. Underwater archaeological sites in Poland and Croatia required specialised approaches using multi-beam sonar surveys to map submerged structures. The current version of these applications (as of project completion in 2020) is best understood as a collection of site-specific implementations rather than a coherent software platform. Development relied on standard industry tools including Unity for VR/AR development, GIS platforms for spatial data management, and web technologies for progressive web applications. The project emphasised visual fidelity and educational value over software sustainability, with limited attention to version control, testing procedures, or technical documentation beyond academic papers. This approach reflects the project-oriented nature of the initiative, prioritising immediate public engagement over long-term software sustainability.","2025-05-31","no","VirtualArch fails to meet essential criteria for research software classification. While it supports research activities (criterion 1) and engages with research data through 3D visualisation (criterion 2), it fundamentally lacks the characteristics of sustainable, distributable research software. The project produced site-specific applications rather than reusable software tools, with no provisions for long-term maintenance, no public code repositories, and no standardised citation mechanisms. The absence of version control, systematic testing procedures, or technical documentation beyond academic papers violates basic software engineering practices expected of research software. Furthermore, the fixed project end date (June 2020) meant no ongoing development community formed, ensuring technical obsolescence as platforms evolve. These fundamental limitations prevent VirtualArch from qualifying as research software despite its valuable contributions to archaeological visualisation research.","","","","https://intarch.ac.uk/journal/issue54/2/","Unknown","Virtual reality|Augmented reality|3D modelling|Photogrammetry|Site mapping|Data management|Visualization|Public archaeology","archaeological visualisation|transnational heritage project|non-sustainable software|VR/AR applications|buried heritage interpretation","2017-07-01","2020-06-30","N/A","Deprecated","Archaeological Heritage Office of Saxony (Germany), Fondazione Bruno Kessler (Italy), University of Toruń (Poland), Czech Academy of Sciences Institute of Archaeology, City of Nitra (Slovakia), Autonomous Province of Trento (Italy), Administration of the Republic of Slovenia for Civil Protection and Disaster Relief, Archaeological Museum of Zagreb (Croatia), NÖ Landesmuseum (Austria), Institute of Archaeology Rzeszów (Poland)","Jan Mařík, Jiří Unger, Christiane Hemker, Christoph Lobinger, Fabio Remondino","Medium (6-20)","Archaeology","Project-specific","Minimal","VirtualArch received €2.1 million in EU funding and involved 10 partner institutions across 8 countries. The project produced visualisations for eight archaeological sites, with documented visitor engagement at museum installations. The primary publication in Internet Archaeology (volume 54, 2020) has received academic citations, though specific usage metrics for the digital applications are not publicly available. The project received recognition through the AVICOM award for the TIME MACHINE platform developed by project partners. No download statistics, user numbers, or community metrics exist as the applications were primarily deployed as on-site installations rather than distributable software. There is no evidence of continued use or development beyond the project end date in 2020, with no active user or developer communities.","Interpretation|Publication","research-specific","Stand-alone software","Unity|JavaScript|HTML5|CSS","Android|iOS|HTC Vive|Web browsers","","The project produced multiple data formats including 3D models (OBJ, FBX), GIS data (Shapefiles, GeoTIFF), and web-based visualisations (HTML/JS/CSS). However, no standardised APIs or data exchange protocols were developed, limiting interoperability between components. Each site implementation functioned as a closed system with minimal provisions for data exchange with external systems. The web applications followed basic web standards but lacked documented APIs for external access.","VirtualArch demonstrated several innovative strengths in archaeological visualisation. The transnational approach fostered knowledge exchange across Central Europe, creating a network of institutions sharing best practices in digital heritage. Unlike many theoretical VR projects, VirtualArch emphasised practical implementation, producing working applications deployed at real heritage sites. The integration of multiple VR/AR technologies showed technical ambition, from immersive projections to augmented print catalogues. The project successfully addressed a genuine gap in archaeological communication, bringing normally invisible heritage (underground, underwater) to life for modern audiences. The interdisciplinary team combining archaeologists, computer scientists, and heritage managers enabled holistic approaches to complex visualisation challenges.","VirtualArch suffered from fundamental limitations as research software. The project-based structure with a fixed end date meant no provisions for long-term software maintenance or community development. Unlike sustainable archaeological software tools, VirtualArch produced no standalone software packages for distribution, no public code repositories, and no standardised citation mechanisms for software outputs. The absence of version control, systematic testing procedures, or technical documentation beyond academic papers violated basic software engineering practices. Interoperability was limited, with no standardised APIs or data exchange formats. The lack of open-source licensing or clear intellectual property frameworks prevented reuse of components by other researchers. These structural issues ensured technical obsolescence once the project funding ended.","VirtualArch has poor long-term survivability. The absence of ongoing development communities, public code repositories, or institutional commitments beyond the project end date ensures technical obsolescence. Without version control systems, bug tracking, or update mechanisms, even functional applications will gradually fail as operating systems and hardware evolve. The project's legacy exists primarily in academic publications rather than living software tools. No provisions were made for long-term hosting, maintenance, or updates to the applications. The EU project funding model, while supporting initial development, provided no sustainability pathway beyond the project timeframe. Future archaeological technology projects would benefit from planning post-project sustainability from inception, including open-source licensing, public code repositories, and deliberate community building.","Arches, an open-source cultural heritage data management platform, provides robust infrastructure for archaeological projects worldwide with better sustainability. Commercial solutions like Lithodomos VR and Wessex Archaeology Studio offer polished VR experiences for archaeological sites with ongoing technical support. The Archaeological Recording Kit (ARK) provides web-based data collection with active developer communities. QGIS plugins including ArkGrid and ArkSpatial offer GIS functionality specifically for archaeological documentation. The ArcheOS Linux distribution bundles specialised archaeological software in a maintained package. For institutions seeking VR/AR solutions, Acadicus by Arch Virtual provides a platform for creating educational VR content with ongoing development. ArcGIS Online offers professional-grade mapping and visualisation capabilities backed by ESRI's commercial infrastructure. These alternatives demonstrate how archaeological software can achieve long-term sustainability through open-source development models, active communities, and institutional support."
```

---
