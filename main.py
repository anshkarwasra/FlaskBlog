from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
import os
from werkzeug.utils import secure_filename
'''
TODO:Add about text functionality 
'''

with open("config.json","r") as c:
    params = json.load(c)["params"]

local_server =params["local_server"]

app = Flask(__name__)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]


app.secret_key = "my-secret-key"

app.config['UPLOADER_FOLDER'] = params['upload_location']

db = SQLAlchemy(app)

class Contactmessage(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120),unique=False,nullable=False)
    phoneNumber = db.Column(db.String(12),unique=False,nullable=False)
    message =db.Column(db.String(120),unique=False,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False)
    email = db.Column(db.String(20),nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120),unique=False,nullable=False)
    content = db.Column(db.String(12),unique=False,nullable=False)
    slug =db.Column(db.String(120),unique=False,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False)
    img_file =db.Column(db.String(120),unique=False,nullable=False)
    upvote = db.Column(db.Integer,unique=False,nullable=False)

class Comments(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.String(120),unique=False,nullable=False)
    content = db.Column(db.String(120),unique=False,nullable=False)
    date = db.Column(db.String(120),unique=False,nullable=False)
    post = db.Column(db.String(120),unique=False,nullable=False)


class Users(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=False,nullable=False)
    email = db.Column(db.String,unique=False,nullable=False)
    pasword = db.Column(db.String,unique=False,nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()[0:params["number_of_posts"]]
    return render_template("index.html",params=params,posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",params=params)

@app.route("/contact",methods = ["GET","POSt"])
def contact():
    if(request.method=="POST"):
        '''add entry to db'''
        name = request.form.get('name')
        email = request.form.get('email')
        msg = request.form.get('msg')
        print(msg)
        phNumber = request.form.get('phNumber')
        date = str("23/03/6969")
        entry = Contactmessage(name=name,message=msg,phoneNumber=phNumber,email=email,date=date)
        db.session.add(entry)
        db.session.commit()
        

    return render_template("contact.html",params=params)


@app.route("/post/<string:post_slug>",methods=["GET"])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    comment = Comments.query.filter_by(post=post_slug)



    return render_template("blog.html",params=params,post=post,comment=comment)






@app.route("/blogs")
def blog():
    return render_template("blog.html",params=params)

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if "user" in session and session["user"]==params["admin_user"]:
        posts=  Posts.query.all()
        return render_template("dashboard.html",params=params,posts=posts)


    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username)[0]
        try:
            session["user"] = username
            posts = Posts.query.all()
            return render_template("dashboard.html",params=params,posts=posts)
        except Exception as e:
            print(e)
            return e
    else:
        return render_template("login.html",params=params)

@app.route("/edit/<string:sno>",methods=["GET","POST"])
def edit(sno):
    if "user" in session and session["user"]==params["admin_user"]:
        if request.method == "POST":
           box_title = request.form.get('title')
           tline=  request.form.get('tline') 
           slug=  request.form.get('slug')
           content = request.form.get('content')
           img_file = request.form.get('img')

           if sno=="0":
               post=  Posts(title=box_title,slug=slug,content=content,date="1/2/11",img_file=img_file)
               db.session.add(post)
               db.session.commit()
               print("post added succesfully")
               return redirect('/dashboard')
           else:
               post=  Posts.query.filter_by(sno=sno).first()
               post.title = box_title
               post.slug = slug
               post.content = content
               post.date=  "1/23/56"
               post.img_file=  img_file
               db.session.commit()
               return redirect('/edit/'+sno)
               
        post=  Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html",params=params,post = post,sno=sno) 


@app.route("/uploader" ,methods = ["GET", "POST"])
def uploader():
    if "user" in session and session["user"]==params["admin_user"]:
        if request.method == "POST":
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOADER_FOLDER'],secure_filename(f.filename)))
            return "Uploaded successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/upvote/<string:post_slug>")
def upvote(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    post.upvote+=1
    db.session.commit()
    return redirect("/post/"+str(post_slug))

@app.route("/comment/<string:post_slug>",methods = ["GET","POST"])
def saveComments(post_slug):
    if "user" in session and session["user"]==params["admin_user"]:
        if request.method =="POST":
            user = params["admin_user"]
            content = request.form.get("content")
            comment = Comments(user=user,content=content,date="000",post=post_slug)
            db.session.add(comment)
            db.session.commit()
        return redirect(f"/post/{post_slug}")
    return "login ker yaar"

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method =="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        user = Users(email=email,password=password,username=username)
        db.session.add(user)
        db.session.commit()
        redirect('/dashboard')
        

    return render_template('login.html',params=params)

app.run(debug=True)