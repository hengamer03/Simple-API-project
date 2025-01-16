import subprocess
import os
from flask import Flask, jsonify
from swagger.swagger_setup import setup_swagger

app = Flask(__name__)

VENV_PATH = os.path.abspath("env")
PYTHON_EXEC = os.path.join(VENV_PATH, "bin", "python")
SCRIPT_PATH = os.path.abspath("test.py")

# Define the endpoint that returns "it works"
@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "it works"}), 200

@app.route('/run-script', methods=['GET'])
def run_script():
    result = subprocess.run([PYTHON_EXEC, SCRIPT_PATH], capture_output=True, text=True)
    return jsonify({"output": result.stdout, "error": result.stderr})

setup_swagger(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
