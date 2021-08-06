from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

db = BibDatabase()
db.entries = [
    {'journal': 'Nice Journal',
     'comments': 'A comment',
     'pages': '12--23',
     'month': 'jan',
     'abstract': 'This is an abstract. This line should be long enough to test\nmultilines...',
     'title': 'An amazing title',
     'year': '2013',
     'volume': '12',
     'ID': 'Cesar2013',
     'author': 'Jean César',
     'keyword': 'keyword1, keyword2',
     'ENTRYTYPE': 'article'}]

writer = BibTexWriter()
writer.indent = '    '     # indent entries with 4 spaces instead of one
# writer.comma_first = True  # place the comma at the beginning of the line
with open('bibtex_writer.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))
