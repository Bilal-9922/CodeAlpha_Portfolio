import streamlit as st

st.set_page_config(page_title="Bilal Portfolio", layout="wide")

# ---------- HEADER ----------
st.markdown("""
<style>
body {background-color: #0f172a; color: white;}
.main {background-color:#0f172a;}

h1,h2,h3 {color:#22c55e;}

.card {
background:#1e293b;
padding:20px;
border-radius:15px;
box-shadow:0 8px 20px rgba(0,0,0,0.4);
transition:0.3s;
}
.card:hover {transform:scale(1.05);}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("<h1>🚀 Mohammad Bilal Shaikh</h1>", unsafe_allow_html=True)
st.write("Frontend Developer | Machine Learning Enthusiast")

st.write("---")

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
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Student Performance Prediction")
    st.write("Predicts student pass/fail using ML model with Streamlit UI.")
    st.write("Tech: Python, ML, Streamlit")
    st.markdown('</div>', unsafe_allow_html=True)

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
