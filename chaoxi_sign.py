#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def sign_in_single_user(username, password, domain):
    """单个用户的潮汐签到函数"""
    logger.info(f"开始处理用户: {username}")
    
    # 创建会话
    session = requests.Session()
    
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Origin': f'https://{domain}',
    }
    
    try:
        # 登录请求
        login_url = f'https://{domain}/auth/login'
        login_data = {
            'email': username,
            'passwd': password
        }
        
        logger.info("尝试登录...")
        login_response = session.post(login_url, headers=headers, json=login_data)
        
        if login_response.status_code != 200:
            logger.error(f"登录失败，状态码: {login_response.status_code}")
            logger.error(f"响应内容: {login_response.text}")
            return False
        
        # 检查登录响应的 JSON
        try:
            login_result = login_response.json()
            if login_result.get('ret') != 1 or login_result.get('msg') != "登录成功":
                logger.error(f"登录验证失败: {login_result}")
                return False
            logger.info("登录成功")
        except json.JSONDecodeError:
            logger.error("无法解析登录响应")
            logger.error(f"响应内容: {login_response.text}")
            return False
        
        # 签到请求
        sign_url = f'https://{domain}/user/checkin'
        
        logger.info("尝试签到...")
        sign_response = session.post(sign_url, headers=headers)
        
        if sign_response.status_code != 200:
            logger.error(f"签到失败，状态码: {sign_response.status_code}")
            logger.error(f"响应内容: {sign_response.text}")
            return False
            
        try:
            result = sign_response.json()
            if result.get('ret') == 1:
                msg = result.get('msg', '未知结果')
                logger.info(f"签到成功: {msg}")
                return True
            else:
                logger.warning(f"签到返回异常: {result}")
                return False
        except json.JSONDecodeError:
            logger.error("无法解析签到响应")
            logger.error(f"响应内容: {sign_response.text}")
            return False
            
    except Exception as e:
        logger.error(f"签到过程中发生错误: {str(e)}")
        return False

def sign_in():
    """潮汐自动签到主函数"""
    # 从环境变量获取域名，默认为 chaoxi.pro
    domain = os.environ.get('CHAOXI_DOMAIN', 'chaoxi.pro')
    
    # 从环境变量获取多个用户凭据
    usernames = os.environ.get('CHAOXI_USERNAME', '').split(',')
    passwords = os.environ.get('CHAOXI_PASSWORD', '').split(',')
    
    if not usernames[0] or len(usernames) != len(passwords):
        logger.error("用户名或密码配置错误，请检查环境变量")
        return False
    
    success_count = 0
    total_users = len(usernames)
    
    logger.info(f"共检测到 {total_users} 个用户")
    
    for i, (username, password) in enumerate(zip(usernames, passwords)):
        logger.info(f"处理用户 {i+1}/{total_users}")
        if sign_in_single_user(username.strip(), password.strip(), domain):
            success_count += 1
    
    logger.info(f"签到完成，成功: {success_count}/{total_users}")
    return success_count > 0

if __name__ == "__main__":
    logger.info(f"开始执行潮汐签到 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    result = sign_in()
    if result:
        logger.info("签到流程完成")
    else:
        logger.error("签到流程失败")
