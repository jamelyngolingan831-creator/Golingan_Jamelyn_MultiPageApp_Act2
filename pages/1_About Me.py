import streamlit as st

st.set_page_config(page_title="About Me", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#313438"
    accent = "#22d3ee"
    card_bg = "rgba(255,255,255,0.04)"
else:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#1e293b"
    accent = "#4a90e2"
    card_bg = "rgba(255,255,255,0.65)"

st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.header {{
    text-align:center;
    padding: 40px 20px;
}}

.header h1 {{
    font-size: 44px;
    margin-bottom: 5px;
    background: linear-gradient(90deg, {accent}, #313438);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.header p {{
    opacity: 0.7;
    font-size: 16px;
}}

.card {{
    padding: 35px;
    border-radius: 22px;
    background: {card_bg};
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
    transition: 0.3s ease;
}}

.card:hover {{
    transform: translateY(-6px);
    box-shadow: 0 15px 50px rgba(0,0,0,0.5);
    border: 1px solid {accent};
}}

h2 {{
    color: {accent};
    margin-bottom: 10px;
}}

h3 {{
    margin-top: 20px;
    opacity: 0.9;
}}

p {{
    line-height: 1.7;
    opacity: 0.9;
}}

/* HIGHLIGHT */
.highlight {{
    color: {accent};
    font-weight: 600;
}}

/* DIVIDER */
hr {{
    border: none;
    height: 1px;
    background: {accent};
    opacity: 0.3;
    margin: 20px 0;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<h1>👤 About Me</h1>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown(f"""
    <div class="card">

    <h2>Hello! I'm Jamelyn Golingan 👋</h2>

    <p>
    I am a <span class="highlight">Computer Science student</span> passionate about 
    technology, design, and building useful digital solutions.
    </p>

    <hr>

    <h3>💡 My Journey</h3>
    <p>
    I started learning programming because I was curious about how websites and applications work.
    Over time, I developed a strong interest in creating user-friendly and interactive systems.
    </p>

    <h3>🚀 What I Do</h3>
    <p>
    I focus on <span class="highlight">web development, UI design, and Python applications</span>.
    I enjoy turning ideas into real, working projects.
    </p>

    <h3>🎯 My Goal</h3>
    <p>
    My goal is to become a skilled developer who builds meaningful and impactful software
    that solves real-world problems.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">

    <h3>🧠 More About Me</h3>

    <p>
    I enjoy learning new technologies and improving my skills every day.
    Consistency and practice are the keys I follow to grow as a developer.
    </p>

    <p>
    I am currently exploring <span class="highlight">frontend, backend, and UI/UX design</span>.
    </p>

    <p>
    Outside coding, I explore ideas, design concepts, and small personal projects
    that help me improve creatively.
    </p>

    <p>
    I always aim to stay motivated and keep improving step by step.
    </p>

    </div>
    """, unsafe_allow_html=True)