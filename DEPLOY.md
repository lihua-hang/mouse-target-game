# 部署指南：将游戏分享给远方的朋友

## 步骤1：注册Vercel账号
1. 访问 [Vercel官网](https://vercel.com/)
2. 点击"Sign Up"按钮注册一个账号（可以使用GitHub、GitLab或Bitbucket账号登录）

## 步骤2：安装Vercel CLI
1. 打开命令提示符（Windows）或终端（Mac/Linux）
2. 运行以下命令安装Vercel CLI：
   ```bash
   npm install -g vercel
   ```
   （如果没有安装Node.js，需要先安装Node.js）

## 步骤3：部署应用
1. 进入项目目录：
   ```bash
   cd D:\各种各样的小程序\1
   ```
2. 运行以下命令初始化并部署项目：
   ```bash
   vercel
   ```
3. 按照提示回答问题：
   - 选择"Create a New Project"
   - 为项目命名（例如"mouse-target-game"）
   - 选择默认的构建和输出设置
   - 确认部署

## 步骤4：获取部署URL
1. 部署完成后，Vercel会提供一个URL（例如：`https://mouse-target-game.vercel.app`）
2. 将这个URL分享给你的朋友，他们就可以通过浏览器访问并玩这个游戏了

## 注意事项
- 部署后，任何更改代码都需要重新运行`vercel`命令来更新部署
- Vercel的免费计划足以支持这个小游戏的访问需求
- 如果遇到部署问题，可以参考Vercel的官方文档或联系Vercel支持