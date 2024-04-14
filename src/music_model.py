from dataclasses import dataclass
from database import db


@dataclass
class MusicModel:
    name: str
    artist: str
    album: str
    release_year: int
    genre: str
    image: str


@dataclass
class StoredMusicModel(MusicModel):
    _id: str

    def __post_init__(self):
        self._id = str(self._id)


class MusicLibraryModel:
    _collection = db["musics"]

    @classmethod
    def list_musics(cls):
        data = cls._collection.find()
        return [StoredMusicModel(**music) for music in data]

    @classmethod
    def add_music(cls, music: MusicModel):
        cls._collection.insert_one(music.__dict__)
        return {"message": "Music added"}
