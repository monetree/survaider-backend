# survaider-backend

`first Clone the repo`
mongoimport -d survaider -c adult --type csv --file adult.data.csv --headerline

`-----------------------------------------Way one using Docker----------------------------------------`

## install docker

1. `sudo apt-get update`
2. `sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common`
3. `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
4. `sudo apt-key fingerprint 0EBFCD88`
5. `sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"`
6. `sudo apt-get update`
7. `sudo apt-get install docker-ce`
8 . open `http://127.0.0.1:8000/` in your browser
   
 ## install docker-compose
   
1. `sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
2. `sudo chmod +x /usr/local/bin/docker-compose`

Now run command `sudo docker-compose up --build` to start project by getting inside root directory


`------------------------------------------------Way two without using docker--------------------------------------`

1. create your database as per settings.py 
2. uncomment the commented database and comment the uncommented database
3. get into root directory.
4. `cd pipenv`
5. `pipenv shell`
6. `cd..`
7.  `python manage.py runserver'
8  open `http://127.0.0.1:8000/` in your browser


`Still having issue??`
please check this video below


