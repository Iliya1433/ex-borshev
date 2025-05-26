from app import app, db
from models import User, Role
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        # Создаем таблицы
        db.create_all()
        
        # Проверяем, существуют ли роли
        admin_role = Role.query.filter_by(name='Администратор').first()
        moderator_role = Role.query.filter_by(name='Модератор').first()
        user_role = Role.query.filter_by(name='Пользователь').first()
        
        # Если роли не существуют, создаем их
        if not admin_role:
            admin_role = Role(name='Администратор', description='Полный доступ к системе')
            db.session.add(admin_role)
        
        if not moderator_role:
            moderator_role = Role(name='Модератор', description='Может редактировать книги и рецензии')
            db.session.add(moderator_role)
        
        if not user_role:
            user_role = Role(name='Пользователь', description='Может просматривать книги и оставлять рецензии')
            db.session.add(user_role)
        
        # Проверяем, существует ли администратор
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                password_hash=generate_password_hash('admin'),
                last_name='Администратор',
                first_name='Системный',
                role=admin_role
            )
            db.session.add(admin)
        
        try:
            db.session.commit()
            print("База данных успешно инициализирована!")
        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при инициализации базы данных: {e}")

if __name__ == '__main__':
    init_db() 