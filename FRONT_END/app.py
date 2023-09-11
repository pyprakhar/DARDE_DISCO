
# # from flask import Flask,render_template, request
# # from flask_mysqldb import MySQL
 
# # app = Flask(__name__)
 
# # app.config['MYSQL_HOST'] = 'localhost'
# # app.config['MYSQL_USER'] = 'root'
# # app.config['MYSQL_PASSWORD'] = ''
# # app.config['MYSQL_DB'] = 'flask'
 
# # mysql = MySQL(app)

# # #Creating a connection cursor
# # cursor = mysql.connection.cursor()
 
# # #Executing SQL Statements
# # cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# # cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# # cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# # #Saving the Actions performed on the DB
# # mysql.connection.commit()
 
# # #Closing the cursor
# # cursor.close()

# # @app.route('/student_signup')
# # def form():
# #     return render_template('student_signup.html')
 
# # @app.route('/student_signup', methods = ['POST', 'GET'])
# # def login():
# #     if request.method == 'GET':
# #         return "Login via the login Form"
     
# #     if request.method == 'POST':
# #         name = request.form['name']
# #         email = request.form['email']
# #         cursor = mysql.connection.cursor()
# #         cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
# #         mysql.connection.commit()
# #         cursor.close()
# #         return f"Done!!"
 
# # app.run(host='localhost', port=5000)

# from flask import Flask, render_template, request, redirect, url_for
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'qs'

# mysql = MySQL(app)

# @app.route('/student_signup', methods=['GET', 'POST'])
# def student_signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']

#         # Create a connection cursor
#         cursor = mysql.connection.cursor()

#         # Insert the form data into the MySQL database
#         cursor.execute("INSERT INTO people(username, email) VALUES (%s, %s)", (username, email))

#         # Commit the changes to the database
#         mysql.connection.commit()

#         # Close the cursor
#         cursor.close()

#         # Redirect to a success page or show a success message
#         return "Sign-up successful!"

#     return render_template('student_signup.html')

# if __name__ == '__main__':
#     app.run(host='localhost', port=5000)

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'qs'  # Use 'qs' as the database name

mysql = MySQL(app)

@app.route('/student_signup', methods=['GET', 'POST'])
def student_signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        try:
            # Create a connection cursor
            cursor = mysql.connection.cursor()

            # Insert the form data into the MySQL database
            cursor.execute("INSERT INTO people(username, email) VALUES (%s, %s)", (username, email))

            # Commit the changes to the database
            mysql.connection.commit()

            # Close the cursor
            cursor.close()

            # Redirect to a success page or show a success message
            return "Sign-up successful!"

        except Exception as e:
            # Print the error for debugging
            print(e)

            # Handle the error gracefully, e.g., show an error message
            return "An error occurred during sign-up."

    return render_template('student_signup.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)




