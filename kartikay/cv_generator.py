from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import os

# Function to collect user details
def collect_details():
    details = {}
    details['name'] = input("Enter your full name: ")
    details['email'] = input("Enter your email: ")
    details['phone'] = input("Enter your phone number: ")
    details['address'] = input("Enter your address: ")
    details['linkedin'] = input("Enter your LinkedIn profile link: ")
    details['github'] = input("Enter your GitHub profile link: ")
    details['website'] = input("Enter your personal website or portfolio link (optional): ")
    details['summary'] = input("Enter a brief summary about yourself: ")
    details['education'] = input("Enter your education details: ")
    details['experience'] = input("Enter your work experience: ")
    details['skills'] = input("Enter your skills (comma-separated): ")
    details['certifications'] = input("Enter your certifications: ")
    details['projects'] = input("Enter your notable projects: ")
    details['languages'] = input("Enter languages you know: ")
    details['hobbies'] = input("Enter your hobbies or interests: ")
    details['photo'] = input("Enter the path to your photo (optional, leave blank to skip): ")
    return details

# Function to generate PDF
def generate_pdf(details):
    file_name = "cv.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Add photo if provided
    if details['photo'] and os.path.isfile(details['photo']):
        c.drawImage(details['photo'], width - 150, height - 200, width=100, height=100)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, details['name'])

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Email: {details['email']}")
    c.drawString(50, height - 100, f"Phone: {details['phone']}")
    c.drawString(50, height - 120, f"Address: {details['address']}")
    c.drawString(50, height - 140, f"LinkedIn: {details['linkedin']}")
    c.drawString(50, height - 160, f"GitHub: {details['github']}")
    if details['website']:
        c.drawString(50, height - 180, f"Website: {details['website']}")

    y = height - 220

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Summary")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['summary'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Education")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['education'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Experience")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['experience'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Skills")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['skills'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Certifications")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['certifications'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Projects")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['projects'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Languages")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['languages'])

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Hobbies")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, details['hobbies'])

    c.save()
    print(f"CV saved successfully as {file_name}")

if __name__ == "__main__":
    user_details = collect_details()
    generate_pdf(user_details)
