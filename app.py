from flask import Flask, render_template , jsonify

app = Flask(__name__)

parts = [
  {
    'id': 1,
    'name': 'CPU',
    'price': "Rs 1000",
    'quant': 1,
    'image': 'static/cpu.jpg'
  },
  {
    'id': 2,
    'name': 'GPU',
    'price': "Rs 2000",
    'quant' : 1,
    'image': 'static/gpu.jpg'
  },
  {
    'id': 3,
    'name': 'RAM',
    'price': "Rs 1000",
    'quant': 1,
    'image': 'static/ram.jpg'
  },
  {
    'id': 4,
    'name': 'SSD',
    'price': "Rs 3000",
    'quant': 1,
    'image': 'static/ssd.jpg'
  }
]

@app.route("/")
def hello_ewastex():
    return render_template("home.html",Parts=parts)

@app.route("/api/parts")
def list_parts():
    return jsonify(parts)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)