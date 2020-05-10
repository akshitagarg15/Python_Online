# file-->character mode
#        binary mode(audio,mp4,images)


# modes--> 
# read-->only read(r)
# write--> overwrite(w)
# append--> at last write (a)
# exclusive creation--> if file already exists then it fails(x)

# try:
#     f=open("doc2.txt",'r')
#     data=f.read()
#     print(data)
# except FileNotFoundError as err:
#     print("File is not available")

# open is inbuilt
# f=open("doc.txt",'r')
# data=f.readline()
# data=f.read(5)
# print(data)
# print(f.readlines())
# for i in f:
#     print(i)

# write mode
# f1=open("doc.txt",'r')
# f=open("doc2.txt",'w')

# for data in f1:
#     f.write(data)


# img=open('watch.jpg','rb')

# print(img.read())

# with open('duplicate2.jpg','wb') as f3:
#     for i in img:
#         f3.write(i)



# f.write("I have written here....")
# f.write("Hey ther")
# f1.close()
# f.close()

import os
os.remove('watch.jpg')
print("File deleted successfully!")






