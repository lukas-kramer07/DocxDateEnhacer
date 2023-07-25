# DocxDateEnhancer

DocxDateEnhancer is a Python script that enhances date patterns in a .docx document by adding the corresponding weekdays to each date. The script uses regular expressions and the `python-docx` library to identify date patterns and then calculates the weekdays for those dates.

## Requirements

- Python 3.x
- `lxml` (version 4.9.3 or later)
- `python-docx` (version 0.8.11 or later)

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository or download the `main.py` script to your local machine.
2. Ensure you have a .docx document (`your_document.docx`) with date patterns in the format "dd.mm" or "dd.mm.yy" (with optional year).
3. Modify the `document_path` and `changed_document_path` variables in `main.py` to specify the path to your input document and the desired output document path, respectively.
4. Run the script using the following command:

```bash
python main.py
```

The script will process the .docx document and enhance the date patterns with the corresponding weekdays. The modified document will be saved at the specified `changed_document_path`.

## Example

Consider the following input paragraph in the .docx document:

```
On 01.01.2023, they announced their debut.
The concert will take place on 15.08.2023.
```

After running the script, the paragraph will be modified to:

```
On 01.01.2023 (Sunday), they announced their debut.
The concert will take place on 14.08 (Saturday).
```

The script adds the weekday "(Sunday)" to the date "01.01.2023" as well as ("Saturday") to the date "14.08" in the paragraph.

