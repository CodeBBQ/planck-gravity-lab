# Papers

This directory is for local storage of retrieved papers (PDFs, HTML, etc.).

## Git exclusion

**This directory is excluded from Git** (see `.gitignore`).  
Do not commit PDFs or large binary files to this repository.

## Retrieving papers

Every paper in `literature/library.bib` has an arXiv ID and/or DOI.  
Retrieve a paper using one of:

```bash
# arXiv (replace XXXX.XXXXX with the actual ID):
curl -L https://arxiv.org/pdf/XXXX.XXXXX -o papers/XXXX.XXXXX.pdf

# DOI via Unpaywall (open-access only):
# https://unpaywall.org/
```

## Naming convention

Name files using the arXiv ID or a short descriptive label:

```
papers/
  2301.12345.pdf          ← arXiv paper
  nist-codata-2018.pdf    ← reference document
```

Record the local filename in the BibTeX entry in `library.bib` if desired,
but do not rely on local storage — always provide the arXiv ID or DOI so any
contributor can retrieve the paper independently.
