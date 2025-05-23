from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    name = request.form['name']
    email = request.form['email']
    complaint = request.form['complaint']
    print(f"Complaint received from {name} ({email}): {complaint}")
    return "<h1>Thank you for your complaint. We will get back to you shortly.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
