from flask import Flask
from controllers.music_controller import music_blueprint

app = Flask(__name__)
app.register_blueprint(music_blueprint)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
