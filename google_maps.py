import googlemaps
import os

# gmaps = googlemaps.Client(key='AIzaSyBPKFuhzLERJC4hDT9wqJl_JMOkJuBzBDM')
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_KEY'))

def get_distance_from_googlemaps(address_origem, address_destiny):
    return gmaps.distance_matrix(address_origem, address_destiny)['rows'][0]['elements'][0]


print(get_distance_from_googlemaps('Rua Padre Achotegui, 25, Rio de Janeiro', 'Av Luiz Aranha 890, Rio de Janeiro'))
