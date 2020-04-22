# python-proxy-server
The story is taking place in a far away kingdom, where everybody (usually) lives happily.
But in a one bright day, suddenly, a cruel virus attacks and spreads throughout the kingdom.

Since this kingdom is very happy and doubtfully democratic, the king decides that the news about the virus shouldn't get to the people. they're better off not knowing.

In order to accomplish his mission the king decides to write a proxy which will be mandatory for every citizen of the kingdom to use, and since he's forced to stay at his palace since the outbreak, the king are trusting you with this mission.
You'd better help the king because he doesn't like to be disappointed.

1. You need to read and implement an simple http proxy and test it.
The server will listen on port 8080, and whenever a client sends an HTTP request, the server will make the request on behalf of the client and return the response.

2. Improve your proxy server, with every request the server will randomly change the user agent of the client.

3. Your server will now have a list of black list domains (that are spreading the news about the virus), with every request the server will check that the destination isn't blacklisted. If it is return some page about human rights and other boring stuff. 

4. With every request the server will look for cookies and credentials and save them to a DB. You need to implement the DB in Django and make it RESTful.

5. You need to add picture censorship, that is whenever a picture is received in the response, you need to replace it with a picture of a happy king.
