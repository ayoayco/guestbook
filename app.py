from flask import Flask
import json
from .guestbook import guestbook
from .cache import cache

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)
cache.init_app(app, config={'CACHE_TYPE': 'SimpleCache'})
app.register_blueprint(guestbook, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
