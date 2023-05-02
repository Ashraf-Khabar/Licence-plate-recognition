#!/bin/bash

# switch to the "api" branch
git checkout api  

# add all changes
git add .          

# pull origin from api branch
git pull origin api

 # commit changes with a timestamp
git commit -m "$*"

# push changes to the "api" branch on the remote repository
git push origin api  
