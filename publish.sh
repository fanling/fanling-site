#!/bin/sh
# Push this folder to GitHub; Vercel redeploys on each push.
# Usage: sh publish.sh owner/repo ["commit message"]
# Run build.sh first so site/ is current. Vercel serves site/ as-is (no build step).
set -e
REPO="$1"; MSG="${2:-Update site}"
[ -n "$REPO" ] || { echo "usage: sh publish.sh owner/repo [message]"; exit 1; }
SRC="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
git clone -q "https://github.com/$REPO.git" "$TMP/repo"
cd "$TMP/repo"
git ls-files -z | xargs -0 -r rm -f
tar -C "$SRC" --exclude=.git --exclude-from="$SRC/.gitignore" -cf - . | tar -xf -
git add -A
if git diff --cached --quiet; then echo "No changes."; else
  git commit -q -m "$MSG" && git push -q origin HEAD && echo "Pushed to $REPO"; fi
rm -rf "$TMP"
