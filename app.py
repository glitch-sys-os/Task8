from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# 🔹 MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9603841428@N",   # 👉 change this
    database="internship_portal"
)

cursor = db.cursor()

# 🔹 Home Page
@app.route('/')
def index():
    return render_template('form.html')

# 🔹 Form Submit
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        domain = request.form['domain']

        query = """INSERT INTO internship_registrations 
                   (student_name, email, phone, course, domain)
                   VALUES (%s, %s, %s, %s, %s)"""

        values = (name, email, phone, course, domain)

        cursor.execute(query, values)
        db.commit()

        return """
        <h2 style='color:green;'>✅ Registration Successful!</h2>
        <a href="/">Go Back</a>
        """

    except Exception as e:
        return f"<h3 style='color:red;'>❌ Error: {str(e)}</h3>"

# 🔹 Run App
if __name__ == '__main__':
    app.run(debug=True)