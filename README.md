## suvaider - > Follow the steps to start

Note: `install mongodb and python version 3.6 if you don't have`

  `then`

`first clone the repo and get inside the cloned directory`
1. open mongo shell `use suvaider` to create database
2. open terminal and type `mongoimport -d suvaider -c adult --type csv --file adult.data.csv --headerline` to import database
3. `pip install pipenv`
4. `cd pipenv`
5. `pipenv shell`
6. `cd ..`
7. `python src/manage.py migrate`
8. `python src/manage.py runserver'
9. open `http://127.0.0.1:8000/` in your browser

Note: `You don't need to install requirements.txt i have shared pipenv because it is slim as compared to virtualenv .
and in frontend i have used reactjs but, you don't need to shart fronend server i have done it with one server bt integrating build of reactjs with django`
