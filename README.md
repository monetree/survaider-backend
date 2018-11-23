## suvaider - > Follow the steps to start

Note: `install mongodb and python version 3.6 if you don't have`

  `then`

`first clone the repo and get inside the cloned directory`
1. open mongo shell `use suvaider` to create database
2. open terminal and type `mongoimport -d suvaider -c adult --type csv --file adult.data.csv --headerline` to import database
3. `cd pipenv`
4. `pipenv shell`
5. `cd ..`
6. `python src/manage.py migrate`
7. `python src/manage.py runserver'
8. open `http://127.0.0.1:8000/` in your browser
