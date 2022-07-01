# Reto Técnico Backend 💻
API para gestión de Posts, la cual permite:

  - Crear posts.
  - Ver los posts de forma paginada.
  - Dar like/dislike a los posts.
---

## Tabla de contenido  📄
1. Requerimientos
2. Instalación
3. Endpoints
    - Obtener listado de posts
    - Crear post
    - Like post
    - Dislike post
4. Pruebas unitarias
5. Autor

 ---
    
### Requerimientos ⚙️
  - Python versión 3

---

### Instalación  🚀

  - Clonar repositorio
    ```sh
        git clone https://github.com/CristianAlba75/Test-Backend-V.git
    ```
  - Crear entorno virtual local, ya sea con **pipenv** o **virtualenv**.
  - Instalar requerimientos del proyecto.
    ```sh
        pip install -r requirements.txt
    ```
 - Hacer migraciones.
    ```sh
        python manage.py makemigrations
        python manage.py migrate
    ```
 - Ejecutar servidor.
    ```sh
        python manage.py runserver
    ```
    
---
### Endpoints 🔩

Los endpoints del API son:

| Acción                 | Url                         |
|------------------------|-----------------------------|
| Obtener post paginados | /api/get_posts/<last_id>    |
| Crear posts            | /api/add_post               |
| Like post              | /api/like_post/<post_id>    |
| Dislike post           | /api/dislike_post/<post_id> |

 A continuación se detalla cada uno de los endpoints del API.

---

 #### Obtener listado de posts  `/api/get_posts/0`📋
 Este endpoint permite consultar el listado de posts paginados de 10 en 10.
 
 ```json
{
    "posts": [
        {
            "id": 16,
            "created_at": "2022-06-30",
            "name": "Post 10",
            "content": "Test post2",
            "email": "aaa@gmail.com",
            "likes": 5,
            "dislikes": 0
        },
        {
            "id": 7,
            "created_at": "2022-06-30",
            "name": "Post 1",
            "content": "Test post2",
            "email": "aaa@gmail.com",
            "likes": 0,
            "dislikes": 0
        }
      ]
  }
```

---

 #### Crear post ` /api/add_post` ➕
 Este endpoint permite crear posts. Recibe 3 parámetros:
 
| Parámetro | Descripción                      | Requerido | Tipo   |
|-----------|----------------------------------|-----------|--------| 
| name      | Nombre del post                  | Si        | String |
| content   | Contenido del post               | Si        | String |
| email     | Email de quien publica el post   | Si        | String |


El **body** de la petición es de la siguiente forma:
 
```json
{
    "name":"Post 22", 
    "content":"Test post2", 
    "email":"aaa@gmail.com"
}
```
 
 Como resultado, este endpoint retorna el post creado con la información relacionada.
 ```json
{
    "posts": {
        "id": 28,
        "created_at": "2022-06-30",
        "name": "Post 22",
        "content": "Test post2",
        "email": "aaa@gmail.com",
        "likes": 0,
        "dislikes": 0
    }
}
```

---

 #### Like post  `/api/like_post/<post_id>`👍
 Este endpoint permite dar like a un post. En la url se envía el id del post.
 
 
 Como resultado, este endpoint retorna el post con el contador de likes aumentado en 1.
 ```json
{
    "post": {
        "id": 16,
        "created_at": "2022-06-30",
        "name": "Post 10",
        "content": "Test post2",
        "email": "aaa@gmail.com",
        "likes": 5,
        "dislikes": 0
    }
}
```

---

 #### Dislike post  `/api/dislike_post/<post_id>`👎
 Este endpoint permite dar dislike a un post. En la url se envía el id del post.
 
 
 Como resultado, este endpoint retorna el post con el contador de dislikes aumentado en 1.
 ```json
{
    "post": {
        "id": 17,
        "created_at": "2022-06-30",
        "name": "Post 11",
        "content": "Test post2",
        "email": "aaa@gmail.com",
        "likes": 0,
        "dislikes": 4
    }
}
```
---

### Pruebas Unitarias 💣
Debe estar ubicado el directorio en donde se encuentra el archivo manage.py.
Para ejecutar las pruebas unitarias ejecutar:

   ```sh
       python manage.py test
   ```

---

### Autor ✒️

Desarrollado por Cristian Eduardo González Alba

📧 ingcristianalba@gmail.com

📇 <https://www.linkedin.com/in/cristian-alba75/>

🛠️<https://github.com/CristianAlba75/Test-Backend-V>