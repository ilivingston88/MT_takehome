# MT_takehome
This app is based on the parameters of an assignment (listed at bottom), to create a CRUD application that acts on FizzBuzz database objects. 
Once the application code is pulled down from github, navigate to the directory that contains the manage.py file. 

To start the party, use the command:
python manage.py fizzparty

This will create 100 FizzBuzz objects. 

The DJANGO admin page can be found here:
#http://127.0.0.1:8000/admin/takehome_app/fizzbuzz/

App currently allows the following:
GET /fizzbuzz                       to list all fizzbuzz objects 
GET /fizzbuzz/123              to retrieve a single fizz buzz object 
POST /fizzbuzz                    to create a new fizzbuzz object 

Future iterations could limit endpoints to just these (currently full CRUD functionality is possible with the DJANGO ViewSet class. 


<!-- Task Summary: 

 
Using Django Rest Framework, create an API endpoint for “fizzbuzzes” that supports 3 operations: retrieve, list, and create. 
 
GET /fizzbuzz                       to list all fizzbuzz objects 
GET /fizzbuzz/123              to retrieve a single fizz buzz object 
POST /fizzbuzz                    to create a new fizzbuzz object 
 
The endpoint has been documented in detail here: http://docs.fizzbuzz.apiary.io 
 
When you’ve completed the code, please upload it to a public git repo and send me the link. 
 
Notes: 

Don’t worry about setting up a postgres db, just use the stock sqllite dev database that Django uses by default.  

Don't worry about hosting, either. To test your endpoint, I will run your code locally and use the Browsable API: http://www.django-rest-framework.org/topics/browsable-api/ 

Use best practices and common sense for field names, default values, validation, unit tests, etc. 

Bonus tasks: If you breeze through the above exercise and want to tackle something a little harder, here are two more features to implement: 

Write Unit Tests to cover basic functionality, using factories or fixtures to populate mock data. 

Document your code (through Docstrings, perhaps? Or in a method of your own choosing)  -->
