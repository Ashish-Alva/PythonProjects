import os

files = os.listdir()
files.remove('main.py')
print(dir)

# images, media, doc

def createifnotexists(folder):
    if not os.path.exists(folder):
        Images = os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


createifnotexists('Images')
createifnotexists('Media')
createifnotexists('Docs')
createifnotexists('Others')

imgexts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgexts ]


mediaexts = [".mp4", ".mp3"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaexts ]


docexts = [".pdf", ".docs", ".doc", ".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docexts ]

others = []
for file in files:
    ext =  os.path.splitext(file)[1].lower()
    if ext not in imgexts and ext not in mediaexts and ext not in docexts and os.path.isfile(file):
        others.append(file)

print(others)

move("Image",images)
move("Media",media)
move("Docs",docs)
move("Others",others)