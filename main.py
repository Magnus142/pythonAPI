from googleapiclient.discovery import build
my_api_key = "AIzaSyCuB3MAJ29XZUVSHgbhIVuNUzW_EQVRKrg"
my_cse_id = "a5db8c49e25224ce3"

fortsett = True
link = False
snippet = False

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res



    # Main
search = input("Hva ønsker du å søke på?: ")
while fortsett:
    search_result = google_search(search, my_api_key, my_cse_id)
    print("\n\n\n\nDu søker etter:",search+", hva ønsker du å få opp?")

    if link == False:
        print("1: Link til nettside")
    elif:
        print("1Link til nettside")

    print("2: En snippet fra nettside")
    print("\n3: Søk med disse valgene")


    valg = input("\n Skriv her: ")
    if valg == 1:
        link == True
    elif valg == 2:
        snippet = True









print("\nFørste snippet for",search+":")
print(search_result["items"][0]["snippet"])
print(search_result["items"][0]["link"])