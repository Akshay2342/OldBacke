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

prompt = f"""

    Give me a list of objects which contains food_name , restaurants , veg 

    Example Question : Best foods to eat in hyderabad
    Example reply:
    {{
    best_foods : [{{
      'food_name' : 'biryani',
      'restaurants' :
       [ 
      'name' : paradise',
      'lat' : 17.42363,
      'lng' : 78.4636,
      'veg' : 'no',
      ]
      }}
      ,
      {{
      food_name: 'haleem',
      restaurants: 
      [
        'name' : 'shah ghouse',
      lat: 17.39897,
      lng: 78.49159,
      veg: 'no',
      ]
      }}
    }}

    if you now location latitude and longitude and place id of restaurant pleasse include those as well
    question : Best Foods to eat in {subprompt}
    return only a valid array of objects please return a valid json object which contains key best_foods and value an array of objects
"""
response = model.generate_content(prompt)
print(response.text)

