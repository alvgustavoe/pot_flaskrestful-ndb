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

        return {'status': {'message': 'created', 'code': 201}}

    def patch(self, team_id):
        team_key = ndb.Key(FootballTeamV2, int(team_id))
        team = team_key.get()

        args = team_parser.parse_args()
        team.name = args['name']
        team.description = args['description']
        team.put()

        return {'status': {'message': 'updated', 'code': 200}}

    def delete(self, team_id):
        team_key = ndb.Key(FootballTeamV2, int(team_id))
        ndb.delete_multi(ndb.Query(ancestor=team_key).iter(keys_only = True))
        team_key.delete()

        return {'status': {'message': 'deleted', 'code': 200}}

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

        return {'status': {'message': 'created', 'code': 201}}
        
    def patch(self, player_id):
        player_key = ndb.Key(PlayerControllerV2, int(player_id))
        player = player_key.get()

        args = player_parser.parse_args()
        player.name = args['name']
        player.put()

        return {'status': {'message': 'updated', 'code': 200}}

    def delete(self, team_id, player_id):
        player_key = ndb.Key(PlayerControllerV2, int(player_id))
        player_key.delete()

        return {'status': {'message': 'deleted', 'code': 200}}
