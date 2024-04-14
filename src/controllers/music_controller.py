from flask import Blueprint, request
from music_model import MusicLibraryModel, MusicModel

music_blueprint = Blueprint("music", __name__)


@music_blueprint.get("/")
def get_musics():
    return MusicLibraryModel.list_musics()


@music_blueprint.post("/")
def add_music():
    music = MusicModel(**request.json)
    return MusicLibraryModel.add_music(music)
