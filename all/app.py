from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        content = request.json
        return jsonify({"received": content}), 201
    else:
        return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
