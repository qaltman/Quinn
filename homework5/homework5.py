#Git vs Github
# git is a version control tool that runs on your computer and ntracks cahnges in files 
# git hub is a website and service that hosts git repositories online. 

#Terminal is the app windown you can type commands into 
#command lines is the same thing but hosted on line that you can push to

#local repository is a git repo stored on your computer. 
#remote repository is the same repo but hosted online that you push to such as github 

#version control is a system for saving and organizing changes to files so you can see history

#Staging area is a prep thing in git where you choose which file changes will be includded in the next commit 
#git add just moves file changes into the staging area 
#git commit saves the file changes to the local repo hostry and lets you add a message 
#git push uploads and comits the changes to the remote repository

#git status shows what branch you are working an and what files are modified, staged, or untracked. 
#git pull downloads updates from the remote repo and merges them in to the local repo 

#pwd is print working directory and shows the full path to the folder you are currently in 
#ls lists all the files and folders in the directory 

#cd is change directory and moves you into another folder 

#nano allows for you to edit in a terminal using a text editor 
#touch creates and new empty file of your choice 

#mv moves or renames a file and or folder 
#rm removes or deletes a file you need to use very carefully because you cannot get it back 
#cat prints the contents of a file to the terminal useful for looking at contents of file without opening using nano or python3 

#-----------------------------------------------------------------------------------------------------------------------------------------

#pwd 
#ls
# you would cd into brianna_decal then use git pull to pull brianna main 
# to move use mv homework.py ~/python_decal/judy_decal/homework/ 
#use cd to move repositories ~/python_decal/judy_decal/homework/ 
# use cat and the homework.py comand to paste into the file. 
#to save changes use git add, commit, and push 
# to fix you should use git pull first then go foward with add commit and push
#to move you would go cd/home/Judy/Recents/
# ----------------------------------------------------------------------------------------------------------------------------------------------------

#Review

def checkDataType(x):
    return type(x)

print (checkDataType(3.14))

def evenOrOdd(y): 
    if y % 2 == 0: 
        return "even"
    else: 
        return "odd"
    

print(evenOrOdd(9))

def sumWithLoop(numbers):
    total = 0 
    for n in numbers: 
        total += n 
    return total

numbers = [1,2,3,4,5]
print(sumWithLoop(numbers))

def duplicateList(lst):
    new_list = []
    for item in lst: 
        new_list.append(item)
        new_list.append(item)
    return new_list

print(duplicateList(["a","b","c"]))

def square(num): 
    return num * num


print (square(6))
