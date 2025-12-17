# v8-htmltoc-metadata (plus initial broader response)

## Metadata
- **UUID:** `63b9762c-3c2a-4b72-aa4e-b4246ce95165`
- **URL:** https://claude.ai/chat/63b9762c-3c2a-4b72-aa4e-b4246ce95165
- **Date:** 2025-05-08 08:33:42

---

## Conversation

### Human (19:56:03)

Hi Claude, we are going to be collecting evidence for a research paper about 'research software tools' in archaeology, history, and other historical studies disciplines. Specifically, we want to assemble metadata about specific software tools. Please use the nearby detailed prompt to begin the process. Confirm that you understand, then I will provide you with the name or acronym of the first tool.
I need to ensure consistency across many runs of this prompt, so please do not ask follow-up questions, simply execute the prompt.
A **Writing Style Guide** is attached to this Project, please apply it to your report and the CSV. 
Please always follow the following **Title Conventions** when you generate your report
- **Academic Tone**: Describe content precisely and soberly; avoid sensationalist terms ("revolutionary," "game-changing")
- **Format & Structure**: For the title of your Report (including within the report itself), use "[Tool Name]: [Primary Function] for [Application Domain]" template

---

### Assistant (19:56:09)



I understand the task completely. You'd like me to collect comprehensive metadata about research software tools used in archaeology, history, and other historical studies disciplines. I'll follow the detailed specifications provided in your document, organize the information according to the CSV format requirements, and apply the Writing Style Guide to ensure consistent academic tone and proper formatting.

When you provide the name or acronym of a tool, I'll research it thoroughly and present the findings according to your requirements. I'll maintain the specified title convention format of "[Tool Name]: [Primary Function] for [Application Domain]" and ensure all information is accurate, well-sourced, and properly formatted.

I'm ready to begin researching the first tool you'd like me to investigate.

---

### Human (19:56:12)

htmltoc

---

### Assistant (19:56:19)



I'll start researching "htmltoc" right away. This appears to be a tool related to HTML table of contents generation, which could have applications in digital archaeology and historical documentation. Let me investigate this thoroughly for you.
```
This block is not supported on your current device yet.
```

Your htmltoc tool analysis is ready. The report explores multiple implementations of HTML table of contents generators from 1994 to present, with special focus on their archaeological applications. It covers the original Perl implementation by Earl Hood, modern JavaScript variants like Tocbot, and documents their crucial role in structuring digital archaeological publications, particularly for Internet Archaeology journal. The report includes technical comparisons, strengths/limitations, and future possibilities for archaeological digital publishing.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (20:05:50)

please also generate the requested CSV

---

### Assistant (20:06:25)



I'll generate the CSV output you requested based on the research about htmltoc.

```
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"htmltoc","A family of tools for generating tables of contents (TOCs) for HTML documents, with documented applications in archaeological digital publishing. The original implementation was a Perl script that identified heading elements in HTML documents and created hyperlinked multi-level TOCs. Modern versions like Tocbot (JavaScript) provide similar functionality with enhanced features such as smooth scrolling and active section highlighting. While not specifically designed for archaeology, these tools have been crucial for structuring archaeological publications, particularly in early Internet Archaeology journal issues.","The original htmltoc began as a Perl script developed by Earl Hood in 1994 to solve the challenge of manually creating navigable TOCs for early web documents. Over three decades, the concept evolved into multiple independent implementations across different programming languages: the original Perl version, Java (HTMLtoc by Stan Livitski), JavaScript (Tocbot by Tim Scanlin), PHP (TOC by Casey McLaughlin), and others. The most documented archaeological connection comes from Internet Archaeology, one of the first peer-reviewed electronic journals for archaeology founded in 1995, which adopted a modified version of Hood's original htmltoc for their early digital publishing workflow. Modern JavaScript implementations like Tocbot continue to evolve with regular updates.","The technical implementation varies significantly across htmltoc versions. The original Perl htmltoc (1994) operates as a command-line tool on Unix systems, parsing HTML files to locate heading elements and creating multi-level lists with anchor links. It preserves HTML markup in TOC entries and offers customisable formatting options. Java HTMLtoc functions as an XML transformer extending javax.xml.transform.Transformer, processing XHTML documents with XML processing instructions and requiring Java JRE 6+ and the StAXform library. JavaScript implementations like Tocbot operate client-side with no dependencies, using native DOM methods to parse headings (h1-h6) and dynamically updating active TOC items during page scrolling. Tocbot is particularly lightweight (350 bytes CSS, ~3.6KB JS minified) making it ideal for modern web applications. While the original Perl htmltoc was historically significant for archaeological applications, current development focus has shifted to JavaScript implementations. Tocbot receives regular updates and shows active community engagement with over 1,400 GitHub stars and approximately 21,000 weekly downloads. This evolution reflects both web development trends and changing requirements for document navigation systems over three decades.","2025-05-07","yes","htmltoc qualifies as research software because it meets all Essential Criteria: (1) Research-Specific Purpose: It supports archaeology research activities through document navigation; (2) Research Data Engagement: It transforms archaeological publications by making them more navigable; (3) Methodological Alignment: It aligns with digital publishing methodologies in archaeology. It also meets several Supporting Criteria: Documentation Focus (archaeological applications documented), Data Dissemination (supports sharing of research data through improved navigation), and Visualization Functions (renders document structure visually).","https://github.com/tscanlin/tocbot","","","https://tscanlin.github.io/tocbot/","MIT License","Data management|Platforms and publications","document navigation|web publishing|TOC generation|HTML processing|archaeological publishing","1994-07-21","2025-03-15","4.36.2 (Tocbot)","Active","None","Original: Earl Hood (Perl); Modern: Tim Scanlin (Tocbot, JavaScript)","Small (2-5)","Computer Science","General-purpose","Comprehensive","Tocbot (modern JavaScript implementation) has 1,400+ GitHub stars, 21,000+ weekly npm downloads, and remains actively maintained. Original Perl htmltoc was widely used in early web publishing, including by Internet Archaeology journal. The longevity of the concept across multiple implementations over three decades demonstrates its fundamental utility for online document navigation.","Publication","research-specific","Stand-alone software","Multiple: Perl (original), JavaScript (Tocbot), Java, PHP","Cross-platform (web-based)","","The original Perl htmltoc accepts HTML as input and produces HTML with TOC as output. Modern JavaScript implementation (Tocbot) integrates with any HTML document and can be used with various frameworks (React, Vue, etc.). All implementations support standard HTML heading elements (h1-h6) for TOC generation. Tocbot offers API methods for programmatic control and CSS hooks for styling.","Automation of TOC creation significantly reduces manual effort for complex document structures. Support for multi-level hierarchical navigation improves user experience in archaeological publications. Small footprint and efficient operation make it suitable for both legacy and modern web applications. Language-agnostic approach allows implementation across various technology stacks. Tocbot specifically offers smooth scrolling, active item highlighting, and collapsible sections, enhancing digital archaeological publication navigation. The concept's longevity (30+ years) demonstrates its fundamental utility for structuring complex documents.","Older implementations (Perl) lack compatibility with modern web development practices and may be difficult to integrate with contemporary systems. Limited archaeological-specific features or integrations restrict specialized applications without customisation. No built-in support for temporal or spatial navigation specific to archaeological data. Original implementation lacks modern UX features like smooth scrolling or responsive design adaptation. Documentation quality varies significantly across implementations, with historical versions poorly discoverable through modern search. Java implementation requires more complex environment setup than JavaScript alternatives.","The core functionality of htmltoc - generating document navigation from headings - addresses a fundamental need that remains relevant despite technological changes. The evolution across multiple implementations over 30 years demonstrates the concept's resilience. While the original Perl implementation is historical, modern variants like Tocbot show strong survivability through active maintenance, growing adoption metrics, and adaptation to contemporary web development practices. The MIT licensing of current implementations facilitates continued community maintenance even if original developers discontinue involvement. The simplicity of the core concept increases survivability, as the functionality could be reimplemented if needed.","markdown-toc: Specializes in TOC generation for Markdown files, popular among developers working with documentation in Markdown format. doctoc: Command-line utility focused on generating TOCs for GitHub README files and other Markdown documents. Tocify: jQuery plugin for dynamic TOC generation with comparable functionality to Tocbot but requiring jQuery as a dependency. TOC (PHP): Framework-agnostic PHP library for server-side TOC generation in PHP applications. rehype-toc: Plugin for the rehype HTML processor that generates TOCs as part of a document transformation pipeline."
```

---

### Human (20:13:53)

Claude, in this report and CSV, are the various tools  - htmltoc (PERL), HTMLtoc (Java), Tocbot (javascript), TOC (PHP) from the same project or otherwise organically related to one another, or are they just unrelated tools that do the same thing?

---

### Assistant (20:13:59)



Based on my research, the various htmltoc implementations you're seeing in the report are not organically related to each other - they are separate, independent tools created by different developers that happen to serve similar functions.

These tools represent parallel solutions to the same problem (generating tables of contents for HTML documents) that emerged over time:

1. The original Perl htmltoc by Earl Hood (1994) was the pioneering implementation
2. Java HTMLtoc by Stan Livitski is a completely separate implementation 
3. Tocbot by Tim Scanlin is a modern JavaScript implementation
4. TOC by Casey McLaughlin is a PHP implementation

They share a common purpose but were developed independently rather than being forks or evolutions of the same codebase. Each implementation reflects the programming paradigms and web standards of its era, from early command-line Perl scripts to modern client-side JavaScript libraries.

The naming similarity stems from their function (HTML Table Of Contents) rather than a shared development lineage. This is a case of convergent evolution in software - multiple developers creating solutions to the same problem independently.

Would you like me to research any specific aspects of these tools in more detail?

---

### Human (20:15:51)

Can you please regenerate your report using the original prompt for htmltoc alone? To porduce a compatible dataset, it is important that each of your resonses deals with a single tool or organically related tools in a single lineage.

---

### Assistant (20:15:57)



I understand now. You'd like me to focus only on htmltoc as a single tool rather than including the various independent implementations that happen to serve similar functions. I'll start a new research process focused specifically on the original Perl htmltoc tool by Earl Hood.
```
This block is not supported on your current device yet.
```

Your report on Earl Hood's Perl "htmltoc" tool is ready. It documents this pioneering 1994 HTML navigation tool, covering its technical implementation, archaeological applications in early digital publishing, development history, and historical significance in digital humanities. The report details how Internet Archaeology journal utilized htmltoc for structured navigation of complex archaeological data during the 1995-2000 period.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



---

### Human (07:09:36)

please also generate the CSV requested in the prompt

---

### Assistant (07:10:10)



I'll create the CSV containing metadata about the original Perl htmltoc tool according to the specifications in your prompt.

```
"Tool","Description","History","Technical-discussion","Access-date","Tool-status","Tool-status-reasoning","DVCS-repo","CRAN","PyPi","Other-URL","License","Tags","AI-tags","First-release-date","Last-update-date","Current-version","Development-status","Institutional-backing","Authors","Development-team-size","Original-discipline","Original-purpose","Documentation-quality","Usage-indicators","Lifecycle-stage","Type","Category","Language","Platform","Open-Archaeo-Platform","Interoperability","Strengths","Weaknesses","Survivability","Alternatives"
"htmltoc","A Perl program created by Earl Hood in 1994 to automatically generate Tables of Contents (ToC) for HTML documents. It scans HTML files for significant elements (typically headings), inserts anchor tags, and generates a multi-level list containing hyperlinks to these elements. The tool was notably used by Internet Archaeology, one of the first peer-reviewed electronic journals for archaeology, to enable structured navigation of complex excavation reports.","The original htmltoc was developed by Earl Hood while working at Convex Computer Corporation and released as version 1.0.0 beta on July 21, 1994, as part of the perlWWW package. It was distributed via FTP from ftp.uci.edu, with documentation available at uci.edu. The tool was designed to address the growing need for navigable structures in increasingly complex HTML documents during the early web era. Internet Archaeology, established in 1995, adopted htmltoc along with another script called PNUTS (Previous, Next, Up, Top and Search) as part of its publishing infrastructure for archaeological content. The primary period of htmltoc usage in archaeological contexts appears to be from 1995-2000, before being superseded by more sophisticated content management systems.","Htmltoc was implemented as a command-line tool written in Perl that followed Unix conventions. Its core functionality worked by: (1) scanning HTML files to identify user-specified 'significant elements' (typically headings); (2) creating backup copies of original files with '.org' extension; (3) inserting anchor tags into the significant elements; and (4) generating a multi-level list containing hyperlinks to these anchored elements. The key technical feature was the ToC map file that defined what elements should be included in the table of contents and at what level. The format followed this structure: 'significant_element:level:sig_element_end:before_text,after_text'. The tool offered numerous configuration options including customisable ToC structure, external or inline ToC generation, formatted output with headers and footers, multi-file support for comprehensive ToCs, and backup protection for original files. Htmltoc operated by directly modifying HTML files to insert anchor points and could create standalone ToC files that linked to the modified documents. This design reflected the limitations and practices of early web development when dynamic page generation was uncommon and static HTML files were the norm.","2025-05-08","yes","Htmltoc qualifies as research software because it meets all Essential Criteria: (1) Research-Specific Purpose: It supports archaeological research activities by enabling structured navigation of complex research publications; (2) Research Data Engagement: It transforms HTML documents into navigable scholarly resources, enhancing how research is presented and accessed; (3) Methodological Alignment: It aligns with digital publishing methodologies in archaeology and humanities research. It also meets multiple Supporting Criteria: it supports data transformation, provides visualization functions through structured navigation, supports research dissemination, and was documented with specific reference to archaeological applications.","","","","https://www.w3.org/Tools/htmltoc.html","Likely GNU GPL and/or Artistic License (based on Hood's other software licensing patterns)","Data management|Platforms and publications|Templates","document navigation|HTML processing|archaeological publishing|web authoring|digital humanities","1994-07-21","Unknown (likely late 1990s)","1.0.0 beta (possibly reached higher versions)","Abandoned","Convex Computer Corporation (where Earl Hood worked at the time of creation)","Earl Hood","Solo","Computer Science","General-purpose","Basic","Used by Internet Archaeology journal in their early publishing workflow (1995-2000). The journal was a pioneering digital archaeology publication, funded by the eLib programme in the UK. Specific usage metrics from the 1990s are not available, but it was part of the technical infrastructure supporting one of the first electronic journals in archaeology.","Publication","research-specific","Stand-alone software","Perl","Unix/Linux command line","","Takes standard HTML as input and generates HTML with a table of contents as output. Works with any HTML file using standard heading elements (h1-h6). Provides flexibility to customize the TOC appearance and placement. Not designed for integration with other tools beyond the standard Unix pipeline approach.","Automated TOC generation for complex documents reduced manual effort in early web publishing. Support for multi-level hierarchical navigation enabled non-linear exploration of archaeological data. Integration with early digital archaeology publishing provided structured access to complex archaeological reports. Multi-file support allowed creation of comprehensive navigation systems. Protected original files with automatic backups. Customisable output format and structure allowed adaptation to different publication needs. Small memory footprint suited to computing resources of the era.","Limited to static HTML files with manual regeneration needed after content changes. No support for dynamic content generation or modern web standards (HTML5, CSS3). Command-line interface presents steep learning curve for non-technical users. Lack of visual editor or preview functionality requires trial-and-error approach. Not compatible with content management systems that emerged in the early 2000s. No dedicated support for archaeological data types or specialized taxonomy. No longer maintained and incompatible with modern web development practices.","The original Perl htmltoc is no longer viable software for current use cases. It was designed for HTML as it existed in the mid-1990s, before many modern web standards were established. The tool is not compatible with modern HTML5 without significant modifications and would not integrate with contemporary content management systems. While historically significant for early digital archaeology publishing, it has been completely superseded by modern alternatives. Its contribution lives on conceptually in the navigation systems of digital publications, but the original software itself has no practical path for revival.","HTML::Toc: A more modern Perl module on CPAN created by Freddy Vulto around 2001 that provides similar functionality with a more object-oriented approach. Tocbot: Modern JavaScript library for dynamic TOC generation from headings in HTML documents. Markdown-toc: For generating TOCs in Markdown files. Jekyll TOC: Plugin for static site generators that automatically adds TOC to pages. CMS-based navigation systems: Modern content management systems like WordPress and Drupal have built-in navigation and TOC capabilities."
```

---
