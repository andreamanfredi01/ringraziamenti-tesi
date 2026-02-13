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

st.markdown(
    "<h1 style='text-align: center;'>Un ringraziamento speciale</h1>",
    unsafe_allow_html=True
)


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

SHEET_NAME = "lista"  
sheet = client.open(SHEET_NAME).sheet1

# -------------------------------
# LINK IMMAGINI GITHUB
# -------------------------------
GITHUB_IMG_BASE_URL = "https://raw.githubusercontent.com/tuo_nome_utente/tesi-ringraziamenti/main/img/"
GITHUB_VIDEO_BASE_URL = "https://raw.githubusercontent.com/tuo_nome_utente/tesi-ringraziamenti/main/videos/"

# -------------------------------
# PASSWORD DA SECRETS
# -------------------------------
personal_thanks = {
     "laura facchinetti": {
        "category": "genitore",
        "password": st.secrets["MAMMA_PASSWORD"],
        "message": "",
        "image": "giulia_bianchi.jpg"
    },
    "giorgio manfredi": {
        "category": "genitore",
        "password": st.secrets["PAPI_PASSWORD"],
        "message": "",
        "image": "giulia_bianchi.jpg"
    },
    "chiara manfredi": {
        "category": "sorella",
        "password": st.secrets["CHIARA_PASSWORD"],
        "message": "Ciao ciccia Chiara ho fornuto anche questa e non é stato facile assai. Ci sono momenti difficili, di smarrimento che nessuno sa e che ti sto raccontando adesso, momenti che affronterai anche te e quando ti sembrerà di non sapere che fare, devi saper valutare tutte le opzioni e saper fare le scelte giuste, e la scelta giusta spesso é non scegliere, attendere, e aspettare il momento giusto per fare ciò che ti senti.

                    Ti ringrazio per esserti concessa l’opportunità di avermi accanto. 
                    
                    Ora andrò a lavorare magari lontano o magari no, ovunque vada sappi che potrai venirmi a trovare quando vorrai. Penso che comprerò un animaletto se andrò lontano e lo chiamerò cicciaobesachiara. Appena avrò una minima stabilità economica di riserverò un trattamento speciale, che a me sarebbe piaciuto molto, ma ne parleremo.",
        "video": "chiara.mov"
    },
    "francesco manfredi": {
        "category": "fratello",
        "password": st.secrets["CICCIO_PASSWORD"],
        "message": "Ciao Ciccio,
                    Ti ringrazio per essere presente in questo momento. É stato un anno di cambiamenti sotto diversi aspetti per te e presto lo sarà anche per me. So che hai passato periodi migliori, e se vuoi parlare di qualcosa sono qua. O ciccia Chiara anche, se preferisci parlare con lei, la obbligo, basta chiedere.
                    So molto poco di tutta la situazione, ma ti dico solo che non c’é motivo di stare così,  vivila con più leggerezza e parlane con qualcuno, anche un professionista o un prete, serve a liberarsi e lasciarsi andare.
                    Mettiti sempre al primo posto.
                    Per il resto ti ringrazio anche per il futuro, so che nel caso venissi a lavorare a Milano mi ospiteresti gràtis da buon terrone e non é da tutti gràtis",
        "video": "chiara.mov"
    },
    "sara ravelli": {
        "category": "",
        "password": st.secrets["SARA_PASSWORD"],
        "message": "Ciao cuore,

                    É finita anche questa e anche stavolta si prospettano cambiamenti. Cambiamenti importanti, d’altronde non c’è due senza tre, ma ci sono anche le eccezioni! E quindi si siamo ancora qua e vedremo cosa ci riserverà il futuro, non posso prometterti nulla, non me la sento di prometterti nulla, valuterò tutte le opzioni prima dal punto di vista lavorativo e poi le rivaluterò tutte dal punto di vista personale. Sei molto molto molto importante per me e vorrei supporto e aiuto nel scegliere, e la ciliegina sarebbe che tu fossi aperta a più orizzonti. Al momento siamo ancora qua, ne abbiamo passate tante e non penso questa sia più difficile di altre, é solo la prossima sfida. 
                    
                    Ti ringrazio per tutto, tutti i momenti belli trascorsi insieme ma anche tutti i momenti complicati: é tutto ciò che mi ha portato fin qui, fino ad oggi un momento speciale, sofferto, voluto e interminabile a tratti, un momento che voglio godermi con te, che mi conosci meglio di tutti ",
        "video": "chiara.mov"
    },
    "noa linan": {
        "category": "dublino",
        "password": st.secrets["NOA_PASSWORD"],
        "message": "Noa, Noa, Noa…
                    La rizada más increíble                     
                    ¿Qué decir? Ya te he dicho casi todo después de la despedida, pero si estás leyendo esto, habrà un motivo.                 
                    Creo que el período que pasé en Dublín fue un tornado de cosas y, al volver a casa y procesarlo todo, me di cuenta de que he encontrado a una persona con defectos por todos lados… para, para, para.                   
                    He encontrado a una persona en la que descubría algo bueno cada vez, y cada vez con un matiz diferente. Tienes una luz interior muy fuerte y también te digo que la noche en la que hablamos toda la noche fue algo que nunca me había pasado con otras personas.
                                                     
                    Tengo un recuerdo especial de ti y espero cruzar tu camino otra vez.",
        "video": "chiara.mov"
    },
    "manuel cueto": {
        "category": "dublino",
        "password": st.secrets["MANUEL_PASSWORD"],
        "message": "Hola, niño, ¿qué tal?
                    Qué increíble es la vida. A veces la fortuna está ciega… y otras veces ve perfectamente. Cuando abrí la puerta del piso por primera vez, no me imaginaba que iba a compartir tres meses con una modelo sueca ninfo de 1,90… pero tampoco con Bin Laden.
                    Luego te encontré a ti y pasé algunos de los mejores meses de mi vida. Fue una experiencia increíble y te agradezco todos los momentos que compartimos.
                    Eres un bravo niño y muy maduro para tu edad. Sigue así y nos vemos pronto.
                    PS La sueca ninfo tampoco habría estado mal, la verdad…",
        "video": "chiara.mov"
    },
    "andrea cucco": {
        "category": "amici",
        "password": st.secrets["CUCCO_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "andrea monti": {
        "category": "amici",
        "password": st.secrets["SCIMMIA_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "gabriel persico": {
        "category": "amici",
        "password": st.secrets["GABA_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "david marchese": {
        "category": "amici",
        "password": st.secrets["DAVID_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "matteo locatelli": {
        "category": "amici",
        "password": st.secrets["MATTI_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "luca pesaresi": {
        "category": "amici",
        "password": st.secrets["KAPPA_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "davide villa": {
        "category": "amici",
        "password": st.secrets["VILLA_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "francesco cantini": {
        "category": "amici",
        "password": st.secrets["CANTI_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "marco pastore": {
        "category": "amici",
        "password": st.secrets["PASTO_PASSWORD"],
        "message": "",
        "video": "chiara.mov"
    },
    "riccardo galimberti": {
        "category": "redona",
        "password": st.secrets["RICHI_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "luca galimberti": {
        "category": "redona",
        "password": st.secrets["LUCA_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "filippo rossi": {
        "category": "redona",
        "password": st.secrets["ROVO_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "diego gandossi": {
        "category": "redona",
        "password": st.secrets["DIEGO_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "federico mistri": {
        "category": "redona",
        "password": st.secrets["FEDE_PASSWORD"],
        "message": "Caro Mario, grazie per esserci sempre stato, anche nei momenti più difficili. Questo traguardo porta anche il tuo nome.",
        "video": "chiara.mov"
    },
    "nicola piazzalunga": {
        "category": "",
        "password": st.secrets["NICOLA_PASSWORD"],
        "message": "Grazie per aver fatto parte di questo lungo percorso, che ora giunge al termine.
                    È stato un lungo viaggio dalle superiori, da spaccarsi dal ridere.
                    Stavo riguardando quel poco che mi è rimasto in galleria e ne è passato parecchio di tempo…
                    bei momenti",
        "video": "chiara.mov"
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
category_content = {
    "genitore": {
        "message": """Ciao genitori,

Vi ringrazio per avermi permesso di studiare qua. Siete stati molto disponibili, anche troppo, a permettermi questo corso magistrale. Più di 20000 euro in un paio di anni, quanti soldi — ma poi sì, vostro figlio si laurea alla Cattolica, certo. Ma in cosa? Mercati? Computer? Non saprei come descriverlo senza sembrare altezzoso e spocchioso come alcune persone che ho incontrato qua dentro, e quindi evito. È comunque molto spendibile e richiesta.

Vi ringrazio per ogni cosa che avete fatto per me e soprattutto per tutte le “battaglie” che ho portato e porto avanti con voi: se non le avessi fatte sarei uscito macellato da qua. C’è chi esce con 110 e lode da questo corso, come negli altri, ma anche avendo fatto il corso perfetto per me non avrei mai ottenuto quei voti. Non fa per me.

In ogni caso ho finito e ora vedrò che fare. Neanche l’Italia forse fa per me, ma per questo mi prenderò del tempo per valutare.

Nel ringraziarvi vi invito a leggere un testo che avevo scritto in quarta o quinta superiore, se lo abbiamo ancora o se lo abbiamo mai avuto.""",
        "image": "genitori.jpg",
        "video": "genitori.mp4"
    },

    "amici": {
        "message": """Grazie per aver fatto parte di questo lungo percorso, che ora giunge al termine.

Che dire se non… grazie per tutti i momenti condivisi e per quelli che ancora ci aspettano.

E ora… in alto i calici!""",
        "image": "amici.jpg",
        "video": "amici.mp4"
    },

    "redona": {
        "message": """Grazie per aver fatto parte di questo lungo percorso, che ora giunge al termine.

Che dire se non… grazie per tutti i momenti condivisi e per quelli che ancora ci aspettano.

E ora… in alto i calici!""",
        "image": "redona.jpg",
        "video": "redona.mp4"
    }
}

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
            
                category = data.get("category")
            
                # -------- IMMAGINE CATEGORIA --------
                if category in category_content and category_content[category].get("image"):
                    st.image(
                        GITHUB_IMG_BASE_URL + category_content[category]["image"],
                        use_container_width=True
                    )
            
                # -------- VIDEO CATEGORIA --------
                if category in category_content and category_content[category].get("video"):
                    st.video(
                        GITHUB_VIDEO_BASE_URL + category_content[category]["video"]
                    )
            
                # -------- IMMAGINE PERSONALE (EXTRA) --------
                if data.get("image"):
                    st.image(
                        GITHUB_IMG_BASE_URL + data["image"],
                        caption=f"Un ricordo speciale per {nome_input.title()}",
                        use_container_width=True
                    )
            
                # -------- VIDEO PERSONALE (EXTRA) --------
                if data.get("video"):
                    st.video(
                        GITHUB_VIDEO_BASE_URL + data["video"]
                    )
            
                # -------- MESSAGGIO --------
                if data.get("message"):
                    final_message = data["message"]
                elif category in category_content:
                    final_message = category_content[category]["message"]
                else:
                    final_message = default_message
            
                st.markdown(f"**{final_message}**")
            
            
            
