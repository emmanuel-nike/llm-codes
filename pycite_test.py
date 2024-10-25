# from pycite import PyCite
# import json
# from citeproc import CitationStylesStyle, CitationStylesBibliography, formatter
# from citeproc import Citation, CitationItem
# from citeproc.source.json import CiteProcJSON

# # Load the PDF file

# json_input = """
# [
#     {
#         "id": "ITEM-1",
#         "issued": {
#             "date-parts": [[1987,  8,  3],
#                            [2003, 10, 23]]
#         },
#         "title": "Ignore me",
#         "type": "book"
#     },
#     {
#       "id" : "ITEM-2",
#       "page" : "1-7",
#       "type" : "article-journal",
#       "issued" : {
#         "date-parts": [[2006]]
#       }
#     },
#     {
#         "author": [
#             {
#                 "family": "Doe",
#                 "given": "John"
#             }
#         ],
#         "id": "ITEM-3",
#         "issued": {
#             "date-parts": [["1965", "6", "1"]]
#         },
#         "title": "His Anonymous Life",
#         "type": "book"
#     },
#     {
#         "author": [
#             {
#                 "family": "Grignon",
#                 "given": "Cyril"
#             },
#                         {
#                 "family": "Sentenac",
#                 "given": "Corey"
#             }
#         ],
#         "id": "ITEM-4",
#         "issued": {
#             "date-parts": [[2000]]
#        },
#         "type": "book"
#     },
#     {
#         "id": "ITEM-5",
#         "title":"Boundaries of Dissent: Protest and State Power in the Media Age",
#         "author": [
#                 {
#                         "family": "D'Arcus",
#                         "given": "Bruce",
#                         "static-ordering": false
#                 }
#         ],
#         "publisher": "Routledge",
#         "publisher-place": "New York",
#         "issued": {
#             "date-parts":[[2006]]
#         },
#         "type": "book",
#         "URL": "http://www.test01.com"
#     }
# ]
# """

# # Parse the JSON input using json.loads()
# # (parsing from a file object can be done with json.load)

# json_data = json.loads(json_input)


# # Convert citations to CiteProcJSON format
# bib_source = CiteProcJSON(json_data)

# # Load the CSL style for APA
# apa_style = CitationStylesStyle('harvard1', validate=False)

# # Create a bibliography object to format the citations
# bibliography = CitationStylesBibliography(apa_style, bib_source, formatter.plain)

# # Add citations to the bibliography
# citation_list = []
# for citation in json_data:
#     #print(citation)
#     citation_item = CitationItem(citation['id'])
#     citation_list.append(citation_item)
# citation = Citation(citation_list)
# bibliography.register(citation)

# # Generate formatted bibliography
# for item in bibliography.bibliography():
#     print(str(item))

from pycite.pycite import PyCite
from citeproc import CitationStylesStyle, CitationStylesBibliography, formatter
from citeproc import Citation, CitationItem
from citeproc.source.json import CiteProcJSON
from citeproc_styles import get_style_filepath
from citation_parser import CitationParser

# Initialize the Text file paths
input_file_path = './pycite_in.txt'
output_file_path = './pycite_out.txt'

# Initialize PyCite
pycite = PyCite(input_file_path, output_file=output_file_path, show_doi=True)

# Extract citations
raw_citations = pycite.cite()

# Convert the extracted citations to a format compatible with citeproc-py
# This requires the citations to be in a specific JSON structure
citations = []
cp = CitationParser()
for i in range(0, len(citations)):
    citation = cp.parse(raw_citations[i])
    citations.append(citation)
    
bib_source = CiteProcJSON(citations)

# Load the APA style
style_path = get_style_filepath('apa')
apa_style = CitationStylesStyle(style_path, validate=False)

# Create the citation processor
bibliography = CitationStylesBibliography(apa_style, bib_source, formatter.plain)

# Add the extracted citations to the bibliography
for citation in citations:
    citation_item = CitationItem(citation['id'])
    bibliography.register(Citation([citation_item]))

# Generate the formatted bibliography
for item in bibliography.bibliography():
    print(str(item))