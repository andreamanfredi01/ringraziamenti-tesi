import streamlit as st
import os
import gspread
from google.oauth2.service_account import Credentials

# -------------------------------
# CONFIGURAZIONE PAGINA
# -------------------------------
st.set_page_config(page_title="Ringraziamenti", page_icon="🎓")

st.markdown("""
<style>
.main { text-align: center; }
.stTextInput { max-width: 400px; margin: 0 auto; }
.stImage { border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

st.title("Un ringraziamento speciale")
st.write("Inserisci nome e cognome per leggere il messaggio dedicato a te.")

# -------------------------------
# CONNESSIONE GOOGLE SHEETS
# -------------------------------
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)

SHEET_NAME = "lista"   # ⚠️ deve essere identico al nome del tuo foglio
sheet = client.open(SHEET_NAME).sheet1

# -------------------------------
# LINK IMMAGINI GITHUB
# -------------------------------
GITHUB_IMG_BASE_URL = "https://raw.githubusercontent.com/tuo_nome_utente/tesi-ringraziamenti/main/img/"

# -------------------------------
# PASSWORD DA SECRETS
# -------------------------------
personal_thanks = {
    "mario rossi": {
        "category": "amici",
        "password": st.secrets["MARIO_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "image": "mario_rossi.jpg"
    },
    "giulia bianchi": {
        "category": "famiglia",
        "password": st.secrets["GIULIA_PASSWORD"],
        "message": "Giulia, il tuo supporto silenzioso è stato fondamentale. Grazie per aver creduto in me anche quando io non ci riuscivo.",
        "image": "giulia_bianchi.jpg"
    },
    "lista nomi": {
        "category": "lista",
        "password": st.secrets["LISTA_NOMI"],
        "message": "Qui puoi vedere la lista dei nomi inseriti.",
        "image": None
    }
}

default_message = "Grazie per aver fatto parte del mio percorso."
default_image = "default.jpg"

# -------------------------------
# INPUT UTENTE
# -------------------------------
nome_input = st.text_input("Inserisci Nome e Cognome").lower().strip()

# -------------------------------
# SALVA / AGGIORNA CONTEGGIO
# -------------------------------
if nome_input and nome_input != "lista nomi":
    records = sheet.get_all_records()
    found = False

    for i, row in enumerate(records):
        if row["nome"].lower() == nome_input:
            current_count = int(row["conteggio"])
            sheet.update_cell(i + 2, 2, current_count + 1)
            found = True
            break

    if not found:
        sheet.append_row([nome_input, 1])

# -------------------------------
# LOGICA PRINCIPALE
# -------------------------------
if nome_input:
    st.write("---")

    data = personal_thanks.get(nome_input, {
        "category": "generale",
        "password": "placeholder",
        "message": "Presto vedrai il tuo messaggio!",
        "image": default_image
    })

    st.success(f"### Dedicato a: {nome_input.title()}")
    st.warning("🔒 Questo messaggio è protetto. Contattami per la password")

    password_input = st.text_input("Inserisci la password", type="password")

    if password_input:
        if password_input == data["password"]:

            # ---- LISTA NOMI CON CONTEGGIO ----
            if nome_input == "lista nomi":
                st.success("📋 Lista dei nomi inseriti:")

                records = sheet.get_all_records()

                if records:
                    for row in sorted(records, key=lambda x: x["nome"]):
                        st.write(f"- {row['nome'].title()} ({row['conteggio']} volte)")
                else:
                    st.info("Nessun nome registrato.")

            # ---- CASO NORMALE ----
            else:
                st.balloons()

                if data.get("image"):
                    st.image(
                        GITHUB_IMG_BASE_URL + data["image"],
                        caption=f"Per {nome_input.title()}",
                        use_container_width=True
                    )

                st.markdown(f"**{data['message']}**")

        else:
            st.error("❌ Password errata")

    st.write("---")

