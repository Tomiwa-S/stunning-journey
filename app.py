from flask import Flask, render_template

web = Flask(__name__)

@web.route("/")
def home():
    return render_template("index.html")

@web.route("/random")
def random():
    return "Some random text"

if __name__ == "__main__":
    web.run(host="0.0.0.0", port=8080)
