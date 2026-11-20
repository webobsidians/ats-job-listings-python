import json
import urllib.request


def get(url):
    # some job boards reject Python's default User-Agent, so send a normal one
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (job-list-script)"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def greenhouse(board):
    data = get(f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs")
    return [{"title": j["title"], "location": j["location"]["name"], "url": j["absolute_url"]}
            for j in data["jobs"]]


def lever(board):
    data = get(f"https://api.lever.co/v0/postings/{board}?mode=json")
    return [{"title": j["text"], "location": j["categories"].get("location"), "url": j["hostedUrl"]}
            for j in data]


def ashby(board):
    data = get(f"https://api.ashbyhq.com/posting-api/job-board/{board}")
    return [{"title": j["title"], "location": j.get("location"), "url": j["jobUrl"]}
            for j in data["jobs"]]


for name, jobs in [("stripe", greenhouse("stripe")), ("palantir", lever("palantir")), ("ramp", ashby("ramp"))]:
    print(name, len(jobs), "open jobs, e.g.", jobs[0]["title"], "-", jobs[0]["location"])
