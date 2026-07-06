import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='.env')
print("API key:",os.getenv("OpenAI_API_KEY"))
client = OpenAI(api_key=os.getenv("OpenAI_API_KEY"))

#Input the text(resume sample) to be summarized
resume_text="""I had an experience in python, SQL and data pipelines"""

#prompt
prompt = f"""You are an AI expert reviewer
              I want you to review and provide:
              1.Resume score out of 100
              resume:{resume_text}"""

#Call OpenAI API

responce = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":prompt}]
)
#print the output

print(responce.choices[0].message.content)
