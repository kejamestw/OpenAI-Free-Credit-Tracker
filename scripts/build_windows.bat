@echo off
cd /d "%~dp0\.."
python -m pip install -r requirements-dev.txt
python -m PyInstaller --noconfirm --clean --onefile --name OpenAI-Free-Credit-Tracker --paths src --add-data "web;web" --add-data "data;data" src\quota_monitorpp.py
if exist "dist\OpenAI-Free-Credit-Tracker.exe" explorer dist
pause
