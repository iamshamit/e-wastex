from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import fetch_parts, supabase
app = Flask(__name__)


@app.route("/")
def hello_ewastex():
    parts = fetch_parts()
    return render_template("home.html", Parts=parts)
  
@app.route("/sell")
def sell():
    return render_template("sell.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add_electronic", methods=["POST"])
def add_electronic():
    name = request.form.get("productName")
    category = request.form.get("productCategory")
    details = request.form.get("productDetails")

    if name and category and details:
        # Insert data into Supabase database
        supabase.from_("ewaste").insert([
            {
                'Name': name,
                'Type': category,
                'Details': details,
            }
        ]).execute()

        laptop_count_query = supabase.from_("ewaste").select("count").filter("Type", "eq", "laptop").execute()
        laptop_count = laptop_count_query.data[0]['count']
        parts = fetch_parts()
        for part in parts:
          part['quant'] = laptop_count
          supabase.from_("parts").update({"quant": part['quant'] }).eq("id", part['id']).execute()
        
        return redirect(url_for('hello_ewastex'))
    else:
        return "Error: Please fill out all fields"

@app.route("/api/parts")
def list_parts():
    parts = fetch_parts()
    return jsonify(parts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)