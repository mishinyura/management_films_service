# Сервис управления списком избранных фильмов
<a href="https://netology.ru/" target="blank"><img align="center" src="https://static.tildacdn.com/tild6635-6562-4662-a365-663533313766/full_1.svg" alt="Netology logo" height="50" width="200" /></a>

<a href="https://www.kinopoisk.ru/" target="blank"><img align="center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Kinopoisk_colored_logo_%282021-present%29.svg/1280px-Kinopoisk_colored_logo_%282021-present%29.svg.png" alt="Kinopoisk logo" height="40" width="250"/></a>

<a href="https://mipt.ru" target="blank"><img align="center" src="https://upload.wikimedia.org/wikipedia/ru/2/27/%D0%9B%D0%BE%D0%B3%D0%BE_%D0%9C%D0%A4%D0%A2%D0%98.png?20180927154454" alt="MIPT logo" height="101" width="150"/></a>

### Команда проекта, студенты 1-го курса магистратуры МФТИ "Разрабортка IT продукта":
- Мишин Юрий
- Михайлов Иван
- Самсуева Екатерина
- Галиев Михаил
- Сорванова Надежда
- Сердюков Георгий

MIRO доска проекта: <a href="https://miro.com/welcomeonboard/VVFGNFBYaVlyeVQ5STN0UnhhWk5yREcxcHlmSUZpbGJHQ0VvazZYMEYrOUVNVzg5cUF5SnFPSmttSVYwbm9KMlk2aSt4OWVSRXVDdFFSSXhubnR5OUg3U2U0ZzFFNHB5bFZrclJBMnhxTmZGYXMvLzdMMTNLZU8xd0liT3ljbDIhZQ==?share_link_id=185867484290"><img align="center" src="https://cdn.worldvectorlogo.com/logos/miro-2.svg" alt="MIRO logo" height="100" width="100"/></a>

DrawSQL архитектура БД: <a href="https://drawsql.app/teams/robot-1/diagrams/films-service" target="blank"><img align="center" src="https://a.fsdn.com/allura/s/drawsql/icon?99f7437d1b6beae286830cfd95339103661d5ec722e44af00dd516341d59941a?&w=148" alt="DRAW SQL logo" height="101" width="150"/></a>

### Техническое задание проекта
Необходимо создать асинхронный RESTful API сервис, который позволяет пользователям регистрироваться, аутентифицироваться и управлять списком своих избранных фильмов.

### Эндпойнты сервиса:
1. Регистрация пользователя:
```
POST /register
```
2. Авторизация пользователя:
```
POST /login
```
3. Получение профиля пользователя:
```
GET /profile.
```
4. Поиск фильмов:
```
GET /movies/search?query=НазваниеФильма
```
5. Ищет фильмы по названию, используя эндпойнт:
```
GET /api/v2.1/films/search-by-keyword
```
6. Получение деталей фильма
```
GET /movies/{kinopoisk_id}
```
7. Получает подробную информацию о фильме по его Kinopoisk ID, используя эндпойнт:
```
GET /api/v2.2/films/{kinopoisk_id}
```
8. Добавление фильма в избранное:
```
POST /movies/favorites
```
9. Удаление фильма из избранного:
```
DELETE /movies/favorites/{kinopoisk_id}
```
10. Просмотр списка избранных фильмов:
```
GET /movies/favorites
```

Требования к реализации:

Аутентификация и авторизация:
> - Аутентификация с использованием JWT.
> - Защита эндпойнтов /profile и всех эндпойнтов под /movies/ от неавторизованного доступа.

Работа с базой данных:
> - SQLAlchemy для взаимодействия с базой данных.
> - Безопасное сохранение информации о пользователях (пароли должны быть захешированы).
> - Список избранных фильмов каждого пользователя хранится в базе данных (Kinopoisk ID и необходимая информация о фильме).

Логирование:
> - Система логирования фиксирует все операции с данными.
> - Логи должны включать информацию о времени операции, типе операции и статусе выполнения.

Сбор метрик:
> - Разработать механизм для сбора и хранения метрик производительности системы.
> - Метрики должны включать время обработки запросов, количество операций в секунду и использование ресурсов.

Взаимодействие с внешним API:
> - Aiohttp, Httpx или Aiosonic для выполнения асинхронных HTTP-запросов напрямую.

Обработка данных:
> - При поиске фильмов отправляется запрос к эндпойнту /api/v2.1/films/search-by-keyword и возвращаются результаты.
> - При получении деталей фильма используется эндпойнт /api/v2.2/films/{kinopoisk_id}.
> - При добавлении фильма в избранное сохраняется информацию о нем в базе данных.
> - При просмотре списка избранных фильмов возвращается детальная информация о каждом фильме.

Безопасность:
> - Пароли хэшируются перед сохранением в базу данных.
> - Исключения обрабатываются. Необходимо избегать утечки подробных технических деталей во внешние сообщения об ошибках.

Тестирование:
> - Необходимо покрыть функционал тестами.
> - Уровень покрытия должен быть больше 80%.

Инфраструктура:
> - Реализовать dockerfile.
> - Реализовать docker-compose.

Технические требования:

Язык программирования: Python.
- Используемые технологии: FastAPI, Pydantic, SQLAlchemy, alembic, PostgreSQL.
- Система логирования: Loguru | Structlog: Sentry.
- Система мониторинга: Prometheus | Statsd: Grafana.
