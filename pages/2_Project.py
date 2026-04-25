import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#e2e8f0"
    accent = "#22d3ee"
    glass = "rgba(255,255,255,0.05)"
else:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#1e293b"
    accent = "#4a90e2"
    glass = "rgba(255,255,255,0.7)"

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.header {{
    text-align:center;
    padding: 50px 20px 30px;
}}

.header h1 {{
    font-size: 46px;
    margin-bottom: 8px;
    background: linear-gradient(90deg, {accent}, #313438);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.header p {{
    opacity: 0.7;
}}

.grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    padding: 20px 40px;
}}

.card {{
    padding: 25px;
    border-radius: 18px;
    background: {glass};
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    transition: 0.35s ease;
}}

.card:hover {{
    transform: translateY(-8px) scale(1.02);
    border: 1px solid {accent};
    box-shadow: 0 15px 45px rgba(0,0,0,0.5);
}}

.title {{
    font-size: 20px;
    font-weight: 600;
    color: {accent};
    margin-bottom: 10px;
}}

.desc {{
    font-size: 15px;
    line-height: 1.6;
    opacity: 0.85;
}}

.tag {{
    margin-top: 12px;
    display: inline-block;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 12px;
    background: rgba(0,245,255,0.15);
    color: {accent};
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<h1>📂 My Projects</h1>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid">

<div class="card">
<div class="title">🌐 Portfolio Website</div>
<div class="desc">
A modern personal portfolio built using Streamlit with glassmorphism UI, dark mode, and responsive layout.
</div>
<div class="tag">Streamlit</div>
</div>

<div class="card">
<div class="title">📝 To-Do App</div>
<div class="desc">
A task management system where users can add, edit, and organize daily tasks.
</div>
<div class="tag">App</div>
</div>

<div class="card">
<div class="title">🎨 UI Concept Design</div>
<div class="desc">
A modern UI prototype focused on spacing, layout, and user experience.
</div>
<div class="tag">UI/UX</div>
</div>

<div class="card">
<div class="title">🎮 Mini Game Project</div>
<div class="desc">
A simple interactive game built with Python for logic and user engagement practice.
</div>
<div class="tag">Game</div>
</div>

</div>
""", unsafe_allow_html=True)