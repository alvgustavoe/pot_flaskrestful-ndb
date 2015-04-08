from google.appengine.ext import ndb


class FootballTeam(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.StringProperty()

class FootballPlayer(ndb.Model):
	name = ndb.StringProperty()
	team = ndb.KeyProperty(kind=FootballTeam)
	#team = ndb.ReferenceProperty(FootballTeam, collection_name='players')
