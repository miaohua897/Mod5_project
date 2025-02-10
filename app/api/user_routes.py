from flask import Blueprint
from flask_login import login_required, current_user
from app.models import User

user_routes = Blueprint("users", __name__)


@user_routes.route("/")
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route("/<int:user_id>")
@login_required
def user(user_id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(user_id)
    return user.to_dict()


@user_routes.route('/current')
@login_required
def get_current_user():
    """
    Query for current user data and returns that user in a dictionary
    """
    user = User.query.get(current_user.id)
    songIds = [song.id for song in user.songs]        
    playlistIds = [playlist.id for playlist in user.playlists]
    albumIds = [album.id for album in user.albums]        
    likedSongIds = [liked_song.id for liked_song in user.liked_songs]
        
    response = user.to_dict()
    response['songIds'] = songIds
    response['playlistIds'] = playlistIds
    response['albumIds'] = albumIds
    response['likedSongIds'] = likedSongIds
        
    return response