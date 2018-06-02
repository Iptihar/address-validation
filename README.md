# address-validation
simple USPS address validation using python and flask module

requirement: python 2.7 or higher, a modern web browser (chrome prefered), Flask module
 (install by "pip install Flask")

front-end: written by html/css, works as a UI to enter adrress, and show returned address or error.
back-end: written in python, reformat the address, send it to USPS address validation service
using API (current API is a trial key works up to 500 transactions and only valid for 30 days)


usage: download "project.html" and "handle.py" to same folder, then create another forlder called
"templates" put "project.html" to "templates" folder, then open cmd and go to your directory 
under which "handle.py" and "templates" reside. type the command "python handle.py", then open
your browser and go to "http://localhost:5000/", you will see hosted webpage. Enter your address 
and use validate button. 

once you run python program from command line you should be able to see "All tests successful." 
message which means the unit tests inside runTest() function returned true.  

Also screen shots were attached. 

libraries used:  Flask library, RESTful API, requests library

USPS address validation api came from: "https://www.serviceobjects.com/products/address-geocoding/usps-address-validation"   if the key expired, go to that website and sign up a new one.
