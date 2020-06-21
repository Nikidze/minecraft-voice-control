# Minecraft Voice Control
Попытка управления майнкрафтом с помощью голоса. Написано на JS+Python.

## Зависимости
Python: asyncio, websocket, pyautogi  
JS: библиотека, для взаимодействия с comet-server, подключена по CDN в файле *client.html*.
Но если изменить код, и настроить ssl на локальном хосте, то можно обойтись и без нее.

## Установка
### 1 вариант
Если вы **НЕ** знаете как установить ssl на localhost

При желании зарегистрироваться на [comet-server.com](https://comet-server.com/)] и в файлах *intermediary.html* и *client.html*
```js
        cometApi.start({
            dev_id: x,
            node: "app.comet-server.ru"
        });
```
x заменить на ваш dev_id

1. Файл *client.html* загрузить на любой хостинг, где есть ssl, иначе работать не будет
2. Командой `python3 server.py` запускаем сервер
3. Только после этого открываем в любом браузере файл *intermediary.html*
4. Открываем залитый на хостинг файл через браузер chrome на телефоне или ПК
5. Запускаем майнкрафт
6. Управляем

### 2 вариант
Если вы знаете как установить ssl на localhost

1. Командой `python3 server.py` запускаем сервер
2. Открываем в браузере файл *client.html* из папки local_ssl
3. Запускаем майнкрафт
4. Управляем

## Команды
* Идти <направление>
* Бежать <напрвление>
* Бежать вприпрыжку <направление>
* Идти в приседе <напрвление>
* Стоп
* Зажать <левую/правую> кнопку
* Отпустить <левую/правую> кнопку
* Нажать <левую/правую> кнопку
* Выбрать слот <1-9>
* Выкинуть предмет
* Переключить перспективу
* Повернуть по <горизонтали/вертикали> на <минус n/n> градусов

## Лицензия
Проект распространятеся под GNU GPL v3
