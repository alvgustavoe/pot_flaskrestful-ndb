from flask import Flask
from flask.ext import restful

from controller.controllers import TeamController, PlayerController

app = Flask(__name__)
api = restful.Api(app)

api.add_resource(TeamController, '/teams')
api.add_resource(PlayerController, '/team/<team_id>/players')

if __name__ == '__main__':
    app.run(debug=True)
