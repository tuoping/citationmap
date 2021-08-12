# -*- coding: utf-8 -*-
import argparse
from bibtex_parser import myBibtexParser

import re

def main () :    
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('INPUT', help='Input bibtex file')
    
    args = parser.parse_args()
    
    bd = myBibtexParser(args)
    bdlist = bd.bib_database.entries
    print("Total num of articles = %d" % len(bdlist))

    bd.removeentry("file")
    bd.removeentry("keywords")
    bd.write("data/bib-refined/"+args.INPUT.split("/")[-1], ("ENTRYTYPE", "year", "author"))

    # keywords = []
    # for item in bdlist:
    #     k = re.split(" |-|{|}|:", item['title'].lower())
    #     keywords.append(k)
    # for item in keywords:
    #     print(item)
    #     print("\n")

if __name__ == "__main__":
    main()
