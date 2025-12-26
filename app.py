from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

app = Flask(__name__)
app.secret_key = "secretkey"

# Load cases
with open("cases.json", "r", encoding="utf-8") as f:
    cases = json.load(f)

users = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("chat"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            flash("Username already exists")
        else:
            users[username] = password
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    return render_template("chat.html", results=None)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "").lower()
    lang = request.args.get("lang", "en")
    results = []
    for case in cases:
        if query in case["title"].lower() or query in case["summary"][lang].lower():
            results.append(case)
    return render_template("results.html", results=results, query=query, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
