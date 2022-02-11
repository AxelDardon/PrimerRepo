import webbrowser
import json
import requests

def GetHomwork(SemanaN,FilePath):
    # Parte I
    Enlace="https://fpmir.azurewebsites.net/{}/AZFMIR?AZFNUM={}".format("api",SemanaN)
    webbrowser.open(Enlace, new=2)
    #Parte II
    response=requests.get(Enlace).text
    response_info=json.loads(response)
    archivo=open(FilePath,"w")
    json.dump(response_info,archivo,indent=6)
    archivo.close()

InputSemana = input("ingrese semana:")
InputFile=input("Ingrese path y nombre de archivo")
GetHomwork(InputSemana,InputFile)