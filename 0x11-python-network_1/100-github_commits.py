#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        api_url = 'https://api.github.com'
        req_url = '{}/repos/{}/{}/commits?{}'.format(
            api_url,
            owner_name,
            repository_name,
            'per_page=10'
        )
        response = requests.get(
            req_url,
            headers={'Accept': 'application/vnd.github.v3+json'}
        )
        if response.status_code == 200:
            for commit in response.json():
                commit_sha = commit['sha']
                commit_author = commit['commit']['author']['name']
                print('{}: {}'.format(commit_sha, commit_author))
