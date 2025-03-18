from io import BytesIO
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER


def clean_directory_name(directory_name):
    # Define a list of illegal characters in directory names
    illegal_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']

    # Replace illegal characters with underscores
    cleaned_name = ''.join(['_' if char in illegal_characters else char for char in directory_name])

    return cleaned_name

def generatePDF(url):
    app_should_generate_pdf = True
    # Replace 'your_url_here' with the actual URL of the web page you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content)  # or 'html5lib'
    
    # Define styles
    styles = getSampleStyleSheet()
    centered_style = styles["Normal"]
    centered_style.alignment = TA_LEFT
    story = []
        
    # Find the <shreddit-title> element and extract the 'title' attribute
    shreddit_title_element = soup.find('shreddit-title')
    if shreddit_title_element:
        title = shreddit_title_element['title']
        print(title)
    else:
        print("Shreddit title element not found.")
    
    title_text = title.split(":")[0]
    # Define a custom title style with left alignment
    title_style = ParagraphStyle(
        "left_title_style",
        parent=getSampleStyleSheet()["Title"],
        alignment=0,  # 0 corresponds to left alignment
        fontSize=12  # Set the font size to 12
    )

    # Add the title to the content list with the custom title style
    title = Paragraph(title_text, style=title_style)
    story.append(title)

    # Add a spacer
    story.append(Spacer(1, 20))

    
    # Create a PDF document
    pdf_filename = f"files/{clean_directory_name(title_text)}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

   
    

    content = soup.find("div", class_="text-neutral-content")
    if  content is None:
        content = soup.find("div", class_="max-h-[100vw] h-full w-full object-contain overflow-hidden relative bg-black")
    
    if  content is None:
        app_should_generate_pdf = False  

    if app_should_generate_pdf:
        for element in content.contents:
            if element.name == "p":
                p_content = []  # Store the content of this <p> element
                for content_tag in element.contents:
                    if isinstance(content_tag, str):
                        # Add text directly
                        p_content.append(content_tag)
                    elif content_tag.name == "a":
                        # Add a link with attributes
                        link_text = content_tag.text
                        link_url = content_tag["href"]
                        p_content.append('<a href="{link_url}">{link_text}</a>')
                    elif content_tag.name == "strong":
                        # Add strong text with bold style
                        strong_text = content_tag.text
                        p_content.append(f'<strong>{strong_text}</strong>')
                
                # Create a Paragraph with the combined content
                combined_content = " ".join(p_content)
                story.append(Paragraph(combined_content, centered_style))
                story.append(Spacer(1, 10))

            elif element.name == "figure":
                img_url = element.find("a")["href"]
                response = requests.get(img_url)
                if response.status_code == 200:
                    img_data = BytesIO(response.content)
                    img_element = Image(img_data, width=300, height=300)
                    story.append(img_element)
        
        
        doc.build(story)
