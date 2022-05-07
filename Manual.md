# For local development

Activate the virtual environment using the commands:
```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the required libraries
```bash
pip3 install -r requirements.txt
pip3 install -r requirements_demon.txt
```

The next step is to export the environment variables like:
```bash
export DB_MESSAGES="postgresql://<__USER__>:<__PASSWORD__>@<__IP__>:<__PORT__>/<__DB__>"
export REDIS_CONNECT="redis://<__USER__>:<__PASSWORD__>@<__IP__>:<__PORT__>"
export API="http://<__IP__>:<__PORT__>"
```

> (!) Do not forget to specify the secret data in the fields, they are all highlighted in the same style.

A list of files where you need to enter secret data:
- [compose_redis.yml](./docker-compose_redis.yml)
- [docker-compose_blenderbot.yml](./docker-compose_blenderbot.yml)
 
And you can run the application:
```bash
python3 run.py
```



# For deploy

On the machine responsible for the neural part, transfer all the project files and run the command
```bash
docker-compose -f docker-compose_blenderbot.yml --compatibility up -d
```

On the machine responsible for Redis, move all the project files and run the command
```bash
docker-compose -f docker-compose_redis.yml --compatibility up -d
```


