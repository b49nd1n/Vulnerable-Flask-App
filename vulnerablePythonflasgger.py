from flask import Flask, render_template,jsonify, request, Response, render_template_string
from flasgger import Swagger
from flask_bootstrap import Bootstrap
import subprocess
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename
import sqlite3


   """
  * pip install flasgger

* Vous pouvez accéder à la documentation Swagger en visitant /apidocs ou /apidocs/index.html sur votre serveur Flask. Assurez-vous de personnaliser les commentaires en fonction de votre logique d'endpoint pour une documentation plus précise.
   """

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/home/kali/Desktop/upload"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
swagger = Swagger(app)  # Initialise Swagger
bootstrap = Bootstrap(app)  # Initialise Flask-Bootstrap

# Nouvel endpoint pour la page d'accueil avec des composants Bootstrap
@app.route("/")
def home():
    """
    Home page with Bootstrap components for security tests.
    """
    return render_template('home.html')

# Nouvel endpoint pour le formulaire sur la page d'accueil
@app.route("/submit_form", methods=["POST"])
def submit_form():
    """
    Endpoint to handle form submission on the home page.
    ---
    parameters:
      - name: username
        in: formData
        type: string
        description: The username from the form.
        required: true
      - name: password
        in: formData
        type: string
        description: The password from the form.
        required: true
    responses:
      200:
        description: Result of the form submission.
    """
    username = request.form.get('username')
    password = request.form.get('password')

    # Perform security tests or other logic here

    result = f"Form submitted with username: {username}, password: {password}"
    return jsonify(data=result), 200

# Endpoint pour rechercher un utilisateur par nom
@app.route("/user/<string:name>")
def search_user(name):
    """
    Endpoint to search for a user by name.
    ---
    parameters:
      - name: name
        in: path
        type: string
        description: The name of the user.
        required: true
    responses:
      200:
        description: Information about the user.
    """
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    cur.execute("select * from test where username = '%s'" % name)
    data = str(cur.fetchall())
    con.close()
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(data)
    return jsonify(data=data), 200

# Endpoint pour saluer un utilisateur
@app.route("/welcome/<string:name>")
def welcome(name):
    """
    Endpoint to welcome a user.
    ---
    parameters:
      - name: name
        in: path
        type: string
        description: The name of the user to welcome.
        required: true
    responses:
      200:
        description: Welcome message.
    """
    data = "Welcome " + name
    return jsonify(data=data), 200

# Endpoint pour obtenir les utilisateurs
@app.route("/get_users")
def get_users():
    """
    Endpoint to get users.
    ---
    parameters:
      - name: hostname
        in: query
        type: string
        description: The hostname to search for.
    responses:
      200:
        description: Result of the command.
    """
    try:
        hostname = request.args.get('hostname')
        command = "dig " + hostname
        data = subprocess.check_output(command, shell=True)
        return data
    except:
        data = str(hostname) + " username didn't found"
        return data

# ... Vos endpoints existants ...

# Endpoint pour lire le contenu d'un fichier
@app.route("/read_file")
def read_file():
    """
    Endpoint to read the content of a file.
    ---
    parameters:
      - name: filename
        in: query
        type: string
        description: The name of the file to read.
        required: true
    responses:
      200:
        description: Content of the file.
    """
    filename = request.args.get('filename')
    file = open(filename, "r")
    data = file.read()
    file.close()
    import logging
    logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
    logging.debug(str(data))
    return jsonify(data=data), 200

# Endpoint pour la désérialisation de données
@app.route("/deserialization/")
def deserialization():
    """
    Endpoint for data deserialization.
    ---
    responses:
      200:
        description: Deserialized data.
    """
    try:
        import socket, pickle
        HOST = "0.0.0.0"
        PORT = 8001
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            connection, address = s.accept()
            with connection:
                received_data = connection.recv(1024)
                data = pickle.loads(received_data)
                return str(data)
    except:
        return jsonify(data="You must connect 8001 port"), 200

# Endpoint pour obtenir l'email de l'administrateur
@app.route("/get_admin_mail/<string:control>")
def get_admin_mail(control):
    """
    Endpoint to get the administrator's email.
    ---
    parameters:
      - name: control
        in: path
        type: string
        description: The control parameter.
        required: true
    responses:
      200:
        description: Administrator's email.
    """
    if control == "admin":
        data = "admin@cybersecurity.intra"
        import logging
        logging.basicConfig(filename="restapi.log", filemode='w', level=logging.DEBUG)
        logging.debug(data)
        return jsonify(data=data), 200
    else:
        return jsonify(data="Control didn't set admin"), 200

# ... Ajoutez d'autres endpoints ...

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)

