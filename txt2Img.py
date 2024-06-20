import requests
import json
import sys
food  = sys.argv[1]
from bing_image_downloader import downloader
query_string =food
downloader.download(query_string, limit=1, output_dir='Food'+query_string, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

# import sys

# foodName = sys.argv[1]
# from bing_image_downloader import downloader
# downloader.download(foodName, limit=1, output_dir='Food'+foodName, adult_filter_off=True, force_replace=True, timeout=60, verbose=True)

