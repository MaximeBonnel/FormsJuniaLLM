import streamlit as st
from pymongo import MongoClient
from streamlit_js_eval import streamlit_js_eval
import pandas as pd

st.set_page_config(page_title='Junia LLM')

# Connexion à la base de données
@st.cache_resource
def init_connection():
    return MongoClient(st.secrets["KEY"])

client = init_connection()
db = client["JuniaLLM"]
collection = db["Q&R"]

# Get example data
examples = collection.find({}, {'_id': 0})

# Page title
st.title('Junia LLM')
st.markdown("---")
st.info("Veuillez entrer une question et une réponse en rapport avec Junia, l'ISEN, l'école...\nVoir les exemples ci-dessous.")

# Champ de saisie pour la question
question = st.text_area("Question :", value='')

# Champ de saisie pour la réponse
response = st.text_area("Réponse :", value='')

# Bouton pour valider
if st.button("Ajouter"):
    if question.strip() == "":
        st.error("Veuillez saisir une question.")
    elif response.strip() == "":
        st.error("Veuillez saisir une réponse.")
    else:
        # Traitement et affichage de la question et de la réponse
        doc = {"instruction": question, "output": response}
        collection.insert_one(doc)
        st.success("Question et réponse envoyées avec succès !")
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


st.markdown("---")
st.markdown("### Exemples")
df = pd.DataFrame(list(examples))
st.write(df)