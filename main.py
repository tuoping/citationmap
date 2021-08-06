# -*- coding: utf-8 -*-
import argparse
from bibtex_parser import BibtexParser

import re

def main () :    
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('INPUT', help='Input bibtex file')
    
    args = parser.parse_args()
    
    bd = BibtexParser(args)
    bdlist = bd.entries
    print("Total num of articles = %d" % len(bdlist))
    numfulltext = 0
    numsnapshot = 0
    for item in bdlist:
        try:
            item.pop("file")
        except:
            continue

    keywords = []
    for item in bdlist:
        k = re.split(" |-|{|}|:", item['title'].lower())
        keywords.append(k)
    for item in keywords:
        print(item)
        print("\n")

if __name__ == "__main__":
    main()
