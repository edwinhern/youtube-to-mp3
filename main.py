from pytube import YouTube
import os


def download_video(url, destination):
    try:
        yt = YouTube(url)

        # Extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # Download the file
        out_file = video.download(output_path=destination)

        # Save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " has been successfully downloaded.")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")
        # Continue with other downloads even if this one fails


def main():
    urls = []
    print("Enter YouTube URLs (press enter on an empty line to start download):")

    while True:
        url = input(">> ")
        if url:
            urls.append(url)
        else:
            print("No more URLs entered. Starting download...")
            break

    destination = os.path.join(os.getcwd(), 'downloaded-music')

    # Check if destination folder exists, if not create it
    if not os.path.exists(destination):
        os.makedirs(destination)

    for url in urls:
        download_video(url, destination)


if __name__ == "__main__":
    main()
