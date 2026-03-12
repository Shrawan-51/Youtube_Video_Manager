import sqlite3

con = sqlite3.connect("Youtube.db")

cur = con.cursor()

cur.execute('''  
            CREATE TABLE IF NOT EXISTS videos(
            id INT PRIMARY KEY ,
            video_name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')
def printall():
    response = cur.execute(''' SELECT * FROM videos''')
    res = response.fetchall()
    print("*" *30)
    print(f" ____________________________________")
    for i,name,time in res:
        print(f"| id:{i} | name:{name} | time:{time} |")
        print(f" ____________________________________")
    print("*" *30)
    print("\n")

def main():
    i = 0
    while True:
        print("Input Selection")
        print("1: List all youtube videos")
        print("2: add a youtube video")
        print("3: Update a youtube video details")
        print("4: delete a youtube video ")
        print("5: Exit the app")
        inp = input("Enter Selection: ")
        match inp:
            case '1':
                printall()
            case '2':
                a = cur.execute("SELECT MAX(id) FROM videos")
                idx = int(a.fetchone()[0])
                idx = idx + 1 
                name = input("Enter Name:")
                time = input("Enter time:")
                data = (idx,name,time)
                cur.execute(''' INSERT INTO videos (id,video_name,time) VALUES(?,?,?) ''',data)
                con.commit()
            case '3':
                printall()
                idx = int(input("Enter index to update:"))
                print("for updating name press 1")
                print("for updating duration press 2")
                inp = int(input("Enter selection:"))
                if inp == 1:
                    value = input("Enter new name:")
                    cur.execute(''' UPDATE videos SET video_name =(?) WHERE id = ? ''',(value,idx))
                    con.commit()
                else:
                    value = input("Enter new time:")
                    cur.execute(''' UPDATE videos SET time = ? WHERE id = ? ''',(value,idx))
                    con.commit()
            case '4':
                printall()
                idx = int(input("Enter id:"))
                cur.execute("DELETE FROM videos WHERE id=?",(idx,))
                con.commit()
            case '5':
                break



if __name__ == "__main__":
    main()