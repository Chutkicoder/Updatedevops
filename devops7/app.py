from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask + Jenkins!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
docker compose up -d
Open in browser : http://localhost:8080
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
optional if ran into errors:
docker compose down -v
docker compose up -d
Unlock Jenkins → Install Suggested Plugins → Create Admin User.
Go to Jenkins → New Item → Name: FlaskAPI-CI-CD.
2. Select Pipeline → OK.
Pipeline script from SCM
"""