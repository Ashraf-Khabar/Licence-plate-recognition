#!/bin/bash

git checkout model   # switch to the "model" branch
git add .          # add all changes
git pull origin model
git commit -m "$*"   # commit changes with a timestamp
git push origin model   # push changes to the "model" branch on the remote repository