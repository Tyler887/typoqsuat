import os, glob
from colorama import *
def addhome(page):
   try:
      if os.path.isfile(page):
       with open(page, "a+") as file:
        if page.endswith(".md"):
         file.write(f"\n\n[<div align=\"center\"><sub><i><< Back to home...</i></sub></div>](/typoqsuat)")
         print(f"{Fore.GREEN}Added{Style.RESET_ALL} home button to {file}!\n")
        else:
         print(f"{Fore.YELLOW}Skipped{Style.RESET_ALL} {file}.\n")
   except:
      pass

for i in glob.glob(f"{os.getcwd()}/*"):
 if i != f"{os.getcwd()}/index.md":
  addhome(i)
print(f"{Fore.BLUE}>>>{Style.RESET_ALL} Generating home buttons for entries.")

for i in glob.glob(f"{os.getcwd()}/typo/*"):
  addhome(i)

print("Generated home buttons!")
