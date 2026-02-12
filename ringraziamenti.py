# cd C:\Users\andre\PycharmProjects\Tesi\ringraziamenti
# streamlit run C:\Users\andre\PycharmProjects\Tesi\ringraziamenti\ringraziamenti.py
import streamlit as st
from dotenv import load_dotenv
import os



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
st.write("Inserisci il tuo nome e cognome per leggere il messaggio dedicato a te.")

# -------------------------------
# LINK IMMAGINI GITHUB
# -------------------------------
GITHUB_IMG_BASE_URL = "https://raw.githubusercontent.com/tuo_nome_utente/tesi-ringraziamenti/main/img/"

# -------------------------------
# CARICA PASSWORD DA .ENV
# -------------------------------
#dotenv_path = r"C:\Users\andre\PycharmProjects\Tesi\ringraziamenti\password.env"
load_dotenv(dotenv_path)

# -------------------------------
# FILE PER LOG NOMI INSERITI
# -------------------------------
FILE_NOMI = "nomi_inseriti.txt"

# -------------------------------
# PERSONE SPECIFICHE (PASSWORD DIVERSE)
# -------------------------------
personal_thanks = {
    "mario rossi": {
        "category": "amici",
        "password": os.getenv("MARIO_PASSWORD"),
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "image": "mario_rossi.jpg"
    },
    "giulia bianchi": {
        "category": "famiglia",
        "password": os.getenv("GIULIA_PASSWORD"),
        "message": "Giulia, il tuo supporto silenzioso è stato fondamentale. Grazie per aver creduto in me anche quando io non ci riuscivo.",
        "image": "giulia_bianchi.jpg"
    },
    # ---- lista nomi come “utente speciale” ----
    "lista nomi": {
        "category": "lista",
        "password": os.getenv("LISTA_NOMI"),  # password nel .env
        "message": "Qui puoi vedere la lista dei nomi inseriti.",
        "image": None
    }
}

# -------------------------------
# CATEGORIE GENERALI (LIBERE)
# -------------------------------
category_thanks = {
    "famiglia": {
        "message": "Alla mia famiglia: grazie per il sostegno costante e per essere sempre stata il mio punto fermo.",
        "image": "famiglia.jpg"
    },
    "amici": {
        "message": "Ai miei amici: grazie per le risate, la leggerezza e la forza che mi avete dato in questo percorso.",
        "image": "amici.jpg"
    }
}

# -------------------------------
# DEFAULT
# -------------------------------
default_message = "Grazie per aver fatto parte del mio percorso."
default_image = "default.jpg"

# -------------------------------
# INPUT UTENTE
# -------------------------------
nome_input = st.text_input("Inserisci Nome e Cognome").lower().strip()

# -------------------------------
# SALVA NOME INSERITO
# -------------------------------
if nome_input and nome_input != "lista nomi":
    with open(FILE_NOMI, "a", encoding="utf-8") as f:
        f.write(nome_input + "\n")

# -------------------------------
# LOGICA PRINCIPALE
# -------------------------------
if nome_input:
    st.write("---")

    # recupera dati personalizzati, altrimenti crea placeholder
    data = personal_thanks.get(nome_input, {
        "category": "generale",
        "password": "placeholder",  # password fittizia per chi non c'è
        "message": "Presto ci sarà il tuo messaggio personalizzato!",
        "image": default_image
    })

    st.success(f"### Dedicato a: {nome_input.title()}")
    st.warning("🔒 Questo messaggio è protetto")

    password_input = st.text_input("Inserisci la password", type="password")

    if password_input:
        if password_input == data["password"]:
            # ---- CASO SPECIALE: LISTA NOMI ----
            if nome_input == "lista nomi":
                st.success("📋 Lista dei nomi inseriti:")
                if os.path.exists(FILE_NOMI):
                    with open(FILE_NOMI, "r", encoding="utf-8") as f:
                        nomi = sorted(set(f.read().splitlines()))
                    for n in nomi:
                        st.write(f"- {n.title()}")
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
