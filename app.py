from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "✅ Hello depuis GitHub Actions et Docker3 !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
