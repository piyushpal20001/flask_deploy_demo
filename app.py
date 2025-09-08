from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Flask Deployment Successful (Updated v2)"

@app.route("/about")
def about():
    return "This is a small project deployed using Flask on Render."

if __name__ == "__main__":
    app.run(debug=True)
