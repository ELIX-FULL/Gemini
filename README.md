<div align="center">

  # GEMINI-PRO-BOT
  
  **Бот Telegram на Python, работающий на основе API LLM `gemini-pro` от Google**

  *Это бот Python Telegram, который использует LLM API Gemini-pro от Google для создания творческих текстовых форматов на основе пользовательского ввода. Он создан как увлекательный и интерактивный способ изучения возможностей больших языковых моделей.*

[Gemini Bot Preview](https://github.com/rabilrbl/gemini-pro-bot/assets/63334479/ffddcdfa-09c2-4f02-b14d-4407e888b605)

</div>

### Функции

* Создавайте творческие текстовые форматы, такие как стихи, коды, сценарии, музыкальные произведения и т. д.
* Потоковая передача процесса генерации, чтобы вы могли видеть, как текст разворачивается в режиме реального времени.
* Отвечайте на ваши сообщения творческими работами Барда.
* Простота использования с помощью простых команд:
    * `/start`: поприветствуйте бота и приступайте к работе.
    * `/help`: Получить информацию о возможностях бота.
* Отправьте любое текстовое сообщение, чтобы запустить процесс генерации.
* Отправьте любое изображение с подписями, чтобы получить ответы на основе изображения. (Мультимодальная поддержка)
* Аутентификация пользователя для предотвращения несанкционированного доступа путем установки `AUTHORIZED_USERS` в файле `.env` (необязательно).

### Требования

* Питон 3.10+
* Токен Telegram Bot API
* API-ключ Google `gemini-pro`
* dotenv (для переменных среды)


### Docker

#### Контейнер GitHub
Просто запустите следующую команду, чтобы запустить предварительно созданный образ из реестра контейнеров GitHub:

```shell
docker run --env-file .env ghcr.io/rabilrbl/gemini-pro-bot:latest
```

Обновите изображение с помощью:
```shell
docker pull ghcr.io/rabilrbl/gemini-pro-bot:latest
```

#### Build
Создайте образ с помощью:
```shell
docker build -t gemini-pro-bot .
```
Как только образ будет создан, вы можете запустить его с помощью:
```shell
docker run --env-file .env gemini-pro-bot
```

### Установка

1. Клонируйте этот репозиторий.
2. Установите необходимые зависимости:
    * `pipenv install` (при использовании Pipenv)
    * `pip install -r require.txt` (если не используется Pipenv)
3. Создайте файл `.env` и добавьте следующие переменные среды:
    * `BOT_TOKEN`: ваш токен API Telegram Bot. Вы можете получить его, поговорив с [@BotFather](https://t.me/BotFather).
    * `GOOGLE_API_KEY`: ваш ключ API Google Bard. Вы можете получить его в [Google AI Studio](https://makersuite.google.com/).
    * `AUTHORIZED_USERS`: разделенный запятыми список имен пользователей Telegram или идентификаторов пользователей, которым разрешен доступ к боту. (необязательно) Пример значения: `shonan23,1234567890`
4. Запустите бота:
    * `python main.py` (если не используется Pipenv)
    * `pipenv run python main.py` (при использовании Pipenv)

### Использование

1. Запустите бота, запустив скрипт.
   ```shell
   основной файл Python
   ```
2. Откройте бота в своем Telegram-чате.
3. Отправьте боту любое текстовое сообщение.
4. Бот сгенерирует креативные текстовые форматы на основе ваших данных и отправит вам результаты.
5. Если вы хотите ограничить публичный доступ к боту, вы можете установить `AUTHORIZED_USERS` в файле `.env` как список идентификаторов пользователей Telegram, разделенных запятыми. Только эти пользователи смогут получить доступ к боту.
    Пример:
    ```shell
    AUTHORIZED_USERS=сёнан23,1234567890
    ```
### Команды бота

| Команды  | описание                       |
|----------|--------------------------------|
| `/start` | Старт бота                     |
| `/help`  | Получить информацию о командах |
| `/new`   | Открыть новую чат сессию       |

### История звезд

<a href="https://star-history.com/#rabilrbl/gemini-pro-bot&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=rabilrbl/gemini-pro-bot&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=rabilrbl/gemini-pro-bot&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=rabilrbl/gemini-pro-bot&type=Date" />
  </picture>
</a>

### Лицензия 
Вся вся информация переведена на русский
Основной https://github.com/rabilrbl