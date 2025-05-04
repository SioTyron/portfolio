import streamlit as st
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import requests
from st_clickable_images import clickable_images

st.set_page_config(layout="wide")

# --------------------------------
#           Fonctions 
# --------------------------------
def load_lottieUrl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --------------------------------
#           Liens 
# --------------------------------
lottie_dev = load_lottieUrl("https://lottie.host/82cffce2-eb7d-4550-91e7-2cae52c439cc/x6jPAZP0XR.json")
lottie_contact = load_lottieUrl("https://lottie.host/dbdaa6ee-87f1-4c6d-9178-55ea8ec09606/oqN1CqB2GH.json")
cv_url = "https://drive.google.com/file/d/1dUqLuY6PvAiKaE3lMbxlnmk7DyGN5yvV/view?usp=sharing"
tableau_synthese_url = "https://drive.google.com/file/d/1HgeU3vJEH4VP4mF2RtfHHRWPa1_hkw9_/view?usp=drive_link"


st.markdown(
    """
    <style>
    @media (max-width: 600px) {
        .reportview-container {
            flex-direction: column;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------
#           CSS 
# --------------------------------
st.markdown( """ <style> 
            bleu 
            { 
            color: #00b4b4; 
            font-weight: bold; 
            } 

            competences {
            color : #00b4b4
            }
            
            name {
            font-weight : bold;
            text-decoration : underline;
            }
            expand {
            text-align : center;
            }

            bold {
            font-weight : bold;
            }
            
            input[type=text],input[type=email], select, textarea {
            width : 100%;
            padding : 12px;
            border : 1px solid #ccc;
            border-radius : 4px;
            box-sizing : border-box;
            margin-top : 6px;
            margin-bottom : 16px;
            resize : vertical;
            }

            input[type=submit] {
            background-color: #04AA6D; /* Couleur de fond */
            color: white; /* Couleur du texte */
            padding: 16px 32px; /* Augmenter la taille du bouton */
            border: none; /* Pas de bordure */
            border-radius: 4px; /* Coins arrondis */
            cursor: pointer; /* Curseur en forme de main */
            font-size: 18px; /* Taille de la police */
            font-weight: bold; /* Texte en gras */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Ombre */
            transition: background-color 0.3s ease; /* Transition pour l'effet de survol */
            display: block; /* Afficher le bouton comme un bloc */
            margin: 0 auto; /* Centrer le bouton */
            }

            input[type=submit]:hover {
                background-color: #45a049; /* Couleur de fond au survol */
            }

            .container{
            border-radius : 5px;
            background-color : #f2f2f2;
            padding : 20px;
            }
            </style> """, unsafe_allow_html=True ) # Ajouter du texte avec les propriétés de la classe CSS 


# --------------------------------
#           Header Accueil 
# --------------------------------
st.write("##")
st.subheader("Bonjour, je suis Tyron :wave:")

col1, col2 = st.columns([1, 1])
with col1:
    st.title("Bienvenue sur mon Portfolio")
    #st.write("##")
    st.write("""
         Je m'appelle <name>de CHADIRAC-LARA Tyron</name>, 
         je suis <bleu>développeur web full stack</bleu> originaire de la <bleu>Guadeloupe :flag-gp:</bleu> et un <bleu>passionné d'informatique</bleu> !""", unsafe_allow_html=True)
    st.write("")
    # -- Lien Réseaux Sociaux -- 
    col99, col100 = st.columns(2)
    with col99:
        st.write("[LinkedIn](https://www.linkedin.com/in/tyron-de-chadirac-lara-1551322a3/)",unsafe_allow_html=True)
        st.write("---")
        st.link_button("📑 Télécharger mon CV", cv_url, help=None, type="secondary", icon=None, disabled=False, use_container_width=False)
    with col100:
        st.write("[GitHub](https://github.com/SioTyron)",unsafe_allow_html=True)
        st.write("---")
        st.link_button("↓ Télécharger mon tableau de synthèse", tableau_synthese_url, help=None, type="secondary", icon=None, disabled=False, use_container_width=False)

with col2:
    st_lottie(lottie_dev,width=400, height=300, loop=True, quality='high')

st.write("---")

# --------------------------------
#          NavBar Page 
# --------------------------------
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Accueil","Veille", "Projets", "Contact"],
        icons=["house","bell-fill", "briefcase", "phone"],
        orientation="horizontal",
        )

# --------------------------------
#         Section Accueil 
#        NavBar == Accueil
# --------------------------------
if selected == "Accueil":
    with st.container():
        st.write("##")
        st.title("À propos")
        #--------------------------------
        # -- Section qui suis-je --
        #--------------------------------
        st.subheader("Qui suis-je ?")
        st.write(""" Je  suis un jeune <bleu>développeur de 19 ans curieux et ambitieux</bleu>. D'abord intéressé par le développement web, j'ai commencé à me former
                     sur <bleu>OpenClassrooms dès la 3ème</bleu>. <br>Par la suite, j'ai choisi un cursus qui m'a permis d'approfondir mes connaissances à ce sujet, faisant de moi <bleu>un développeur web full stack.</bleu>
             """, unsafe_allow_html=True) 
        st.write("##")
        
        # --------------------------------
        # -- Section Formation -- 
        #--------------------------------
        st.subheader("Formation")
        st.write("")
        col3, col4 = st.columns([3, 2])
        #--------------------------------
        # -- Nom de l'école --
        #--------------------------------
        with col3:
            st.write(":school: LGT Baimbridge - BTS SIO Option SLAM") 
            with st.expander("Détails de la formation"):
                st.write(""" Le BTS SIO (Services Informatiques aux Organisations) est un diplôme de niveau Bac+2 qui forme des techniciens spécialisés dans les services informatiques. Il propose deux options :<br><br>
                            <bleu>-Option SISR (Solutions d'Infrastructure, Systèmes et Réseaux)</bleu> : Formation axée sur la gestion et la maintenance des réseaux et systèmes informatiques.<br><br>
                            <bleu>-Option SLAM (Solutions Logicielles et Applications Métiers)</bleu> : Formation centrée sur le développement et la maintenance des applications logicielles.
                            """,unsafe_allow_html=True)
        #--------------------------------
        # -- Dates --
        #--------------------------------
        with col4:
            st.write(" :calendar: 2023 - 2025")
            st.write("##")
        
        #--------------------------------
        # -- Section Expérience Pro --
        #--------------------------------
        st.write("##")
        st.subheader("Expériences professionnelles")
        st.write("")
        col5, col6 = st.columns([3, 2])
        # -- Intitulé des Postes -- 
        with col5:
            st.write(":office: Crédit Agricole Mutuel de Guadeloupe - *stagiaire au service informatique*")
            with st.expander("Activités Réalisées"):
                st.write(""" -Création d'une solution <bleu>logicielle sur Excel en VBA</bleu> pour simplifier le travail d'une collègue du service de 
                             comptabilité. <br>
                             -Création d'une <bleu>base de données</bleu> et un <bleu>serveur Syslog</bleu> pour récupérer les logs d'un PfSense <br>
                             -Interface graphique pour interpréter les logs en utilisant le <bleu>framework python : streamlit</bleu><br>
                             -Informatique de proximité <br>
                             -Création d'un <bleu>thème enfant sur WordPress</bleu> (avec et sans plugin) 
                     """,unsafe_allow_html=True)
                st.write("[Consulter l'attestation de stage](https://drive.google.com/file/d/1XYu2Uwhie--SL_-qruLNmTpqDu9LVyhw/view?usp=sharing)",unsafe_allow_html=True)
            st.write("##")
            st.write(" :office: La Créole Beach Hôtel & Spa - *stagiaire au service informatique*") 
            with st.expander("Activités Réalisées"):
                    st.write(""" -Création d’un site internet avec Wix pour un organisme de formation <br>
                             -Création de réseaux Wi-Fi avec <bleu>Unify</bleu> <br>
                             -Mise en place de <bleu>VLAN avec Unify</bleu> pour accueillir la CONCACAF <br>
                             -Mise en place d’ordinateurs portables piloté par <bleu>les règles de groupe de l'active directory (AD)</bleu> <br>
                             -<bleu>Exploitation de base de données avec python</bleu> pour créer une web app avec <bleu>streamlit</bleu> <br>
                             -<bleu>Maintenance d’équipement réseaux.</bleu>
                     """, unsafe_allow_html=True)
                    st.write("[Consulter l'attestation de stage](https://drive.google.com/file/d/1O1y7fGHOLFB2rYlGoMW6GvZZOCzRz1lk/view?usp=sharing)",unsafe_allow_html=True)
        # -- Dates -- 
        with col6:
            st.write(" :calendar: 9 Décembre 2024 - 17 Janvier 2025")
            st.write("##") 
            st.write("##")
            st.write(" :calendar: 6 Mai 2024 - 14 Juin 2024")
        
        st.write("##")
        st.subheader("Compétences")
        with st.container():
            col7, col8, col9 = st.columns([2,1,2])  
            with col7:
                st.write("<competences>Anglais</competences> - ⭐️⭐️⭐️⭐️☆",unsafe_allow_html=True)
                st.write("---")

                st.write("<competences>HTML/CSS</competences> - ⭐️⭐️⭐️⭐️☆",unsafe_allow_html=True)
                st.write("---")

                st.write("<competences>C++</competences> - ⭐️⭐️☆☆☆",unsafe_allow_html=True)
                st.write("---")
            with col9:
                st.write("<competences>SQL </competences>- ⭐️⭐️⭐️⭐️☆",unsafe_allow_html=True)
                st.write("---")

                st.write("<competences>PHP </competences>- ⭐️⭐️⭐️☆☆",unsafe_allow_html=True)
                st.write("---")

                st.write("<competences>Java Script</competences> - ⭐️⭐️☆☆☆",unsafe_allow_html=True)
                st.write("---")



# --------------------------------
#   Section Veille Technologique 
#   NavBar == Veille Technologique
# --------------------------------
if selected =="Veille":
    with st.container():
            #--------------------------------
            # -- Certifications --
            #--------------------------------
            st.header("Certifications")
            st.write("##")
            st.write("""Vous trouverez ici les certifications que j'ai <bleu>acquises</bleu>, celles qui sont <bleu>en cours d'acquisition</bleu>, ainsi que celles que <bleu>j'envisage de réaliser</bleu>.
                     
                     """,unsafe_allow_html=True)
            #--------------------------------
            # -- Menu de sélection des catégories de certifications --
            #--------------------------------
            certif_select_status = option_menu(
                menu_title=None,
                options=["Terminées","En Cours", "Envisagées"],
                icons=["award-fill","award", "calendar4-event"],
                orientation="horizontal",
            )
            #--------------------------------
            # -- Certifications Terminées --
            #--------------------------------
            if certif_select_status == "Terminées":
                st.write("##")
                st.write("""<bold>En cliquant sur le nom d'une certification, un apreçu de celle-ci s'affichera.</bold>""",unsafe_allow_html=True)
                col10, col11, col12 = st.columns(3)
                with col10: 
                    with st.expander("Cambridge"):
                        st.write("""Détails de la certification :<br>
                                 Certification de niveau de langue en anglais, délivrée par le centre de Cambridge. <br>
                                 L'épreuve se compose d'une épreuve Orale d'interraction en binôme face à un jurry.<br>
                                 Puis une épreuve écrite de compréhension Orale et Écrite.
                                 """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Mars 2023</bleu>",unsafe_allow_html=True)
                        st.write("<belu>Niveau B2</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1TTuv0BIHPpmm5WIRLABYL6EgMKPE77ve/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                    with st.expander("Certification HTML/CSS"):
                        st.write("""Détails de la certification :<br>
                                    Cette certification couvre les bases du HTML5 pour structurer le contenu (titres, paragraphes, liens, images) et du CSS3 pour la mise en forme et le style visuel.
                                    """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Mars 2025</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1QeAbchKwXZJBsgoaqS2Vtol-349hBrL9/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                    with st.expander("Certification Commuity Management"):
                        st.write("""Détails de la certification :<br>
                                    Cette certification présente les bases du métier de Community Manager. <br> Ainsi que les
                                    étapes d'une campagne éditoriale sur les réseaux sociaux. <br>
                                    """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Juin 2024</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1ABJLUlvDyrD8ljfd0d44NUCskE1Xt5Cm/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                with col11:
                    with st.expander("Pix"):
                        st.write(""" Détails de la certification :<br>
                                 Cette certification permet d'assurer un niveau de compétence numérique. <br>
                                 Il s'agit d'une certification reconnue par l'état. <br> Réunissant divers domaines de compétences numériques.<br>
                                 """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Février 2025</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1QFyzhjGCl64cGOJNI7d471CTLLLFs5L2/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                    with st.expander("Certification PHP/MySQL"):
                        st.write("""Détails de la certification :<br>
                                    Cette certification couvre les bases du langage PHP pour développer des fonctionnalités interactives et utilise MySQL pour gérer les bases de données. Permettant de créer des sites internet dynamiques.
                                    """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Avril 2025</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1twwZvzlEPdaSmbO50q7l9K0PrT4p79_y/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                    with st.expander("Certification Introduction Swift"):
                        st.write("""Détails de la certification :<br>
                                    Cette certification est une introduction au monde de la programmation IOS. <br>
                                    Elle permet de découvrir le langage Swift et de créer des applications IOS. <br> En utilisant Xcode et SwiftUI.
                                    """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Mars 2025</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1uzDcfuGqCE1NZ4H8m1cbOTmsR4RIkH1g/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                with col12:
                    with st.expander("Utilisez ChatGPT pour améliorer votre Productivité"):
                        st.write("""Détails de la certification :<br>
                                 Certification d'introduction au "prompt engineering". <br>
                                 Au cours de ce parcours, j'ai pu apprendre à utiliser ChatGPT pour améliorer ma productivité au quotidien. <br>
                                 Ainsi qu'à améliorer mes compétences en matière de rédaction des prompts pour obtenir des résultats précis.
                                 """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Janvier 2024</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1xCZRnQVyPKV5mk0rjPBm5WptAgHs9nww/view?usp=drive_link)",unsafe_allow_html=True)
                    st.write("##")
                    with st.expander("Augmentez votre trafic grâce au référencement naturel (SEO)"):
                        st.write("""Détails de la certification :<br>
                                 Cette certification couvre les bases du SEO, les bonnes pratiques pour optimiser le référencement naturel de son site web. Ainsi que les mauvaises pratiques qui peuvent pénaliser un site internet dans les classements.
                                 Nous y apprenons aussi à mettre en place une stratégie de référencement pour augmenter le trafic sur un site web (analyse de mots-clés, analyse des balises de la page...).
                                 """,unsafe_allow_html=True)
                        st.write("<bleu>Date d'obtention : Juin 2024</bleu>",unsafe_allow_html=True)
                        st.write("[Voir le certificat](https://drive.google.com/file/d/1T2GVqkWVz5-48kbLCAC3sEybLk1pdO_T/view?usp=drive_link)",unsafe_allow_html=True)
 
            #--------------------------------
            # -- Certifications En Cours --
            #--------------------------------
            if certif_select_status == "En Cours":
                st.write("##")
                st.header("Certifications")
                col13, col14, col15 = st.columns([2,1,2])  
                with col13:
                    st.write("Swift")
                    html_progress = 30
                    st.progress(html_progress)
                    st.write(f"Avancement : {html_progress}%")
                        
                    st.write("---")

                    st.write("Java")
                    java_progress = 55
                    st.progress(java_progress)
                    st.write(f"Avancement : {java_progress}%")

                    st.write("---")

                    st.write("C++")
                    php_sql_progress = 75
                    st.progress(php_sql_progress)
                    st.write(f"Avancement : {php_sql_progress}%")

                    st.write("---")

                    st.write("TOEIC")
                    csharp_progress = 50
                    st.progress(csharp_progress)
                    st.write(f"Avancement : {csharp_progress}%")

                with col15:
                    st.write("Python")
                    python_progress = 80
                    st.progress(python_progress)
                    st.write(f"Avancement : {python_progress}%")

                    st.write("---")

                    st.write("C#")
                    csharp_progress = 75
                    st.progress(csharp_progress)
                    st.write(f"Avancement : {csharp_progress}%")

                    st.write("---")

                    st.write("UI/UX Design")
                    csharp_progress = 75
                    st.progress(csharp_progress)
                    st.write(f"Avancement : {csharp_progress}%")
            st.write("##")
            #--------------------------------
            # -- Certifications Envisagées --
            #--------------------------------
            if certif_select_status == "Envisagées":
                st.write("Cette section regroupe les certifications que j'envisage de réaliser, ainsi que leur rapport avec mon projet professionnel.")
                st.write("")
                col1, col2, col3 = st.columns(3)
                with col1:
                    with st.expander("Big Data"):
                        st.write(""" J'envisage cette formation par curiosité pour l'exploitation de data avec python.<br>

                        """,unsafe_allow_html=True)
                with col2:
                    with st.expander("Sécurisez vos applications web avec l'OWASP"):
                        st.write(""" Cette certifitcaiton couvre les bases de la sécurité des applications web. <br> Elle est donc intéressante pour améliorer la sécurité des applications que je développe.
                        """,unsafe_allow_html=True)
                with col3:
                    with st.expander("C"):
                        st.write(""" Je souhaite m'orienter en licence après mon BTS.<br>
                                 Ainsi, j'aurais besoin de connaître les bases du language C pour suivre le programme de<br>
                                 Licence.

                        """,unsafe_allow_html=True)
            st.write("##")
            #--------------------------------
            # -- Outils Veille Techno --
            #--------------------------------

            st.header("Mes sources de Veille Technologique")
            st.write("##")
            col1, col2 = st.columns([1,2])
            with col1 :
                 st.image("Images/underscore.png", caption="Underscore_", width=200)
            with col2:
                 st.write("""<bold>Underscore_</bold> est une émission hedomadaire sur des sujets variés.<br>
                          Ils ont comme thème principal la technologie et traitent chaque mercredi de sujets tel que : 
                          <li>:robot_face: L'intelligence articielle</li>
                          <li>:newspaper: Les dernières innovations</li>
                          <li>:lock: La Cybersécurité</li>
                    """,unsafe_allow_html=True)
                 st.write(":globe_with_meridians:[YouTube](https://www.youtube.com/@Underscore_)")
            st.write("---")

            col1, col2 = st.columns([1,2])
            with col1 :
                 st.image("Images/ddev.jpeg", caption="Daily Dev", width=200)
            with col2:
                 st.write("""<bold>DailyDev</bold> est une extension qui permet de centraliser des flux RSS.<br>
                          Cet outil est spécialisé pour les nouvelles dans le domaine de l'informatique.<br>
                          Ainsi, il est possible de sélectionner nos sujets d'intérêts et de recevoir dans son "feed" des articles qui y sont liés.<br>
                          Cette plateforme professionnelle open-source est dédiée aux développeurs. <br>
                          Elle permet aux développeurs de se réunir pour apprendre et collaborer.
                    """,unsafe_allow_html=True)
                 st.write(":globe_with_meridians:[Daily Dev](https://daily.dev/fr-fr)")
            st.write("---")

            col1, col2 = st.columns([1,2])
            with col1 :
                 st.image("Images/feedly.png", caption="Feedly", width=200)
            with col2:
                 st.write("""<bold>Feedly</bold>Feedly est un agrégateur de flux RSS qui permet 
                          aux utilisateurs de centraliser et de suivre les actualités de leurs sites préférés en un seul endroit.<br>
                          En plus de faciliter la veille informationnelle, Feedly permet de partager les sources d'information sur les réseaux sociaux.<br>
                          Grâce à Feedly, il est possible de recevoir automatiquement des contenus provenant de divers sites web, qu'il s'agisse de journaux, de blogs ou d'autres sources d'information
                    """,unsafe_allow_html=True)
                 st.write(":globe_with_meridians:[Feedly](https://feedly.com/)")
            st.write("---")
                

# --------------------------------
#       Section Projets
#        NavBar == Projet
# --------------------------------
if selected =="Projets":
    st.header("Mes Projets")
    st.write("##")
         #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/PriceScope.png",caption="Price Scope", width=200)
    with col17:
        st.subheader("Price Scope")
        st.write(""" <bleu>Description du projet : </bleu><br>
                    Price Scope est un comparateur de prix collaboratif. <br>
                    En effet, il se base sur les données saisies par les utilisateurs pour comparer les prix des produits. <br>
                    Ce projet à pour vocation de permettre aux utilisateurs d'adapter leurs mode de consommation en fonction des prix pratiqués par les différents commerces.
                    """,unsafe_allow_html=True)
        st.write("Technologie Utilisée : <bold>Streamlit</bold>", unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Comparateur de Prix</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Mars 2025</bold>",unsafe_allow_html=True)
        st.write(":computer: [Voir le code du projet](https://github.com/SioTyron/PriceScope)")
        st.write(":globe_with_meridians: [Voir le projet en ligne](https://pricescope.streamlit.app/)")
    st.write("---") 
          #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/logoPlayCache.png",caption="Play Cache logo", width=200)
    with col17:
        st.subheader("Bibliothèque de Jeux")
        st.write(""" <bleu>Description du projet : </bleu><br>
                Play Cache est une application codée en Swift pour permettre la gestion de jeux originaux. <br>
                J'ai du utiliser des Api en PHP pour communiquer avec la base de données pour permettre les fonctionnalités suivantes :<br>
                <li>Recherche de jeux</li>
                <li>Ajout de jeux</li>
                <li>Suppression de jeux</li>
                <li>Modification de jeux</li>
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Application Responsive</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Janvier 2025</bold>",unsafe_allow_html=True)
        st.write(":computer: [Voir le code du projet](https://github.com/SioTyron/PlayCache)")
        st.write(":camera: [Voir le projet en image](https://drive.google.com/drive/folders/1EKR8oxnRQWCcK-Nlo4BnJqT8e-c5rtIg?usp=sharing)")
    st.write("---")
     #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/logo6.png",caption="Web Scraping", width=200)
    with col17:
        st.subheader("Web Scraping")
        st.write(""" <bleu>Description du projet : </bleu><br>
                    J'ai utiliser Python pour réaliser un programme de web scraping. <br> 
                    L'objectif de ce programme est de maintenir en ligne un site internet. <br>
                    J'utilise également un script tmux qui permet d'exécuter le programme en tâche de fond. <br>
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Projet Automatisation avec Python</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Janvier 2025</bold>",unsafe_allow_html=True)
        st.write(":computer: [Voir le code du projet](https://github.com/SioTyron/TBot/tree/main)")
        #st.write(":camera: [Voir une démonstration]()")
    st.write("---")
    #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/logo4.jpg",caption="Logo Excel", width=200)
    with col17:
        st.subheader("Macro Tri")
        st.write(""" <bleu>Description du projet : </bleu><br>
                    <li>Création d'une macro Excel pour trier des fichiers de comptabilités.</li>
                    <li>Réalisation d'un cas d'utilisation.</li>
                    <li>Réalisation d'une documentation de l'outil</li>
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Projet VBA Excel</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Décembre 2024</bold>",unsafe_allow_html=True)
        st.write(":camera: [Voir le projet](https://drive.google.com/drive/folders/1eJ4__XphThraIjkN3jZ7zZK8Rstl88DX?usp=drive_link)")
        st.markdown("*Vous y retrouverez également la documentation de l'outil*")
    st.write("---")
    #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/logo5.jpeg",caption="Logo AichiBox", width=200)
    with col17:
        st.subheader("Aichi Box")
        st.write(""" <bleu>Description du projet :</bleu> <br>
                   Il s'agit d'un projet de groupe consistant à créer une application de gestion pour une entreprise de grande distribution.<br>
                   Il fallait dans un premier temps créer les diagrammes de cas d'utilisation selon le cahier des charges qui nous à été remis.<br>
                   Durant ce projet, je m'assurais du développement des fonctionnalités de l'application avec le chef de projet.<br>
                   Notre troisième membre était chargé du design de l'application. Ainsi que de son implémentation dans le code.<br>
                 Notre projet regroupe les fonctionnalités suivantes : <br>""",unsafe_allow_html=True)
        with st.expander("En voir plus"):
                 st.write("""
                 <li>Connexion à une base de données pour la connexion à l'application</li>
                 <li>Une page concernant les articles</li>
                 <li>Une page concernant les clients</li>
                 <li>Une page concernant les commandes</li><br>
                 Chacune de ces pages propose des fonctionnalités comme :<br>
                 <li>La recherche d'un élément (lié à la base de données)</li>
                 <li>L'ajout d'un élément dans la base de données depuis l'application</li>
                 <li>La suppression d'un élément</li>
                 <li>La Modification d'un élément</li>
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Projet Application Java    </bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Novembre 2024</bold>",unsafe_allow_html=True)
        st.write(":computer: [Voir le code du projet](https://github.com/SioTyron/Aichi_Box)")
        st.write(":camera: [Voir le projet en image](https://drive.google.com/drive/folders/10zrWUwFr-13N_H2pa3HQciIeC7HquJ5a?usp=drive_link)")
    st.write("---")
     #-------------------------------------------------------
    col16, col17 = st.columns([1,2])
    with col16:
        st.image("Images/logo.png",caption="Logo Lavage Auto", width=200 )
    with col17:
        st.subheader("Lavage Auto")
        st.write(""" <bleu>Description du projet :</bleu> <br>
                    - Création d'un site vitrine dynamique pour une entreprise de lavage automobile. 
                    L'objectif est de pouvoir générer un devis en PDF via un formulaire html.
                    Il faut également afficher des prestations et des services depuis une base de données MySQL.<br>
                    J'ai implémenter une gestion d'un panier utilisateur pour ajouter des produits et des services, ainsi qu'une interface de paiement.
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Projet Web Dynamique MVC</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Octobre 2024</bold>",unsafe_allow_html=True)
        st.write(":camera: [Plus d'images](https://drive.google.com/drive/folders/1lDgOvAXOME41kVx0s-GfyIXS2Fn4Tv1h?usp=drive_link)")
    st.write("---")
     #-------------------------------------------------------
    col16,col17 = st.columns([1,2])
    with col16:
        st.image("Images/logo7.png",caption="Logo HT Auto", width=200)
    with col17:
        st.subheader("HtAuto")
        st.write(""" <bleu>Description du projet :</bleu> <br>
                   Il s'agit d'un projet Web en PHP en utilisant l'architecture <bold>MVC (Modèle Vue Controller)</bold><br>""",unsafe_allow_html=True)
        with st.expander("En voir plus"):
                 st.write("""
                 <li>Connexion à une base de données pour l'affichage des données <br>(les images sont également dans la base de données)</li>
                 <li>Option permettant de rechercher une voiture par rapport à son type</li>
                 <li>Option permettant de rechercher une voiture par rapport à sa marque</li>
                 <li>Une page de connexion pour les utilisateurs et pour les administrateurs</li><br>
                 Utilisation d'une varaible de session en php pour :<br>
                 <li>Ajouter une voiture dans la base de données via un formulaire</li>
                 <li>La Suppression d'une voiture dans le catalogue avec l'ajout d'un bouton supprimer</li>
                    """,unsafe_allow_html=True)
        st.write("Type de Projet : <bold>Projet Site Web Dynamique MVC</bold>", unsafe_allow_html=True)
        st.write("Date de réalisation : <bold>Mai 2024</bold>",unsafe_allow_html=True)
        #st.write(":computer: [Voir le code du projet](https://github.com/SioTyron/Aichi_Box)")
        st.write(":camera: [Voir le projet en image](https://drive.google.com/drive/folders/1W5ze1GB7Oadeq6xDvYr9xApr86kKV4R6?usp=drive_link)")
    st.write("---")
    col18, col19 = st.columns([1,2])
    with col18:
            st.image("Images/logo2.png", caption="Logo Jardin Saint-Eloi", width=200)
    with col19:
            st.subheader("Jardins Saint-Eloi")
            st.write("""
                    <bleu>Description du projet :</bleu> <br>
                    - Création d'un site vitrine statique pour une entreprise qui vend des bouquets de fleurs et des paniers de spécialités locales. 
                    L'objectif est de pouvoir présenter les produits proposés par l'entreprise.
                    Il faut également afficher un prix.<br>
                     <bold>Il s'agit de mon premier projet web en groupe</bold>
            """,unsafe_allow_html=True)
            st.write("Type de Projet : <bold>Projet Web Statique</bold>", unsafe_allow_html=True)
            st.write("Date de réalisation : <bold>Novembre 2023</bold>",unsafe_allow_html=True)
            st.write(":globe_with_meridians: [Voir le site en ligne](https://siotyron.github.io/projet-saint-eloi/)")
    st.write("---")
    #-------------------------------------------------------
    col18,col19 = st.columns([1,2])
    with col18:
        st.image("Images/logo3.jpeg",caption="FileZilla Logo",width=200)
    with col19:
            st.subheader("Serveur FTP")
            st.write("""
                    <bleu>Description du projet : </bleu><br>
                    - Création et configuration d'un serveur FTP (File Transfer Protocole) Avec FileZilla. <br>
                    - Création d'un tutoriel pour l'installation et la configuration du logiciel.
            """,unsafe_allow_html=True)
            st.write("Type de Projet : <bold>Projet FTP </bold>", unsafe_allow_html=True)
            st.write("Date de réalisation : <bold>Octobre 2023</bold>",unsafe_allow_html=True)
            st.write(":book: [Voir le tutoriel](https://a42c0f8f-a9c8-4e4c-af3c-2fb65312b092.filesusr.com/ugd/bc2be2_2568a300276748edbc79f37efb8ec027.pdf)")
    st.write("---")
     #-------------------------------------------------------

# --------------------------------
#         Section Contact 
#        NavBar == Contact
# --------------------------------
if selected =="Contact":
    st.write("##")
    st.header("Me Contacter")
    contact_form = """
                <form
                action="https://formspree.io/f/xrbpqqvl"
                method="POST">
                <input type="text" name="name" placeholder="Votre Nom" required>
                <input type="email" name="email" placeholder="Votre Email" required>
                <textarea name="message"placeholder="Votre Message" required></textarea>
                <button type="submit">Envoyer</button>
                </form>
             """
    left_col, right_col = st.columns([2,1])
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact,width=400, height=300,speed=0.1 , loop=True)

