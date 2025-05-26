import os

def init_directories():
    # Создаем директорию для загрузки файлов, если она не существует
    uploads_dir = os.path.join('static', 'uploads')
    covers_dir = os.path.join(uploads_dir, 'covers')
    
    os.makedirs(covers_dir, exist_ok=True)
    
    # Создаем .gitkeep файл, чтобы сохранить структуру директорий
    gitkeep_file = os.path.join(covers_dir, '.gitkeep')
    if not os.path.exists(gitkeep_file):
        with open(gitkeep_file, 'w') as f:
            pass

if __name__ == '__main__':
    init_directories() 