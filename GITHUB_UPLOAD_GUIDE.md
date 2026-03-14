# GitHub上传指南

## 步骤1: 安装Git

### Windows用户
1. 下载Git: https://git-scm.com/download/win
2. 运行安装程序，使用默认选项
3. 安装完成后，重启命令行工具

### 验证安装
```bash
git --version
```

## 步骤2: 配置Git

### 设置用户名和邮箱
```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

### 验证配置
```bash
git config --list
```

## 步骤3: 初始化Git仓库

### 进入项目目录
```bash
cd "D:\360MoveData\Users\Mamihlapinatapai\Desktop\Project_AIVideoFlow_易学"
```

### 初始化Git
```bash
git init
```

### 添加所有文件
```bash
git add .
```

### 提交更改
```bash
git commit -m "初始提交: 基于ComfyUI的全自动多模态AI视频生产流"
```

## 步骤4: 连接到GitHub仓库

### 创建GitHub仓库
1. 登录GitHub: https://github.com
2. 点击右上角 "+" → "New repository"
3. 填写信息:
   - Repository name: `Project_AIVideoFlow`
   - Description: `基于ComfyUI的全自动多模态AI视频生产流`
   - 选择: Public
   - 不要初始化README（我们已经有了）

### 添加远程仓库
```bash
git remote add origin https://github.com/2923858564/Project_AIVideoFlow.git
```

### 验证远程仓库
```bash
git remote -v
```

## 步骤5: 推送到GitHub

### 首次推送
```bash
git push -u origin main
```

如果遇到错误，可能需要先拉取：
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### 输入GitHub凭据
- 用户名: 你的GitHub用户名
- 密码: 使用Personal Access Token（见步骤6）

## 步骤6: 创建Personal Access Token

### 生成Token
1. 登录GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 点击 "Generate new token"
3. 选择 "Generate new token (classic)"
4. 设置:
   - Note: `Project_AIVideoFlow Upload`
   - Expiration: 90 days (推荐)
   - Select scopes: 勾选 `repo` (全部权限)
5. 点击 "Generate token"
6. **复制Token**（只显示一次）

### 使用Token
- 当Git要求输入密码时，粘贴Token

## 步骤7: 验证上传

### 检查GitHub仓库
1. 访问: https://github.com/2923858564/Project_AIVideoFlow
2. 确认文件已上传

### 本地验证
```bash
git status
git log --oneline
```

## 步骤8: 后续更新

### 添加新文件
```bash
git add .
git commit -m "更新描述"
git push
```

### 更新特定文件
```bash
git add 文件名
git commit -m "更新特定文件"
git push
```

## 常见问题解决

### 问题1: 拒绝推送
```bash
# 先拉取最新更改
git pull origin main
# 解决冲突（如果有）
# 然后推送
git push
```

### 问题2: 大文件上传
```bash
# 如果视频文件太大，需要.gitignore排除
# 或者使用Git LFS
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add .
git commit -m "添加大文件支持"
git push
```

### 问题3: 网络问题
```bash
# 设置代理（如果需要）
git config --global http.proxy http://proxy.example.com:8080
git config --global https.proxy https://proxy.example.com:8080

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 自动化脚本

### Windows批处理脚本 (`upload_to_github.bat`)
```batch
@echo off
chcp 65001 >nul
title 上传到GitHub

echo.
echo ========================================
echo   上传Project_AIVideoFlow到GitHub
echo ========================================
echo.

cd /d "D:\360MoveData\Users\Mamihlapinatapai\Desktop\Project_AIVideoFlow_易学"

echo 步骤1: 检查Git状态
git status

echo.
echo 步骤2: 添加所有文件
git add .

echo.
echo 步骤3: 提交更改
set /p commit_msg=请输入提交信息: 
git commit -m "%commit_msg%"

echo.
echo 步骤4: 推送到GitHub
git push origin main

echo.
echo 上传完成！
pause
```

### 创建脚本
将上面的批处理脚本保存为 `upload_to_github.bat` 在项目根目录，然后双击运行。

## 最佳实践

1. **定期提交**: 每天工作结束后提交更改
2. **有意义的提交信息**: 描述做了什么更改
3. **分支管理**: 为新功能创建分支
4. **忽略大文件**: 使用.gitignore排除模型文件和视频
5. **备份重要文件**: 重要的配置文件和代码

## 获取帮助

- Git官方文档: https://git-scm.com/doc
- GitHub帮助: https://docs.github.com
- 常见问题: 查看项目README.md

---

**注意**: 首次上传可能需要一些时间，特别是如果包含大文件。请确保网络连接稳定。