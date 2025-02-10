import git
import requests
import os


def update_project():
    """Подтягивает обновления с гита"""
    repo_path = os.getcwd()
    repo = git.Repo(repo_path)

    repo.git.reset('--hard')

    origin = repo.remotes.origin
    origin.pull()


def get_last_version() -> str:
    """Получает название последней версии с гита"""
    url = f"https://api.github.com/repos/MIFIKUS/BigBotV2/contents/version.py"
    response = requests.get(url)

    content = response.json().get("content", "")
    # Декодируем содержимое из base64
    import base64
    return base64.b64decode(content).decode("utf-8").strip().split(' ')[-1].replace("'", "")


update_project()
