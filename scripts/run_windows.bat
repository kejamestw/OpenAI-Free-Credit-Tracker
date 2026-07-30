@echo off
cd /d "%~dp0\.."
set PYTHONPATH=%CD%\src
py -3 -m quota_monitor
if errorlevel 1 python -m quota_monitor
pause
