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
         je suis <bleu>développeur web full stack</bleu> originaire de la <bleu>Guadeloupe</bleu> et un <bleu>passionné d'informatique</bleu> ! Je suis actuellement en deuxième année de BTS SIO option SLAM.""", unsafe_allow_html=True)
    st.write("")
    # -- Lien Réseaux Sociaux -- 
    # -- Lien Réseaux Sociaux -- 
    col99, col100 = st.columns(2)
    with col99:
        st.markdown("""
        <style>
            .social-badge {
                display: inline-flex;
                align-items: center;
                padding: 0.5rem 1rem;
                margin: 0.5rem 0;
                border-radius: 5px;
                background: #f0f2f6;
                color: #2d2d2d;
                text-decoration: none;
                transition: all 0.3s ease;
                border: 1px solid #d0d0d0;
            }
            .social-badge:hover {
                transform: translateY(-2px);
                box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
                background: #00b4b4;
                color: white;
            }
            .social-icon {
                font-size: 1.2rem;
                margin-right: 0.7rem;
            }
        </style>
        
        <a href='https://www.linkedin.com/in/tyron-de-chadirac-lara-1551322a3/' class='social-badge' target='_blank'>
            <span class='social-icon'>👔</span>
            LinkedIn
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <a href='{cv_url}' class='social-badge' download target='_blank'>
            <span class='social-icon'>📑</span>
            Télécharger mon CV
        </a>
        """, unsafe_allow_html=True)

    with col100:
        st.markdown(f"""
        <a href='https://github.com/SioTyron' class='social-badge' target='_blank'>
            <span class='social-icon'>💻</span>
            GitHub
        </a>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown(f"""
        <a href='{tableau_synthese_url}' class='social-badge' download target='_blank'>
            <span class='social-icon'>📊</span>
            Tableau de synthèse
        </a>
        """, unsafe_allow_html=True)

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
        #--------------------------------
        # -- Section qui suis-je --
        #--------------------------------
        st.subheader("À propos de moi")

        with st.container():
            st.markdown("""
            <style>
                .timeline-card {
                    padding: 1.5rem;
                    margin: 1rem 0;
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;
                }
                .timeline-card:hover {
                    transform: translateY(-5px);
                }
                .emoji-header {
                    font-size: 2.5rem;
                    margin-bottom: 1rem;
                }
                .highlight {
                    color: #00b4b4;
                    font-weight: 600;
                }
            </style>
            """, unsafe_allow_html=True)

            # Première ligne - Cartes horizontales
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="timeline-card">
                    <div class="emoji-header">🚀</div>
                    <h4 style='margin-bottom: 0.5rem;'>Mon Parcours</h4>
                    <ul style='list-style-type: none; padding-left: 0;'>
                        <li>▪️ Début en 3ème avec HTML/CSS</li>
                        <li>▪️ Formation OpenClassrooms</li>
                        <li>▪️ BTS SIO SLAM</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="timeline-card">
                    <div class="emoji-header">💻</div>
                    <h4 style='margin-bottom: 0.5rem;'>Mon Expertise</h4>
                    <ul style='list-style-type: none; padding-left: 0;'>
                        <li>▪️ Development Web Full Stack </li>
                        <li>▪️ Conception d'applications</li>
                        <li>▪️ Bases de données SQL</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown("""
                <div class="timeline-card">
                    <div class="emoji-header">🎯</div>
                    <h4 style='margin-bottom: 0.5rem;'>Ma Vision</h4>
                    <ul style='list-style-type: none; padding-left: 0;'>
                        <li>▪️ Transmettre mon savoir</li>
                        <li>▪️ Automatisation des tâches répétitives</li>
                        <li>▪️ Apprendre toujours plus</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        st.write("##")
        
        # --------------------------------
        # -- Section Formation -- 
        #--------------------------------
        st.subheader("🎓 Formation")
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown("""
                <div style='
                    padding: 1.5rem;
                    margin: 1rem 0;
                    background: #f8f9fa;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
                    border-left: 4px solid #00b4b4;
                    min-height: 180px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                '>
                    <div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <span style="font-size: 1.5rem;">🏫</span>
                            <div>
                                <h4 style="margin: 0;">BTS SIO Option SLAM</h4>
                                <p style="margin: 0; color: #6c757d;">LGT Baimbridge</p>
                            </div>
                        </div>
                        <details>
                            <summary style="cursor: pointer; color: #00b4b4; margin-top: 1rem;">Détails de la formation</summary>
                            <div style="margin-top: 1rem;">
                                <p>Le <strong>BTS SIO</strong> (Services Informatiques aux Organisations) propose deux options :</p>
                                <ul>
                                    <li><span style="color: #00b4b4;">SISR</span> : Solutions d'Infrastructure, Systèmes et Réseaux</li>
                                    <li><span style="color: #00b4b4;">SLAM</span> : Solutions Logicielles et Applications Métiers</li>
                                </ul>
                            </div>
                        </details>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style='
                    height: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 1.5rem;
                    background: white;
                    border-radius: 15px;
                    text-align: center;
                    min-height: 180px;
                '>
                    <div>
                        <div style="color: #00b4b4; font-weight: 600; font-size: 1.1rem; line-height: 1.4;">
                            📅 2023 - 2025
                        </div>
                        <div style="color: #6c757d; margin-top: 0.5rem;">
                            En cours
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Section Expérience Pro
        st.write("##")
        st.subheader("💼 Expériences Professionnelles")

        # Expérience 1
        with st.container():
            col3, col4 = st.columns([3, 1])
            
            with col3:
                st.markdown(f"""
                <div style='
                    padding: 1.5rem;
                    margin: 1rem 0;
                    background: #f8f9fa;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
                    border-left: 4px solid #00b4b4;
                    min-height: 220px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                '>
                    <div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <span style="font-size: 1.5rem;">🏦</span>
                            <div>
                                <h4 style="margin: 0;">Crédit Agricole Guadeloupe</h4>
                                <p style="margin: 0; color: #6c757d;">Stagiaire en informatique</p>
                            </div>
                        </div>
                        <details>
                            <summary style="cursor: pointer; color: #00b4b4; margin-top: 1rem;">🔍 Voir les réalisations</summary>
                            <div style="margin-top: 1rem;">
                                <ul>
                                    <li>Solution Excel VBA pour la comptabilité</li>
                                    <li>Base de données et serveur Syslog</li>
                                    <li>Interface Streamlit d'analyse de logs</li>
                                    <li>Thème WordPress personnalisé</li>
                                </ul>
                                <a href="https://drive.google.com/file/d/1XYu2Uwhie--SL_-qruLNmTpqDu9LVyhw/view" 
                                style="text-decoration: none; color: #00b4b4; font-size: 0.9rem;">
                                📎 Attestation de stage
                                </a>
                            </div>
                        </details>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown("""
                <div style='
                    height: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 1.5rem;
                    background: white;
                    border-radius: 15px;
                    text-align: center;
                    min-height: 220px;
                '>
                    <div>
                        <div style="color: #00b4b4; font-weight: 600; line-height: 1.4;">
                            📅 9 Déc 2024<br>au<br>17 Jan 2025
                        </div>
                        <div style="color: #6c757d; margin-top: 0.5rem;">
                            6 semaines
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Expérience 2
        with st.container():
            col5, col6 = st.columns([3, 1])
            
            with col5:
                st.markdown(f"""
                <div style='
                    padding: 1.5rem;
                    margin: 1rem 0;
                    background: #f8f9fa;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
                    border-left: 4px solid #00b4b4;
                    min-height: 220px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                '>
                    <div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <span style="font-size: 1.5rem;">🏨</span>
                            <div>
                                <h4 style="margin: 0;">Créole Beach Hôtel</h4>
                                <p style="margin: 0; color: #6c757d;">Stagiaire en informatique</p>
                            </div>
                        </div>
                        <details>
                            <summary style="cursor: pointer; color: #00b4b4; margin-top: 1rem;">🔍 Voir les réalisations</summary>
                            <div style="margin-top: 1rem;">
                                <ul>
                                    <li>Configuration réseau Unify</li>
                                    <li>Gestion Active Directory</li>
                                    <li>Application Streamlit</li>
                                    <li>Maintenance réseau</li>
                                </ul>
                                <a href="https://drive.google.com/file/d/1O1y7fGHOLFB2rYlGoMW6GvZZOCzRz1lk/view" 
                                style="text-decoration: none; color: #00b4b4; font-size: 0.9rem;">
                                📎 Attestation de stage
                                </a>
                            </div>
                        </details>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col6:
                st.markdown("""
                <div style='
                    height: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 1.5rem;
                    background: white;
                    border-radius: 15px;
                    text-align: center;
                    min-height: 220px;
                '>
                    <div>
                        <div style="color: #00b4b4; font-weight: 600; line-height: 1.4;">
                            📅 6 Mai 2024<br>au<br>14 Juin 2024
                        </div>
                        <div style="color: #6c757d; margin-top: 0.5rem;">
                            6 semaines
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        
        st.write("##")
        st.write("##")
    st.subheader("Technologies et Outils")
    st.markdown("**Liste des technologies et outils que j'utilise dans mes projets**")
    
    badges = [
        # Langages
        {"name": "Python", "url": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"},
        {"name": "Java", "url": "https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white"},
        {"name": "C%23", "url": "https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white"},
        {"name": "Swift", "url": "https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white"},
        
        # Web
        {"name": "HTML5", "url": "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"},
        {"name": "CSS3", "url": "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"},
        {"name": "JavaScript", "url": "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"},
        
        # Data
        {"name": "MySQL", "url": "https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"},
        {"name": "Pandas", "url": "https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"},
        {"name": "Plotly", "url": "https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"},
        
        # Frameworks
        {"name": "Bootstrap", "url": "https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"},
        {"name": "React Native", "url": "https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"},
        {"name": "Streamlit", "url": "https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"},
        
        # Design & Outils
        {"name": "Figma", "url": "https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white"},
        {"name": "Canva", "url": "https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white"},
        {"name": "Wix", "url": "https://img.shields.io/badge/Wix-0C6EFC?style=for-the-badge&logo=wix&logoColor=white"},
        {"name": "GitHub", "url": "https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"}
    ]

    categories = {
        "Langages": ["Python", "Java", "C%23", "Swift"],
        "Développement Web": ["HTML5", "CSS3", "Wix", "JavaScript"],
        "Data & Base de données": ["MySQL", "Pandas", "Plotly"],
        "Frameworks": ["Bootstrap", "React Native", "Streamlit"],
        "Design & Outils": ["Figma", "Canva", "GitHub"]
    }

    # Nouveau style avec catégories
    st.markdown("""
    <style>
    .badges-section {
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .category-title {
        color: #00b4b4;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .badges-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 1.2rem;
        padding: 0.5rem;
    }
    .badge-item {
        transition: transform 0.3s ease;
        text-align: center;
    }
    .badge-item:hover {
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)


    for category, items in categories.items():
        with st.container():
            st.markdown(f'<div class="badges-section">'
                        f'<div class="category-title">{category}</div>'
                        f'<div class="badges-grid">'
                        + ''.join([f'<div class="badge-item"><img src="{next(b["url"] for b in badges if b["name"] == item)}" height="60"></div>'
                                for item in items]) +
                        '</div></div>', 
                        unsafe_allow_html=True)

    st.write("---")



# --------------------------------
#   Section Veille Technologique 
#   NavBar == Veille Technologique
# --------------------------------
if selected == "Veille":
        with st.container():
            st.write("##")
            st.header("Certifications")
            st.write("##")
            st.markdown("""
            <style>
                .certif-card {
                    padding: 1.5rem;
                    margin: 1rem 0;
                    background: white;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s ease;
                    border-left: 4px solid #00b4b4;
                }
                .certif-card:hover {
                    transform: translateY(-3px);
                }
                .progress-card {
                    background: linear-gradient(45deg, #f8f9fa, #ffffff);
                    padding: 1.5rem;
                    border-radius: 15px;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
                }
            </style>
            """, unsafe_allow_html=True)

            # Menu de sélection
            certif_status = option_menu(
                menu_title=None,
                options=["Terminées", "En Cours", "Envisagées"],
                icons=["award-fill", "award", "calendar4-event"],
                orientation="horizontal",
            )

            # Certifications Terminées
            if certif_status == "Terminées":
                cols = st.columns(3)
                certifications = [
                    {
                        "title": "Cambridge English B2",
                        "icon": "🌐",
                        "date": "Mars 2023",
                        "details": "Certification de niveau d'anglais avec épreuves orales et écrites",
                        "link": "https://drive.google.com/file/d/1TTuv0BIHPpmm5WIRLABYL6EgMKPE77ve/view"
                    },
                    {
                        "title": "Promp Engineering Chat GPT",
                        "icon": "💬",
                        "date": "Janvier 2024",
                        "details": "Introduction au promp engineering et à l'utilisation de Chat GPT pour améliorer ma productivité.",
                        "link": "https://drive.google.com/file/d/1xCZRnQVyPKV5mk0rjPBm5WptAgHs9nww/view?usp=drive_link"
                    },
                    {
                        "title": "Référencement SEO",
                        "icon": "📈",
                        "date": "Juin 2024",
                        "details": "Maîtrise des fondamentaux du référencement Web et des stratégies d'optimisation.",
                        "link": "https://drive.google.com/file/d/1T2GVqkWVz5-48kbLCAC3sEybLk1pdO_T/view?usp=drive_link"
                    },
                    {
                        "title": "Community Manager",
                        "icon": "👥",
                        "date": "Juin 2024",
                        "details": "Bases de la gestion de communauté et des réseaux sociaux et des campagnes éditoriales",
                        "link": "https://drive.google.com/file/d/1ABJLUlvDyrD8ljfd0d44NUCskE1Xt5Cm/view?usp=drive_link"
                    },
                    {
                        "title": "Pix",
                        "icon": "💻",
                        "date": "Février 2025",
                        "details": "Certification de diverses compétences numériques de base.",
                        "link": "https://drive.google.com/file/d/1QFyzhjGCl64cGOJNI7d471CTLLLFs5L2/view?usp=drive_link"
                    },
                    {
                        "title": "HTML/CSS",
                        "icon": "🖥️",
                        "date": "Mars 2025",
                        "details": "Maîtrise des fondamentaux du développement web front-end",
                        "link": "https://drive.google.com/file/d/1QeAbchKwXZJBsgoaqS2Vtol-349hBrL9/view"
                    },
                    {
                        "title": "PHP/MySQL",
                        "icon": "⛁",
                        "date": "Avril 2025",
                        "details": "Maîtrise des bases de données et du langage PHP, pour la conception de sites web dynamiques.",
                        "link": "https://drive.google.com/file/d/1twwZvzlEPdaSmbO50q7l9K0PrT4p79_y/view?usp=drive_link"
                    },
                    {
                        "title": "Swift",
                        "icon": "< / >",
                        "date": "Avril 2025",
                        "details": "Introduction aux bases de la programmation IOS, avec Xcode et SwiftUI.",
                        "link": "https://drive.google.com/file/d/1uzDcfuGqCE1NZ4H8m1cbOTmsR4RIkH1g/view?usp=drive_link"
                    },
                ]

                for idx, certif in enumerate(certifications):
                    with cols[idx % 3]:
                        st.markdown(f"""
                        <div class="certif-card">
                            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                                <span style="font-size: 1.5rem;">{certif['icon']}</span>
                                <h4 style="margin: 0;">{certif['title']}</h4>
                            </div>
                            <p style="color: #6c757d; margin-bottom: 0.5rem;">{certif['details']}</p>
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="color: #00b4b4; font-size: 0.9rem;">{certif['date']}</span>
                                <a href="{certif['link']}" target="_blank" style="text-decoration: none; color: #00b4b4;">📎 Voir</a>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

            # Certifications En Cours
            elif certif_status == "En Cours":
                progresses = [
                    {"name": "Swift", "progress": 30, "icon": "📱"},
                    {"name": "Java", "progress": 55, "icon": "☕"},
                    {"name": "Python", "progress": 80, "icon": "🐍"},
                    {"name": "C++", "progress": 75, "icon": "🅲"},
                    {"name": "TOEIC", "progress": 50, "icon": "🇬🇧"},
                    {"name": "C#", "progress": 60, "icon": "💻"},
                    {"name": "UX/UI Desing", "progress": 30, "icon": "💻"},
                ]

                cols = st.columns(2)
                for idx, prog in enumerate(progresses):
                    with cols[idx % 2]:
                        st.markdown(f"""
                        <div class="progress-card">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                                <div style="display: flex; align-items: center; gap: 0.6rem;">
                                    <span style="font-size: 1.2rem;">{prog['icon']}</span>
                                    <h5 style="margin: 0;">{prog['name']}</h5>
                                </div>
                                <span style="color: #00b4b4;">{prog['progress']}%</span>
                            </div>
                            <div style="height: 8px; background: #f1f1f1; border-radius: 4px;">
                                <div style="width: {prog['progress']}%; height: 100%; background: #00b4b4; border-radius: 4px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        st.write("")

            # Section Envisagées
            elif certif_status == "Envisagées":
                st.write("##")
                certifications = [
                    {
                        "title": "Big Data",
                        "icon": "📊",
                        "details": "Exploitation de données avec Python"
                    },
                    {
                        "title": "Sécurité OWASP",
                        "icon": "🔒", 
                        "details": "Bonnes pratiques de sécurité web"
                    },
                    {
                        "title": "Langage C",
                        "icon": "🅒",
                        "details": "Pour ma poursuite d'études"
                    },
                    {
                        "title": "Gestion de Projet",
                        "icon": "📈",
                        "details": "Compétence clé pour la gestion de projets"
                    },
                ]

                cols = st.columns(3)
                for i, cert in enumerate(certifications):
                    with cols[i % 3]:
                        st.markdown(f"""
                        <div class="certif-card">
                            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                                <span style="font-size: 1.5rem;">{cert['icon']}</span>
                                <h4 style="margin: 0;">{cert['title']}</h4>
                            </div>
                            <p style="color: #6c757d; margin-bottom: 0.5rem;">{cert['details']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                st.write("##")
            #--------------------------------
            # -- Outils Veille Techno --
            #--------------------------------
            st.write("##")
            st.write("##")
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

