import bibtexparser
from bibtexparser.bparser import BibTexParser


class TestBibtexParser () :

    def setup(self):
        pass

    def test_bibtexparser(self):
        with open('bibtex.bib') as bibtex_file:
            self.bib_database = bibtexparser.load(bibtex_file)
        # print(self.bib_database.entries)

    def test_bparser_BibTexParser(self):
        parser = BibTexParser(common_strings=False)
        parser.ignore_nonstandard_types = False
        parser.homogenise_fields = False

        with open('bibtex.bib') as bibtex_file:
            bibtex_str = bibtex_file.read()
        
        self.bib_database = bibtexparser.loads(bibtex_str, parser)
        # print(self.bib_database.entries)

    def test_dumpstr(self):
        bibtex_str = bibtexparser.dumps(self.bib_database)
        print(bibtex_str)

    def test_dumpbibtexfile(self):
        with open('bibtex_duplicate.bib', 'w') as bibtex_file:
            bibtexparser.dump(self.bib_database, bibtex_file)


if __name__ == '__main__':
    test = TestBibtexParser()
    test.test_bibtexparser()
    test.test_dumpbibtexfile()
