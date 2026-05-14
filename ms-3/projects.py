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

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    margin-bottom:20px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.project-card{
    background:#f8f9fa;
    padding:20px;
    border-radius:10px;
    margin-top:20px;
    transition:0.3s;
    border-left:5px solid #0a66c2;
}

.project-card:hover{
    transform:translateY(-5px);
}

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
    gap:20px;
    margin-top:20px;
}

.stat-box{
    background:#eef3f8;
    padding:20px;
    border-radius:10px;
    text-align:center;
}

.stat-box h1{
    color:#0a66c2;
}

.tech-stack{
    margin-top:15px;
}

.tech{
    display:inline-block;
    background:#0a66c2;
    color:white;
    padding:8px 15px;
    border-radius:20px;
    margin:5px;
    font-size:14px;
}

button{
    margin-top:15px;
    padding:10px 20px;
    border:none;
    border-radius:20px;
    background:#0a66c2;
    color:white;
    cursor:pointer;
}

.footer{
    text-align:center;
    padding:20px;
    color:#666;
}

</style>
"""

NAVBAR = """
<div class="navbar">

    <div class="logo">☁️ DineshCloud Projects</div>

    <div class="menu">
        <a href="/">Home</a>
        <a href="/projects">Projects</a>
        <a href="/opensource">Open Source</a>
        <a href="/deployments">Deployments</a>
    </div>

</div>
"""

@app.route("/")
@app.route("/projects")
def projects():

    projects_data = [
        {
            "title":"AWS EKS Microservices",
            "description":"Deployed scalable microservices architecture using Kubernetes on AWS EKS.",
            "status":"Production",
            "tech":["AWS", "EKS", "Docker", "Ingress"]
        },
        {
            "title":"CI/CD Automation Pipeline",
            "description":"Built Jenkins-based CI/CD automation with Docker and Kubernetes.",
            "status":"Running",
            "tech":["Jenkins", "Docker", "GitHub", "Kubernetes"]
        },
        {
            "title":"Monitoring Stack",
            "description":"Implemented monitoring and alerting system for cloud-native applications.",
            "status":"Active",
            "tech":["Prometheus", "Grafana", "AlertManager"]
        }
    ]

    html = f"""
    <html>

    <head>
        <title>DineshCloud Projects</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="card">

            <h1>DevOps Projects 🚀</h1>
            <p>Production-grade cloud-native projects portfolio</p>

            <div class="stats">

                <div class="stat-box">
                    <h1>{random.randint(10,100)}</h1>
                    <p>Total Projects</p>
                </div>

                <div class="stat-box">
                    <h1>{random.randint(50,500)}</h1>
                    <p>Deployments</p>
                </div>

                <div class="stat-box">
                    <h1>{random.randint(1000,5000)}</h1>
                    <p>GitHub Stars</p>
                </div>

            </div>

        </div>
    """

    for project in projects_data:

        tech_html = ""

        for tech in project['tech']:
            tech_html += f"<span class='tech'>{tech}</span>"

        html += f"""

        <div class="project-card">

            <h2>{project['title']}</h2>

            <p>{project['description']}</p>

            <p><strong>Status:</strong> {project['status']}</p>

            <div class="tech-stack">
                {tech_html}
            </div>

            <button>View Project</button>

        </div>

        """

    html += f"""

        <div class="card">

            <h2>Infrastructure Details</h2>

            <p><strong>Hostname:</strong> {socket.gethostname()}</p>

            <p><strong>Time:</strong> {datetime.datetime.now()}</p>

        </div>

    </div>

    <div class="footer">
        Flask | Kubernetes | AWS | Docker | DevOps
    </div>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/opensource")
def opensource():

    html = f"""
    <html>

    <head>
        <title>Open Source</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="card">

            <h1>Open Source Contributions 🌍</h1>

            <div class="project-card">
                <h2>Kubernetes Community</h2>
                <p>Contributed Helm templates and YAML optimizations.</p>
            </div>

            <div class="project-card">
                <h2>Terraform Modules</h2>
                <p>Reusable infrastructure-as-code modules.</p>
            </div>

            <div class="project-card">
                <h2>Docker Images</h2>
                <p>Maintained lightweight production-ready images.</p>
            </div>

        </div>

    </div>

    </body>
    </html>
    """

    return render_template_string(html)

@app.route("/deployments")
def deployments():

    html = f"""
    <html>

    <head>
        <title>Deployments</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="card">

            <h1>Deployment Dashboard 📦</h1>

            <div class="project-card">
                <h2>Production Cluster</h2>
                <p>Status: Running ✅</p>
            </div>

            <div class="project-card">
                <h2>Staging Cluster</h2>
                <p>Status: Healthy ✅</p>
            </div>

            <div class="project-card">
                <h2>Ingress Controller</h2>
                <p>Status: Active ✅</p>
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
        "service":"projects-service",
        "version":"1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
