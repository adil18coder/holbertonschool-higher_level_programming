import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts and print status + post titles."""
    response = requests.get(API_URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If successful → parse JSON and print titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body into posts.csv."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        # Convert JSON into a list of dictionaries with selected keys
        cleaned_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(cleaned_posts)
