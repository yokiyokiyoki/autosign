[潮汐](https://chaoxi.pro/)自动签到脚本

## 功能
- 自动完成[潮汐](https://chaoxi.pro/)网站的每日签到，获取流量奖励。
- 支持通过 Telegram 机器人推送签到结果通知。
- 模块化设计，易于扩展其他通知方式。
- 自动清理过期的 GitHub Actions 运行记录。

## 使用方法
### 方法一：GitHub Actions（推荐）
1. Fork 本仓库
2. 在 Fork 后的仓库中添加以下 Secrets:
   - `CHAOXI_USERNAME`: 潮汐账号邮箱，多个账号用英文逗号分隔，如 `user1@example.com,user2@example.com`
   - `CHAOXI_PASSWORD`: 潮汐账号密码，与账号一一对应，如 `password1,password2`
   - `CHAOXI_DOMAIN`: 潮汐网站IP，域名有CF墙
   - `TG_BOT_TOKEN`: Telegram 机器人的 API 令牌（可选）
   - `TG_CHAT_ID`: 接收通知的 Telegram 聊天 ID（可选）
3. GitHub Actions 将会按计划（每天北京时间9点）自动运行，也可以手动触发运行

### 方法二：本地运行
1. 克隆本仓库
2. 安装依赖：`pip install requests`
3. 设置环境变量:
   ```
   export CHAOXI_USERNAME="user1@example.com,user2@example.com"
   export CHAOXI_PASSWORD="password1,password2"
   export CHAOXI_DOMAIN="网站域名"  # 可选，默认为 chaoxi.pro
   export TG_BOT_TOKEN="你的Telegram机器人令牌"  # 可选，用于Telegram通知
   export TG_CHAT_ID="你的Telegram聊天ID"  # 可选，用于Telegram通知
   ```
4. 运行脚本：`python chaoxi_sign.py`

## 多用户配置说明
- 用户名和密码使用英文逗号(,)分隔，一一对应
- 例如三个用户的配置：
  - CHAOXI_USERNAME: user1,user2,user3
  - CHAOXI_PASSWORD: pwd1,pwd2,pwd3

## Telegram 通知配置
### 获取 Bot Token
1. 在 Telegram 中搜索 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot` 命令创建一个新机器人
3. 按照提示完成创建，获取 API Token

### 获取 Chat ID
1. 在 Telegram 中搜索你创建的机器人并发送一条消息
2. 访问 `https://api.telegram.org/bot<你的Bot Token>/getUpdates`
3. 在返回的 JSON 中找到 `chat` 对象中的 `id` 字段

### 通知内容
成功配置后，每次签到完成会收到包含以下信息的通知：
- 执行时间（北京时间）
- 执行状态（成功/失败）
- 签到结果统计


