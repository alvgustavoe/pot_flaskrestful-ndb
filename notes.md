
#POT: Flask-RESTful integration with NDB
##Questions
1. Dado que las keys de NDB son objetos compuestos... Como maneja/publica las keys NDB? Soporta mas de una manera de mostrar las keys?

2. Quiero una apreciación personal de cuanto mas trabajosa es de usar que Eve. Como punto de partida, se que una tarea extra es el armar las queries a NDB.

##Answers
1. Por lo que veo las Keys esta formadas por n-uplas de Kind + ID siendo Kind analogo a Tabla en el modelo relacional.

Va un ejemplo:
```python
from google.appengine.ext import ndb
from api.model.model import FootballTeam

team_key = ndb.Key(FootballTeam, 5066549580791808)
print 'Key ' + str(team_key)

team = team_key.get()
print 'Team ' + str(team)
```
Output
```ssh
Key Key('FootballTeam', 5066549580791808)
Team FootballTeam(key=Key('FootballTeam', 5066549580791808), description=u'El mejor', name=u'River Plate')
```

Para acceder a la key de una entidad podemos hacer lo siguiente:
```python
team.key.id()
```
Respecto al ID podemos pasarlo como parametros en la creacion del objeto o sino NDB asigna uno.

Por lo que pude ver NDB maneja un mecanismo de consistencia de datos mediante relaciones parent/child, me parecio bastante importate lo siguiente:

*Entities whose keys have the same root form an entity group or group. If entities are in different groups, then changes to those entities might sometimes seem to occur "out of order". If the entities are unrelated in your application's semantics, that's fine. But if some entities' changes should be consistent, your application should make them part of the same group when creating them.*
