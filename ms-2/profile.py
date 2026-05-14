from flask import Flask, render_template_string
import random
import datetime
import socket

app = Flask(__name__)

STYLE = """
<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#f3f2ef;
}

.navbar{
    background:#0a66c2;
    padding:15px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    color:white;
}

.logo{
    font-size:28px;
    font-weight:bold;
}

.menu a{
    color:white;
    text-decoration:none;
    margin-left:20px;
    font-weight:bold;
}

.container{
    width:90%;
    margin:30px auto;
}

.profile-banner{
    background:linear-gradient(135deg,#0a66c2,#004182);
    height:220px;
    border-radius:20px;
    position:relative;
    box-shadow:0 4px 15px rgba(0,0,0,0.2);
}

.profile-card{
    background:white;
    margin-top:-70px;
    border-radius:20px;
    padding:30px;
    position:relative;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.avatar{
    width:130px;
    height:130px;
    border-radius:50%;
    background:white;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:48px;
    font-weight:bold;
    color:#0a66c2;
    border:6px solid white;
    position:absolute;
    top:-65px;
}

.profile-info{
    margin-top:80px;
}

.profile-info h1{
    font-size:36px;
    color:#222;
}

.profile-info p{
    margin-top:8px;
    color:#555;
}

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
    gap:20px;
    margin-top:30px;
}

.stat-box{
    background:#eef3f8;
    padding:20px;
    border-radius:15px;
    text-align:center;
}

.stat-box h1{
    color:#0a66c2;
    font-size:32px;
}

.skills{
    margin-top:20px;
}

.skill{
    display:inline-block;
    background:#0a66c2;
    color:white;
    padding:10px 18px;
    border-radius:25px;
    margin:8px;
    font-size:14px;
}

.section{
    background:white;
    padding:25px;
    border-radius:20px;
    margin-top:25px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.experience-card{
    background:#f8f9fa;
    padding:20px;
    border-radius:12px;
    margin-top:15px;
}

button{
    margin-top:20px;
    padding:12px 25px;
    border:none;
    border-radius:25px;
    background:#0a66c2;
    color:white;
    cursor:pointer;
    font-size:15px;
}

.footer{
    text-align:center;
    padding:30px;
    color:#666;
}

</style>
"""

NAVBAR = """
<div class="navbar">

    <div class="logo">☁️ DineshCloud Profile</div>

    <div class="menu">
        <a href="/">Home</a>
        <a href="/profile">Profile</a>
        <a href="/experience">Experience</a>
        <a href="/certifications">Certifications</a>
    </div>

</div>
"""

@app.route("/")
@app.route("/profile")
def profile():

    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    skills = [
        "Kubernetes",
        "Docker",
        "AWS",
        "Terraform",
        "Linux",
        "CI/CD",
        "Jenkins",
        "Prometheus"
    ]

    skills_html = ""

    for skill in skills:
        skills_html += f"<span class='skill'>{skill}</span>"

    html = f"""
    <html>

    <head>
        <title>DineshCloud Profile</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="profile-banner"></div>

        <div class="profile-card">

            <div class="avatar">
                D
            </div>

            <div class="profile-info">

                <h1>Dinesh Cloud</h1>

                <p>DevOps Engineer | Kubernetes | AWS | Docker</p>

                <p>Building scalable cloud-native applications & infrastructure automation.</p>

                <button>Connect</button>

                <div class="stats">

                    <div class="stat-box">
                        <h1>{random.randint(1000,10000)}</h1>
                        <p>Followers</p>
                    </div>

                    <div class="stat-box">
                        <h1>{random.randint(100,1000)}</h1>
                        <p>Projects</p>
                    </div>

                    <div class="stat-box">
                        <h1>{random.randint(10000,50000)}</h1>
                        <p>Profile Views</p>
                    </div>

                </div>

            </div>

        </div>

        <div class="section">

            <h2>Skills 🚀</h2>

            <div class="skills">
                {skills_html}
            </div>

        </div>

        <div class="section">

            <h2>About 👨‍💻</h2>

            <p>
            Passionate DevOps Engineer focused on Kubernetes, Docker,
            AWS EKS, CI/CD automation, and cloud-native infrastructure.
            Experienced in designing scalable production-grade systems.
            </p>

        </div>

        <div class="section">

            <h2>System Information 🖥️</h2>

            <div class="experience-card">

                <p><strong>Hostname:</strong> {hostname}</p>

                <p><strong>Current Time:</strong> {current_time}</p>

                <p><strong>Application:</strong> DineshCloud Profile Service</p>

            </div>

        </div>

    </div>

    <div class="footer">
        Flask | Kubernetes | Docker | AWS | DevOps
    </div>

    </body>

    </html>
    """

    return render_template_string(html)

@app.route("/experience")
def experience():

    html = f"""
    <html>

    <head>
        <title>Experience</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="section">

            <h1>Experience 💼</h1>

            <div class="experience-card">

                <h2>DevOps Engineer</h2>

                <p><strong>Company:</strong> Cloud Native Systems</p>

                <p><strong>Duration:</strong> 2023 - Present</p>

                <p>
                Managing Kubernetes clusters, AWS infrastructure,
                CI/CD pipelines, monitoring systems, and automation workflows.
                </p>

            </div>

            <div class="experience-card">

                <h2>Cloud Engineer</h2>

                <p><strong>Company:</strong> DevOps Labs</p>

                <p><strong>Duration:</strong> 2021 - 2023</p>

                <p>
                Worked on Docker containerization, Terraform automation,
                and scalable deployment architectures.
                </p>

            </div>

        </div>

    </div>

    </body>

    </html>
    """

    return render_template_string(html)

@app.route("/certifications")
def certifications():

    html = f"""
    <html>

    <head>
        <title>Certifications</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="section">

            <h1>Certifications 📜</h1>

            <div class="experience-card">

                <h2>AWS Certified Solutions Architect</h2>

                <p>Amazon Web Services</p>

            </div>

            <div class="experience-card">

                <h2>Certified Kubernetes Administrator (CKA)</h2>

                <p>Cloud Native Computing Foundation</p>

            </div>

            <div class="experience-card">

                <h2>Docker Certified Associate</h2>

                <p>Docker Inc.</p>

            </div>

        </div>

    </div>

    </body>

    </html>
    """

    return render_template_string(html)

@app.route("/health")
def health():
    return {
        "status":"healthy",
        "service":"profile-service",
        "version":"1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
