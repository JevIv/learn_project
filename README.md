# learn_project

<<<<<<< HEAD
### Запустить сервер `export FLASK_APP=learn_project && export FLASK_ENV=development && flask run`
=======
### Запуск web-сервера <br>
`export FLASK_APP=learn_project && export FLASK_ENV=development && flask run`

### Запуск локального прокси в docker
1. Установить docker
2. Загрузить образ <br>
`docker pull mattes/rotating-proxy:latest`
3. Запустить прокси <br>
`docker run -d -p 5566:5566 -p 4444:4444 --env tors=25 mattes/rotating-proxy`
>>>>>>> e99760d2e5b23a0ba8ac435756c59baef3262361