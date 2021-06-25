import os 

os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/pawn') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'pawn' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)




os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/knight') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'knight' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)



os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/bishop') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'bishop' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)






os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/king') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'king' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)





os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/rook') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'rook' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)





os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/queen') 
print(os.getcwd()) 

count = 1



for img in os.listdir():
    img_name, img_ext = os.path.splitext(img)
    img_name = str(count) + 'queen' 
    count += 1

    update_name = '{} {}'.format(img_name, img_ext) 
    os.rename(img, update_name)


