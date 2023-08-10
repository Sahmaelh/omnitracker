import requests

# Informations d'authentification pour OmniTracker
omnitracker_url = "https://votre-serveur-omnitracker/api"
omnitracker_auth = ("votre_nom_utilisateur", "votre_mot_de_passe")

# Informations d'authentification pour Jira
jira_url = "https://votre-instance-jira.atlassian.net"
jira_auth = ("votre_nom_utilisateur", "votre_token_api_jira")

# Appel à l'API OmniTracker pour récupérer les éléments non mis à jour
response_omnitracker = requests.get(
    f"{omnitracker_url}/elements-non-mis-a-jour",
    auth=omnitracker_auth
)

if response_omnitracker.status_code == 200:
    elements_non_mis_a_jour = response_omnitracker.json()

    for element in elements_non_mis_a_jour:
        # Création d'un ticket Jira pour chaque élément non mis à jour
        jira_payload = {
            "fields": {
                "project": {"key": "ITSM"},
                "summary": f"Élément non mis à jour : {element['nom']}",
                "description": f"L'élément {element['nom']} nécessite une mise à jour.",
                "priority": {"name": "High"},
                # ... autres champs nécessaires
            }
        }

        response_jira = requests.post(
            f"{jira_url}/rest/api/3/issue",
            json=jira_payload,
            auth=jira_auth
        )

        if response_jira.status_code == 201:
            print(f"Ticket créé pour l'élément {element['nom']}")
        else:
            print(f"Échec de la création du ticket pour {element['nom']}", response_jira.text)
else:
    print("Échec de la récupération des données depuis OmniTracker", response_omnitracker.text)
