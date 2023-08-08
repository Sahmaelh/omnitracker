import requests

# Configuration de l'API Omnitracker
API_URL = 'https://example.com/omnitracker-api/tickets'
HEADERS = {
    'Authorization': 'Bearer YOUR_API_TOKEN',  # Remplacez YOUR_API_TOKEN par le token d'authentification réel
    'Content-Type': 'application/json',
}

# Données pour créer un nouveau ticket (remplacez ces valeurs par les données réelles)
ticket_data = {
    'title': 'Nouveau ticket',
    'description': 'Description du ticket',
    'assigned_to': 'John Doe',
    # Ajoutez d'autres champs nécessaires pour créer le ticket selon l'API Omnitracker
}

def create_ticket_in_omnitracker(ticket_data):
    try:
        response = requests.post(API_URL, json=ticket_data, headers=HEADERS)

        if response.status_code == 200:
            print("Ticket créé avec succès.")
        else:
            print(f"La création du ticket a échoué avec le code d'état: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête API: {e}")

if __name__ == "__main__":
    create_ticket_in_omnitracker(ticket_data)