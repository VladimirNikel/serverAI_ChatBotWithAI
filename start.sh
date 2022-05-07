#!/bin/bash

export DB_MESSAGES="postgresql://<__USER__>:<__PASSWORD__>@<__IP__>:<__PORT__>/<__DB__>"
export REDIS_CONNECT="redis://<__USER__>:<__PASSWORD__>@<__IP__>:<__PORT__>"
export API="http://<__IP__>:<__PORT__>"

pthon3 run.py
