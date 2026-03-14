@echo off
chcp 65001 >nul
title 上传Project_AIVideoFlow到GitHub

echo.
echo ========================================
echo   上传Project_AIVideoFlow到GitHub
echo ========================================
echo.

REM 检查是否在项目目录
if not exist "README.md" (
    echo 错误: 请确保在项目根目录运行此脚本
    echo 当前目录: %cd%
    pause
    exit /b 1
)

REM 步骤1: 检查Git是否安装
where git >nul 2>nul
if errorlevel 1 (
    echo 错误: Git未安装
    echo 请先安装Git: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Git已安装: 
git --version

echo.
echo ========================================
echo 步骤1: 检查Git状态
echo ========================================
git status

echo.
echo ========================================
echo 步骤2: 添加所有文件
echo ========================================
git add .

echo.
echo ========================================
echo 步骤3: 提交更改
echo ========================================
set /p commit_msg=请输入提交信息: 
if "%commit_msg%"=="" (
    set commit_msg="更新项目文件"
)
git commit -m "%commit_msg%"

echo.
echo ========================================
echo 步骤4: 推送到GitHub
echo ========================================
echo 正在推送到GitHub...
git push origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo 推送失败，尝试初始化仓库
    echo ========================================
    
    echo 初始化Git仓库...
    git init
    
    echo 添加远程仓库...
    git remote add origin https://github.com/2923858564/Project_AIVideoFlow.git
    
    echo 重新添加文件...
    git add .
    
    echo 重新提交...
    git commit -m "%commit_msg%"
    
    echo 强制推送...
    git push -u origin main --force
)

echo.
echo ========================================
echo 上传完成！
echo ========================================
echo.
echo 请访问: https://github.com/2923858564/Project_AIVideoFlow
echo 确认文件已成功上传
echo.

pause