from flask import render_template, request, redirect, url_for, flash, session, abort
from models import Users_Data, Notes
from datetime import datetime
from app import db, bcrypt
from flask_login import current_user , login_user, logout_user, login_required

def register_routes(app):
    
    @app.route("/")
    def home():
        blogs = db.session.query(
            Notes.title, 
            Notes.content, 
            Notes.created_on, 
            Users_Data.username
        ).join(Users_Data, Notes.user_id == Users_Data.uid).all()
        blogs = blogs[::-1]
        
        return render_template("index.html", current_user=current_user, blogs=blogs)
    
    
    @app.route("/register", methods= ['GET', "POST"])
    def register():
        if request.method == "POST":    
            username = request.form.get("username").strip()
            password = request.form.get("password").strip()
            
            user_exists = Users_Data.query.filter_by(username=username).first()
            if user_exists:
                flash("Current Username is not available, try another!", "danger")
                return redirect(url_for("register"))
            
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            
            user = Users_Data(username=username, password=hashed_password, created_on=datetime.now().replace(microsecond=0))
            
            db.session.add(user)
            db.session.commit()
            flash("You Signed Up successfully!", "success")
            
            return redirect(url_for('login'))
            
        return render_template("register.html")
            
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username").strip()
            password = request.form.get("password").strip()
            
            
            user = Users_Data.query.filter(Users_Data.username == username).first()
            
            if user is None:
                flash("No account found", "danger")
                return redirect(url_for("login"))
            
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid username or password", "danger")
                return redirect(url_for("login"))
            
        return render_template("login.html")
    
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("home"))
    
    @app.route("/dashboard")
    @login_required
    def dashboard():
        if current_user.is_authenticated:
            
            details = [Notes.query.filter_by(user_id=current_user.uid).count(), current_user.created_on, current_user.username]
            

            
            return render_template("dashboard.html", user = current_user, details = details)
        else:
            return redirect(url_for("login"))
        
        
    @app.route("/create-note", methods=["GET", "POST"])
    @login_required
    def create_note():
        if request.method == "POST":
            title = request.form.get("title").strip()
            content = request.form.get("content").strip()
            
                # Add validation
            if not title or not content:
                flash("Title and content are required!", "danger")
                return render_template("create_note.html", title=title, content=content)
            
            if len(title) > 200:  # Assuming you have length limits
                flash("Title too long!", "danger")
                return render_template("create_note.html", title=title, content=content)
            
            note = Notes(title = title, 
                         content = content, 
                         created_on = datetime.now().replace(microsecond=0), 
                         user_id = current_user.uid
                         )
            
            db.session.add(note)
            db.session.commit()            
            
            flash("Blog created Successfully!", "success")
            
            return redirect(url_for('view_notes'))
        else:
            
        
            return render_template("create_note.html")
    
    @app.route("/view-notes")
    @login_required
    def view_notes():
        notes = Notes.query.filter_by(user_id = current_user.uid).all()
        return render_template("view_notes.html", notes = notes)
    
    @app.route("/edit-note/<int:nid>", methods=["GET", "POST"])
    @login_required
    def edit_note(nid):
        note = Notes.query.get_or_404(nid)
        
        if note.user_id != current_user.uid:
            abort(403)  # Forbidden

        if request.method == "POST":
            note.title = request.form.get("title").strip()
            note.content = request.form.get("content").strip()
            note.created_on = datetime.now().replace(microsecond=0)
            
            db.session.commit()            
            
            flash("Blog updated Successfully!", "success")
            
            return redirect(url_for('view_notes'))
        
        return render_template("edit_note.html", note = note)
        
    @app.route("/delete-note/<int:nid>")
    @login_required
    def delete_note(nid):
        note = Notes.query.get_or_404(nid)
        if note:
            db.session.delete(note)
            db.session.commit()
        
        return redirect(url_for("view_notes"))
    
    
