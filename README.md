# Grigorios Loukides — academic website

Static, responsive website for GitHub Pages. No installation, framework, tracking, or runtime API calls.

## Publish

In this repository, open **Settings → Pages**. Select **Deploy from a branch**, **main**, **/(root)**, then **Save**.

Expected URL after GitHub finishes deployment:
https://grigorios-loukides.github.io/

## Contents

- King's College London biography, LinkedIn portrait, research themes and sourced academic service roles.
- 131 displayed bibliographic records: 126 DBLP records plus 6 PubMed additions, minus the excluded thesis (18 PubMed records total; 12 overlaps).
- 20 visible Google Scholar entries matched to existing records. Scholar access was partial; the site does not claim complete Scholar coverage or display stale citation metrics.
- Search by title/author/venue; filters by year, type and source; BibTeX exports; static HTML fallback without JavaScript.

## Maintain

Edit `data/publications.json` and/or `template.html`, then run `python3 build.py` and commit the changed files. Publication metadata is HTML-escaped. All asset links are relative, so project Pages paths work.

`data/dblp.json`, `data/pubmed.json`, and `data/scholar.json` retain source records or matched source titles. `data/coverage.json` documents retrieval limitations and reconciliation. Source retrieval date: 20 October 2026. The Google Scholar observation came from an older indexed snapshot, not a fresh complete export.

Deduplication joins unambiguous normalized titles with compatible publication years. Conference, journal, preprint, book/chapter and correction records remain distinct. The total is a count of records, not unique research contributions. Author identity was checked using full names, subject matter, affiliations, and ORCID 0000-0003-0888-5061. PubMed's abbreviated G. Loukides record was cross-checked against its DBLP title.

Profile: https://www.kcl.ac.uk/people/grigorios-loukides
DBLP: https://dblp.org/pid/96/4724
PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Loukides+G%5BAuthor%5D
Scholar: https://scholar.google.com/citations?user=OtmncdQAAAAJ

Portrait remains credited to King's College London; no blanket license is asserted over third-party material.

Academic service: ICDM programme committee service since 2011 is confirmed by the author; linked committee archives document individual editions. Other listed roles link to conference, publisher, institutional, or organiser announcements. CIKM is omitted at the author’s request.

Portrait updated from the public LinkedIn profile image served on [Grigorios Loukides’ post](https://www.linkedin.com/posts/grigorios-loukides-78ba065_humbled-to-receive-the-faculty-of-natural-activity-7274537849201262594-fSMI). The image is embedded locally to avoid a dependency on expiring LinkedIn image URLs.
