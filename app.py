from flask import Flask, render_template, jsonify
import os
from supabase import Client

app = Flask(__name__)

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")
supabase = Client(url, key)

@app.route("/")
def hello_ewastex():
    parts = fetch_parts()
    return render_template("home.html", Parts=parts)

@app.route("/api/parts")
def list_parts():
    parts = fetch_parts()
    return jsonify(parts)

def fetch_parts():
    parts_data = supabase.from_("parts").select("*").execute().data
    parts_set = []
    for part in parts_data:
        parts_set.append({
            'id': part['id'],
            'name': part['name'],
            'price': "Rs " + str(part['price']),
            'quant': part['quant'],
            'image': part['image']
        })
    return parts_set

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
