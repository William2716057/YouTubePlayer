import random
import webbrowser

# List of YouTube links
youtube_links = [
    "https://www.youtube.com/watch?v=A2p5XUy-Zpo",
    "https://www.youtube.com/watch?v=coWrx7BPCsU",
    "https://www.youtube.com/watch?v=HJv59PVHxFE",
    "https://www.youtube.com/watch?v=qNAo2LNkzQ4",
    "https://www.youtube.com/watch?v=qPZk5IODBRI"
]

# Select a random link
selected_link = random.choice(youtube_links)

# Open the selected link in the default web browser
webbrowser.open(selected_link)

print(f"Playing video: {selected_link}")