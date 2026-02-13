import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# ------------------------------------------------
# CONFIGURAZIONE PAGINA
# ------------------------------------------------
st.set_page_config(
    page_title="Ringraziamenti",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.stTextInput input {
    text-align: center;
}
img, video {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Un ringraziamento speciale</h1>", unsafe_allow_html=True)

# ------------------------------------------------
# GOOGLE SHEETS
# ------------------------------------------------
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)
sheet = client.open("lista").sheet1

# ------------------------------------------------
# URL MEDIA
# ------------------------------------------------
GITHUB_IMG_BASE_URL = "https://raw.githubusercontent.com/andreamanfredi01/tesi-ringraziamenti/main/img/"
GITHUB_VIDEO_BASE_URL = "https://raw.githubusercontent.com/andreamanfredi01/tesi-ringraziamenti/main/img/"

# ------------------------------------------------
# FUNZIONE PER MOSTRARE MEDIA (supporta lista o singolo)
# ------------------------------------------------
def show_images(images, caption=None):
    if isinstance(images, list):
        for img in images:
            st.image(GITHUB_IMG_BASE_URL + img, use_container_width=True)
    else:
        st.image(GITHUB_IMG_BASE_URL + images, caption=caption, use_container_width=True)

def show_videos(videos):
    if isinstance(videos, list):
        for vid in videos:
            st.video(GITHUB_VIDEO_BASE_URL + vid)
    else:
        st.video(GITHUB_VIDEO_BASE_URL + videos)

# ------------------------------------------------
# DATI PERSONALIZZATI (STRINGHE LUNGHE SISTEMATE)
# ------------------------------------------------
personal_thanks = {

    "chiara manfredi": {
        "category": "sorella",
        "password": st.secrets["CHIARA_PASSWORD"],
        "message": """Ciao ciccia Chiara,

Ho finito anche questa e non è stato facile.  
Ci sono momenti difficili, di smarrimento che nessuno sa e che ti sto raccontando adesso.

Quando ti sembrerà di non sapere che fare, devi valutare tutte le opzioni.  
E spesso la scelta giusta è non scegliere subito, ma aspettare il momento giusto.

Ti ringrazio per esserti concessa l’opportunità di avermi accanto.

Ovunque andrò potrai venirmi a trovare.  
Appena avrò stabilità economica ti riserverò un trattamento speciale.""",
        "video": "Chiara.mov"
    },

    "sara ravelli": {
        "category": "",
        "password": st.secrets["SARA_PASSWORD"],
        "message": """Ciao cuore,

È finita anche questa.  
Si prospettano cambiamenti importanti.

Sei molto importante per me e vorrei il tuo supporto nelle scelte future.  
Voglio godermi questo momento con te.""",
        "video": ["Sara1.mov", "Sara2.mov", "Sara3.mov"],
        "image": ["s1.PNG", "s2.PNG"]
    },

    "lista nomi": {
        "category": "lista",
        "password": st.secrets["LISTA_NOMI"],
        "message": "Qui puoi vedere la lista dei nomi inseriti."
    }
}

default_message = "Grazie per aver fatto parte del mio percorso."

category_content = {
    "amici": {
        "message": """Grazie per aver fatto parte di questo lungo percorso.

E ora… in alto i calici!""",
        "video": ["Gaba(1).mov", "Gaba.mov"]
    }
}

# ------------------------------------------------
# INPUT NOME
# ------------------------------------------------
nome_input = st.text_input("Inserisci Nome e Cognome").lower().strip()

# ------------------------------------------------
# SALVA CONTEGGIO
# ------------------------------------------------
if nome_input and nome_input != "lista nomi":
    records = sheet.get_all_records()
    found = False

    for i, row in enumerate(records):
        if row["nome"].lower() == nome_input:
            sheet.update_cell(i + 2, 2, int(row["conteggio"]) + 1)
            found = True
            break

    if not found:
        sheet.append_row([nome_input, 1])

# ------------------------------------------------
# LOGICA PRINCIPALE
# ------------------------------------------------
if nome_input:

    st.divider()

    data = personal_thanks.get(nome_input, None)

    if not data:
        st.error("Nome non trovato.")
        st.stop()

    st.success(f"Dedicato a: {nome_input.title()}")
    password_input = st.text_input("Inserisci la password", type="password")

    if password_input == data["password"]:

        if nome_input == "lista nomi":
            st.subheader("Lista nomi registrati")
            records = sheet.get_all_records()
            for row in sorted(records, key=lambda x: x["nome"]):
                st.write(f"- {row['nome'].title()} ({row['conteggio']} volte)")
        else:

            st.balloons()

            category = data.get("category")

            # MEDIA CATEGORIA
            if category in category_content:
                cat_data = category_content[category]

                if "image" in cat_data:
                    show_images(cat_data["image"])

                if "video" in cat_data:
                    show_videos(cat_data["video"])

            # MEDIA PERSONALI
            if "image" in data:
                show_images(data["image"])

            if "video" in data:
                show_videos(data["video"])

            # MESSAGGIO
            st.markdown(f"### 💌")
            st.markdown(data.get("message", default_message))
