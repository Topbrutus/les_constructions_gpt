import json
import os
import urllib.request

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
API = f"https://api.github.com/repos/{REPO}"


def gh(method: str, path: str, data=None):
    body = None
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")

    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")

    with urllib.request.urlopen(req, body) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else None


with open("backlog.json", "r", encoding="utf-8") as f:
    backlog = json.load(f)

open_issues = gh("GET", "/issues?state=open&per_page=100")
open_titles = {issue["title"] for issue in open_issues if "pull_request" not in issue}

for task in backlog:
    if task["title"] in open_titles:
        print(f"Doublon évité : {task['title']}")
        continue

    created = gh(
        "POST",
        "/issues",
        {
            "title": task["title"],
            "body": task["body"],
            "labels": task["labels"],
        },
    )
    print(f"Issue créée : #{created['number']} — {created['title']}")
    break
else:
    print("Aucune nouvelle issue à créer.")
