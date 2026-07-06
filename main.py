import os
from openai import OpenAI
from dotenv import load_dotenv
from docx import Document

# Load API key
load_dotenv(dotenv_path=".env")
print("API KEY:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    
    for para in doc.paragraphs:
        text += para.text + "\n"
    
    return text

# Input text (your resume sample)
file_name = input("Enter resume file name (with .docx): ")
resume_text = extract_text_from_docx(file_name)

job_description = input("Paste job description here: ")

#resume_text = extract_text_from_docx("Sowmya_Sree_resume_AWS.docx")
#print("DEBUG RESUME TEXT:")
#print(resume_text[:1000])

#job_description = """
#Looking for a Data Engineer with experience in Python, SQL, Apache Airflow, AWS, and data pipeline development.
#"""

# Prompt
prompt = f"""

You are an expert AI hiring assistant.

Analyze the RESUME and JOB DESCRIPTION deeply.

Give output STRICTLY in this format:

Match Score: X/100

Matching Skills:
- ...

Missing Skills:
- ...

Suggestions (VERY SPECIFIC to candidate experience):
- Give actionable steps based on current skills
- Avoid generic advice

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""


# Call OpenAI
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Print output
#print(response.choices[0].message.content)

result = response.choices[0].message.content
print(result)
#with open("output2.txt", "w") as file:
    #file.write(result)
output_file = "analysis_result.txt"

with open(output_file, "w") as file:
    file.write(result)

print(f"Output saved to {output_file}")