#!/bin/bash

# Make sure we are on the main branch
git checkout main

# Merge the model branch into the main branch
git merge model

# Create a new directory named "model" in the root of the repository
mkdir model

# Copy the contents of the model folder from the model branch into the newly created model directory
git checkout model -- model/*

# Add the new model directory to the main branch
git add model

# Commit the changes
git commit -m "$*"


git pull origin main

# Push the changes to the remote repository
git push origin main