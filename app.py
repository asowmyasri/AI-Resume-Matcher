import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
from docx import Document

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Function to extract text from docx file
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    
    for para in doc.paragraphs:
        text += para.text + "\n"
    
    return text

st.title("AI Resume Matcher")

#Upload resume file
uploaded_file = st.file_uploader("Upload your resume (.docx )", type=["docx"])

#Input job description
job_description = st.text_area("Paste job description here:")

#Button to analyze
if st.button("Analyze Resume"):
    if uploaded_file is not None and job_description:
        resume_text = extract_text_from_docx(uploaded_file)

        prompt = f"""
        You are an expert AI hiring assistant.
        compare the RESUME and JOB DESCRIPTION.
        Give Output:
        Match Score:
        Matching Skills:
        Missing Skills:
        Suggestions:
        RESUME:
        {resume_text}
        JOB DESCRIPTION:
        {job_description}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content
        st.subheader("Analysis Result:")
        st.write(result)
    else:
        st.warning("Please upload a resume and enter a job description.")







