# survaider-backend

`Clone the repo`

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
   
 ## install docker-compose
   
1. `sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
2. `sudo chmod +x /usr/local/bin/docker-compose`

Now run command `sudo docker-compose up --build` to start project by getting inside root directory
