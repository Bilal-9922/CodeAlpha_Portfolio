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
    <p>Machine learning model that predicts student performance based on academic data.</p>
    <p><b>Features:</b> Prediction, risk analysis, study plan</p>
    <p><b>Tech:</b> Python, Scikit-learn, Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📧 Spam Email Classifier</h3>
    <p>Detects whether an email is spam or not using NLP techniques.</p>
    <p><b>Features:</b> Text preprocessing, TF-IDF, classification</p>
    <p><b>Tech:</b> Python, NLP, Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🎬 Movie Recommendation System</h3>
    <p>Recommends movies based on user preferences and similarity.</p>
    <p><b>Features:</b> Content-based filtering, cosine similarity</p>
    <p><b>Tech:</b> Python, Pandas, ML</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🌐 Portfolio Website</h3>
    <p>Responsive personal portfolio with modern UI and animations.</p>
    <p><b>Features:</b> Sections, smooth navigation, animations</p>
    <p><b>Tech:</b> HTML, CSS, JavaScript</p>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">
    <h3>💼 Salary Predictor</h3>
    <p>Predicts salary based on experience using regression models.</p>
    <p><b>Features:</b> Data analysis, real-time prediction</p>
    <p><b>Tech:</b> Python, Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧮 Calculator App</h3>
    <p>Animated calculator with interactive UI.</p>
    <p><b>Features:</b> Arithmetic operations, animations</p>
    <p><b>Tech:</b> HTML, CSS, JavaScript</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>📊 Student Dashboard</h3>
    <p>Visualization dashboard showing student performance analytics.</p>
    <p><b>Features:</b> Charts, insights, analytics</p>
    <p><b>Tech:</b> Python, Pandas, Matplotlib</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🤖 AI Chatbot (Basic)</h3>
    <p>Simple chatbot for answering basic user queries.</p>
    <p><b>Features:</b> Rule-based responses</p>
    <p><b>Tech:</b> Python</p>
    </div>
    """, unsafe_allow_html=True)
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
