from flask import Blueprint, render_template, current_app
from .cache import cache

blueprintname = Blueprint("blueprintname", __name__, template_folder="templates", static_folder="static")


def get_attribution():
    return current_app.config['ATTRIBUTION']

def get_app_config():
    return current_app.config['APPS']['blueprintname']


@blueprintname.route("/")
@cache.cached(timeout=300)
async def home():

    # DO STUFF...

    return render_template("_home.html", app=get_app_config(), attribution=get_attribution())
