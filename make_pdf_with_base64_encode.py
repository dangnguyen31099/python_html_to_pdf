import pdfkit
import io, os, base64, tempfile

temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_path = temp_file.name


with open("template.html", "r") as file:
    html_content = file.read()

options = {
    "page-size": "A4",
    "margin-top": "1.5cm",
    "margin-bottom": "1.5cm",
    "margin-left": "2cm",
    "margin-right": "1.5cm",
    "encoding": "UTF-8",
    "no-outline": None,
    "quiet": "",
}

pdfkit.from_string(
    html_content,
    temp_file_path,
    options=options,
)
temp_file.close()

with open(temp_file_path, "rb") as file:
    pdf_base64 = base64.b64encode(file.read()).decode("utf-8")

os.remove(temp_file_path)

with open("base64.txt", "+w") as file:
    file.write(pdf_base64)
