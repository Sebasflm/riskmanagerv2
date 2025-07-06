
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form.get("domain")
        if domain:
            return redirect(url_for("results", domain=domain))
    return render_template("index.html")

@app.route("/results/<domain>")
def results(domain):
    return render_template("results.html", domain=domain)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
