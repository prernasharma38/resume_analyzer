import docx2txt
import re

def extract_info(filepath):
    text = docx2txt.process(filepath)
    data = {}

    # Extract name (very basic assumption from first line)
    lines = text.strip().split("\n")
    data['name'] = lines[0] if lines else 'Unknown'

    # Extract email
    email_match = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
    data['email'] = email_match.group(0) if email_match else 'Not found'

    # Extract phone number (common formats)
    phone_match = re.search(r'\b(\+\d{1,3}[- ]?)?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{4}\b', text)
    data['phone'] = phone_match.group(0) if phone_match else 'Not found'

    # Extract education
    education_keywords = ['BCA', 'MCA', 'B.Tech', 'M.Tech', 'Bachelor', 'Master']
    data['education'] = [word for word in education_keywords if word in text]

    # Extract hobbies
    hobbies_match = re.search(r'Hobbies\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
    data['hobbies'] = hobbies_match.group(1).split(',') if hobbies_match else []

    # Extract lifestyle
    lifestyle_match = re.search(r'Lifestyle\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
    data['lifestyle'] = lifestyle_match.group(1).split(',') if lifestyle_match else []

    # Extract address using keywords
    address_keywords = ['Address', 'Location', 'Residence', 'Home']
    address = ''
    for keyword in address_keywords:
        match = re.search(rf'{keyword}\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
        if match:
            address = match.group(1)
            break
    data['address'] = address if address else 'Not found'

    return data
