import  urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
#orig = "Santiago, chile"    # para realizar pruebas 
#dest = "Arica,chile"        # para realizar pruebas  
key = "JOj82lGfKrrLXE0HvD5u9eqFpOrqxrCj"   # Key personal 


while True:
    orig = input("Starting Location: ")    #Se debe colocar la localidad 
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")           #Localidad a cual quiero ir 
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig, "to":dest}) # se valida la Key si esta acativa, origen y destino
    json_data = requests.get(url).json()

    print("URL: " + (url))
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("==================================================")
        print("Direccion: " + (orig) + " to " + (dest)) # indica la direccion colocada 
        print("Duration: " + (json_data["route"]["formattedTime"])) # Duracion del viaje 
        print("==================================================")
        print("Kilómetros:" + str ("{:.2f}" .format((json_data ["route"] ["distance"]) *1.61)))  # Los Kilometros que se deben recorrer 
        print("==================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:   # Las indicaciones. 
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
            print("==================================================================================")
    print("*****************Para salir debe colocar q*****************")
