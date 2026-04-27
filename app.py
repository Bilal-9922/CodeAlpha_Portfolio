import streamlit as st

st.set_page_config(page_title="Bilal Portfolio", layout="wide")

# ---------- HEADER ----------
st.markdown("""
<style>

/* GLOBAL */
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
}

/* MAIN CONTAINER */
.main {
    background: transparent;
}

/* HEADINGS */
h1 {
    font-size: 48px;
    color: #22c55e;
    text-align: center;
    margin-bottom: 10px;
}

h2 {
    color: #38bdf8;
    border-left: 5px solid #22c55e;
    padding-left: 10px;
}

/* SUBTEXT */
p {
    font-size: 16px;
    color: #cbd5f5;
}

/* CARD DESIGN */
.card {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: all 0.3s ease-in-out;
    border: 1px solid rgba(255,255,255,0.1);
}

/* HOVER EFFECT */
.card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 0 20px #22c55e;
}

/* SKILL BARS */
.stProgress > div > div {
    background: linear-gradient(90deg, #22c55e, #38bdf8);
}

/* CONTACT LINKS */
a {
    color: #22c55e;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    color: #38bdf8;
}

/* DIVIDER */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #22c55e, transparent);
    margin: 30px 0;
}

/* BUTTON STYLE (if added later) */
button[kind="primary"] {
    background: linear-gradient(135deg, #22c55e, #38bdf8);
    border-radius: 10px;
    border: none;
}

/* ANIMATION */
.card {
    animation: fadeUp 0.6s ease;
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)
# ---------- HERO ----------
st.markdown("""
<h1>🚀 Mohammad Bilal Shaikh</h1>
<p style='text-align:center; font-size:18px;'>
Frontend Developer | Machine Learning Enthusiast
</p>
<hr>
""", unsafe_allow_html=True)

# ---------- ABOUT ----------
st.header("👨‍💻 About Me")
st.write("""
I am a Third Year Computer Engineering student passionate about building modern web applications 
and solving real-world problems using Machine Learning.

💡 Skills:
- Python, C++, SQL  
- HTML, CSS, JavaScript  
- Machine Learning (Scikit-learn)  
""")

# ---------- PROJECTS ----------
st.header("🔥 Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📊 Student Performance Prediction</h3>
    <p>Predicts student pass/fail using ML model with Streamlit UI.</p>
    <p><b>Tech:</b> Python, ML, Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📧 Spam Email Classifier")
    st.write("Detects spam emails using NLP techniques.")
    st.write("Tech: Python, TF-IDF, ML")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎬 Movie Recommendation System")
    st.write("Recommends movies using similarity algorithms.")
    st.write("Tech: Python, Cosine Similarity")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💼 Salary Predictor")
    st.write("Predicts salary based on experience using regression.")
    st.write("Tech: Python, ML")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧮 Calculator App")
    st.write("Animated calculator using HTML, CSS, JS.")
    st.write("Tech: HTML, CSS, JS")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌐 Portfolio Website")
    st.write("Responsive personal portfolio website.")
    st.write("Tech: HTML, CSS")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SKILLS ----------
st.header("🧠 Skills")

st.write("Python")
st.progress(90)

st.write("Machine Learning")
st.progress(85)

st.write("Web Development")
st.progress(80)

st.write("SQL")
st.progress(75)

# ---------- CONTACT ----------
st.header("📞 Contact")

st.write("📧 Email: bilalshaikh1339@gmail.com")
st.write("💻 GitHub: https://github.com/Bilal-9922")
st.write("🔗 LinkedIn: https://www.linkedin.com/in/mohammad-bilal-shaikh-2a73b3327")

st.write("---")
st.write("⭐ Built with Streamlit")
