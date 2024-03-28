import streamlit as st
from pymongo import MongoClient

# Connexion à la base de données
client = MongoClient(st.secrets["KEY"])
db = client["JuniaLLM"]
collection = db["Q&R"]

# Page title
st.set_page_config(page_title='Junia LLM', page_icon=":mortar_board:")
st.title('Junia LLM')
st.markdown("---")
st.info("Veuillez entrer une question et une réponse en rapport avec Junia, l'ISEN, l'école...\nVoir les exemples ci-dessous.")

examples = [
    ["Quand doit-on choisir une spécialité à l'ISEN ?", "Vous devez choisir une spécialité en fin de 3ème année."], 
    ["Quel est le prix du RU ?", "Le prix du RU est de 3,30€ pour les non-boursiers et de 1€ pour les boursiers."]
]

# Write examples
st.write("- **Question**: " + examples[0][0])
st.write("- **Réponse**: " + examples[0][1])
st.write("*Ou*")
st.write("- **Question**: " + examples[1][0])
st.write("- **Réponse**: " + examples[1][1])

st.markdown("---")

# Champ de saisie pour la question
question = st.text_input("Question :", "")

# Champ de saisie pour la réponse
reponse = st.text_input("Réponse :", "")

# Bouton pour valider
if st.button("Ajouter"):
    if question.strip() == "":
        st.error("Veuillez saisir une question.")
    elif reponse.strip() == "":
        st.error("Veuillez saisir une réponse.")
    else:
        # Traitement et affichage de la question et de la réponse
        doc = {"instruction": question, "output": reponse}
        collection.insert_one(doc)
        st.success("Question et réponse envoyées avec succès !")
        question = ""
        reponse = ""

# CSS inline pour styliser les éléments
st.markdown(
    """
    <style>
        .stButton>button {
            color: #ffffff;
            background-color: #228B22;
            font-size: 20px;
            display: block;
            margin: 0 auto;
        }

        .stButton>button:hover {
            color: #dddddd;
            border-color: #228B22;
        }
    </style>
    """,
    unsafe_allow_html=True
)