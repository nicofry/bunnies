import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
      #Page d'accueil
      st.title("Vous faites partie de la TEAM!")
      st.image("https://imgs.search.brave.com/q2Jpn6rOZbqDC9urVfJUpezvSmfP5LyauLQA4Bnz0dk/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pLmlt/Z2ZsaXAuY29tLzQv/NTExZXUuanBn")

def photos():
    
    st.title("Un peu de douceur dans ce monde de brutes")
        # Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne : 
    with col1:
        st.header("Lapin tête de lion")
        st.image("https://www.lapins.info/wp-content/uploads/2018/10/lionhead1_a-1.jpg")

    # Contenu de la deuxième colonne :
    with col2:
        st.header("Lapin bélier")
        st.image("https://images.ctfassets.net/denf86kkcx7r/7itme2jen6rliVDzBuFBmL/26b8b7eacd32ae52d5f2edf052051e40/lapin_b%C3%A9lien_lop.jpg?fit=fill&w=1024&q=80")

    # Contenu de la troisième colonne : 
    with col3:
        st.header("Lapin Angora")
        st.image("https://www.zooplus.fr/magazine/wp-content/uploads/2021/11/AdobeStock_77279140-768x511-1.jpeg")
      



if st.session_state["authentication_status"]:
    with st.sidebar:
    # On affiche le menu dans la sidebar
        authenticator.logout("Déconnexion")
        st.text(f"Bienvenue {st.session_state.get("name")}, vous êtes BG aujourd'hui! ")
        selection = option_menu(
                menu_title="Menu du jour",
                options = ["Accueil", "Instant douceur"]
        )
    if selection == "Accueil":
        accueil()
    elif selection == "Instant douceur":
        photos()



  # Le bouton de déconnexion

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')