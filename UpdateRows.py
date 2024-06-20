import pathlib
import textwrap
import sys

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import json
import sys

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyC_djVzzPW8y63obBNRF5i5WvbjcZkZ1aA")

model = genai.GenerativeModel('gemini-pro')

data = sys.argv[1]
# print(data)


# data = """[
# {
#   "columns": {
#     "Bucket": {
#       "name": "Bucket",
#       "items": []
#     },
#     "Day1": {
#       "name": "Day1",
#       "items": [
#         {
#           "content": "Lumbini Park",
#           "id": "1228084",
#           "lng": 78.4636,
#           "lat": 17.42363
#         },
#         {
#           "content": "Christian Cemetery",
#           "id": "4401096",
#           "lng": 78.49159,
#           "lat": 17.39897
#         },
#         {
#           "content": "Sri Ramakrishna Math",
#           "id": "4401161",
#           "lng": 78.48224,
#           "lat": 17.41153
#         },
#         {
#           "content": "Yogibear Mini Golf Park",
#           "id": "4421905",
#           "lng": 78.46512,
#           "lat": 17.42147
#         }
#       ]
#     },
#     "Day2": {
#       "name": "Day2",
#       "items": [
#         {
#           "content": "Pegasus Shopping Mall",
#           "id": "6041254",
#           "lng": 78.47452,
#           "lat": 17.39179
#         },
#         {
#           "content": "Buddha Statue",
#           "id": "6496303",
#           "lng": 78.47515,
#           "lat": 17.415571
#         },
#         {
#           "content": "Nizamia Observatory",
#           "id": "4401114",
#           "lng": 78.45274,
#           "lat": 17.42727
#         }
#       ]
#     },
#     "Day3": {
#       "name": "Day3",
#       "items": []
#     }
#   }
#   }
# ]"""

# print(data)

jsonobj = '''{
  "Bucket": {
    "name": "Bucket",
    "items": [
      {
        "content": "example1name",
        "id": "example1id",
        "lng": example1longitude,
        "lat": example2latitude
      },

    ]
  },
  "Day1": {
    "name": "Day1",
    "items": [
          {
        "content": "example2name",
        "id": "example2id",
        "lng": example2longitude,
        "lat": example2latitude
      },
            {
        "content": "example3name",
        "id": "example3id",
        "lng": example3longitude,
        "lat": example3latitude
      }
    ]
  },
  "Day2": {
    "name": "Day2",
    "items": []
  },
  "Day3": {
    "name": "Day3",
    "items": []
  }
}''';

prompt = f"""
You will be asked a question , given some data to update. Your 
    Please update the given object move the places from bucket to 
    days and make the best trip possible considering all the constains and best 
    timimngs to vist the particular place 

    consider this example Json Object 
    your response should follow this basic  structure 

    now please consider this data actual data : 
    {data}
    
  select the places and shuffle them into best possible trip experience ,
  please update the data and make the best trip possible .dont forget to consider the timings and the distance between the places
  please dont change the format of data , just update the data in json format only add one key value pair to the data name as itenerary_name give the plan for each day and ensure that it is an valid json object
  trim the beginning and ending charecters it should only be an json object and should be in same format as actual data  
  make sure the text you are returning is a valid json object cross check it 
"""
# print(prompt)
response = model.generate_content(prompt)
# parsed_data = json.loads(response.text)
print(response.text)
# print(parsed_data)

