import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Use regular expressions to find a video ID in the HTML string
    video_id_match = re.search(r'https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s, re.IGNORECASE)
    if video_id_match:
        return shorten_url(video_id_match.group(1))
    else:
        return None


def shorten_url(video_id):
    return "https://youtu.be/" + video_id


if __name__ == "__main__":
    main()