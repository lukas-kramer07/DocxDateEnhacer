from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
import re
import datetime
import locale

# Path to the Word document
document_path = r"" # Path to your document
changed_document_path = r"" # Path to the changed document
# Create a new document instance
document = Document(document_path)

# Get the 'Heading 3' style
style_heading3 = document.styles['Heading 3 Char']

# Modify the 'Heading 3' style to hide the numbering
xml = '''
        <w:pPr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:numPr>
                <w:ilvl w:val="0"/>
                <w:numId w:val="0"/>
            </w:numPr>
        </w:pPr>
      '''
xml_element = parse_xml(xml)
style_heading3._element.append(xml_element)

pattern = r"\d{2}\.\d{2}:"

def weekday(datum):
    day, month = map(int, datum.split('.'))
    year = datetime.datetime.now().year  # uses the current year

    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

    # calculate weekday
    weekday = datetime.datetime(year, month, day).strftime("%A")

    return weekday

def main():

    for paragraph in document.paragraphs:
        match = re.findall(pattern, paragraph.text)
        print(match)
        if match:
            date = ''.join(match)[:-1]
            print(date)
            paragraph.text = f""
            run1 = paragraph.add_run(f"{date} ({weekday(date)})")
            run1.style = 'Heading 3 Char'
            run = paragraph.add_run(':')




main()

# Save the modified document
document.save(changed_document_path)
