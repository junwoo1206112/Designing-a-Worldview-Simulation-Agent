@echo off
chcp 65001 > nul
title OpenSpec 초기화 - 라프라시아 야구 시뮬레이션 RPG

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║   OpenSpec 초기화                                      ║
echo ║   라프라시아 야구 시뮬레이션 RPG                       ║
echo ╚════════════════════════════════════════════════════════╝
echo.

cd /d "%~dp0\.."

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Node.js 가 설치되어 있지 않습니다.
    echo https://nodejs.org/ 에서 Node.js 20.19.0 이상을 설치해주세요.
    pause
    exit /b 1
)

echo [1/4] Node.js 버전 확인...
node --version

echo.
echo [2/4] OpenSpec 설치...
call npm install -g @fission-ai/openspec@latest

echo.
echo [3/4] 디렉토리 구조 생성...
if not exist "openspec" mkdir openspec
if not exist "openspec\changes\active" mkdir openspec\changes\active
if not exist "openspec\changes\archive" mkdir openspec\changes\archive
if not exist "openspec\specs" mkdir openspec\specs
if not exist "openspec\proposals" mkdir openspec\proposals
if not exist ".openspec" mkdir .openspec

echo.
echo [4/4] 설정 파일 생성...

(
    echo {
    echo   "version": "1.0",
    echo   "project": "라프라시아 야구 시뮬레이션 RPG",
    echo   "profile": "spec-driven",
    echo   "created_at": "%date% %time%"
    echo }
) > .openspec\config.json

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║   OpenSpec 초기화 완료!                                ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo 이제 다음 명령으로 시작하세요:
echo.
echo   /opsx:propose "추가하고 싶은 기능"
echo.
echo 예시:
echo   /opsx:propose "배틀 시스템 추가"
echo   /opsx:propose "새 NPC 추가 - 올리비아"
echo   /opsx:propose "에피소드 4 작성"
echo.

pause
