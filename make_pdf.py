import pdfkit
import datetime

with open("template.html", "r") as file:
    html_content = file.read()

current_date = datetime.datetime.now().strftime("%d-%b-%Y")
options = {
    "page-size": "A4",
    "margin-top": "1.5cm",
    "margin-bottom": "1.5cm",
    "margin-left": "2cm",
    "margin-right": "1.5cm",
    "encoding": "UTF-8",
    "no-outline": None,
    "quiet": "",
    "footer-right": "[page] of [topage]",
    "footer-left": current_date,
    "footer-font-size": 9,
}

pdfkit.from_string(html_content, "output.pdf", options=options)
