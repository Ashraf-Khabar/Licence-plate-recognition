#!/bin/bash

git checkout api   # switch to the "api" branch
git add .          # add all changes
git commit -m "Automated commit at $(date)"   # commit changes with a timestamp
git push origin api   # push changes to the "api" branch on the remote repository
