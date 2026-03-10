from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/data")
def data():
    return jsonify({"data": [1, 2, 3, 4]}), 200

@app.route("/api/error")
def error():
    return jsonify({"error": "Simulated failure"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
