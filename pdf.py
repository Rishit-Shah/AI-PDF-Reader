#install required imports for reading pdf's and using oepnai API.
import PyPDF2
import openai
from openai import OpenAI

client = OpenAI(
  api_key="---your openai api key")
  
def extract_pdf_text(pdf_path):
  with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    # Iterate through the PDF
    for page in range(len(reader.pages)):
      text += reader.pages[page].extract_text()
  return text


pdf_text = extract_pdf_text("---/.....pdf")  # Replace with the path to your PDF file

prompt = f"Write a summary of the pdf. {pdf_text}"

# Make the API call
try:
  completion = client.chat.completions.create(
    model="---your model",
    store=True,
    messages=[
      {"role": "user", "content": prompt}
    ]
  )

  print("Response from OpenAI:")
  print(completion.choices[0].message)
  
#checking if api didnt call anything
except Exception as e:
  print(f"Error during API call: {e}")