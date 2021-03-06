
<h1>Dataminr Challenge</h1>

<h2>How to setup the app</h2>

* Open a terminal
* Navigate to the main folder
* use command ```docker-compose build```
* After the build phase, just ```docker-compose up```


<h2>Relevant Info</h2>
<p>The Api is located at locahost:8000</p>
<p>An instance of Adminer is running at localhost:8080</p>
<p>Username and Password for Database can be found inside docker-compose.override.yml</p>

<h2>How to run the app</h2>
<ul>
    <li>Register a Subscription using the API</li>
    <li>Start monitoring using an external command (*)</li>
</ul>

(*) The external command is: </br>

```docker exec -it api python manage.py shell_plus --command="run_polling(subscription=Subscriptions.objects.get(id=1))"```
You can choose the id of the subcription you like to monitor

<h2>API schema</h2>
<p>Subscriptions support GET, POST, PUT and DELETE operations</p>
<p>the POST payload look like this:</p>

```json
{
    "address": "anotherEmail@gmail.com",
    "location": "Rome",
    "observers": [{"key": "temp", "target": 9, "condition": "below"}]
}
```

<h2>How to run the tests</h2>

Use the command ```docker exec -it api python manage.py tests```

<h2>Some considerations</h2>
<p>As you can see, there is not automatic system for starting the monitors.</br>
This is just to keep the challenge simple and give and idea of how it could work.</p>
<p>Also the views and serializers are very simple and didn't require any customization in order to speed up the process.</p>
