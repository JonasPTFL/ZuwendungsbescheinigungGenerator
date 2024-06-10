from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader
import os
from number_to_german_word import number_to_german_word

# Define paths
temporary_text_pdf_filename = "./../text.pdf"


def merge_pdfs(template_path, text_pdf_path, output_path):
    # Read the template PDF
    template_pdf = PdfReader(template_path)
    output_pdf = PdfWriter()

    # Read the text PDF
    text_pdf = PdfReader(text_pdf_path)

    template_page = template_pdf.pages[0]
    text_page = text_pdf.pages[0]
    template_page.merge_page(text_page)
    output_pdf.add_page(template_page)

    # Write the merged PDF to a new file
    with open(output_path, "wb") as f:
        output_pdf.write(f)


def create_pdf_from_member_data(name, address, location, value, date, template_filename, output_filename):
    # create pdf canvas
    c = canvas.Canvas(temporary_text_pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 12)

    # name und anschrift
    c.drawString(50, 677, name)
    c.drawString(50, 665, address)
    c.drawString(50, 653, location)

    # -60,00-
    value_number_formatted = f"-{value:,.2f}-".replace(".", ",")
    c.drawString(50, 605, value_number_formatted)

    # -sechzig-
    value_as_text_formatted = f"-{number_to_german_word(value)}-"
    c.drawString(180, 605, value_as_text_formatted)

    # datum
    c.drawString(435, 605, date)

    c.save()

    # Merge the text PDF with the template PDF
    merge_pdfs(template_filename, temporary_text_pdf_filename, output_filename)
    # remove the text pdf
    os.remove(temporary_text_pdf_filename)
