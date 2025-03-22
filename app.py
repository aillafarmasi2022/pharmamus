from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data kamus dari CSV
df = pd.read_csv("data/kamus.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    
    if request.method == "POST":
        istilah = request.form["istilah"].strip().lower()
        terjemahan = df[df["Istilah"].str.lower() == istilah]["Terjemahan"].values
        hasil = terjemahan[0] if len(terjemahan) > 0 else "Istilah tidak ditemukan."

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
