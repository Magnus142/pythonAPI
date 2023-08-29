from googleapiclient.discovery import build
my_api_key = "AIzaSyCuB3MAJ29XZUVSHgbhIVuNUzW_EQVRKrg"
my_cse_id = "a5db8c49e25224ce3"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

search_result = google_search("kaffe", my_api_key, my_cse_id)

for keyword in search_result:
    print(search_result[keyword])