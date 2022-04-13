import os, glob
from colorama import *
def addhome(page, entry=False):
   try:
      if os.path.isfile(page):
       with open(page, "a+") as file:
        if page.endswith(".md"):
         if entry:
          file.write(f"\n\n[<sub><i><< Back to home...</i></sub>](/typoqsuat) <sub>|</sub> [<sub><i>YAML source...</i></sub>](https://github.com/Tyler887/typoqsuat/blob/main/api/entry/{os.path.basename(page).replace('.md','.yaml')})")
         else:
          file.write(f"\n\n[<sub><i><< Back to home...</i></sub>](/typoqsuat)")
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
  addhome(i, entry=True)

print("Generated home buttons!")
