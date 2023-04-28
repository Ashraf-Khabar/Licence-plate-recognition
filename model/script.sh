#!/bin/bash

# Make sure we are on the main branch
git checkout main

# Merge the api branch into the main branch
git merge model

# Create a new directory named "api" in the root of the repository
mkdir model

# Copy the contents of the api folder from the api branch into the newly created api directory
git checkout model -- model/*

# Add the new api directory to the main branch
git add model

# Commit the changes
git commit -m "Added model directory to main branch"

git pull origin main

# Push the changes to the remote repository
git push origin main