# learn_project

### Запуск web-сервера <br>
`run.sh`

### Запуск локального прокси в docker
1. Установить docker
2. Загрузить образ <br>
`docker pull mattes/rotating-proxy:latest`
3. Запустить прокси <br>
`docker run -d -p 5566:5566 -p 4444:4444 --env tors=25 mattes/rotating-proxy`
