"""Replace content.md's body with a markdown export of the Claude Doc (everything from '# Basics' on).
Usage: python3 sync_from_doc.py <exported.md>   (the editor note at the top of content.md is kept)"""
import os, sys

here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, "..", "content.md")
doc = open(sys.argv[1], encoding="utf-8").read()
cur = open(target, encoding="utf-8").read()
body = doc[doc.index("# Basics"):]
open(target, "w", encoding="utf-8").write(cur[:cur.index("# Basics")] + body.rstrip() + "\n")
print("content.md updated from", sys.argv[1])
