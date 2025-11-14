# CP5632 Assignment 3 - Slack & GitHub API Tool

## Overview

This Python program demonstrates the integration of two popular APIs:
- **Slack API**: Used to fetch workspace information and channel listings
- **GitHub API**: Used to search public repositories by keywords

The program provides a command-line interface to:
1. Query Slack workspace details and channel list
2. Search GitHub repositories by keyword

## Installation & Setup

### Prerequisites
- Python 3.x
- `requests` library (install via `pip install requests`)

### Configuration
Create a `tokens.txt` file in the project root directory with the following format:

```
GITHUB_TOKEN=your_github_token_here
SLACK_BEARER_TOKEN=your_slack_token_here
```
- **Attention**: There should be no spaces or other symbols after the "=", enter your token directly. I have uploaded a template on GitHub that can be used by directly modifying the content.
- **GitHub Token**: Generate from [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
- **Slack Token**: Generate from [Slack API Dashboard](https://api.slack.com/) (create an app and add `conversations:read` and `auth:test` scopes)
- **GitHub Token**: GitHub need repo permissions
- **Slack Token**：Slack need `conversations:read` permissions

### Running the Program
```bash
python assignment3.py
```

## API Documentation

### Slack API

- **Endpoint**: `conversations.list` + `auth.test`
- **Documentation**: [Slack API Methods](https://api.slack.com/methods)
- **Key Features**:
  - `auth.test`: Verifies authentication and returns workspace information
  - `conversations.list`: Retrieves list of channels (public and private) with pagination support

### GitHub API

- **Endpoint**: `search/repositories`
- **Documentation**: [GitHub Search Repositories](https://docs.github.com/en/rest/search/repositories)
- **Key Features**:
  - Search repositories by keyword
  - Pagination support via `per_page` parameter
  - Returns repository metadata including stars, description, and URL

## Lessons Learned About APIs

### Authentication Best Practices

1. **Token Management**:
   - Store tokens securely in environment variables or encrypted files (never hardcode)
   - Use least privilege principle when generating tokens
2. **Rate Limiting**:
   - Both APIs enforce rate limits (GitHub: 60 requests/hour for unauthenticated, much higher for authenticated)
   - Implement exponential backoff for retries
3. **Error Handling**:
   - Always check HTTP status codes and API-specific error responses
   - Handle network errors gracefully with try/except blocks

### API Design Considerations

1. **Pagination**:
   - GitHub uses `per_page` and `page` parameters
   - Slack uses `limit` and `cursor` for pagination
   - Always consider memory usage when processing large datasets
2. **Data Formatting**:
   - APIs return data in different formats (GitHub: nested JSON, Slack: flat structure)
   - Normalize data before processing (as shown in the repository information extraction)
3. **Endpoint Selection**:
   - Choose endpoints carefully (e.g., `conversations.list` vs `channels.list` in Slack)
   - Some endpoints require additional scopes/permissions

### Practical Challenges

1. **Async vs Sync**:
   - This program uses synchronous requests for simplicity
   - For production, consider async requests (e.g., `aiohttp`) for better performance
2. **Data Consistency**:
   - Slack's `exclude_archived` parameter helps filter results
   - GitHub's search may return inconsistent results for complex queries
3. **Documentation Quality**:
   - GitHub has excellent documentation with concrete examples
   - Slack's documentation requires more trial-and-error to understand parameter combinations

## Example Output

----------------------------------------
Slack channel query & GitHub repository search tool
----------------------------------------
【1】Slack workspace query
------------------------------
Workspace name = YourWorkspace
Found 10 channels：
  1. #general | ID: C1234567890
  2. #random | ID: C0987654321

    ...

【2】GitHub repository search
------------------------------
Keywords：python
Found 3 repositories：

1. Name：requests
   Star count: 50000 
   Description：Python HTTP for Humans.
   URL：https://github.com/psf/requests

2. Name：flask
   Star count: 62000 
   Description：The Python micro framework for building web applications.
   URL：https://github.com/pallets/flask

3. Name：django
   Star count: 78000 
   Description：The Web framework for perfectionists with deadlines.
   URL：https://github.com/django/django

Program ended!

## Key Takeaways

This assignment provided hands-on experience with:
1. Working with multiple APIs in a single application
2. Handling authentication for different platforms
3. Processing and presenting API responses in a user-friendly way
4. Implementing robust error handling for network requests

The skills gained are directly applicable to real-world development scenarios involving third-party API integrations.

```

```

