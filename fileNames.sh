#!/bin/bash

#script to change file names
cd Solutions
for d in */; do
    cd $d
    ls
    for f in *; do
        if [ "${f: -2}" == "md" ]       #README 
        then   
            mv "$f" "README.md"

        elif [ "${f: -2}" == "py" ]     #python 
        then   
            mv "$f" "Solution.py"

        elif [ "${f: -4}" == "java"]    #java 
        then 
            mv "$f" "Solution.java"

        elif [ "${f: -1}" == "c" ]      #c 
        then 
            mv "$f" "Solution.c"

        elif [ "${f: -2}" == "hs" ]     #haskell 
        then 
            mv "$f" "Solution.hs"

        else                            #...
            echo "Error"                      
        fi
    done
    ls 
    cd ..
done 
cd ..
echo "Updated"