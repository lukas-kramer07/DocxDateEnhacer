from docx import Document
import re
import datetime
import locale

# Path to the Word document
document_path = r"E:\Protokoll 2023.docx"  # Path to your document
changed_document_path = r"E:\test2.docx"  # Path to the changed document
# Create a new document instance
document = Document(document_path)

pattern = r"\d{2}\.\d{2}(?:\.\d{4})?"
def weekday(datum):
    day, month, *year = map(int, datum.split('.'))
    if year:
        year = year[0]
    else:
        year = datetime.datetime.now().year
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

    # calculate weekday
    weekday = datetime.datetime(year, month, day).strftime("%A")

    return weekday

def enhance_date_with_weekday(text):
    matches = re.findall(pattern, text)
    for match in matches:
        print(match)
        date = match 
        weekday_text = f"{date} ({weekday(date)})"
        # Replace the date pattern with the formatted text
        text = text.replace(match, weekday_text)
        print(F"text: {text}")
    return text

def main():
    for paragraph in document.paragraphs:
        if paragraph.runs:
            # Enhance date patterns in the inline text
            for i in range(len(paragraph.runs)):
                paragraph.runs[i].text = enhance_date_with_weekday(paragraph.runs[i].text)

main()

# Save the modified document
document.save(changed_document_path)

