#!/bin/bash

# switch to the "model" branch
git checkout model   

# add all changes
git add .    

# pull origin from main
git pull origin model

# commit changes with a timestamp
git commit -m "Automated commit at $(date)"   

# push changes to the "model" branch on the remote repository
git push origin model   