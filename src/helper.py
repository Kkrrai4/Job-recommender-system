import fitz # PyMuPDF
import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# client = OpenAI(api_key=OPENAI_API_KEY)


def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

from openai import OpenAI



def ask_openai(prompt, max_tokens=500):
    response = client.chat.completions.create(
        model= "openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content