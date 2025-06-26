import pathlib
import os
#rember: counting starts at 0
#trucate means to remove content from the end of a file 

#print(os.path.expanduser("~"))

#/Documents/VScode/githubStaging/fileWritingProgram/readTest.txt

#os.system('echo hello')

#os.system('sed -i "s/bread=pitta/bread=garlic/g" /home/corvo/Desktop/readTest.txt')

# sed -i 's/STRING_TO_REPLACE/STRING_TO_REPLACE_IT/g' filename -WORKS!!!

# variable.strip() removes any newline characters

textFileDir = (os.path.expanduser("~") + "/Documents/VScode/githubStaging/fileWritingProgram/readTest.txt")

toggleOne = "cheese=brie"
toggleTwo = "cheese=cheddar"

with open(textFileDir) as fp:
    deez=fp.readlines()[0]
    print(deez)
    if (deez.strip() == toggleOne):
        print("ur nan")
        os.system('sed -i "s/' + toggleOne + '/' + toggleTwo + '/g" ' + textFileDir)
        print(deez)
    if (deez.strip() == toggleTwo):
        print("jello")
        os.system('sed -i "s/' + toggleTwo + '/' + toggleOne + '/g" ' + textFileDir)
        print(deez)
    else:
        print("something went wrong lul")
