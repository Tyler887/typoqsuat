import os, glob
for i in glob.glob(f"{os.getcwd()}/*.md"):
  with open(i, "w+") as file:
    if i != f"{os.getcwd()}/index.md":
      file.write(f"<a href=\"/typoqsuat\"><small><< Home</small></a>\n{file.read()}")
      print(f"Added home button to {i}")
