import json



def load_data():
    try:
        with open("youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*"*30)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. Video Name:{video['name']}  Duration: {video['time']} ")
    print("*"*30)
def add_video(videos):
    name = input("Enter Video Name:")
    time = input("Enter video time:")
    videos.append({'name':name , 'time':time})
    save_data_helper(videos)

def update_video_details(videos):
    list_all_videos(videos)
    idx = int(input("Enter index to update:"))
    if 1 > idx > len(videos):
        return
    print("for updating name press 1")
    print("for updating duration press 2")
    inp = input("Enter selection:")
    if inp == '1':
        value = input("Enter new name:")
        videos[idx-1]['name'] =value
    else:
        value = input("Enter new duration:")
        videos[idx-1]['time'] = value
    save_data_helper(videos)

    
def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter index to update:"))
    if 1 > idx > len(videos):
        return
    del videos[idx-1]
    save_data_helper(videos)
    


def main():
    videos = load_data()
    while True:
        print("Input Selection")
        print("1: List all youtube videos")
        print("2: add a youtube video")
        print("3: Update a youtube video details")
        print("4: delete a youtube video ")
        print("5: Exit the app")
        inp = input("Enter Selection:")
        match inp:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video_details(videos)
            case '4':
                delete_video(videos)
            case '5':
                break

if __name__ == "__main__":
    main()


