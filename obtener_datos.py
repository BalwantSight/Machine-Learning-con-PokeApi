import requests
import pandas as pd

# Obtener datos de la PokeAPI
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100")
data = response.json()['results']

# Preprocesamiento de datos
pokemon_attributes = []
for pokemon in data:
    pokemon_data = requests.get(pokemon['url']).json()
    attributes = {
        'nombre': pokemon['name'],
        'tipo': pokemon_data['types'][0]['type']['name'],
        'experiencia_base': pokemon_data['base_experience'],
        'altura': pokemon_data['height'],
        'peso': pokemon_data['weight']
    }
    pokemon_attributes.append(attributes)

# Crear DataFrame
df = pd.DataFrame(pokemon_attributes, columns=[
                  'nombre', 'tipo', 'experiencia_base', 'altura', 'peso'])

# Guardar los datos en un archivo CSV
df.to_csv('pokemon_data.csv', index=False)
