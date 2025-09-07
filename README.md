# Ubuntu_Requests

## 🌍 Project Overview
This project embodies the Ubuntu philosophy of **community, respect, and sharing** by connecting to the web, downloading images from user-provided URLs, and organizing them for later appreciation.

> "A person is a person through other persons." – Ubuntu Philosophy

## ✨ Features
- Prompt the user for one or multiple image URLs
- Download and save images into a `Fetched_Images` folder
- Automatically creates the folder if it doesn’t exist
- Extracts filename from the URL or generates one if missing
- Prevents duplicate downloads
- Gracefully handles errors (invalid URLs, connection issues, bad responses)
- Displays clear, human-friendly messages

## 📂 Project Structure
Ubuntu_Requests/
│── Ubuntu.py # Main script
│── Fetched_Images/ # Created automatically for downloaded images


## ⚙️ Requirements
- Python 3.x
- `requests` library
  
##Usage
1. Clone Repository
Install with:
```bash
pip install requests
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests


2. Run the Script
python fetch_image.py

3. Enter one or more images:
Please enter image URL(s): https://example.com/img1.jpg, https://example.com/img2.png

Example Output
✓ Successfully fetched: img1.jpg
✓ Image saved to Fetched_Images/img1.jpg
⚠ Duplicate detected. Skipping: img2.png

Connection strengthened. Community enriched.

