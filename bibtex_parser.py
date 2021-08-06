import bibtexparser
from bibtexparser.bparser import BibTexParser

from bibtexparser.customization import *

# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record


def BibtexParser(args):
    FILE = args.INPUT

    parser = BibTexParser(interpolate_strings=False)
    parser.customization = customizations

    with open(FILE) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    
    return bib_database
