from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import as_text


bibtex = """@STRING{ jean = "Jean"}

@ARTICLE{Cesar2013,
  author = jean # { César},
  title = {An amazing title},
  year = {2013},
  month = jan,
  volume = {12},
  pages = {12--23},
  journal = {Nice Journal},
}
"""

bp = BibTexParser(interpolate_strings=False)
bib_database = bp.parse(bibtex)
bib_database.entries[0]
print(as_text(bib_database.entries[0]['author']))
