@echo off
chcp 65001 > nul
cd /d "%~dp0"
python build_sk.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build failed.
    exit /b %ERRORLEVEL%
)
echo [SUCCESS] SK hynix Follow-up Q&A Dashboard built successfully.
