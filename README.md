# AI Resume Matcher

An AI-powered web application that analyzes resumes against job descriptions and provides intelligent insights such as match score, skill gaps, and actionable improvement suggestions.

---

## Overview

This project leverages Large Language Models (LLMs) to simulate real-world resume screening used by modern hiring systems.
It helps candidates understand how well their resume matches a job description and what improvements are needed to increase their chances of selection.

---
## Features

-  Upload resume (DOCX format)
-  Input job description dynamically
-  AI-powered resume-job matching
-  Match score calculation
-  Skill gap analysis
-  Personalized improvement suggestions
-  Interactive web interface using Streamlit
---
##  Tech Stack

- **Programming Language:** Python  
- **AI Model:** OpenAI GPT (LLM)  
- **Frontend:** Streamlit  
- **Document Processing:** python-docx  
- **Environment Management:** dotenv  
---
##  How It Works
1. User uploads resume (.docx)
2. User enters job description
3. Resume text is extracted and processed
4. AI model analyzes both inputs
5. System returns:
   - Match Score
   - Matching Skills
   - Missing Skills
   - Improvement Suggestions
---
## How to Run Locally

1. Clone the repository:
   ```bash
     git clone https://github.com/asowmyasri/AI-Resume-Matcher.git

2. Navigate to Project folder:
  ```bash
     cd AI-Resume-Matcher
3. Install dependencies:
    ```bash
         pip install -r requirements.txt
4. Create .env file and add your OpenAI API key:
    OPENAI_API_KEY=your_api_key_here
5. Run the application:
    ```bash
     streamlit run app.py
--------------------------
Author
Sowmya Sree
Aspiring AI Engineer | Data Enthusiast

If you like this project
Give it a ⭐ on GitHub and share your feedback!
