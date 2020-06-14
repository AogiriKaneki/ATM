<h1>INSTALL AND RUN INSRTUCTIONS </h1> <br />
you will need python3 and pip3 install via apt-get once pip3 is installed,  <br />
$ git clone https://github.com/AogiriKaneki/ATM.git <br />
$ pip3 install virtualenv <br />
$ Virtualenv venv_name <br />
$ source path/to/virtualenv/bin/activate <br />
$ pip3 install django djangorestframework djangorest-jwt pypscopg2 <br />
$ cd path/to/project <br />
$ python3 manage.py makemigrations <br />
$ python3 manage.py migrate <br />
$ python3 manage.py collectstatic <br />
$ python3 manage.py runserver <br />
