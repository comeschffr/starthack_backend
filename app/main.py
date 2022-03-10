from flask import Flask, jsonify
app= Flask(__name__)


@app.route('/')
def index():
    return jsonify(["<h1>Welcome to my app bro through github (main branch)</h1>"])



@app.route('/register', methods=["GET", "POST"])
def register():
    return jsonify(["user alredy existssssssssssssssss"])


@app.route('/login', methods=["GET", "POST"])
def login():
    return jsonify(["login bro"])


@app.route('/new', methods=["GET"])
def new_feature():
    return jsonify(["good job accessing the new feature"])


@app.route('/hello', methods=["GET"])
def hello():
    return jsonify(["hello"])

# from flask import Blueprint, request, json, jsonify
# from .models import Student
# from software import db

# views = Blueprint('views', __name__)

# @views.route('/register', methods=["GET", "POST"])
# def register():
#     d={}
#     if request.method =="POST":
#         mail = request.form["email"]
#         password = request.form["password"]

#         email = Student.query.filter_by(email=mail).first()

#         if email is None:
#             register = Student(email=mail, password=password)

#             db.session.add(register)
#             db.session.commit()
           
#             return jsonify(["Register success"])
#         else:
#             # already exist
            
#             return jsonify(["user alredy exist"])


# @views.route('/login', methods=["GET", "POST"])
# def login():
#     d = {}
#     if request.method == "POST":
#         mail = request.form["email"]
#         password = request.form["password"]

#         login = Student.query.filter_by(email=mail, password=password).first()

#         if login is None:
#             # acount not found
            
#             return jsonify(["Wrong Credentials"]) 
#         else:
#             # acount found
            
#             return jsonify([ "success"])