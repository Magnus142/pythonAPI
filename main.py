from googleapiclient.discovery import build
my_api_key = "AIzaSyCuB3MAJ29XZUVSHgbhIVuNUzW_EQVRKrg"
my_cse_id = "a5db8c49e25224ce3"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


# print(search_result)
# print(search_result.keys())
# print(search_result.get("items"))

    # Main
search = input("Hva ønsker du å søke på?: ")
search_result = google_search(search, my_api_key, my_cse_id)
print("\nFørste snippet for",search+":")
print(search_result["items"][0]["snippet"])
print(search_result["items"][0]["link"])