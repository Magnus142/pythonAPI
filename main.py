from googleapiclient.discovery import build
my_api_key = "AIzaSyCuB3MAJ29XZUVSHgbhIVuNUzW_EQVRKrg"
my_cse_id = "a5db8c49e25224ce3"

fortsett = True
link = False
snippet = False


def funkerdetint(string,min,max):   # gjør slik at man kun kan skrive inn kun en integer mellom to verdier
    tallk = False
    while tallk == False:
        try:
            print("\n"+string)
            testet = int(input("skriv her: "))
            if testet > max or testet < min:    # om integeren er større eller mindre enn det jeg ønsker blir det en error
                error
            tallk = True
        except:
            print("\n\n████ Skriv inn et heltall mellom",min,"og",max,"████")
    return testet








def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res



    # Main
search = input("Hva ønsker du å søke på?: ")
search_result = google_search(search, my_api_key, my_cse_id)
while fortsett:
    print("\n\n\n\nDu søker etter:",search+", hva ønsker du å få opp?")


    if link == False:
        print("1: Link til nettside     x")
    elif link == True:
        print("1: Link til nettside     ✓")
    if snippet == False:
        print("2: En snippet fra nettside   x")
    elif snippet == True:
        print("2: En snippet fra nettside   ✓")
    print("\n3: Søk med disse valgene")


    valg = int(funkerdetint("", 1, 3))

    if valg == 1:
        if link == False:
            link = True
        else:
            link = False
    elif valg == 2:
        if snippet == False:
            snippet = True
        else:
            snippet = False
    else:
        fortsett = False
        print("\n\n\n")
        if link == True:
            print("Link: ",search_result["items"][0]["link"])
        if snippet == True:
            print("Snippet: ",search_result["items"][0]["snippet"])
