import requests
import json
import sys

# Replace these with your own API key and custom search engine ID
api_key = "AIzaSyDSEng_KzYUgAyJpuD4UNQVOGXmvgPM3zg"
cse_id = "468a880f545744823"
cityName = sys.argv[1]
# print(cityName)
# cityName = input('Enter the city Name : ')

def google_search(search_term, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
        **kwargs
    }
    response = requests.get(url, params=params)
    return response.json()

# Get the first 10 results

search1 = f"best foods to each in {cityName}" 
search2 = f"Popular street food in {cityName}"
search3 = f"Famous food to eat in {cityName}"
search4 = f"Must Try food in  {cityName}"
search4 = f"best Food Items in  {cityName}"

results1 = google_search(search1, api_key, cse_id)

# Get the next 10 results
results2 = google_search(search2, api_key, cse_id)

# Get the next 10 results
results3 = google_search(search3, api_key, cse_id)

results4 = google_search(search4, api_key, cse_id)

# Combine all the results
all_results = results1['items'] + results2['items'] + results3['items']

f_data =[]

for result in all_results:
    data={}
    # print(f"Title: {result['title']}")
    data['title'] = result['title']
    # print(f"Link: {result['link']}")
    data['link'] = result['link']
    # print(f"Snippet: {result['snippet']}")
    data['snippet'] = result['snippet']
    # print(f"PageMap: {result['pagemap']}")
    data['pagemap'] = result['pagemap']
    # print("\n")
    f_data.append(data)
json_data = json.dumps(f_data)

print(json_data)


# print("Hello World")