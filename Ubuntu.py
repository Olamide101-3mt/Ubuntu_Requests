import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    """Fetch and save a single image from the given URL."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Extract filename or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"⚠ Duplicate detected. Skipping: {filename}")
            return

        # Save image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get URLs from user (support multiple, separated by commas)
    urls = input("Please enter image URL(s) (separate multiple with commas): ").split(",")

    for url in urls:
        fetch_image(url.strip())

    print("\nConnection strengthened. Community enriched.")
    print("Ubuntu: 'I am because we are'.")


if __name__ == "__main__":
    main()
