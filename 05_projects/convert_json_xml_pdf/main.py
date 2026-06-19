# https://youtu.be/Kbj9vPljsnE
# https://pypi.org/project/pdfitdown/


from pathlib import Path

from pdfitdown.pdfconversion import Converter

converter = Converter()


converter.convert(file_path=str(Path("users.json")),
                  output_path=str(Path("json.pdf")))

converter.convert(file_path=str(Path("users.xml")),
                  output_path=str(Path("xml.pdf")))
