# Web Crawler & Link Extraction Tool

A Python-based web crawler that recursively traverses websites, extracts hyperlinks, classifies internal and external URLs, and generates crawl reports for website analysis and data collection.

## Features

* Recursive website crawling.
* Internal and external link extraction.
* URL validation and normalization.
* Duplicate URL detection and prevention.
* Real-time crawl monitoring with color-coded logs.
* Crawl performance measurement and timing analysis.
* Internal and external link statistics generation.
* Export discovered URLs to separate output files.
* Command-line interface for flexible execution.

## Technical Highlights

* Built using Python, Requests, and BeautifulSoup.
* Implemented recursive crawling for automated website traversal.
* Applied URL parsing and normalization using urllib.
* Utilized set-based storage for efficient duplicate detection.
* Generated structured crawl reports with performance metrics.
* Classified discovered URLs into internal and external categories.

## Architecture

```text
Target Website
       │
       ▼
HTTP Request (Requests)
       │
       ▼
HTML Parser (BeautifulSoup)
       │
       ▼
Link Extraction
       │
 ┌─────┴─────┐
 ▼           ▼
Internal   External
 Links      Links
 ▼           ▼
Storage & Reporting
```

## Tech Stack

* Python
* Requests
* BeautifulSoup
* urllib.parse
* Colorama
* Command-Line Interface (CLI)

## Example Output

* Total Internal Links
* Total External Links
* Total URLs Discovered
* Crawl Duration
* Internal Link Report (.txt)
* External Link Report (.txt)

## Use Cases

* Website Structure Analysis
* Link Discovery
* SEO Auditing
* Data Collection
* Research and Web Mining
* Website Integrity Checking

## Future Improvements

* Multi-threaded crawling
* Crawl depth limitation
* Robots.txt support
* URL filtering rules
* Database integration
* Website classification using Machine Learning


Tech Stack :
Python • BeautifulSoup • Requests • URL Parsing • Web Crawling • Data Collection • Command-Line Tools
