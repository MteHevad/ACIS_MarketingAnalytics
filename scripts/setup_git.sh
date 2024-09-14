#!/bin/bash
git init
git remote add origin https://github.com/MteHevad/ACIS_MarketingAnalytics.git
git add .
git commit -m "Initial commit"
git push -u origin main
git checkout -b task-1
git push -u origin task-1
