import pytube

def download_video(url):
    # Create a YouTube object with the video URL
    yt = pytube.YouTube(url)

    # Get the streams for the video
    streams = yt.streams

    # Prompt the user to select a stream to download
    print("Available streams:")
    for i, stream in enumerate(streams):
        print(f"{i+1}. {stream}")
    while True:
        stream_num = int(input("Enter the number of the stream you want to download: "))
        if 1 <= stream_num <= len(streams):
            break
        print(f"Invalid stream number. Please enter a number between 1 and {len(streams)}.")
    stream = streams[stream_num-1]

    # Download the stream to the specified directory
    output_path = r"ENTER REQUIRED FOLDER PATH"
    print(f"Downloading video to {output_path}...")
    stream.download(output_path=output_path)

# List of video URLs to download
video_links = [
     'import links list'


 ]

# Download each video in the list
for url in video_links:
    download_video(url)
