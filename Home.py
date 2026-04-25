import streamlit as st 

st.set_page_config(page_title="My Portfolio", layout="wide") 

theme = st.sidebar.toggle("🌙 Dark Mode")

if theme:
    bg = "linear-gradient(135deg, #E4DFB5, #9FCB98)"
    text = "#313438"
    accent = "#22d3ee"
    card_bg = "rgba(255,255,255,0.04)"
else:
    bg = "linear-gradient(135deg, #E4DFB5, #9FCB98)"
    text = "#1e293b"
    accent = "#4a90e2"
    card_bg = "rgba(255,255,255,0.65)"
    
st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    color: {text};
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    padding: 30px;
    margin-bottom: 20px;
">
<h1 style="
    font-size: 42px;
    margin: 0;
    background: linear-gradient(90deg, #000000, #4a90e2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
">
🌐 My Personal Portfolio
</h1>

<p style="
    font-size: 18px;
    opacity: 0.7;
    margin-top: 10px;
">
Aspiring IT Developer | Learning | Growing
</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col2:
    st.image("2efd0aaf-07f8-492c-989e-e94a6e0604d0.jpg", width=300)

    st.markdown("""
    <div style="
    text-align:center;
    margin-top:15px;
    margin-bottom:15px;
    padding:10px 15px;
    border-radius:10px;
    background: rgba(255, 255, 255, 0.10);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 0 8px 25px rgba(0,0,0,0.35),
                0 0 15px rgba(0,245,255,0.15);
    ">
    <h3 style="margin:0; color:#black;">
    Jamelyn Golingan
    <p style="margin:0; opacity:0.75; font-size:14px;">
    Aspiring Developer
    </p>
    </h3>

    
    </div>
    """, unsafe_allow_html=True)

with col1:
    st.markdown("""
<div style="
        padding: 35px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4),
                    inset 0 0 10px rgba(255,255,255,0.05);
">

<h2 style="
        font-size: 28px;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #000000, #4a90e2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
">
Hi! Welcome to my Portfolio
</h2>

<p style="font-size:16px; line-height:1.7; opacity:0.9;">
I am a Computer Science student passionate about software development,
UI/UX design, and building modern digital experiences.
</p>

<p style="font-size:16px; line-height:1.7; opacity:0.9;">
I enjoy creating web-based applications that are functional and visually appealing,
turning ideas into real projects.
</p>

<p style="font-size:16px; line-height:1.7; opacity:0.9;">
Right now, I am improving my skills in Python, Streamlit, and web development.
</p>

<div style="
    margin-top: 20px;
    padding: 15px;
    border-left: 3px solid #00f5ff;
    background: rgba(0,245,255,0.08);
    border-radius: 10px;
">
<p style="margin:0; font-size:16px;">
My goal is to grow as a developer and build meaningful solutions that make an impact.
</p>
</div>

</div>
""", unsafe_allow_html=True)