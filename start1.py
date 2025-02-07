import subprocess

def call_other_script():
    # Запускаем другой скрипт
    result = subprocess.run(['python', 'start.py'])


if __name__ == "__main__":
    call_other_script()