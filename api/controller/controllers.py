from flask.ext.restful import reqparse, abort, Api, Resource
from ..model.model import FootballTeam, FootballPlayer

from ..common.response import *
from ..common.validator import *
from ..common.util import *

team_parser = reqparse.RequestParser()
team_parser.add_argument('name', type=str)
team_parser.add_argument('description', type=str)

class TeamController(Resource):
    def get(self):    	
    	teams = FootballTeam.query().fetch()

    	resObj = ResBase()
    	prep_entity_list(resObj, teams)
        return resObj.get_json()

    def put(self):    	
        args = team_parser.parse_args()
        team = FootballTeam(name=args['name'], description=args['description'])
        team.put()

        resObj = ResBase()
    	prep_entity_list(resObj, [team])
        return resObj.get_json()

player_parser = reqparse.RequestParser()
player_parser.add_argument('name', type=str)

class PlayerController(Resource):
    def get(self, team_id):
    	team_key = ndb.Key(FootballTeam, int(team_id))
    	players = FootballPlayer.query(FootballPlayer.team == team_key).fetch()

    	resObj = ResBase()
    	prep_entity_list(resObj, players)
        return resObj.get_json()

    def put(self, team_id):
    	team_key = ndb.Key(FootballTeam, int(team_id))

        args = player_parser.parse_args()
        player = FootballPlayer(name=args['name'], team=team_key)
        player.put()

        resObj = ResBase()
    	prep_entity_list(resObj, [player])
        return resObj.get_json()
        