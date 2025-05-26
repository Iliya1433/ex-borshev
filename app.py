from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

# Импортируем маршруты
from routes import *

# Инициализируем директории и базу данных при запуске
with app.app_context():
    # Создаем необходимые директории
    from init_dirs import init_directories
    init_directories()
    
    # Создаем все таблицы
    db.create_all()
    
    # Проверяем, есть ли данные в базе
    from models import Book
    if not Book.query.first():
        # Если база пустая, запускаем скрипты инициализации
        from init_db import init_db
        from add_initial_data import add_initial_data
        from add_covers import add_covers
        init_db()
        add_initial_data()
        add_covers()

if __name__ == '__main__':
    app.run(debug=True) 
