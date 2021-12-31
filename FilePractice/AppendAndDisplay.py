'''
Created on Dec 5, 2021

@author: justi
'''
with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\Error.txt.txt", "a") as myfile:
    
    
    user_text = input('What would you like to append to the file: ')
    
    myfile.write(user_text + '\n')

with open(r"C:\Users\justi\My Documents\LiClipse Workspace\IT\Chapter7\Error.txt.txt") as myfile:
    
    filetext = myfile.read()
    print(filetext)