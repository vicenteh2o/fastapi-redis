# Este proyecto fue iniciado con:

- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt

# Redis Setup

Para usar Redis con Docker:

```bash
# Iniciar Redis
docker run -d --name fastapi-redis-server -p 6379:6379 redis:latest

# Detener Redis
docker stop fastapi-redis-server

# Reiniciar Redis
docker start fastapi-redis-server
```

Para instalar redis-cli:

```bash
# Instalar Redis (incluye redis-cli)
brew install redis

# Conectar a Redis
redis-cli -h localhost -p 6379
```

## Comandos básicos de Redis:

```bash
# Ver todas las keys
KEYS *

# Obtener el valor de una key
GET key_name

# Ver tipo de dato de una key
TYPE key_name

# Ver TTL (tiempo de vida) de una key
TTL key_name

# Eliminar una key específica
DEL key_name

# Eliminar todas las keys de la base de datos actual
FLUSHDB

# Eliminar todas las keys de todas las bases de datos
FLUSHALL
```

# Test con httpie

- brew install httpie
- http :8000/rick-morty/1
