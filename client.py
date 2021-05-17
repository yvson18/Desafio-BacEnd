import requests

r_todas_prop = requests.get(f"http://127.0.0.1:8000/proposicoes")

r_autor_prop = requests.get(f"http://127.0.0.1:8000/autor/Kim Kataguiri")

r_tipo_prop = requests.get(f"http://127.0.0.1:8000/tipo/Projeto de Lei")

#print(r_todas_prop.json())

#print(r_autor_prop.json())

#print(r_tipo_prop.json())