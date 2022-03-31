import os, glob, datetime
generated_on = datetime.datetime.now()
if os.path.isfile(f"{os.getcwd()}/map.md"):
  print("Note: Detected existing index. Removing existing index...")
  os.unlink(f"{os.getcwd()}/map.md")
with open(f"{os.getcwd()}/map.md", "w") as index:
  index.write(f"<!-- Do not edit - This is auto-generated by the Python 3 script \"generate-index.py\"! -->\n\nThis is a list of **all entrys** on Typoqsuat. The index was last generated on {generated_on}. Contributors to this site should edit `generate-index.py` to contribute to the list and **not** updating this page.\n")
  old = index.read()
for i in glob.glob(f"{os.getcwd()}/typo/*.md"):
  print(f"Adding to index: {os.path.basename(i)}")
  with open(f"{os.getcwd()}/map.md", "w") as index:
    index.write(f"{old}\n* [Entry file {os.path.basename(i)} in Typoqsuat](/typos/{os.path.basename(i).replace('.md', '.html')})")
                   # ^
                # We need this to prevent the entire index from being overwritten.
    old = index.read()
