# IDcom
 
Work training for fastapi

## Commands

- black **filename** : formatting files
- alembic revision --autogenerate : create migration

### Containers

- docker-compose -f .\docker\docker-compose.yml build : build image
- docker-compose down -v : delete containers and volumes
- docker-compose -f .\docker\docker-compose.yml --env-file .\backend\.env up : start containers with env file
- docker exec -it IDcom_fastapi bash : going into container terminal

### Testing

- pytest : starting tests
- --lf : last failed
- -vv : show full errors
- -s : show print
- -k : run only tests with this name
- -x : stop after first fail
- --pdb : start debugger after fail
- --cov : show coverage
