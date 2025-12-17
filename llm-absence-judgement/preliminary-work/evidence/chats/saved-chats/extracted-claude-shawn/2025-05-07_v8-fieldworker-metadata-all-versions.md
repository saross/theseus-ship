# v8-FieldWorker-metadata (all versions)

## Metadata
- **UUID:** `8de379d8-8f55-4033-982b-222b66757567`
- **URL:** https://claude.ai/chat/8de379d8-8f55-4033-982b-222b66757567
- **Date:** 2025-05-07 09:02:07

---

## Conversation

### Human (08:03:22)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow these **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (08:03:26)



I understand completely. I'll be collecting evidence and assembling metadata about research software tools in archaeology, history, and other historical studies disciplines according to the detailed specifications provided.

I'll maintain Australian spelling and punctuation per your preferences and follow the Writing Style Guide to ensure a consistent academic tone throughout the report and CSV output.

For each tool you provide, I'll follow the title convention format of "[Tool Name]: [Primary Function] for [Application Domain]" and conduct thorough research to complete all required metadata fields.

I'm ready to begin with the first tool name or acronym you'd like me to research.

---

### Human (08:03:41)

FieldWorker

---

### Assistant (08:03:46)



I'll research FieldWorker as a research software tool for archaeology/historical studies according to the detailed metadata collection framework you've provided. Let me gather comprehensive information about this tool.
```
This block is not supported on your current device yet.
```

Your FieldWorker archaeological software report is ready. It examines this 1995 Newton MessagePad tool's brief role in digital archaeology, including its GPS integration capabilities, price points ($149-$599+), technical limitations, and minimal adoption. The report analyzes why it remained a historical footnote rather than transforming archaeological practice, and compares it with modern alternatives like FAIMS, Arches, and STRATUM that now dominate digital fieldwork.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (08:56:33)

can you also please generate the CSV?

---

### Assistant (08:57:13)



I'll generate the CSV with all the metadata fields for FieldWorker according to the framework you provided.

```csv
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"FieldWorker","FieldWorker was a mobile data collection tool for the Apple Newton MessagePad that allowed researchers to record field observations with integrated GPS functionality. While not exclusively designed for archaeology, it provided archaeologists with the capability to create custom forms for recording different types of archaeological data in the field, automatically capturing precise GPS coordinates, and later exporting this data to GIS platforms. The software came in three versions with increasing functionality: Basic ($149), Advanced ($599), and Pro (price unspecified). It represented one of archaeology's earliest attempts at digital field recording in the mid-1990s.","FieldWorker was developed by FieldWorker Products Ltd of Toronto and released around 1995 specifically for the Apple Newton MessagePad platform. The software evolved through several versions, with the most thoroughly documented being Advanced (version 2.3.5) and Pro (version 0.91), which were reviewed in Internet Archaeology in 1997. The Pro version was still in pre-release when reviewed. FieldWorker's development effectively ended when Apple discontinued the Newton platform in 1998, making the software obsolete as it was tied exclusively to this hardware. No evidence suggests it was later ported to other platforms, and the company appears to have evolved into a different entity focused on modern mobile data collection but disconnected from archaeological applications.","FieldWorker was built specifically for the Apple Newton platform using NewtonScript and the Newton Toolkit (NTK), which fundamentally limited its longevity and portability. The software implemented a project-based data structure with user-definable screens and fields for customizable data collection. Key technical features included direct integration with GPS receivers via the NMEA 0183 protocol, data synchronization between the Newton device and desktop computers, and export capabilities to various GIS formats including MapInfo and ArcView. The architecture allowed customization of data entry forms with specialized field types appropriate for archaeological recording. Hardware requirements were substantial for the era, requiring an Apple Newton MessagePad (models 120, 130, or 2000), Newton OS 2.0 or later, a compatible GPS receiver supporting NMEA 0183, and optionally a differential beacon receiver for improved GPS accuracy. The Pro version pushed hardware limits, with reviewers recommending the MessagePad 2000 with its 160MHz StrongARM processor. Performance issues were noted in the 1997 review, with operations described as 'treacle' on the MessagePad 130. The software's architecture was inextricably tied to Apple's PDA ecosystem, which proved fatal when Apple discontinued the Newton line in 1998.","2025-05-07","yes","FieldWorker meets all essential criteria for research software: it was designed for a research-specific purpose (field data collection), engaged meaningfully with research data (recording observations with GPS coordinates), and aligned with recognized methodologies (archaeological field recording and GIS integration). It also satisfies multiple supporting criteria: it incorporated domain knowledge through customizable forms, supported the data collection stage of the research lifecycle, transformed data between field notes and GIS formats, and facilitated visualization through mapping capabilities.","","","","https://intarch.ac.uk/journal/issue3/reviews/ryan.html","Proprietary","Data collection|Spatial analysis|Data management","mobile-data-collection|archaeological-recording|gps-integration|newton-platform|historical-technology","1995","1998","Pro 0.91 (1997)","Abandoned","FieldWorker Products Ltd (Toronto)","Unknown","Small (2-5)","Commercial mobile computing","General-purpose","Basic","FieldWorker had limited adoption in archaeology based on available literature. The most comprehensive assessment comes from a 1997 review in Internet Archaeology by Ryan, Pascoe, and Morse. Beyond this review, minimal evidence exists of widespread archaeological use or publications resulting from projects using the software. The prohibitive cost (software: $149-$599, plus hardware: $600-1000 for the Newton MessagePad, $300-15,000 for GPS equipment) likely limited adoption to well-funded projects or institutional early adopters. No citation metrics, download statistics, or community forums exist for this historical software product.","Data Acquisition","research-specific","Stand-alone software","NewtonScript","Apple Newton MessagePad","","FieldWorker could export data to several GIS formats including MapInfo and ArcView. It supported direct integration with GPS receivers using the NMEA 0183 protocol and could synchronize recorded data between the Newton device and desktop computers. The Pro version offered enhanced data structure options compared to the Basic and Advanced versions.","FieldWorker's strengths included: 1) Pioneering integration of GPS data with field notes in a single mobile device, enabling spatial recording of archaeological features. 2) Customizable forms that could be adapted for different types of archaeological recording needs. 3) Multiple data export formats compatible with then-current GIS software like MapInfo and ArcView. 4) A responsive development company that provided regular updates based on user feedback. 5) The capacity to record data digitally in the field, reducing post-fieldwork data entry errors and time.","FieldWorker suffered from several significant weaknesses: 1) Prohibitive cost that limited adoption primarily to well-funded projects (total investment including hardware could exceed $2000 in 1995). 2) Significant performance limitations on available hardware, with reviews describing operation as 'treacle' on the MessagePad 130. 3) Complete dependency on the Apple Newton platform, which was discontinued in 1998, effectively ending the software's viability. 4) Limited archaeological-specific functionality compared to modern purpose-built alternatives. 5) Inadequate documentation and support for archaeological workflows. 6) Challenging synchronization processes and data export procedures that required technical expertise.","FieldWorker had essentially zero long-term survivability due to its complete dependency on the Apple Newton platform, which Apple discontinued in 1998. The software was never ported to other platforms, and the proprietary nature of both the software and the Newton operating system made preservation nearly impossible. The company appears to have evolved into a different entity focused on modern mobile data collection but disconnected from archaeological applications. Today, FieldWorker exists primarily as a historical footnote in the evolution of digital archaeological methods rather than as functioning software. No repositories, archives, or emulation environments are known to preserve it in working condition.","Modern alternatives that have completely supplanted FieldWorker include: 1) FAIMS/Fieldmark: Developed at Macquarie University specifically for archaeological fieldwork with offline capabilities and support for structured, free-text, geospatial, and multimedia data on Android devices. 2) Arches: An open-source heritage management platform with robust GIS integration, developed by the Getty Conservation Institute and World Monuments Fund. 3) ARK (Archaeological Recording Kit): A web-based toolkit developed by L-P Archaeology, adaptable to different recording systems with standards compliance. 4) STRATUM: A newer mobile platform designed 'by archaeologists for archaeologists' with mapping, drawing, and form-filling capabilities. 5) iDig: Developed at the Athenian Agora Excavations for archaeological excavation, with wireless connection to Leica Total Stations and synchronization across multiple iPads."
```

This CSV contains comprehensive metadata for FieldWorker based on thorough research of this historical archaeological software tool. The information covers all required fields including technical specifications, historical context, strengths and weaknesses, and modern alternatives that have since replaced this pioneering but ultimately short-lived tool.

---

### Human (08:58:23)

Please regenerate your Report with **exactly** the same content, but use the following **Title Conventions**:
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (08:59:08)



I'll regenerate the report with the same content using the specified title conventions.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



I've regenerated the report with the same content using the requested title format "[Tool Name]: [Primary Function] for [Application Domain]" and maintaining an academic tone throughout.

The new report title is "FieldWorker: Mobile Data Collection for Archaeological Fieldwork" which precisely describes the tool's primary function and application domain without using sensationalist language.

All the content remains identical - the report still provides a comprehensive analysis of FieldWorker as an early archaeological digital recording tool, including its technical specifications, historical context, limitations, and the modern alternatives that have since replaced it.

---

### Human (09:01:18)

Is it possible to retain the citations / links in the report when you regenerate it?

---

### Assistant (09:02:07)



I understand you'd like to retain the citations/links in the regenerated report. This is definitely possible and important for academic integrity. Let me regenerate the report while preserving all the citations and references.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



I've regenerated the report with all citations preserved using footnotes. The new report maintains:

1. The academic title format: "FieldWorker: Mobile Data Collection for Archaeological Fieldwork"
2. All the original content and analysis
3. Proper citations with footnotes linking to the original sources
4. The same comprehensive assessment of FieldWorker's historical significance in archaeological computing

The footnote format makes the citations more academic and formal while providing clear references to the source materials. Each major claim is supported by a citation to its source, which is essential for scholarly writing about research software tools.

This approach ensures academic credibility while maintaining readability. The footnotes appear at the end of the document with proper formatting and include direct links to the original sources where available.

---
