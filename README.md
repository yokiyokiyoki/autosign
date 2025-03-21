[潮汐](https://chaoxi.pro/)自动签到脚本

## 功能
自动完成[潮汐](https://chaoxi.pro/)网站的每日签到，获取流量奖励。

## 使用方法
### 方法一：GitHub Actions（推荐）
1. Fork 本仓库
2. 在 Fork 后的仓库中添加以下 Secrets:
   - `CHAOXI_USERNAME`: 潮汐账号邮箱，多个账号用英文逗号分隔，如 `user1@example.com,user2@example.com`
   - `CHAOXI_PASSWORD`: 潮汐账号密码，与账号一一对应，如 `password1,password2`
   - `CHAOXI_DOMAIN`: 潮汐网站IP，域名有CF墙
3. GitHub Actions 将会按计划（每天北京时间9点）自动运行，也可以手动触发运行

### 方法二：本地运行
1. 克隆本仓库
2. 安装依赖：`pip install requests`
3. 设置环境变量:
   ```
   export CHAOXI_USERNAME="user1@example.com,user2@example.com"
   export CHAOXI_PASSWORD="password1,password2"
   export CHAOXI_DOMAIN="网站域名"  # 可选，默认为 chaoxi.pro
   ```
4. 运行脚本：`python chaoxi_sign.py`

## 多用户配置说明
- 用户名和密码使用英文逗号(,)分隔，一一对应
- 例如三个用户的配置：
  - CHAOXI_USERNAME: user1,user2,user3
  - CHAOXI_PASSWORD: pwd1,pwd2,pwd3

