"""
CP5632 Assignment 3 - Slack & GitHub API Tool
Program Overview:
  A Python program that demonstrates the use of two APIs:
  1. Slack API (conversations.list + auth.test): Fetch workspace name and channel list.
  2. GitHub API (search/repositories): Search public repositories by keywords.
Instructions:
  1. Create tokens.txt in project root (see README.md for format).
  2. Install dependencies: pip install requests.
  3. Run: python assignment3.py
APIs Used:
  - Slack API: https://api.slack.com/methods
  - GitHub API: https://docs.github.com/en/rest/search/repositories
"""
import requests
from requests.exceptions import RequestException

TOKEN_FILE = "tokens.txt"


def main():
    """Display Slack and GitHub Search"""
    print("-" * 40)
    print("Slack channel query & GitHub repository search tool")
    print("-" * 40)

    # Check if tokens are loaded properly
    if not GITHUB_TOKEN or not SLACK_BEARER_TOKEN:
        print("Token is not loaded correctly")
        return

    # 1. Check the Slack channel
    print("【1】Slack workspace query")
    print("-" * 30)
    workspace_name = get_slack_workspace_name()
    channels = get_slack_channels(limit=10)

    # Show Slack data if retrieval succeeds
    if channels and workspace_name:
        print(f"Workspace name = {workspace_name}")
        print(f"Found {len(channels)} channels：")
        for index, channel in enumerate(channels, start=1):
            print(f"  {index}. #{channel['name']} | ID: {channel['id']}")
    else:
        print("Failed to retrieve Slack data")

    # 2. Check the GitHub repository
    print("\n【2】GitHub repository search")
    print("-" * 30)
    query = input("Keywords：").strip()

    if not query:
        print("No keywords")
    else:
        repo_results = search_github_repository(query, per_page=3)
        # Show GitHub data if search succeeds
        if repo_results:
            print(f"Found {len(repo_results)} repositories：")
            for index, repository in enumerate(repo_results, start=1):
                print(f"\n{index}. Name：{repository['name']}")
                print(f"   Star count: {repository['stargazers_count']} ")
                print(f"   Description：{repository['description']}")
                print(f"   URL：{repository['url']}")

        else:
            print(f"\nNo repository related to '{query}' was found.")

    print("\n")
    print("Program ended!")


def read_tokens_from_file(file_path):
    """Read the API Token from the configuration file, skipping blank lines and comments"""
    tokens = {"GITHUB_TOKEN": "", "SLACK_BEARER_TOKEN": ""}

    try:
        # Open and read the token file
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: The token file does not exist")

    # Extract tokens from file lines
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if key == "GITHUB_TOKEN":
                tokens["GITHUB_TOKEN"] = value
            elif key == "SLACK_BEARER_TOKEN":
                tokens["SLACK_BEARER_TOKEN"] = value

    # Check for missing tokens
    if not tokens["GITHUB_TOKEN"] or not tokens["SLACK_BEARER_TOKEN"]:
        print("Error: The Token is missing in the configuration file！")
        return None

    return tokens


token_dict = read_tokens_from_file(TOKEN_FILE)
GITHUB_TOKEN = token_dict.get("GITHUB_TOKEN")
SLACK_BEARER_TOKEN = token_dict.get("SLACK_BEARER_TOKEN")
