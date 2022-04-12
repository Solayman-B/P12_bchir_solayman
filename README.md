# P12_bchir_solayman

Summaries
---------

* General description
* Requirements
* Installation
* Run the script

General description
-------------

This project is customer relationship management software for the Epic Events company.


Requirements
---------

This application uses the following packets:

* asgiref==3.5.0
* attrs==21.4.0
* Django==4.0.3
* django-filter==21.1
* djangorestframework==3.13.1
* djangorestframework-simplejwt==5.1.0
* iniconfig==1.1.1
* packaging==21.3
* pluggy==1.0.0
* psycopg2==2.9.3
* psycopg2-binary==2.9.3
* py==1.11.0
* PyJWT==2.3.0
* pyparsing==3.0.7
* python-dateutil==2.8.2
* python-decouple==3.6
* pytz==2022.1
* six==1.16.0
* sqlparse==0.4.2
* tomli==2.0.1


Installation
------------

First, you can download this project by :

clicking on « code » then « download ZIP »

or [click here to download it directly](https://github.com/Solayman-B/P12_bchir_solayman/archive/refs/heads/main.zip)

Unzip the file when the download is completed

You can also install [Git via this link](https://git-scm.com/downloads) and use :

    gh repo clone Solayman-B/P12_bchir_solayman


To use this application properly, you need to use [python3](https://www.python.org/downloads/)

Then you can create a virtual environment:

    python3 -m venv env # env is the name of the directory, but you can choose another one if you want

On Windows, run:

    env\Scripts\activate.bat

On Unix or macOS, run:

    source env/bin/activate

And to deactivate, simply use:

    deactivate

You can install all the required paquets with:

    pip install -r requirements.txt


Run
---

Go to the folder containing the project and use `python3 main.py runserver` then open Postman or another program and follow the  [documentation](https://documenter.getpostman.com/view/19329986/UVyyut4y) to see examples of all the URIs of the project.


