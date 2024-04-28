import cv2
import face_recognition
import os
import pickle



# Importing the Student images 

folderPath = 'images'
imgPathList = os.listdir(folderPath)
imgList = []
studentId_list = []
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) 
    studentId_list.append(path.split(".")[0])
    filename = f'{folderPath}/{path}'
    

print(studentId_list)


def findEncodings(imagesList):
    encode_list = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

print("Encoding Started...")

encodeList = findEncodings(imgList)

encodeListId =  [encodeList,studentId_list]
print("Encoding Complete...")

# print(encodeList)


file = open("encodeFile.p","wb")
pickle.dump(encodeListId,file)
file.close()

print("File Saved...")



