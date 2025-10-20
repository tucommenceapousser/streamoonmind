# app.py
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime

# ---------- CONFIG ----------
# ---------- META TAGS (pour preview réseaux sociaux) ----------
st.markdown("""
<meta property="og:title" content="Compagnie MoonMind Anonymous">
<meta property="og:description" content="Collectif de hackers éthiques et créatifs, dédié à la sensibilisation numérique et à la protection de la vie privée.">
<meta property="og:image" content="/logo2.jpeg">
<meta property="og:url" content="https://moonmind.streamlit.app">
<meta property="og:type" content="website">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Compagnie MoonMind Anonymous">
<meta name="twitter:description" content="Collectif de hackers éthiques et créatifs, dédié à la sensibilisation numérique et à la protection de la vie privée.">
<meta name="twitter:image" content="/logo2.jpeg">
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="Compagnie MoonMind Anonymous",
    page_icon="😈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CSS / THEME ----------
st.markdown("""
<style>
:root{
    --bg:#060606;
    --panel:#0f1113;
    --accent:#00ff99;
    --muted:#7fffd4;
    --glass: rgba(255,255,255,0.03);
}
html, body, [class*="css"]  {
    background: radial-gradient(circle at 10% 10%, rgba(0,255,153,0.02), transparent 10%),
                radial-gradient(circle at 90% 90%, rgba(0,255,153,0.02), transparent 10%),
                var(--bg) !important;
    color: var(--accent);
    font-family: "Source Code Pro", "Courier New", monospace;
}
.stButton>button {
    background: transparent;
    border: 1px solid var(--accent);
    color: var(--accent);
    padding: 6px 12px;
    border-radius: 8px;
}
.stButton>button:hover {
    background: var(--accent);
    color: #0b0b0b;
}
.big-title { font-size: 42px; font-weight: 700; letter-spacing: 1px; color: var(--accent);}
.subtle { color: #9ef6c9; opacity: 0.9;}
.card {
    background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.02));
    border: 1px solid rgba(0,255,153,0.08);
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 6px 30px rgba(0,0,0,0.6);
}
.tag {
    display:inline-block;
    padding:4px 9px;
    border-radius:999px;
    border:1px solid rgba(0,255,153,0.12);
    margin-right:6px;
    font-size:13px;
}
hr { border: 0; height: 1px; background: rgba(0,255,153,0.06); margin: 12px 0 18px 0; }
</style>
""", unsafe_allow_html=True)

# ---------- Helper: sample OPs ----------
def default_ops():
    return [
        {"title": "#opvendetta",
         "description": "Campagne de sensibilisation et d'exposition publique visant à dénoncer des pratiques perçues comme injustes. (Description informative — aucun détail opérationnel fourni.)",
         "tags": ["dénonciation", "sensibilisation"],
         "status": "Active",
         "created": "2025-10-20"
        },
        {"title": "#opprivacy",
         "description": "Actions de sensibilisation autour de la protection de la vie privée en ligne et la promotion d'outils de chiffrement (activités éthiques, éducatives).",
         "tags": ["vie privée", "éducation"],
         "status": "En pause",
         "created": "2025-09-01"
        }
    ]

if "ops" not in st.session_state:
    st.session_state.ops = default_ops()

# ---------- SIDEBAR NAV ----------
st.sidebar.markdown("""
<div class='card'>
<div style='display:flex; align-items:center; gap:10px;'>
    <div style='font-size:28px'>😈</div>
    <div>
        <div style='font-weight:700'>Compagnie MoonMind Anonymous</div>
        <div class='subtle' style='font-size:12px'>Collectif — Hacking éthique & sensibilisation</div>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.selectbox("Navigation", ["Accueil", "Qu'est‑ce qu'Anonymous ?", "OPs en cours", "Ajouter une OP", "Mentions / Éthique"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Année**: 2025  •  **Style**: Hacker • Interface démo")
st.sidebar.markdown("---")
st.sidebar.caption("Cette interface est une présentation. Ne diffusez pas d'instructions illégales ni ne coordonnez d'activités illicites via cet outil.")

# ---------- HEADER + LOGOS + ANIMATION ----------
if page == "Accueil":
    # Logo principal
    st.image("logo1.jpeg", width=180, caption="Logo officiel de MoonMind Anonymous", use_container_width=False)
    st.markdown("<div class='big-title'>😈 Compagnie MoonMind Anonymous</div>", unsafe_allow_html=True)
    st.markdown("**Le collectif des esprits libres, hackers éthiques et créatifs.**")
    st.markdown("---")

    # Trois logos partenaires côte à côte
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("logo1.jpg", width=150, caption="Logo partenaire 1")
    with col2:
        st.image("logo2.jpeg", width=150, caption="Logo partenaire 2")
    with col3:
        st.image("logo.jpeg", width=150, caption="Logo partenaire 3")

    # Terminal-like animated intro
    html("""
    <div style="background:#071017; padding:14px; border-radius:10px; border:1px solid rgba(0,255,153,0.06); font-family: monospace;">
    <pre id="term" style="white-space:pre-wrap; color:#9ef6c9; margin:0;"></pre>
    </div>
    <script>
    const lines = [
      "Bienvenue dans la Compagnie MoonMind Anonymous...",
      "Nous explorons, éduquons et protégeons la liberté numérique.",
      "Hacking éthique, open-source, et actions de sensibilisation.",
      "Respect de la loi et responsabilité sont nos priorités."
    ];
    let idx = 0;
    let pos = 0;
    let out = '';
    function type(){
      if(idx < lines.length){
        if(pos < lines[idx].length){
          out += lines[idx][pos++];
          document.getElementById('term').innerText = out + "_";
          setTimeout(type, 28);
        } else {
          out += "\\n";
          idx++;
          pos = 0;
          setTimeout(type, 400);
        }
      } else {
        document.getElementById('term').innerText = out;
      }
    }
    type();
    </script>
    """, height=180)

    # Présentation
    st.markdown("### Qui sommes‑nous ?")
    st.markdown("""
    Compagnie MoonMind Anonymous est une entité créative s'inspirant des traditions du hacktivisme afin de promouvoir
    la sensibilisation numérique, la protection de la vie privée et l'accès à l'information. Nous favorisons l'éthique,
    l'éducation, et l'usage responsable des technologies.
    """)
    st.markdown("---")

    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("#### Nos activités (exemples)")
        st.markdown(
            "- Ateliers d'éducation à la cybersécurité\n"
            "- Publication d'outils open-source pédagogiques\n"
            "- Campagnes de sensibilisation sur la protection des données\n"
            "- Recherche et partage de bonnes pratiques"
        )
    with col2:
        st.markdown("#### Statut")
        st.markdown("<div class='card'><b>Collectif</b><br><span class='subtle'>Actif — axé sur l'éducation</span></div>", unsafe_allow_html=True)

# ---------- ABOUT ANONYMOUS ----------
elif page == "Qu'est‑ce qu'Anonymous ?":
    st.markdown("<div class='big-title'>❓ Qu'est‑ce qu'Anonymous ?</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    **Anonymous** est un terme utilisé pour décrire un ensemble décentralisé de personnes, groupes et acteurs en ligne
    partageant parfois des objectifs communs — souvent liés à la liberté d'information, la vie privée, et des actions de protestation.
    Il n'existe pas d'organisation centrale, de hiérarchie officielle, ni de structure formelle unique.
    """)
    st.info("""
    Historique / contexte :
    - Origines sur des forums et communautés en ligne (ex. 4chan) ; adoption du masque de Guy Fawkes comme symbole.
    - Actions variées : campagnes de sensibilisation, divulgations d'information, opérations de protestation en ligne.
    - Diversité d'acteurs : allant d'activistes pacifiques à des individus ayant commis des actes illégaux.
    """)
    st.markdown("#### Notions importantes")
    st.markdown("""
    - **Décenralisation** : pas de chef unique.  
    - **Symbolisme** : le masque de Guy Fawkes est un symbole culturel.  
    - **Ambiguïté éthique** : certaines actions ont visées l'intérêt public, d'autres ont enfreint la loi.  
    - **Responsabilité** : s'inspirer d'idéaux ne justifie pas des actions illégales — privilégier l'éducation et la légalité.
    """)
    st.markdown("---")
    st.warning("""
    Cette page explique le phénomène de manière informative. **Nous ne promouvons ni n'encourageons la commission d'actes illégaux.**
    Si vous êtes intéressé par la cybersécurité, formez‑vous, agissez de manière éthique, et respectez la loi.
    """)

# ---------- OPS ----------
elif page == "OPs en cours":
    st.markdown("<div class='big-title'>🔥 OPs en cours</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "Sur cette page sont listées des **opérations / campagnes** présentées à titre informatif. Aucune instruction opérationnelle n'est fournie."
    )

    # filters
    status_filter = st.selectbox("Filtrer par statut", ["Tous", "Active", "En pause", "Archivée"])
    tag_filter = st.text_input("Filtrer par tag (ex: sensibilisation, vie privée)", "")

    # display ops
    def show_op(op):
        st.markdown(f"<div class='card'><div style='display:flex; justify-content:space-between; align-items:center;'>"
                    f"<div><strong style='font-size:18px'>{op['title']}</strong><div class='subtle' style='font-size:12px'>Créée: {op.get('created','?')}</div></div>"
                    f"<div style='text-align:right'><span class='tag'>{op['status']}</span></div></div>"
                    f"<hr>"
                    f"<div style='margin-top:6px'>{op['description']}</div>"
                    f"<div style='margin-top:10px'>"
                    + " ".join([f"<span class='tag'>{t}</span>" for t in op.get("tags", [])])
                    + "</div></div>", unsafe_allow_html=True)

    any_shown = False
    for op in st.session_state.ops:
        if status_filter != "Tous" and op["status"] != status_filter:
            continue
        if tag_filter:
            if tag_filter.lower() not in " ".join(op.get("tags", [])).lower() and tag_filter.lower() not in op["title"].lower():
                continue
        show_op(op)
        any_shown = True

    if not any_shown:
        st.info("Aucune OP ne correspond aux filtres. Vous pouvez en ajouter une via 'Ajouter une OP'.")

# ---------- ADD OP ----------
elif page == "Ajouter une OP":
    st.markdown("<div class='big-title'>➕ Ajouter une OP (mockup)</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "Formulaire d'ajout **local** (stockage en session uniquement). **Ne partagez pas d'informations qui faciliteraient des actions illégales.**"
    )
    with st.form("add_op"):
        title = st.text_input("Titre (ex: #opvendetta)", value="#opnouvelle")
        description = st.text_area("Description (strictement informative - pas d'instructions)", value="Description de l'opération — expliquer le but et le cadre, sans détails opérationnels.")
        tags = st.text_input("Tags (séparés par des virgules)", value="sensibilisation, education")
        status = st.selectbox("Statut", ["Active", "En pause", "Archivée"])
        submitted = st.form_submit_button("Ajouter (mockup)")
        if submitted:
            new = {
                "title": title.strip(),
                "description": description.strip(),
                "tags": [t.strip() for t in tags.split(",") if t.strip()],
                "status": status,
                "created": datetime.utcnow().strftime("%Y-%m-%d")
            }
            st.session_state.ops.insert(0, new)
            st.success(f"OP '{new['title']}' ajoutée en session.")
            st.experimental_rerun()

# ---------- MENTIONS / ETHIQUE ----------
elif page == "Mentions / Éthique":
    st.markdown("<div class='big-title'>📜 Mentions & Éthique</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    **Avertissement légal & éthique**  
    Cette interface est conçue pour la présentation et l'éducation. Toute action en ligne doit respecter la loi.
    Si vous souhaitez apprendre la cybersécurité : suivez des formations reconnues, travaillez dans des environnements de test (labs),
    et adoptez une démarche responsable (responsible disclosure).
    """)
    st.markdown("#### Ressources recommandées")
    st.markdown("- OWASP (sécurité applicative)\n- Cours et certifications en cybersécurité\n- Communautés d'open-source et projets éducatifs")
    st.markdown("---")
    st.caption("© 2025 Compagnie MoonMind Anonymous — Présentation démo. Respectez la législation locale et l'éthique numérique.")

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='font-size:12px; color:#8fffc6'>Compagnie MoonMind Anonymous — Interface démo. Pour usages éducatifs uniquement.</div>", unsafe_allow_html=True)
