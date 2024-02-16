@echo off
cd /d %~dp0

git status
echo "If everythng seems good you're going to add ."
pause
git add .
echo "If everythng seems good you're going to commit "
pause
set /p commitMessage=Enter your commit message :
git commit -m "%commitMessage%"
echo "If everythng seems good you're going to push origin master "
pause
git push origin main

