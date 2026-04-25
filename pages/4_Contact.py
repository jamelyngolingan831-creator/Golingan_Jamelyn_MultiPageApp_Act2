import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

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
    glass = "rgba(255,255,255,0.65)"

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Segoe UI', sans-serif;
}}

.header {{
    text-align:center;
    padding: 55px 20px 20px;
}}

.header h1 {{
    font-size: 50px;
    background: linear-gradient(90deg, {accent}, #313438);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.header p {{
    opacity: 0.7;
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr;
    gap: 25px;
    padding: 20px 120px;
}}

.card {{
    padding: 30px;
    border-radius: 18px;
    background: {glass};
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    transition: 0.3s;
}}

.card:hover {{
    transform: translateY(-6px);
    border: 1px solid {accent};
}}

.input {{
    width: 100%;
    padding: 10px;
    margin: 8px 0 15px;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.06);
    color: {text};
    outline: none;
}}

.btn {{
    display:inline-block;
    padding: 10px 18px;
    border-radius: 10px;
    background: linear-gradient(90deg, {accent}, #8b5cf6);
    color: white;
    font-weight: bold;
    cursor: pointer;
}}

.tag {{
    display:inline-block;
    margin-top:10px;
    padding:5px 12px;
    border-radius:20px;
    background: rgba(0,245,255,0.15);
    color: {accent};
    font-size:12px;
}}

.info {{
    font-size: 14px;
    opacity: 0.85;
    line-height: 1.7;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
<h1>📬 Contact Me</h1>
<p>Let’s build something amazing together</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid">

<div class="card">
<h2>✉️ Send Message</h2>

<label>Name</label>
<input class="input" type="text" placeholder="Your name">

<label>Email</label>
<input class="input" type="email" placeholder="Your email">

<label>Message</label>
<textarea class="input" rows="5" placeholder="Write your message..."></textarea>

<div class="btn">Send Message</div>
</div>

</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid">

<div class="card">
<h3>📍 Contact Info</h3>

<p class="info">
📧 Email: jamelyn@example.com<br>
📱 Phone: +63 9XX XXX XXXX<br>
📍 Location: Philippines
</p>

<div class="tag">Available for Freelance</div>

<hr style="margin:15px 0; opacity:0.2;">

<h3>🌐 Social Links</h3>

<p class="info">
GitHub: github.com/yourname<br>
Facebook: fb.com/yourname<br>
LinkedIn: linkedin.com/in/yourname
</p>

</div>

</div>
""", unsafe_allow_html=True)