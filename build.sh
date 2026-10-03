#!/bin/sh
# Rebuild the portfolio PDF and the static site from content.md.
set -e
cd "$(dirname "$0")/src"
python3 portfolio.py portfolio.html
node render.js portfolio.html ../../gsd-application/portfolio/LingFan_GSD_Portfolio_draft.pdf
rm -rf ../site && python3 site.py ../site
echo "Built: ../gsd-application/portfolio/LingFan_GSD_Portfolio_draft.pdf and site/"
