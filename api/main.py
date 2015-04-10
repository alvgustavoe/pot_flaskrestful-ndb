from flask import Flask
from flask.ext import restful

from controller.controllers import TeamController, PlayerController
from controller.controllers_v2 import TeamControllerV2, PlayerControllerV2


app = Flask(__name__)
api = restful.Api(app)

api.add_resource(TeamController, '/v1/teams')
api.add_resource(PlayerController, '/v1/team/<team_id>/players')

api.add_resource(TeamControllerV2, '/v2/teams')
api.add_resource(PlayerControllerV2, '/v2/team/<team_id>/players')

if __name__ == '__main__':
    app.run(debug=True)
