import os

def detectText(filename):
    with open(filename,'r') as f:
        content = f.read()
    
    if 'abc' in content.lower():
        return True
    else:
        return False



if __name__ == "__main__":
    FOLDER = "assets/"
    files = os.listdir(FOLDER)
    # print(file)
    count = 0
    for file in files:
        if file.endswith('txt'):
            print("***********Detecting text*********")
            found = detectText(f"{FOLDER}/{file}")
            
            if(found):
                print("Text found")
                count+=1
            else:
                print("Not found")

    print(f"Total Count: {count}")

