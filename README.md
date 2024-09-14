# Repair Service App

## Описание

Добро пожаловать в **Repair Service App** — мой первый коммерческий проект, посвящённый автоматизации процесса приёма заявок на ремонт для сервисной службы. Этот проект представляет собой веб-приложение с админ-панелью, которая упрощает обработку заявок и управление ими.

Проект был начат во время моего обучения и использует стек технологий, с которыми я уже работал на тот момент. В процессе разработки я столкнулся с различными проблемами и учёл свои ошибки, что позволило мне значительно расширить свои знания и навыки. Хотя проект изначально кажется простым, я потратил много времени на изучение тонкостей и нюансов разработки, что дало мне ценнейший опыт.

## Технологический стек

- **Python 3.12** — основной язык программирования проекта.
- **Flask** — легковесный веб-фреймворк для создания веб-приложений.
- **SQLite** — встроенная база данных для хранения данных приложения.
- **Peewee** — ORM для удобной работы с SQLite.
- **Telebot** — библиотека для взаимодействия с Telegram Bot API.

## Основные функции

- **Приём заявок**: Пользователи могут легко создавать и отправлять заявки на ремонт через ТГ-бот.
- **Админ-панель**: Веб-интерфейс для администраторов, позволяющий просматривать, обрабатывать и управлять заявками.
- **Уведомления через Telegram**: Интеграция с Telegram для уведомления о новых заявках и других важных событиях.

## Установка и запуск

1. Клонируйте репозиторий:
  ```bash
  git clone https://github.com/SasquatchMe/repair_service_app.git
  ```
2. Перейдите в каталог проекта:
  ```bash
  cd repair_service_app
  ```
3. Создайте и активируйте виртуальное окружение:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
  ```
4. Установите зависимости:

  ```bash
  pip install -r requirements.txt
  ```
5. Запустите приложение:

```bash
python app.py
```
Теперь вы можете открыть веб-браузер и перейти по адресу http://127.0.0.1:5000 для доступа к приложению.

Замечания
Так как проект является результатом моего обучения и первого коммерческого опыта, он может содержать некоторые недочёты и ограничения. Тем не менее, он представляет собой полезный инструмент для автоматизации процесса приёма заявок и может быть легко адаптирован под различные нужды.

Я буду рад вашим отзывам и предложениям по улучшению проекта.

## Лицензия
Этот проект лицензирован под MIT License.
