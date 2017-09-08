# Django news digest app

### Technologies:
  - [Python] - for using latests node version
  - [Django]
  - [Celery]
  - [RabbitMQ]
  - [Redis]
  - [PostgreSQL]
  - [Docker]
  - [Node.JS]
  - [Swagger]

### Want to use this project?

#### Setup

1. Fork/Clone this repo

1. Download [Docker] (if necessary)

1. Make sure you are using a Docker version >= 17:

    ```sh
    $ docker -v
    Docker version 17.06.0-ce, build 02c1d87
    ```

#### Fire up the Containers

Build the images:

```sh
$ docker-compose build
```

Run the containers:

```sh
$ docker-compose up -d
```

To stop the containers:

```sh
$ docker-compose stop
```

To bring down the containers:

```sh
$ docker-compose down
```

Want to force a build?

```sh
$ docker-compose build --no-cache
```

Remove images:

```sh
$ docker rmi $(docker images -q)
```

##### Swagger - <http://localhost:8005/docs>

Access Swagger docs at the above URL

[Python]: <https://www.python.org>
[Django]: <https://www.djangoproject.com/>
[Celery]: <http://www.celeryproject.org>
[RabbitMQ]: <https://www.rabbitmq.com>
[Redis]: <https://redis.io>
[PostgreSQL]: <https://www.postgresql.org>
[Docker]: <https://docker.com>
[Swagger]: <https://swagger.io>
[Node.JS]: <https://nodejs.org>


#### Описание
> Требуется разработать приложение, которое будет строить дайджест новостей с сайта http://lenta.ru (или например Медузы или нашего Insider.Pro). Дайджест — это выборка новостей (дата, название и краткое описание) за определенный промежуток дат по определенным категориям.

> Новости запрашиваются приложением раз в несколько минут по RSS, после чего лента разбирается и свежие новости сохраняются в БД. На фронтенде должна быть форма с автодополнением списка категорий, вводом двух дат (от и до) и адресом email.

> По запросу из формы должен генерироваться PDF-документ с дайджестом статей по запрошенным категориям. Затем документ должен отправляться на запрошенный адрес по электронной почте.

> Приложение архитектурно должно быть расчитано на обработку большого числа параллельных запросов, так что длительные операции: получение RSS, генерация PDF, отправка email — нужно вынести из основного процесса. Для этих целей можно использовать очередь сообщений (например, celery). Для генерации PDF по html есть простая и удобная библиотека xhtml2pdf.

> Платформа — Django, для разбора RSS можно применить любое удобное решение (от lxml.etree до BeautifulSoup). Периодический запрос данных очень желательно реализовать средствами проекта (например, в celery есть такая возможность), не используя системный crontab.
