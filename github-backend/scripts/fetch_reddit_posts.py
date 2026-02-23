"""Fetch top posts from subreddits using Reddit's public JSON endpoint.

Reads subreddits from subreddits.txt, fetches top posts from the past
week for each, and saves the combined results as JSON. No API
credentials required.

Usage:
    python fetch_reddit_posts.py
    python fetch_reddit_posts.py --limit 50 --output posts.json
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import requests

_BASE_DIR = Path(__file__).resolve().parent
_DEFAULT_SUBREDDITS_FILE = _BASE_DIR / "subreddits.txt"
_DEFAULT_OUTPUT_FILE = _BASE_DIR / "posts.json"
_USER_AGENT = "TrendDigest/1.0"
_REQUEST_DELAY_SECONDS = 2


def load_subreddits(filepath: Path) -> list[str]:
    """Reads subreddit names from a text file.

    Blank lines and lines starting with '#' are ignored.

    Args:
        filepath: Path to the subreddits file.

    Returns:
        A list of subreddit name strings.
    """
    subreddits = []
    for line in filepath.read_text().splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            subreddits.append(stripped)
    return subreddits


def fetch_subreddit_posts(
    subreddit: str,
    limit: int = 50,
    time_filter: str = "week",
) -> list[dict[str, Any]]:
    """Fetches top posts from a single subreddit via the JSON endpoint.

    Args:
        subreddit: The subreddit name (without 'r/' prefix).
        limit: Maximum number of posts to retrieve (max 100).
        time_filter: Time window for top posts. One of 'hour', 'day',
            'week', 'month', 'year', or 'all'.

    Returns:
        A list of post dictionaries with keys: 'subreddit', 'title',
        'score', 'url', 'author', 'num_comments', 'created_utc',
        'selftext', and 'permalink'.

    Raises:
        requests.HTTPError: If the HTTP request fails.
    """
    url = (
        f"https://www.reddit.com/r/{subreddit}/top/.json"
        f"?t={time_filter}&limit={limit}"
    )
    headers = {"User-Agent": _USER_AGENT}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    children = data.get("data", {}).get("children", [])

    posts = []
    for child in children:
        post_data = child.get("data", {})
        posts.append({
            "subreddit": post_data.get("subreddit", subreddit),
            "title": post_data.get("title", ""),
            "score": post_data.get("score", 0),
            "url": post_data.get("url", ""),
            "author": post_data.get("author", "[deleted]"),
            "num_comments": post_data.get("num_comments", 0),
            "created_utc": post_data.get("created_utc", 0),
            "selftext": post_data.get("selftext", ""),
            "permalink": post_data.get("permalink", ""),
        })

    return posts


def fetch_all_posts(
    subreddits: list[str],
    limit_per_sub: int = 50,
) -> list[dict[str, Any]]:
    """Fetches top weekly posts from all subreddits.

    Includes a delay between requests to avoid rate limiting.

    Args:
        subreddits: List of subreddit names.
        limit_per_sub: Max posts to fetch per subreddit.

    Returns:
        Combined list of posts sorted by score descending.
    """
    all_posts = []

    for i, subreddit in enumerate(subreddits):
        print(f"  [{i + 1}/{len(subreddits)}] r/{subreddit}...", end=" ")
        try:
            posts = fetch_subreddit_posts(subreddit, limit=limit_per_sub)
            all_posts.extend(posts)
            print(f"{len(posts)} posts")
        except requests.HTTPError as e:
            print(f"FAILED ({e})", file=sys.stderr)
        except Exception as e:
            print(f"ERROR ({e})", file=sys.stderr)

        if i < len(subreddits) - 1:
            time.sleep(_REQUEST_DELAY_SECONDS)

    all_posts.sort(key=lambda p: p["score"], reverse=True)
    return all_posts


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parses command-line arguments.

    Args:
        argv: Argument list to parse. Defaults to sys.argv[1:].

    Returns:
        Parsed argument namespace.
    """
    parser = argparse.ArgumentParser(
        description="Fetch top Reddit posts from tracked subreddits."
    )
    parser.add_argument(
        "--subreddits-file",
        type=Path,
        default=_DEFAULT_SUBREDDITS_FILE,
        help="Path to subreddits list file.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Max posts per subreddit (default: 50, max: 100).",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=100,
        help="Keep only the top N posts overall (default: 100).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_OUTPUT_FILE,
        help="Output JSON file path.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Entry point for the script.

    Args:
        argv: Command-line arguments. Defaults to sys.argv[1:].
    """
    args = parse_args(argv)

    subreddits = load_subreddits(args.subreddits_file)
    if not subreddits:
        print("No subreddits found in file.", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching top posts from {len(subreddits)} subreddits...")
    all_posts = fetch_all_posts(subreddits, limit_per_sub=args.limit)
    top_posts = all_posts[:args.top_n]

    args.output.write_text(json.dumps(top_posts, indent=2))
    print(
        f"\nSaved {len(top_posts)} posts to {args.output} "
        f"(from {len(all_posts)} total)."
    )


if __name__ == "__main__":
    main()
