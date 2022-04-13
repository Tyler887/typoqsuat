# PYSquat: PYthon Typoqsuat

import requests
import yaml
import argparse
import sys

parser = argparse.ArgumentParser(description='View typo entries from Typoqsuat.')
parser.add_argument('entry', type=str,
                    help='entry to view from API')
parser.add_argument('-v', '--verbose', dest='verbose', action='true',
                    help='show more verbose output')
parser.add_argument('-q', '--quiet', dest='quiet', action='true',
                    help='do not print version/copyright messages')

args = parser.parse_args()

if not args.quiet:
  print(f"PYSquat Version 1.0 (Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")
  print("(C) 2022 Tyler887 and contributors. All Rights Reserved.")
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        if r.status_code != 200:
          print(f"error: {url} returned http {r.status_code}")
          sys.exit(1)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

if args.verbose:
  print(f"[VERBOSE] Downloading https://tyler887.github.io/typoqsuat/api/entry/{args.entry}.yaml.")
entryfile = download_file(f"https://tyler887.github.io/typoqsuat/api/entry/{args.entry}.yaml")
if args.verbose:
  print("[VERBOSE] Starting to show data.")
yaml = open(entryfile, "r").read()

dictionary = yaml.full_load(yaml)

if dictionary["digicert"]:
  global digicert
  digicert = "Yes"
else:
  global digicert
  digicert = "No"
print(f"""Domain: {dictionary['domain']}
Server: {dictiomary['server']}
HTTPS: {digicert}
Squatted From: {dictionary['squatted_from']}
Notes: {dictionary['notes_plain']""")
if args.verbose:
  print("[VERBOSE] Exiting.")
