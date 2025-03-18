from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generatePDF(file_name):
    # Create a PDF document
    pdf_file = file_name +".pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Sample content
    title_text = "My Simple PDF"
    
    # Create a list to hold the content elements
    content = []

    # Define a custom title style with left alignment
    title_style = ParagraphStyle(
        "left_title_style",
        parent=getSampleStyleSheet()["Title"],
        alignment=0,  # 0 corresponds to left alignment
    )

    # Add the title to the content list with the custom title style
    title = Paragraph(title_text, style=title_style)
    content.append(title)

    # Add a spacer
    content.append(Spacer(1, 20))

    # Define a custom paragraph style with left alignment
    paragraph_style = ParagraphStyle(
        "left_paragraph_style",
        parent=getSampleStyleSheet()["Normal"],
        alignment=0,  # 0 corresponds to left alignment
    )

    # Add the paragraphs to the content list with the custom paragraph style
    for para_text in paragraphs:
        paragraph = Paragraph(para_text, style=paragraph_style)
        content.append(paragraph)
        content.append(Spacer(1, 10))

    # Build the PDF document
    doc.build(content)

