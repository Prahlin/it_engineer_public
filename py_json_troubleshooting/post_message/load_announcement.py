import json

def load_announcement():
    with open('announcement.json', 'r') as file:
        announcement = json.load(file)
    return announcement

def main():
    announcement = load_announcement()
    print("Announcement loaded:")
    print("Title:", announcement.get("title"))
    print("Body:", announcement.get("body"))
    print("Audience:", announcement.get("audience"))

if __name__ == "__main__":
    main()