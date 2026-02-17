import streamlit as st
import os
import gspread
from google.oauth2.service_account import Credentials


PARENTI = [
    "claudia facchinetti",
    "umberto facchinetti",
    "paola facchinetti",
    "stefano facchinetti",
    "enrico facchetti",
    "massimo facchetti",
    "barbara malinverni",
    "giuseppe fogaroli",
    "giulio fogaroli",    
    "giuseppe pagani",
    "gabriele pagani",
    "anna manfredi",
    "maria manfredi",
    "luca varinelli",
    "alberto varinelli",
    "giovanni varinelli "
]

# -------------------------------
# CONFIGURAZIONE PAGINA
# -------------------------------
st.set_page_config(page_title="Ringraziamenti", page_icon="🎓")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0c1e61;
    }

    /* Rende il testo leggibile su sfondo scuro */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #f5f5f5 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
GITHUB_IMG_BASE_URL = "https://raw.githubusercontent.com/andreamanfredi01/ringraziamenti-tesi/main/img/"
GITHUB_VIDEO_BASE_URL = "https://raw.githubusercontent.com/andreamanfredi01/ringraziamenti-tesi/main/img/"

# -------------------------------
# PASSWORD DA SECRETS
# -------------------------------
personal_thanks = {
     "laura facchinetti": {
        "category": "genitore",
        "password": st.secrets["MAMMA_PASSWORD"],
        "message": "",
        "image": "",
         "video" : "Mamms.mov"
    },
    "giorgio manfredi": {
        "category": "genitore",
        "password": st.secrets["PAPI_PASSWORD"],
        "message": "",
        "video": "Papi.mov"
    },
    "chiara manfredi": {
        "category": "sorella",
        "password": st.secrets["CHIARA_PASSWORD"],
        "message": """Ciao ciccia Chiara ho fornuto anche questa e non é stato facile assai. Ci sono momenti difficili, di smarrimento che nessuno sa e che ti sto raccontando adesso, momenti che affronterai anche te e quando ti sembrerà di non sapere che fare, devi saper valutare tutte le opzioni e saper fare le scelte giuste, e la scelta giusta spesso é non scegliere, attendere, e aspettare il momento giusto per fare ciò che ti senti. 
        Ti ringrazio per esserti concessa l’opportunità di avermi accanto.
        Ora andrò a lavorare magari lontano o magari no, ovunque vada sappi che potrai venirmi a trovare quando vorrai. Penso che comprerò un animaletto se andrò lontano e lo chiamerò cicciaobesachiara. Appena avrò una minima stabilità economica di riserverò un trattamento speciale, che a me sarebbe piaciuto molto, ma ne parleremo.""",
        "video": "Chiara.mov"
    },
    "francesco manfredi": {
        "category": "fratello",
        "password": st.secrets["CICCIO_PASSWORD"],
        "message": """Ciao Ciccio,
        Ti ringrazio per essere presente in questo momento. É stato un anno di cambiamenti sotto diversi aspetti per te e presto lo sarà anche per me. So che hai passato periodi migliori, e se vuoi parlare di qualcosa sono qua. O ciccia Chiara anche, se preferisci parlare con lei, la obbligo, basta chiedere.
        So molto poco di tutta la situazione, ma ti dico solo Mettiti sempre al primo posto e che non c’é motivo di stare così,  vivila con più leggerezza e parlane con qualcuno.
        Per il resto ti ringrazio anche per il futuro, so che nel caso venissi a lavorare a Milano mi ospiteresti gràtis da buon terrone e non é da tutti gràtis""",
        "video": "Bismarck.mov"
    },
    "sara ravelli": {
        "category": "",
        "password": st.secrets["SARA_PASSWORD"],
        "message": """Ciao cuore,
        É finita anche questa e anche stavolta si prospettano cambiamenti. Cambiamenti importanti, d’altronde non c’è due senza tre, ma ci sono anche le eccezioni! E quindi si siamo ancora qua e vedremo cosa ci riserverà il futuro, non posso prometterti nulla, non me la sento di prometterti nulla, valuterò tutte le opzioni prima dal punto di vista lavorativo e poi le rivaluterò tutte dal punto di vista personale. Sei molto molto molto importante per me e vorrei supporto e aiuto nel scegliere, e la ciliegina sarebbe che tu fossi aperta a più orizzonti. Al momento siamo ancora qua, ne abbiamo passate tante e non penso questa sia più difficile di altre, é solo la prossima sfida. 
        Ti ringrazio per tutto, tutti i momenti belli trascorsi insieme ma anche tutti i momenti complicati: é tutto ciò che mi ha portato fin qui, fino ad oggi un momento speciale, sofferto, voluto e interminabile a tratti, un momento che voglio godermi con te, che mi conosci meglio di tutti """,
        "video":["Sara3.mov", "Sara2.mov", "Sara1.mov" ],
        "image" : ["s1.PNG","s3.PNG", "s2.PNG" ]
    },
    "noa linan": {
        "category": "dublino",
        "password": st.secrets["NOA_PASSWORD"],
        "message": """Noa, Noa, Noa…
        La rizada más increíble
        ¿Qué decir? Ya te he dicho casi todo después de la despedida, pero si estás leyendo esto, habrà un motivo.
        Creo que el período que pasé en Dublín fue un tornado de cosas y, al volver a casa y procesarlo todo, me di cuenta de que he encontrado a una persona con defectos por todos lados… para, para, para.                   
        He encontrado a una persona en la que descubría algo bueno cada vez, y cada vez con un matiz diferente. Tienes una luz interior muy fuerte y también te digo que la noche en la que hablamos toda la noche fue algo que nunca me había pasado con otras personas.
        Tengo un recuerdo especial de ti y espero cruzar tu camino otra vez.""",
        "image": "dub.PNG",
        "video": "noa.MOV"         
    },
    "manuel cueto": {
        "category": "dublino",
        "password": st.secrets["MANUEL_PASSWORD"],
        "message": """Hola, niño, ¿qué tal?
        Qué increíble es la vida. A veces la fortuna está ciega… y otras veces ve perfectamente. Cuando abrí la puerta del piso por primera vez, no me imaginaba que iba a compartir tres meses con una modelo sueca ninfo de 1,90… pero tampoco con Bin Laden.
        Luego te encontré a ti y pasé algunos de los mejores meses de mi vida. Fue una experiencia increíble y te agradezco todos los momentos que compartimos.
        Eres un bravo niño y muy maduro para tu edad. Sigue así y nos vemos pronto.
        PS La sueca ninfo tampoco habría estado mal, la verdad…""",
        "image" : ["dub.PNG", "manuel.jpg" , "manuel.PNG"]
    },
    "andrea cucco": {
        "category": "amici",
        "password": st.secrets["CUCCO_PASSWORD"],
        "message": "",
    },
    "andrea monti": {
        "category": "amici",
        "password": st.secrets["SCIMMIA_PASSWORD"],
        "message": "",
    },
    "gabriel persico": {
        "category": "amici",
        "password": st.secrets["GABA_PASSWORD"],
        "message": "",
    },
    "david marchese": {
        "category": "amici",
        "password": st.secrets["DAVID_PASSWORD"],
        "message": "",
    },
    "matteo locatelli": {
        "category": "amici",
        "password": st.secrets["MATTI_PASSWORD"],
        "message": "",
    },
    "luca pesaresi": {
        "category": "amici",
        "password": st.secrets["KAPPA_PASSWORD"],
        "message": "",
    },
    "davide villa": {
        "category": "amici",
        "password": st.secrets["VILLA_PASSWORD"],
        "message": "",

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

    },
    "riccardo galimberti": {
        "category": "redona",
        "password": st.secrets["RICHI_PASSWORD"],
        "message": "",
         "image" : ["richi.PNG" , "richi2.PNG", "richi3.PNG", "richi4.PNG"]
    },
    "luca galimberti": {
        "category": "redona",
        "password": st.secrets["LUCA_PASSWORD"],
        "message": "",
    
    },
    "filippo rossi": {
        "category": "redona",
        "password": st.secrets["ROVO_PASSWORD"],
        "message": "",
    
    },
    "diego gandossi": {
        "category": "redona",
        "password": st.secrets["DIEGO_PASSWORD"],
        "message": "",
    
    },
    "federico mistri": {
        "category": "redona",
        "password": st.secrets["FEDE_PASSWORD"],
        "message": "",
        "image" : ["fede1.PNG" , "fede2.PNG"]
    },
    "nicola piazzalunga": {
        "category": "",
        "password": st.secrets["NICOLA_PASSWORD"],
        "message": """Grazie per aver fatto parte di questo lungo percorso, che ora giunge al termine.
        È stato un lungo viaggio dalle superiori, da spaccarsi dal ridere.
        Stavo riguardando quel poco che mi è rimasto in galleria e ne è passato parecchio di tempo…
        bei momenti""",
        "image" : ["nicola2.PNG" , "nicola1.PNG", "nicola5.PNG", "nicola3.PNG"],
        "video" : "nicola.mp4"
    },
    
    
    "lista nomi": {
        "category": "lista",
        "password": st.secrets["LISTA_NOMI"],
        "message": "Qui puoi vedere la lista dei nomi inseriti.",
        "image": None
    }
}

default_message = "Grazie"
default_image = "default.jpg"
category_content = {
    "genitore": {
        "message": """Ciao genitori,
        Vi ringrazio per avermi permesso di studiare qua. Siete stati molto disponibili, anche troppo, a permettermi questo corso magistrale. Più di 20000 euro in un paio di anni, quanti soldi — ma poi sì, vostro figlio si laurea alla Cattolica, certo. Ma in cosa? Mercati? Computer? Non saprei come descriverlo senza sembrare altezzoso e spocchioso come alcune persone che ho incontrato qua dentro, e quindi evito. È comunque molto spendibile e richiesta.Vi ringrazio per ogni cosa che avete fatto per me e soprattutto per tutte le “battaglie” che ho portato e porto avanti con voi: se non le avessi fatte sarei uscito macellato da qua. C’è chi esce con 110 e lode da questo corso, come negli altri, ma anche avendo fatto il corso perfetto per me non avrei mai ottenuto quei voti. Non fa per me.
        In ogni caso ho finito e ora vedrò che fare. Neanche l’Italia forse fa per me, ma per questo mi prenderò del tempo per valutare.
        Nel ringraziarvi vi invito a leggere un testo che avevo scritto in quarta o quinta superiore, se lo abbiamo ancora o se lo abbiamo mai avuto.""",
    },

    "amici": {
        "message": """Grazie per aver fatto parte di questo percorso, che ora giunge al termine.
        Che dire se non… grazie per tutti i momenti condivisi e per quelli che ancora ci aspettano.
        E ora… in alto i calici!""",
        "video": ["Gaba(1).mov","Gaba.mov"]
    },

    "redona": {
        "message": """Grazie per aver fatto parte di questo percorso, che ora giunge al termine.
        Che dire se non… grazie per tutti i momenti condivisi e per quelli che ancora ci aspettano.
        E ora… in alto i calici!""",
        "video": ["Richi.mov","Richi(1).mov", "Richi(2).mov"]
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
    nome_norm = nome_input.strip().lower()

    # ---- CONTROLLO PARENTI SENZA PASSWORD ----
    if nome_norm in PARENTI:
        st.success(f"### Dedicato a: {nome_input.title()}")
        st.write("""
Ai miei parenti,
grazie per esserci stati in questo percorso, ognuno a modo suo.
Sapere che facevate il tifo per me è stato importante.
Sono felice di poter condividere questo traguardo con voi.
""")
        st.balloons()
    
    else:
        # Recupera dati della persona
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

                if nome_input == "lista nomi":
                    st.success("📋 Lista dei nomi inseriti:")
                    records = sheet.get_all_records()
                    if records:
                        for row in sorted(records, key=lambda x: x["nome"]):
                            st.write(f"- {row['nome'].title()} ({row['conteggio']} volte)")
                    else:
                        st.info("Nessun nome registrato.")
                else:
                    st.balloons()



            # -------- MESSAGGIO --------
            category = data.get("category")
            
            # Messaggio di categoria
            category_message = ""
            if category in category_content and category_content[category].get("message"):
                category_message = category_content[category]["message"]

            # Messaggio personale
            personal_message = data.get("message", "")

            # Combina messaggi: categoria prima, poi personale
            final_message = ""
            if category_message:
                final_message += category_message + "\n\n"
            if personal_message:
                final_message += personal_message

            st.markdown(final_message)
            
            # -------- EXTRA PER AMICI --------
            if category == "amici":
                st.write("---")
                if st.button("Quando hai bevuto clicca 👇"):
                    st.success("Gabri… Gabri giù tutto 🍻")
            
            if category == "redona":
                st.write("---")
                if st.button("Quando hai bevuto clicca 👇"):
                    st.success("Giù tutto Cunningham🍻")

            # -------- VIDEO --------
            # Video di categoria
            if category in category_content and category_content[category].get("video"):
                videos = category_content[category]["video"]
                if isinstance(videos, list):
                    for vid in videos:
                        st.video(GITHUB_VIDEO_BASE_URL + vid)
                else:
                    st.video(GITHUB_VIDEO_BASE_URL + videos)

            # Video personali
            if data.get("video"):
                videos = data["video"]
                if isinstance(videos, list):
                    for vid in videos:
                        st.video(GITHUB_VIDEO_BASE_URL + vid)
                else:
                    st.video(GITHUB_VIDEO_BASE_URL + videos)

            # -------- FOTO / IMMAGINI --------
            # Immagini di categoria
            if category in category_content and category_content[category].get("image"):
                images = category_content[category]["image"]
                if isinstance(images, list):
                    for img in images:
                        st.image(
                            GITHUB_IMG_BASE_URL + img,
                            use_container_width=True
                        )
                else:
                    st.image(
                        GITHUB_IMG_BASE_URL + images,
                        use_container_width=True
                    )

            # Immagini personali
            if data.get("image"):
                images = data["image"]
                if isinstance(images, list):
                    for img in images:
                        st.image(
                            GITHUB_IMG_BASE_URL + img,
                            use_container_width=True
                        )
                else:
                    st.image(
                        GITHUB_IMG_BASE_URL + images,
                        use_container_width=True
                    )
          





















