import requests

# Configuration de l'API Omnitracker ITSM
API_BASE_URL = 'https://example.com/omnitracker-itsm-api'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'  # Remplacez YOUR_AUTH_TOKEN par le token d'authentification réel

# Endpoint pour créer un nouvel enregistrement
CREATE_RECORD_ENDPOINT = '/records'

# Endpoint pour mettre à jour un enregistrement existant
UPDATE_RECORD_ENDPOINT = '/records/{record_id}'  # Remplacez {record_id} par l'ID de l'enregistrement réel

# Fonction pour effectuer une requête POST pour créer un nouvel enregistrement
def create_record(data):
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json',
    }
    response = requests.post(API_BASE_URL + CREATE_RECORD_ENDPOINT, json=data, headers=headers)
    return response

# Fonction pour effectuer une requête PUT pour mettre à jour un enregistrement existant
def update_record(record_id, data):
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json',
    }
    endpoint = UPDATE_RECORD_ENDPOINT.format(record_id=record_id)
    response = requests.put(API_BASE_URL + endpoint, json=data, headers=headers)
    return response

if __name__ == '__main__':
    # Exemple de création d'un nouvel enregistrement
    new_record_data = {
        'title': 'Nouvel enregistrement',
        'description': 'Description de l\'enregistrement',
        # Ajoutez d'autres champs nécessaires pour créer le nouvel enregistrement
    }
    create_response = create_record(new_record_data)
    print(create_response.status_code)
    print(create_response.json())

    # Exemple de mise à jour d'un enregistrement existant
    record_id_to_update = '12345'  # Remplacez 12345 par l'ID de l'enregistrement à mettre à jour
    update_record_data = {
        'title': 'Enregistrement mis à jour',
        # Ajoutez d'autres champs nécessaires pour la mise à jour de l'enregistrement
    }
    update_response = update_record(record_id_to_update, update_record_data)
    print(update_response.status_code)
    print(update_response.json())
