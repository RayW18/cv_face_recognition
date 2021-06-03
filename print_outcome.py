import os
path = "data/images/"


def embedded_numbers(s):
    title = s.split('.')[0]                 # 切成数字和非数字
    pieces = int(title[2:])      # 将数字部分转成整数
    return pieces


def galleryImages():
    galleryFList = ""
    galleryPath = path + "gallery"
    for root, dirs, files in os.walk(galleryPath):
        newFile = list(sorted(files, key=embedded_numbers))
        for name in newFile:
            galleryFName = galleryPath + "/" + name
            galleryFList = galleryFList + " " + galleryFName
    return galleryFList


def compareImage():
    f1 = []
    valPath = path + "test"
    for root, dirs, files in os.walk(valPath):
        newFile = list(sorted(files, key=embedded_numbers))
        for name in newFile:
            valName = valPath + "/" + name
            f1.append(valName)
    return f1


model_name = "src/models/train_4/20210603-164544"
f1 = compareImage()
f2 = galleryImages()
imageList = ""
print(len(f1))
count = 0
for image in f1:
    count+=1
    imageList += " " + image
# print(imageList)
# print(f2)
os.system("python src/compare.py" + " " + model_name + " " + imageList + f2)
