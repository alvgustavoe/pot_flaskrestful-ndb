
#POT: Flask-RESTful integration with NDB
##Questions
1. Dado que las keys de NDB son objetos compuestos... Como maneja/publica las keys NDB? Soporta mas de una manera de mostrar las keys?

2. Quiero una apreciación personal de cuanto mas trabajosa es de usar que Eve. Como punto de partida, se que una tarea extra es el armar las queries a NDB.

##Answers
1) Por lo que veo las Keys estan formadas por n-uplas de Kind + ID siendo Kind analogo a Tabla en el modelo relacional.

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
Respecto al ID podemos pasarlo como parametro en la instanciacion del objeto o sino NDB asigna uno.

Por lo que pude ver NDB maneja un mecanismo de consistencia de datos mediante relaciones parent/child, me parecio bastante importate lo siguiente:

*Entities whose keys have the same root form an entity group or group. If entities are in different groups, then changes to those entities might sometimes seem to occur "out of order". If the entities are unrelated in your application's semantics, that's fine. But if some entities' changes should be consistent, your application should make them part of the same group when creating them.*

A la hora de modelar el negocio creo importante podes generar este tipo de relacion para no perder la integridad de datos, si es que aplica. En el ejemplo comiteado la relacion de hace por una propiedad Key para almacenar las claves en relacion, pero no existe integridad por ejemplo en caso de que se borre un Team sus jugadores van a seguir apuntando a un Team inexistente.

Estaria bueno encarar el mismo ejemplo de Equipos y Jugadores usando esta forma de modelo. Si te parece lo codeo, avisame.

Respecto a la keys compuestas responden a este modelo parent/child, ejemplo:
```python
ndb.Key('Account', 'sandy@foo.com', 'Message', 123, 'Revision', '1')
ndb.Key('Revision', '1', parent = ndb.Key('Account', 'sandy@foo.com', 'Message', 123)
# or
ndb.Key('Revision', '1',
  parent = ndb.Key('Message', 123, parent = ndb.Key('Account', 'sandy@foo.com')))
```
2) Respecto a Python EVE por lo que veo FlaskRESTful ofrece mayor flexibilidad para hacer una solucion custom y una mejor adaptacion, realmente EVE nos libra de codear varios componentes aunque pienso que usando FlaskRESTful + calllog211 de Modesty (ejemplo que me enviaste) tenemos varios componentes a disposicion (ordenamiento, segmentacion, timestamps en entidades (created, updated), filtros) y lo mejor de todo compotibilidad no NBD. Seguro varios features de EVE si nos escapan y tendremos que desarrollarlos pero personalmente prefiero esto a tener que tocar el framework EVE para que responda a nuestras necesidades.

NDB nos ofrece tambien GQL: SQL-like language for retrieving entities or keys from the App Engine Datastore.

Por lo que veo es simple y pienso que simple tiene que ser dado que es un motor no-sql (joins no estarian disponibles).

Va el ejemplo que existe en la doc. de google:
```python
qry = ndb.gql("SELECT * FROM Account WHERE spam > :1")
qry2 = qry.bind(10)
#or
qry = ndb.gql("SELECT * FROM Account WHERE spam > :1", 10)
```
