# htmltoc archaeological tool

## Metadata
- **Conversation ID:** `6813d3e3-35bc-800c-8653-cf04298a2032`
- **Created:** 2025-05-01 22:04:51
- **Updated:** 2025-12-07 21:39:55
- **Default Model:** `o3`
- **Project ID:** `g-p-682fbda4eb1c819180b176f6de9d9cd8`
- **Source:** Official ChatGPT Export

---

## Conversation

### Human (22:04:50)

Hi ChatGPT, can you tell me anything about the archaeological software tool 'htmltoc'

---

### Assistant (22:07:08) [Model: o3]

**In brief:** *htmltoc* is a lightweight command-line utility that scans one or more HTML files, inserts anchors where necessary, and emits a hierarchically-nested, hyper-linked “Table of Contents” (ToC).  Written in Perl by Earl Hood in July 1994, later absorbed into Norman Ramsey’s *noweb* literate-programming tool-chain and packaged by most GNU/Linux distributions, it became a quiet work-horse of early digital-archaeology publishing—most visibly in the production pipeline of *Internet Archaeology* from Issue 2 (1997) onward.  Although development ceased two decades ago, the script is still shipped with *noweb* and remains handy when archaeologists need to retrofit legacy excavation pages with navigable structure or to post-process HTML emitted by tools such as Pandoc.

---

## 1  Origins and historical context  

| Year | Milestone | Notes |
|------|-----------|-------|
| **1994** | Hood posts the first public release to comp.infosystems.www and the W3C “Tools” archive citeturn8view0 | Implements a *tocmap* file, `-inline`, `-header`, `-footer`, etc. |
| **1994-96** | Bundled into the *perlWWW* and *txt2html* ecosystems | *txt2html*’s README recommends running `htmltoc` after conversion citeturn13search0 |
| **1997** | Adopted (with local tweaks) by *Internet Archaeology* to automate navigation bars and per-paper ToCs citeturn9view0 | Used alongside `pnuts` and `htmlfig` |
| **1999-2001** | Norman Ramsey rewrites/slims it for the *noweb* pipeline; included in *noweb 2.11b* and documented in a manpage citeturn10view0 |
| **2008** | An Icon re-implementation appears in the CTAN mirror, again attributed to Ramsey’s original citeturn16view0 |
| **2000s-present** | Shipped by Debian/Ubuntu inside *noweb* and via the dedicated `libhtml-toc-perl` module citeturn14search2turn14search0 |

---

## 2  How the script works  

### 2.1 Input parsing  
*htmltoc* tokenises the HTML, looks for heading tags (`<H1>`–`<H6>` by default), and—if a heading lacks an `id`/`name` anchor—inserts one whose value is prefixed `xtocid-n`.  The headings and their levels are cached in memory to build the ToC structure.  If the user provides a **toc-map** file, arbitrary elements (e.g. `<DT>`, `<DIV class="context">`) can be treated as “significant”. citeturn8view0  

### 2.2 Output modes  

| Option | Effect |
|--------|--------|
| `-toc file` | Write ToC to *file* (stdout if omitted). |
| `-inline` | Insert the generated ToC between the markers `<!--tableofcontents-->` and `<!--/tableofcontents-->` inside the original file. |
| `-ol` / `-ul` (implicit) | Render the first-level list as `<OL>` or `<UL>`. |
| `-prefix STR` | Change anchor prefix (defaults to `xtocid`). |
| `-textonly` | Strip embedded markup from heading text. |

The *noweb* workflow pipes the prettified HTML produced by `noweave` straight through `htmltoc`:  

```bash
noweave -filter l2h -index -html diary.nw | htmltoc -inline > diary.html
```  

(This example is lifted verbatim from *Noweb* documentation citeturn15search3.)

### 2.3 Known limitations  

* The noweb edition only recognises headings on a **single physical line**—multi-line tags are ignored citeturn10view0.  
* It is HTML 4-oriented; headings introduced via ARIA-role or `<header>` sectional markup are missed.  
* No built-in Unicode normalisation; projects containing non-ASCII IDs may need a wrapper script.

---

## 3  Why archaeologists cared  

Digital excavation reports and research articles often sprawl over dozens of screens, each with nested sub-sections for context descriptions, finds catalogues, compositional analyses, GIS exports, and appendix data.  When *Internet Archaeology* launched in 1996, hand-maintaining inter-page navigation quickly became unviable.  Their 1997 editorial explains that a “modified version” of *htmltoc* let editors choose which heading levels to expose, auto-link anchors, and regenerate every ToC en-masse whenever a page changed citeturn9view0.  

The same need recurs in contemporary fieldwork portals: static-site generators (Hugo, Jekyll) will happily spit out raw HTML from Markdown, but if your HTML originates elsewhere—say, from a bespoke MS Access-to-HTML export of unit sheets—*htmltoc* is still the fastest way to add navigability without re-tooling the whole pipeline.

---

## 4  Obtaining and installing  

| Platform | Package / Command |
|----------|------------------|
| Debian/Ubuntu | `sudo apt-get install noweb` (installs `/usr/bin/htmltoc` and its manpage) citeturn10view0 |
| Fedora / RHEL | `dnf install noweb` |
| Any OS with Perl 5 | Download the original 1994 release or the slimmer “noweb” script, mark executable, and place on `$PATH`. |
| Programmatic use | `cpan install HTML::Toc` for a fully-OO Perl module with update-in-place features citeturn14search0 |

---

## 5  Strengths, weaknesses, and survivability  

| ✔︎ Strength | ✖︎ Weakness / Risk |
|------------|-------------------|
| **Tiny footprint** (≈250 LOC) and zero non-core dependencies. | Not HTML5-aware; will not detect `<section>`-based outlines. |
| Works as a pure filter—easy to place inside `make` or CI pipelines. | Generates opaque anchor IDs (`xtocid3`) that impede semantic linking. |
| Retains authors’ hierarchy choices (through *toc-map*). | Project effectively unmaintained; bug fixes rely on community forks (e.g. `hacks-website/htmltoc`) citeturn13search1. |

---

## 6  Modern alternatives and interoperability  

* **Pandoc** `--toc` flag—ideal when your source is Markdown/Word but not when you start with raw HTML.  
* **HTML::GenToc** Perl module—handles multi-line headings, supports insertion or external files, and is maintained in Debian citeturn14search8.  
* **Static-site generators** (Jekyll, Hugo, Quarto): built-in ToC generation but require reformatting source.  
* **JavaScript client-side TOCs** (e.g. Tocbot) avoid build-time steps but increase load time and can break under CSP.

---

## 7  Take-aways for archaeological practice  

1. *htmltoc* remains a quick, scriptable fix for legacy excavation pages or exported datasets that lack navigational aids.  
2. For born-digital workflows, modern markdown-centric or CMS-native ToC features are preferable, but having *htmltoc* on hand is valuable when external collaborators send “messy” HTML dumps.  
3. If reproducibility is paramount (e.g. publishing code + narrative with *noweb* or org-mode), piping through *htmltoc* keeps the build fully deterministic and free of browser-side dependencies—a virtue for digital preservation.

---

## Further reading  

* Hood, E. “ANNOUNCE: Table of Contents Generator for HTML.” Usenet posting, 21 July 1994. citeturn8view0  
* Vince, A. “Editorial: Automation of paper production.” *Internet Archaeology* 2 (1997). citeturn9view0  
* Ramsey, N. *htmltoc(1) manpage*, *noweb 2.11b* (2001). citeturn10view0  
* “Noweb,” *Wikipedia*, rev. Jan 2025—example pipeline with `htmltoc`. citeturn15search3  
* Debian Package `libhtml-toc-perl`, description and file list. citeturn14search0turn14search4  
* *txt2html* README: suggestion to use `htmltoc` for post-processing. citeturn13search0  
* `hacks-website/htmltoc`—community fork with minor fixes. citeturn13search1  
* CTAN Icon port *htmltoc.nw* (2008) for non-Perl environments. citeturn16view0  

---

**Bottom line:** if you need a no-frills, build-time Table of Contents for archaeological web material—especially legacy HTML or output from literate-programming notebooks—install *noweb* (or grab the script), add `| htmltoc` to your pipeline, and move on to the next trench.

---
