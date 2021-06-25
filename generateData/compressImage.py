from PIL import Image
import os
import PIL 
import glob 

os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/pawn') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/pawn/{counter}compressedpawn.png')  
    counter += 1


os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/knight') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/knight/{counter}compressedknight.png')  
    counter += 1

os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/bishop') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/bishop/{counter}compressedbishop.png')  
    counter += 1


os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/rook') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/rook/{counter}compressedrook.png')  
    counter += 1





os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/queen') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/queen/{counter}compressedqueen.png')  
    counter += 1


os.chdir('/home/mc145/Programming/BoardToFen/generateData/rawdata/king') 

counter = 1

for img in os.listdir():
    image = Image.open(img) 
    resized_image = image.resize((64,64))
    print(resized_image.size) 
    resized_image = resized_image.save(f'/home/mc145/Programming/BoardToFen/training/data/king/{counter}compressedking.png')  
    counter += 1


