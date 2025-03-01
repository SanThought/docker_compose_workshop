# API de Estudiantes con Docker Compose y PostgreSQL

Este proyecto demuestra cómo configurar una API en Flask con PostgreSQL utilizando Docker Compose. Es parte del ejercicio del taller sobre la orquestación de servicios con Docker Compose.

## Objetivos del Ejercicio

1. Configurar y ejecutar múltiples servicios con Docker Compose.
2. Reemplazar el almacenamiento en archivo JSON por PostgreSQL.
3. Conectar una API Flask a PostgreSQL utilizando SQLAlchemy ORM.
4. Ejecutar la API en un entorno orquestado por Docker Compose.

## Estructura del Proyecto

```
docker_compose_workshop/
├── api/
│   ├── app.py              # Aplicación Flask con SQLAlchemy ORM
│   ├── Dockerfile          # Configuración de Docker para la API
│   └── requirements.txt    # Dependencias de Python
└── docker-compose.yml      # Configuración de Docker Compose
```

## Prerrequisitos

- Docker y Docker Compose instalados en tu sistema Ubuntu.
- Conocimientos básicos de APIs REST y bases de datos SQL.

## Configuración y Ejecución

### 1. Clonar el Repositorio

```bash
git clone https://github.com/SanThought/docker_compose_workshop.git
cd docker_compose_workshop
```

### 2. Iniciar los Servicios con Docker Compose

```bash
docker-compose up -d
```

Esto iniciará los servicios de la API, PostgreSQL y opcionalmente pgAdmin.

### 3. Verificar que los Contenedores Están Corriendo

```bash
docker-compose ps
```

La API estará disponible en: [http://localhost:5000](http://localhost:5000)

## Endpoints de la API

- **GET /students**: Obtener todos los estudiantes.
- **GET /students/{id}**: Obtener un estudiante específico por ID.
- **POST /students**: Crear un nuevo estudiante.
  - Campos requeridos: `nombre`
  - Campos opcionales: `edad`, `carrera`
- **PUT /students/{id}**: Actualizar un estudiante.
- **DELETE /students/{id}**: Eliminar un estudiante.

## Ejemplo de Uso

### Agregar un Nuevo Estudiante

```bash
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Perez", "edad": 21, "carrera": "Ingeniería"}'
```

### Obtener Todos los Estudiantes

```bash
curl http://localhost:5000/students
```

## Gestión de la Base de Datos

El proyecto incluye pgAdmin para la administración de la base de datos:

- URL: [http://localhost:5050](http://localhost:5050)
- Email: `admin@example.com`
- Contraseña: `admin`

Para conectar la base de datos en pgAdmin:

1. Agregar un nuevo servidor.
2. Configurar el host como "db" y el puerto como `5432`.
3. Usuario: `postgres`.
4. Contraseña: `postgres`.

## Detener la Aplicación

Para detener todos los servicios:

```bash
docker-compose down
```

Para detener los servicios y eliminar volúmenes (borrar todos los datos):

```bash
docker-compose down -v
```

## Notas Adicionales

1. **Comprensión de Docker Compose**:

   - Cada servicio definido en `docker-compose.yml` se ejecuta en un contenedor.
   - Los servicios pueden referenciarse por su nombre en `depends_on`.
   - El almacenamiento persistente se maneja con volúmenes de Docker.

2. **Depuración**:

   - Ver logs de los servicios: `docker-compose logs`
   - Ver logs de la API: `docker-compose logs api`
   - Ver logs de la base de datos: `docker-compose logs db`

3. **Recomendaciones para Producción**:

---
