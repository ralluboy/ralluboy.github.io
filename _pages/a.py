#!/usr/bin/env python3
import sys
from pprint import pprint
import yaml

rows = None
with open(sys.argv[1]) as fh:
    rows = fh.read().split("\n")

ii = 1
lst = []
for r in rows:
    if r and not r.startswith('search') and not r.startswith('id'):
        c = r.split(',')
        print(ii, c[0], c[1])
        ii += 1
        lst.append({
            "id": c[0],
            "title": c[1],
            "link": c[-2],
        })

patents = {'patent_list': lst}
yaml.safe_dump(patents)


# with open("../_data/patents.yml", "w") as fh:
    # fh.write(yaml.safe_dump(patents))
