import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter

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


class myBibtexParser () :

    def __init__(self, args):
        FILE = args.INPUT
        self.bib_database = self._BibTexParser(FILE)

    def _BibTexParser(self, FILE):
        parser = BibTexParser(interpolate_strings=False)
        # parser.customization = customizations
        with open(FILE) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file, parser = parser)
        return bib_database

    def removeentry(self, key):
        for item in self.bib_database.entries:
            value = item.setdefault(key)
            del item[key]

    def displayentry(self, key):
        for item in self.bib_database.entries:
            value = item.setdefault(key)
            print(value)

    def dump(self, filename):
        with open(filename, 'w') as outputfile:
            bibtexparser.dump(self.bib_database, outputfile)

    def write(self, filename):
        writer = BibTexWriter()
        writer.indent = '    '     # indent entries with 4 spaces instead of one
        with open(filename, "w") as outputfile:
            outputfile.write(writer.write(self.bib_database))
            
