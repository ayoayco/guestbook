from flask import Flask
import json
from .blueprintname import blueprintname
from .cache import cache

# TODO: Update blueprintname

app = Flask(__name__)
cache.init_app(app, config={'CACHE_TYPE': 'SimpleCache'})
app.register_blueprint(blueprintname, url_prefix='/')
app.config.from_file("config.json", load=json.load)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
