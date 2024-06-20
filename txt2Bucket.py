import pathlib
import textwrap
import sys

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

subprompt = sys.argv[1]
# subprompt =[
#   {
#     "name": "The Golkonda Hotel",
#     "latitude": "17.4043",
#     "longitude": "78.45384"
#   },
#   {
#     "name": "Best Western Ashoka",
#     "latitude": "17.403893",
#     "longitude": "78.465225"
#   },
#   {
#     "name": "Lemon Tree Hotel",
#     "latitude": "17.41201",
#     "longitude": "78.44992"
#   },
#   {
#     "name": "Treebo Trend Address Inn",
#     "latitude": "17.40893",
#     "longitude": "78.44799"
#   },
#   {
#     "name": "The Central Court Hotel",
#     "latitude": "17.404297",
#     "longitude": "78.465126"
#   },
#   {
#     "name": "Hampshire Plaza",
#     "latitude": "17.405224",
#     "longitude": "78.464584"
#   },
#   {},
#   {
#     "name": "Treebo Trend Srico",
#     "latitude": "17.40917",
#     "longitude": "78.44441"
#   },
#   {
#     "name": "Itsy By Treebo - Arastu Inn",
#     "latitude": "17.397957",
#     "longitude": "78.4628"
#   },
#   {
#     "name": "Ohri's Banjara",
#     "latitude": "17.408419",
#     "longitude": "78.438995"
#   },
#   {
#     "name": "Park Continental Hotel",
#     "latitude": "17.399273",
#     "longitude": "78.44804"
#   },
#   {
#     "name": "The Platinum Boutique Business Hotel",
#     "latitude": "17.404373",
#     "longitude": "78.48163"
#   },
#   {
#     "name": "OYO 1405 Hotel The Platinum",
#     "latitude": "17.402592",
#     "longitude": "78.49324"
#   },
#   {
#     "name": "Hotel Kubeera Palace",
#     "latitude": "17.402868",
#     "longitude": "78.48328"
#   },
#   {
#     "name": "Amrutha Castle Hotel",
#     "latitude": "17.407434",
#     "longitude": "78.4689"
#   },
#   {},
#   {
#     "name": "Treebo Trend Aamantran",
#     "latitude": "17.410822",
#     "longitude": "78.49777"
#   },
#   {
#     "name": "Elysium Inn",
#     "latitude": "17.411087",
#     "longitude": "78.45487"
#   },
#   {
#     "name": "Treebo Trend Wood Bridge",
#     "latitude": "17.402779",
#     "longitude": "78.460556"
#   },
#   {
#     "name": "OYO 9796 Hotel Alekhya Residency",
#     "latitude": "17.40788",
#     "longitude": "78.46996"
#   },
#   {
#     "name": "The Platinum Boutique Inn",
#     "latitude": "17.406656",
#     "longitude": "78.47815"
#   },
#   {
#     "name": "Rukmini Riviera Hotel",
#     "latitude": "17.40276",
#     "longitude": "78.46105"
#   },
#   {
#     "name": "Rainbow International Lakdikapul",
#     "latitude": "17.4022",
#     "longitude": "78.4635"
#   },
#   {
#     "name": "Hotel Imperial Classic",
#     "latitude": "17.40476",
#     "longitude": "78.49597"
#   },
#   {},
#   {
#     "name": "The Cent",
#     "latitude": "17.406174",
#     "longitude": "78.46303"
#   },
#   {
#     "name": "Tabla Pride Hotel & Spa",
#     "latitude": "17.412086",
#     "longitude": "78.45001"
#   },
#   {
#     "name": "Fortune Park Vallabha",
#     "latitude": "17.411346",
#     "longitude": "78.43566"
#   },
#   {
#     "name": "Deccan Comforts",
#     "latitude": "17.40757",
#     "longitude": "78.469666"
#   },
#   {
#     "name": "Hyderabad Heights",
#     "latitude": "17.4009",
#     "longitude": "78.4896"
#   },
#   {
#     "name": "Bikanervala Boutique",
#     "latitude": "17.411047",
#     "longitude": "78.449776"
#   },
#   {
#     "name": "Hotel Abode By Shree Venkateshwara",
#     "latitude": "17.405308",
#     "longitude": "78.46506"
#   },
#   {
#     "name": "The Down Town Hotel",
#     "latitude": "17.406845",
#     "longitude": "78.44809"
#   }
# ]

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyC_djVzzPW8y63obBNRF5i5WvbjcZkZ1aA")

model = genai.GenerativeModel('gemini-pro')

prompt = f"""
You will be given a list of places . Your reply should include a name ,  
latitude , longitude as illustrated below in json format include the best places to travel
in it only . Select the places if they are worth travelling 

Example question: Best places to visit India ?

Example reply:
best_places=[{{
  'name' : 'Birla Mandir',
  'latitude' : '17.3850',
  'longitude' : '78.4867',
  }}
  ,
  {{
  'name': 'Golconda Fort',
  latitude: '17.3833',
  longitude: '78.4011',
  }}
]
the above reply is only for example purposes

Now consider this data actual data is :{subprompt}
please setect and reeturn top 10 best places among the guven data to  travel in it only in array of objects format 
"""
# print(prompt)
response = model.generate_content(prompt)
print(response.text)

