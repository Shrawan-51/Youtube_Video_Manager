import pymongo
from bson import ObjectId

try:
    client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.4wyji15.mongodb.net/ytmanager")
except:
    raise Exception("Cinnection failed")
db = client['ytmanager']
video_collection = db["videos"]



def list_videos():
    for data in video_collection.find():
        print(f"ID:{data['_id']} Name:{data['name']} Time:{data['time']}")
    

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_video(id,new_name,new_time):
    video_collection.update_one(
        {'_id':ObjectId(id)},
        {"$set":{"name":new_name,"time":new_time}}
        )

def delete_video(vid_id):
    video_collection.delete_one({'_id':ObjectId(vid_id)})


def main():
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
                list_videos()
            case '2':
                name = input("Enter Video Name:")
                time = input("Enter video time:")
                add_video(name,time)
            case '3':
                id = input("Enter video id")
                name = input("Enter updated Video Name:")
                time = input("Enter updated video time:")
                update_video(id,name,time)
            case '4':
                id = input("Enter video id")
                delete_video(id)
            case '5':
                break

if __name__ == "__main__":
    main()