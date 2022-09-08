from datetime import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    count = int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"])
    date = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    customer = f"{request.form['first_name']} {request.form['last_name']}"
    print(f"Charging {customer} for {count} fruits")
    return render_template("checkout.html", count = count, date = date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    