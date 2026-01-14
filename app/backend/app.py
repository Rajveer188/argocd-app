from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify({
        "service": "backend",
        "status": "ok",
        "data": [
            {"id": 1, "name": "ArgoCD"},
            {"id": 2, "name": "Ingress"},
            {"id": 3, "name": "GitOps"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

