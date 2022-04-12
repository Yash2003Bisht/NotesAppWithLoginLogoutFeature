from flask import Blueprint, flash, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from website.models import UserNotes
from . import db

views = Blueprint('views', __name__)

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    print(len(current_user.notes))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['desc']
        if len(title) < 4:
            flash("Your title is too short.", category="danger")
        elif len(description) < 10:
            flash("Your description is too short.", category="danger")
        else:
            note = UserNotes(title=title, description=description, refrence_key=current_user.id)
            db.session.add(note)
            db.session.commit()
            flash("Note added successfully.", category="success")
    return render_template("home.html", user=current_user)

@views.route("/delete/<int:user_id>")
@login_required
def delete(user_id):
    note = UserNotes().query.filter_by(id=user_id).first()
    db.session.delete(note)
    db.session.commit()
    flash("Note deleted successfully.", category="success")
    return redirect(url_for('views.home'))

@views.route("/update/<int:user_id>", methods=['GET', 'POST'])
@login_required
def update(user_id):
    note = UserNotes().query.filter_by(id=user_id).first()
    if request.method == 'POST':
        note.title = request.form['title']
        note.description = request.form['desc']
        note.refrence_key = current_user.id
        db.session.commit()
        flash("Note updated successfully.", category="success")
        return redirect(url_for('views.home'))
    return render_template('update.html', note=note, user=current_user)

