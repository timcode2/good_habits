Описание проекта Проект представляет собой бэкенд-часть SPA веб-приложения для отслеживания полезных привычек. Идея пришла после прочтения книги "Атомные привычки" Джеймса Клира, посвященной приобретению новых полезных привычек и избавлению от старых вредных.

Модель Привычка Пользователь: Создатель привычки. Место: Место, в котором необходимо выполнять привычку. Время: Время, когда необходимо выполнять привычку. Действие: Действие, представляющее из себя привычку. Признак приятной привычки: Привычка, которую можно привязать к выполнению полезной привычки. Связанная привычка: Привычка, связанная с другой привычкой, указывается для полезных привычек, но не для приятных. Периодичность: Периодичность выполнения привычки, по умолчанию - ежедневная. Вознаграждение: Награда, которой пользователь должен себя порадовать после выполнения. Время на выполнение: Предполагаемое время, которое пользователь потратит на выполнение привычки. Признак публичности: Возможность публиковать привычки для общего доступа. Последнее время выполнения: Время последнего выполнения привычки. Валидаторы Исключение одновременного выбора связанной привычки и указания вознаграждения. Время выполнения не должно превышать 120 секунд. В связанные привычки могут попадать только привычки с признаком приятной привычки. У приятной привычки не может быть вознаграждения или связанной привычки. Нельзя выполнять привычку реже, чем 1 раз в 7 дней. Права доступа Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD. Пользователь может видеть список публичных привычек без возможности их редактирования или удаления. Эндпоинты Регистрация: POST запрос на http://127.0.0.1:8000/users/register/

Параметры: email, password, telegram_id (необходим для рассылки уведомлений через Telegram). Авторизация: POST запрос на http://127.0.0.1:8000/users/token/

Ответ: access_token и refresh_token для доступа к другим эндпоинтам. Создание привычки: POST запрос на http://127.0.0.1:8000/habits/create/

Изменение привычки: PATCH или PUT запрос на http://127.0.0.1:8000/habits/update/<id привычки> (редактировать можно только свои привычки).

Удаление привычки: DELETE запрос на http://127.0.0.1:8000/habits/update/<id привычки> (удалять можно только свои привычки).

Просмотр списка привычек (по 5 на странице): GET запрос на http://127.0.0.1:8000/habits/

Просмотр списка публичных привычек: GET запрос на http://127.0.0.1:8000/habits/public/

Просмотр документации проекта:

В адресной строке браузера ввести http://127.0.0.1:8000/swagger/ или http://127.0.0.1:8000/redoc/ Интеграция с Telegram Для получения уведомлений о привычках через Telegram, при регистрации необходимо указать telegram_id. Получить его можно, воспользовавшись ботом @userinfobot. Найти бота @ArtemGoodHabits(https://t.me/habits_timcode_bot) в Telegram и нажать start для разрешения ему отправки уведомлений. Ждать уведомлений о привычках через Telegram. Бот обязательно напомнит в нужное время. Запуск проекта Установите зависимости: pip install -r requirements.txt Примените миграции: python manage.py migrate Запустите сервер: python manage.py runserver Теперь вы можете использовать эндпоинты и наслаждаться отслеживанием своих привычек!

Инструкции по запуску:

Создать .env файл на основании .env.sample Запустить проект командой: docker-compose up --build -d Проверить работу открыв страницу с документацией http://localhost:8000/swagger/ или http://localhost:8000/redoc/ Начать работать с проектом через Postman