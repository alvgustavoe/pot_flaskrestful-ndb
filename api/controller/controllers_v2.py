from flask.ext.restful import reqparse, abort, Api, Resource
from ..model.model_v2 import FootballTeamV2, FootballPlayerV2

from ..common.response import *
from ..common.validator import *
from ..common.util import *


team_parser = reqparse.RequestParser()
team_parser.add_argument('name', type=str)
team_parser.add_argument('description', type=str)

class TeamControllerV2(Resource):
    def get(self):    	
    	teams = FootballTeamV2.query().fetch()

    	resObj = ResBase()
    	prep_entity_list(resObj, teams)
        return resObj.get_json()

    def put(self):    	
        args = team_parser.parse_args()
        team = FootballTeamV2(name=args['name'], description=args['description'])
        team.put()

        resObj = ResBase()
    	prep_entity_list(resObj, [team])
        return resObj.get_json()

player_parser = reqparse.RequestParser()
player_parser.add_argument('name', type=str)

class PlayerControllerV2(Resource):
    def get(self, team_id):
    	team_key = ndb.Key(FootballTeamV2, int(team_id))
    	players = FootballPlayerV2.query(ancestor=team_key).fetch()

    	resObj = ResBase()
    	prep_entity_list(resObj, players)
        return resObj.get_json()

    def put(self, team_id):
    	team_key = ndb.Key(FootballTeamV2, int(team_id))

        args = player_parser.parse_args()
        player = FootballPlayerV2(parent=team_key, name=args['name'])
        player.put()

        resObj = ResBase()
    	prep_entity_list(resObj, [player])
        return resObj.get_json()
        