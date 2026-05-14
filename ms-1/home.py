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
    position:sticky;
    top:0;
    z-index:1000;
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

.hero{
    background:linear-gradient(135deg,#0a66c2,#004182);
    color:white;
    padding:60px;
    border-radius:25px;
    box-shadow:0 5px 20px rgba(0,0,0,0.2);
}

.hero h1{
    font-size:52px;
}

.hero p{
    margin-top:20px;
    font-size:18px;
    line-height:1.6;
}

button{
    margin-top:25px;
    padding:14px 28px;
    border:none;
    border-radius:30px;
    background:white;
    color:#0a66c2;
    font-weight:bold;
    cursor:pointer;
}

.stats{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-top:30px;
}

.stat-box{
    background:white;
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.stat-box h1{
    color:#0a66c2;
    font-size:38px;
}

.section{
    margin-top:30px;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    margin-top:20px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
}

.feed-post{
    padding:20px;
    border-bottom:1px solid #ddd;
}

.feed-post:last-child{
    border-bottom:none;
}

.feed-post h3{
    color:#0a66c2;
}

.tags{
    margin-top:10px;
}

.tag{
    display:inline-block;
    background:#0a66c2;
    color:white;
    padding:8px 15px;
    border-radius:20px;
    margin:5px;
    font-size:13px;
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

    <div class="logo">☁️ DineshCloud</div>

    <div class="menu">
        <a href="/home">Home</a>
        <a href="/network">Network</a>
        <a href="/jobs">Jobs</a>
        <a href="/projects">Projects</a>
        <a href="/profile">Profile</a>
    </div>

</div>
"""

@app.route("/")
@app.route("/home")
def home():

    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    posts = [
        {
            "name":"Dinesh Cloud",
            "role":"DevOps Engineer",
            "content":"Successfully deployed Kubernetes microservices using AWS EKS and ALB Ingress 🚀"
        },
        {
            "name":"Cloud Native Team",
            "role":"Platform Engineers",
            "content":"Implemented production-grade CI/CD pipelines using Jenkins & Docker."
        },
        {
            "name":"AWS Community",
            "role":"Cloud Experts",
            "content":"Configured Route53, ACM SSL, and Ingress path-based routing."
        }
    ]

    html = f"""
    <html>

    <head>
        <title>DineshCloud Home</title>
        {STYLE}
    </head>

    <body>

    {NAVBAR}

    <div class="container">

        <div class="hero">

            <h1>Welcome to DineshCloud 🚀</h1>

            <p>
            Professional cloud-native networking platform for DevOps Engineers,
            Kubernetes Administrators, AWS Architects, and Platform Engineers.
            </p>

            <button>Explore Platform</button>

        </div>

        <div class="stats">

            <div class="stat-box">
                <h1>{random.randint(1000,10000)}</h1>
                <p>Cloud Engineers</p>
            </div>

            <div class="stat-box">
                <h1>{random.randint(100,1000)}</h1>
                <p>Projects</p>
            </div>

            <div class="stat-box">
                <h1>{random.randint(500,5000)}</h1>
                <p>Deployments</p>
            </div>

            <div class="stat-box">
                <h1>{random.randint(10000,50000)}</h1>
                <p>Connections</p>
            </div>

        </div>

        <div class="section">

            <div class="card">

                <h2>Trending Technologies 🔥</h2>

                <div class="tags">
                    <span class="tag">Kubernetes</span>
                    <span class="tag">Docker</span>
                    <span class="tag">AWS EKS</span>
                    <span class="tag">Terraform</span>
                    <span class="tag">Prometheus</span>
                    <span class="tag">Grafana</span>
                </div>

            </div>

        </div>

        <div class="section">

            <div class="card">

                <h2>Cloud Feed 🌍</h2>
    """

    for post in posts:

        html += f"""

                <div class="feed-post">

                    <h3>{post['name']}</h3>

                    <p><strong>{post['role']}</strong></p>

                    <p>{post['content']}</p>

                </div>

        """

    html += f"""

            </div>

        </div>

        <div class="section">

            <div class="card">

                <h2>Infrastructure Details 🖥️</h2>

                <p><strong>Hostname:</strong> {hostname}</p>

                <p><strong>Current Time:</strong> {current_time}</p>

                <p><strong>Application:</strong> DineshCloud Home Service</p>

            </div>

        </div>

    </div>

    <div class="footer">
        Flask | Kubernetes | AWS | Docker | DevOps
    </div>

    </body>

    </html>
    """

    return render_template_string(html)

@app.route("/health")
def health():
    return {
        "status":"healthy",
        "service":"home-service",
        "version":"1.0.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
