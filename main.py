from docx import Document
import re
import datetime
import locale

# Path to the Word document
document_path = r""  # Path to your document
changed_document_path = r""  # Path to the changed document
# Create a new document instance
document = Document(document_path)

pattern = r"\d{2}\.\d{2}(?:\.\d{2})?"

def weekday(datum):
    day, month, *_ = map(int, datum.split('.'))
    year = datetime.datetime.now().year  # uses the current year

    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

    # calculate weekday
    weekday = datetime.datetime(year, month, day).strftime("%A")

    return weekday

def enhance_date_with_weekday(text):
    matches = re.findall(pattern, text)
    for match in matches:
        date = match  # Remove the trailing colon
        weekday_text = f"{date} ({weekday(date)})"
        # Replace the date pattern with the formatted text
        text = text.replace(match, weekday_text)
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

