import os
import uuid
import subprocess
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/generate", methods=["POST"])
def generate():

    # Get request data
    data = request.get_json()

    # Get d2 diagram data
    diagram_content = data.get("diagram")

    file_name = None
    for i in range(0,100):

        file_name = f"/tmp/{uuid.uuid4()}"

        if not os.path.exists(f"{file_name}.d2"):
            break

    if not file_name:
        return
            
    # Create file content
    f = open(f"{file_name}.d2", "w")
    f.write(diagram_content)
    f.close()

    process = subprocess.run([
        "d2",
        f"{file_name}.d2",
        f"{file_name}.svg"
    ])

    # Get svg file content
    f = open(f"{file_name}.svg", "r")
    diagram_svg = f.read()
    f.close()

    os.remove(f"{file_name}.d2")
    os.remove(f"{file_name}.svg")

    return jsonify({
        "diagram": diagram_svg
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=5000,
    )