from google.appengine.ext import ndb


class FootballTeamV2(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.StringProperty()

class FootballPlayerV2(ndb.Model):
	name = ndb.StringProperty()
