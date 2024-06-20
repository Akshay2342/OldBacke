import pathlib
import textwrap
import sys

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# subprompt = sys.argv[1]

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyC_djVzzPW8y63obBNRF5i5WvbjcZkZ1aA")

model = genai.GenerativeModel('gemini-pro')

prompt = """
You will be asked a question. Your reply should include type , name , amount and catagory as illustrated below in json format
type will be either expense or revenue
Example data: I recently recived my salary of 60 rupeees of my partime job

Example reply:
{
  "type": "revenue",
  "name": "salary",
  "amount": 60,
  "catagory":"PartTime"
}

Now the actudal data : " I got 400 rupees in lottory  "

"""
response = model.generate_content(prompt)
print(response.text)

