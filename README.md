# UniMarket
Платформа для покупки и продажи товаров между студентами университета.

Технологии
- Backend: FastAPI 0.104+
- Database: PostgreSQL + SQLAlchemy
- Python: 3.10+

Установка

```bash
git clone https://github.com/YOUR_USERNAME/UniMarket.git
cd UniMarket
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

Создайте файл `.env` (пример в проекте)

Запуск

```bash
python src/main.py
# или
uvicorn src.main:app --reload
```

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Структура проекта
```
UniMarket/
├── src/              # Исходный код
│   ├── main.py      # Точка входа
│   └── config.py    # Конфигурация
├── tests/           # Тесты
├── .env             # Переменные окружения
└── requirements.txt # Зависимости
```

Разработка

Установите pre-commit hooks:

```bash
pre-commit install
```

Автор
Ваше имя - Студент курса FastAPI
