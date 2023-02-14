### Big Data Purification (Company names) with Flask application


This project obtains data about companies from a SQLite file using an API and after 
editing the names of the companies posts the same data in the MongoDB database.
The project is entirely written in 2 work files, the first one is a Flask application
used for the APIs and the second is normal Python used to normalise the names of the 
companies.
The Flask application is written only for the 2 APIs and works only for the formats
described.
The Python code is made with several functions to edit the name, there are two 
functions that remove parenthesis and the text between them, and the quotation marks.
There is also a function which lowers all letters in a word except the first, which
also takes care of acronyms leaving them with all capital letters.

For the Flask application the following modules are necessary:
<!-- Unordered List -->
* flask
* pymongo
* sqlite3
* json

For the Python code the following modules are necessary:
<!-- Unordered List -->
* requests
* json
* re
* cleanco version 2.1

Note: this project does not include the front-end part, although there is room in the
code for the front-end part to be implemented.