import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Bilal Portfolio", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body{
 margin:0;
 font-family: 'Segoe UI', sans-serif;
 background:#0f172a;
 color:white;
}

/* HEADER */
header{
 text-align:center;
 padding:60px 20px;
 background:linear-gradient(135deg,#6366f1,#22c55e);
 animation:fadeIn 1.5s;
}

@keyframes fadeIn{
 from{opacity:0;}
 to{opacity:1;}
}

header h1{
 font-size:40px;
 margin:10px 0;
}

header p{
 font-size:18px;
}

/* NAV */
nav{
 margin-top:15px;
}

nav a{
 color:white;
 margin:0 15px;
 text-decoration:none;
 font-weight:bold;
 transition:0.3s;
}

nav a:hover{
 color:#000;
 background:white;
 padding:5px 10px;
 border-radius:5px;
}

/* SECTIONS */
section{
 padding:60px;
}

/* ABOUT */
#about{
 display:flex;
 flex-wrap:wrap;
 align-items:center;
 gap:40px;
}

#about img{
 width:200px;
 border-radius:50%;
 border:4px solid #22c55e;
 box-shadow:0 0 20px #22c55e;
}

.about-text{
 max-width:600px;
}

/* PROJECTS */
.project-grid{
 display:grid;
 grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
 gap:25px;
}

.project{
 background:#1e293b;
 padding:20px;
 border-radius:15px;
 transition:0.4s;
 box-shadow:0 10px 20px rgba(0,0,0,0.4);
}

.project:hover{
 transform:translateY(-10px) scale(1.03);
}

/* CERTIFICATIONS */
.cert-grid{
 display:grid;
 grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
 gap:20px;
}

.cert{
 background:#1e293b;
 padding:15px;
 border-radius:10px;
 text-align:center;
}

.cert img{
 width:100%;
 border-radius:10px;
}

/* CONTACT */
#contact{
 text-align:center;
}

a{
 color:#22c55e;
}

/* RESPONSIVE */
@media(max-width:768px){
 #about{
  flex-direction:column;
  text-align:center;
 }
}

</style>
</head>

<body>

<header>
<h1>Mohammad Bilal Shaikh</h1>
<p>🚀 Frontend Developer | ML Enthusiast</p>

<nav>
<a href="#about">About</a>
<a href="#projects">Projects</a>
<a href="#certifications">Certifications</a>
<a href="#contact">Contact</a>
</nav>
</header>

<section id="about">
<img src="https://via.placeholder.com/200">
<div class="about-text">
<h2>About Me</h2>
<p>
I am a Third Year Computer Engineering student passionate about building modern web applications and solving real-world problems using Machine Learning.
</p>
</div>
</section>

<section id="projects">
<h2>🔥 Projects</h2>

<div class="project-grid">

<div class="project">
<h3>📊 Student Performance ML</h3>
<p>ML model to predict student performance with Streamlit UI.</p>
</div>

<div class="project">
<h3>🧮 Calculator App</h3>
<p>Animated calculator using HTML, CSS, JavaScript.</p>
</div>

<div class="project">
<h3>🌐 Portfolio Website</h3>
<p>Modern responsive portfolio with animations.</p>
</div>

</div>
</section>

<section id="certifications">
<h2>📜 Certifications</h2>

<div class="cert-grid">

<div class="cert">
<img src="https://via.placeholder.com/300">
<p>HTML & CSS Course</p>
</div>

<div class="cert">
<img src="https://via.placeholder.com/300">
<p>MySQL Course</p>
</div>

</div>
</section>

<section id="contact">
<h2>📞 Contact</h2>
<p>Email: bilalshaikh1339@gmail.com</p>
<p>GitHub: <a href="https://github.com/Bilal-9922" target="_blank">Bilal-9922</a></p>
<p>LinkedIn: <a href="https://www.linkedin.com/in/mohammad-bilal-shaikh-2a73b3327" target="_blank">Profile</a></p>
</section>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)