@echo off
chcp 65001 > nul
title 라프라시아 야구 시뮬레이션 RPG - Diamond and Magic

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║   라프라시아 야구 시뮬레이션 RPG                       ║
echo ║   "Diamond & Magic"                                    ║
echo ╚════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

if not exists "saves" mkdir saves
if not exists "logs" mkdir logs

python engine.py

pause
