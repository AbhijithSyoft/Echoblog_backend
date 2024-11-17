#!/bin/bash

# Remove previous deployment files
rm -rf .vercel

# Remove Python cache files
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Deploy to Vercel
vercel --prod 