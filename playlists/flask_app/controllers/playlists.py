from flask_app import app
from flask import get_flashed_messages, render_template, redirect, request, session, flash
from flask_app.models.playlist import Playlist

@app.route("/playlist/new")
def new_playlist():
    return render_template("new_playlist.html")

@app.route("/playlist/create", methods=["POST"])
def create_playlist():
    data = {
        "name": request.form['name'],
        "user_id": session['user_id']
    }
    Playlist.create(data)
    return redirect("/dashboard")
    
@app.route("/playlist/<int:id>")
def get_one_playlist(id):
    this_playlist = Playlist.get_one({"id": id})
    return render_template("one_playlist", playlist = this_playlist)