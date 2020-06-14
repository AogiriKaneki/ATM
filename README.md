INSTALL AND RUN INSRTUCTIONS
you will need python3 and pip3 install via apt-get once pip3 is installed, 
$ git clone https://github.com/AogiriKaneki/ATM.git
$ pip3 install virtualenv
$ Virtualenv venv_name
$ source path/to/virtualenv/bin/activate
$ pip3 install django djangorestframework djangorest-jwt pypscopg2
$ cd path/to/project
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
$ python3 manage.py runserver
