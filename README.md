# POT: Flask-RESTful integration with NDB
Build a POT (Proof of Technology) for Flask-RESTful integration with NDB. 

The main objective is to validate Flask-RESTful integrated with NDB and meet the requirements of this particular application. 

Even this POT is an asset of the project, it will have it's own repository. 

The idea behind this is to keep it free from business logic. 

This way will be easier teach to new developers how we use this technology.

***
## API Endpoints
### Retrieve all Teams
### curl -v http://localhost:8080/v2/teams
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /teams HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 258
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Wed, 08 Apr 2015 19:45:00 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "result": {
        "entities": [
            {
                "id": 5629499534213120,
                "name": "River Plate",
                "description": "The best team of the world"
            },
            {
                "id": 6192449487634432,
                "name": "Boca Juniors",
                "description": "The worst team of the world"
            }
        ]
    },
    "status": {
        "code": 200,
        "message": "OK"
    }
}
```
### Create new Team
### curl -vX PUT http://localhost:8080/v2/teams -H "Content-Type: application/json" -d '{"name": "Racing Club", "description": "amargos"}'
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> PUT /teams HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> Content-Type: application/json
> Content-Length: 49
> 
* upload completely sent off: 49 out of 49 bytes
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 143
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Wed, 08 Apr 2015 20:06:52 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "status": {
        "code": 201,
        "message": "created"
    }
}
```
### Retrieve all Players from existing Team
### curl -v http://localhost:8080/v2/team/5629499534213120/players
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> GET /team/5629499534213120/players HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 329
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Wed, 08 Apr 2015 20:10:02 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "result": {
        "entities": [
            {
                "team": "ahdkZXZ-Zmxhc2tyZXN0ZnVscGx1c25kYnIZCxIMRm9vdGJhbGxUZWFtGICAgICAgIAKDA",
                "id": 4644337115725824,
                "name": "Teo Gutierrez"
            },
            {
                "team": "ahdkZXZ-Zmxhc2tyZXN0ZnVscGx1c25kYnIZCxIMRm9vdGJhbGxUZWFtGICAgICAgIAKDA",
                "id": 6473924464345088,
                "name": "Barovero"
            }
        ]
    },
    "status": {
        "message": "OK",
        "code": 200
    }
}
```
### Create new Player from existing Team
### curl -vX PUT http://localhost:8080/v2/team/5629499534213120/players -H "Content-Type: application/json" -d '{"name": "Alvarez Balanta"}'
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> PUT /team/5629499534213120/players HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> Content-Type: application/json
> Content-Length: 27
> 
* upload completely sent off: 27 out of 27 bytes
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 203
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Wed, 08 Apr 2015 20:15:03 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "status": {
        "code": 201,
        "message": "created"
    }
}
```
### Delete Team
### curl -vX DELETE http://localhost:8080/v2/team/5629499534213120
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> DELETE /v2/team/5629499534213120 HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> 
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 47
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Fri, 10 Apr 2015 18:37:20 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "status": {
        "message": "deleted",
        "code": 200
    }
}
```
### Update Player
### curl -vX PATCH http://localhost:8080/v2/team/6333186975989760/player/4925812092436480 -H "Content-Type: application/json" -d '{"name": "Alvarez Balanta"}'
```ssh
* Hostname was NOT found in DNS cache
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8080 (#0)
> PATCH /v2/team/6333186975989760/player/4925812092436480 HTTP/1.1
> User-Agent: curl/7.35.0
> Host: localhost:8080
> Accept: */*
> Content-Type: application/json
> Content-Length: 27
> 
* upload completely sent off: 27 out of 27 bytes
< HTTP/1.1 200 OK
< content-type: application/json
< Cache-Control: no-cache
< Expires: Fri, 01 Jan 1990 00:00:00 GMT
< Content-Length: 47
* Server Development/2.0 is not blacklisted
< Server: Development/2.0
< Date: Fri, 10 Apr 2015 19:06:05 GMT
< 
* Connection #0 to host localhost left intact
```
```json
{
    "status": {
        "code": 200,
        "message": "updated"
    }
}
```
