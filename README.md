## pot_flaskrestful-ndb
Build a POT (Proof of Technology) for Flask-RESTful integration with NDB. 

The main objective is to validate Flask-RESTful integrated with NDB and meet the requirements of this particular application. 

Even this POT is an asset of the project, it will have it's own repository. 

The idea behind this is to keep it free from business logic. 

This way will be easier teach to new developers how we use this technology.

***
## API Endpoints
### curl -v http://localhost:8080/teams
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