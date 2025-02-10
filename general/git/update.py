import git
import requests
import os

repo_path = os.getcwd()


def update_project():
    """Подтягивает обновления с гита"""
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


def get_new_versions_description() -> list:
    """Получает описание новых версий"""
    repo = git.Repo(repo_path)

    repo.remotes['origin'].fetch()

    local_branch = repo.heads['master']
    remote_branch = repo.remotes['origin'].refs['master']

    unfetched_commits = list(repo.iter_commits(f"{remote_branch}..{local_branch}"))
    commit_messages = [commit.message.strip() for commit in unfetched_commits]

    return commit_messages

