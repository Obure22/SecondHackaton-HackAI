# свэн-тим AI Devtools Hack / Хакатон Cloud.ru

Агент для автоматического поиска вакансий работы hh.ru . Api открыто к использованию.

---

## Состав команды

Акаев Адам Баудинович 

Швецов Георгий Владимирович

---

## Инструкция по запуску

ССЫЛКА НА ВИДЕО https://drive.google.com/file/d/1u0PKV-0npjldTu1XEXZyO-tukI9phOLo/view?usp=sharing

Установка зависимостей.

```
pip install -r requirements.txt
```

Вот сюда ввести ключ в файле .env: LLM_API_KEY=

Запуск агента через cmd

```
set PYTHONPATH=путь-до-проекта\SecondHackaton-HackAI;путь-до-проекта\SecondHackaton-HackAI\app
cd путь-до-проекта\SecondHackaton-HackAI\app
python main_agent_test.py
```

Запуск MCP сервера

```
cd путь-до-проекта\SecondHackaton-HackAI
python main.py
```

---
