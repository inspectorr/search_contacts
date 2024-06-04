```
docker compose up -d
docker exec sc_server python -m database.create_tables
docker exec sc_server python -m database.scripts.import_contacts
docker exec sc_server python -m elastic.manage
```
