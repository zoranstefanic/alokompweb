import requests
data = requests.get(f'https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{code}').json()[code.lower()]
print(data[0]['sequence'])
