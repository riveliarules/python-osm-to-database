# Python OSM to database

Este é um projeto desenvolvido com a intenção de automatizar a importação dados do OpenStreetMaps para um banco de dados PostgreSQL.

## Instruções para o uso

### Um detalhe importante: 
Este script executa processos do Postgres que requerem a senha do usuário do banco de dados. Sendo assim, para o script rodar de forma 100% automatizada, sem a necessidade de inserção de senha via terminal, é necessário ter um arquivo .pgpass na pasta local do usuário que deseja rodá-lo.

**Instruções de como criar um arquivo .pgpass:** https://tableplus.com/blog/2019/09/how-to-use-pgpass-in-postgresql.html

### Instalação:
Clonar o projeto:
```shell
git clone https://git.pti.org.br/equipe-propria-de-desenvolvimento/python_osm_to_database/
```
Criar venv python e ativá-la:
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Instalar requirements:
```shell
pip install -r requirements.txt
```
Rodar o script:
```shell
python3 index.py
```

### Docker:
*em desenvolvimento*
