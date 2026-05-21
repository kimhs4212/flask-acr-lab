from flask import Flask
<<<<<<< HEAD
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Azure Docker Deploy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
=======

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from GitHub Actions + Azure ACR!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 77b998713556ff72574aa0e4f81282f8718998f3
