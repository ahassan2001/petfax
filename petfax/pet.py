from flask import Blueprint 

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

def create_app():
    from.import pet
    app.register_blueprint(pet.bp)

    return app

import json 

pets = json.load(open('pets.json'))
print(pets)

