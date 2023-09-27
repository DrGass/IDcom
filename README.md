<style>
question { color: #4491c7 }
answer { color: #f8f8ff }

</style>

# IDcom

Work training for fastapi

## Commands

- black **filename** : formatting files
- alembic revision --autogenerate : create migration

## Containers

### <question> build image

<answer> docker-compose -f .\docker\docker-compose.yml build

### <question> delete containers and volumes

<answer> docker-compose down -v

### <question> start containers with env file

<answer> docker-compose -f .\docker\docker-compose.yml --env-file .\backend\\.env up

### <question> going into container terminal

<answer> docker exec -it IDcom_fastapi bash

## Testing

- pytest : starting tests
- --lf : last failed
- -vv : show full errors
- -s : show print
- -k : run only tests with this name
- -x : stop after first fail
- --pdb : start debugger after fail
- --cov : show coverage
