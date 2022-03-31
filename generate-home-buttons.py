import os, glob
def addhome(page):
   try:
      if os.path.isfile(page):
       with open(page, "a+") as file:
        if page.endswith(".md"):
         file.write(f"\n\n[<sub><< Home</sub>](/typoqsuat)")
         print(f"Added home button to {file}")
        else:
         print(f"Skipped {file}")
      else:
        for i in glob.glob(page):
          addhome(i)
   except:
      pass

for i in glob.glob(f"{os.getcwd()}/*"):
 if i != f"{os.getcwd()}/index.md":
  addhome(i)
