import pathlib
import textwrap
import sys

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

subprompt = sys.argv[1]

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyC_djVzzPW8y63obBNRF5i5WvbjcZkZ1aA")

model = genai.GenerativeModel('gemini-pro')

prompt = """
You will be asked a question. Your reply should include a title, a 
descriptive paragraph, and a concluding paragraph as illustrated below in json format

Example question: Best places to visit India ?

Example reply:
best_places=[{
  'place_name' : 'hyderabad',
  'description' : 'Hyderabad is the capital of southern India's Telangana state. A major center for the technology industry, it's home to many upscale restaurants and shops. Its historic sites include Golconda Fort, a former diamond-trading center that was once the Qutb Shahi dynastic capital. The Charminar, a 16th-century mosque whose 4 arches support towering minarets, is an old city landmark near the long-standing Laad Bazaar.',
  }
  ,
  {
  place_name: 'goa',
  description: \"Goa is a state in western India with coastlines stretching along the Arabian Sea. Its long history as a Portuguese colony prior to 1961 is evident in its preserved 16th-century churches and the area’s tropical spice plantations. Goa is also known for its beaches, ranging from popular stretches at Baga and Palolem to those in laid-back fishing villages such as Agonda.\",
  }
]

"""
prompt=prompt+" "+subprompt + ' ?'
response = model.generate_content(prompt)
print(response.text)

