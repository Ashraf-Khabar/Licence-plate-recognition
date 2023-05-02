#!/bin/bash

# Make sure we are on the main branch
git checkout main

# Merge the api branch into the main branch
git merge api

# Create a new directory named "api" in the root of the repository
mkdir api

# Copy the contents of the api folder from the api branch into the newly created api directory
git checkout api -- api/*

# Add the new api directory to the main branch
git add api

# Commit the changes
git commit -m "$*"

# Pull origin from main
git pull origin main

# Push the changes to the remote repository
git push origin main
