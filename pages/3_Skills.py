import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#e2e8f0"
    accent = "#22d3ee"
    glass = "rgba(255,255,255,0.04)"
else:
    bg = "linear-gradient(135deg, #9FCB98, #546B41)"
    text = "#1e293b"
    accent = "#4a90e2"
    glass = "rgba(255,255,255,0.6)"

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.header {{
    text-align:center;
    padding: 50px 20px 20px;
}}

.header h1 {{
    font-size: 48px;
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
    gap: 22px;
    padding: 20px 40px;
}}

.skill-card {{
    padding: 25px;
    border-radius: 18px;
    background: {glass};
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    transition: 0.3s ease;
}}

.skill-card:hover {{
    transform: translateY(-8px) scale(1.02);
    border: 1px solid {accent};
    box-shadow: 0 15px 50px rgba(0,0,0,0.5);
}}

.section {{
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
    color: {accent};
}}

.skill {{
    margin-bottom: 14px;
}}

.label {{
    display:flex;
    justify-content: space-between;
    font-size: 14px;
    margin-bottom: 5px;
}}

/* BAR */
.bar {{
    height: 8px;
    border-radius: 20px;
    background: rgba(255,255,255,0.12);
    overflow: hidden;
}}

.fill {{
    height: 100%;
    background: linear-gradient(90deg, {accent}, #8b5cf6);
    border-radius: 20px;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<h1>🛠 My Skills</h1>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid">

<div class="skill-card">
<div class="section">💻 Programming</div>

<div class="skill">
<div class="label"><span>Python</span><span>85%</span></div>
<div class="bar"><div class="fill" style="width:85%"></div></div>
</div>

<div class="skill">
<div class="label"><span>Java</span><span>70%</span></div>
<div class="bar"><div class="fill" style="width:70%"></div></div>
</div>

<div class="skill">
<div class="label"><span>C / C++</span><span>65%</span></div>
<div class="bar"><div class="fill" style="width:65%"></div></div>
</div>

</div>

<div class="skill-card">
<div class="section">🌐 Web Development</div>

<div class="skill">
<div class="label"><span>HTML</span><span>90%</span></div>
<div class="bar"><div class="fill" style="width:90%"></div></div>
</div>

<div class="skill">
<div class="label"><span>CSS</span><span>85%</span></div>
<div class="bar"><div class="fill" style="width:85%"></div></div>
</div>

<div class="skill">
<div class="label"><span>Streamlit</span><span>80%</span></div>
<div class="bar"><div class="fill" style="width:80%"></div></div>
</div>

</div>

<div class="skill-card">
<div class="section">🎨 UI / UX</div>

<div class="skill">
<div class="label"><span>UI Design</span><span>75%</span></div>
<div class="bar"><div class="fill" style="width:75%"></div></div>
</div>

<div class="skill">
<div class="label"><span>UX Thinking</span><span>70%</span></div>
<div class="bar"><div class="fill" style="width:70%"></div></div>
</div>

<div class="skill">
<div class="label"><span>Figma</span><span>65%</span></div>
<div class="bar"><div class="fill" style="width:65%"></div></div>
</div>

</div>

<div class="skill-card">
<div class="section">⚙️ Other Skills</div>

<div class="skill">
<div class="label"><span>Problem Solving</span><span>85%</span></div>
<div class="bar"><div class="fill" style="width:85%"></div></div>
</div>

<div class="skill">
<div class="label"><span>Git / GitHub</span><span>70%</span></div>
<div class="bar"><div class="fill" style="width:70%"></div></div>
</div>

<div class="skill">
<div class="label"><span>Teamwork</span><span>80%</span></div>
<div class="bar"><div class="fill" style="width:80%"></div></div>
</div>

</div>

</div>
""", unsafe_allow_html=True)