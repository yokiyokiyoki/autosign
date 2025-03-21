#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import requests

# 配置日志
logger = logging.getLogger(__name__)

def send_notification(message, notification_type='telegram'):
    """
    发送通知，支持多种通知方式
    
    Args:
        message (str): 要发送的消息内容
        notification_type (str): 通知类型，目前支持 'telegram'
        
    Returns:
        bool: 成功返回True，失败返回False
    """
    if notification_type == 'telegram':
        return send_telegram_notification(message)
    else:
        logger.warning(f"不支持的通知类型: {notification_type}")
        return False

def send_telegram_notification(message):
    """
    发送Telegram通知
    
    Args:
        message (str): 要发送的消息内容
        
    Returns:
        bool: 成功返回True，失败返回False
    """
    tg_bot_token = os.environ.get('TG_BOT_TOKEN')
    tg_chat_id = os.environ.get('TG_CHAT_ID')
    
    if not tg_bot_token or not tg_chat_id:
        logger.info("未配置Telegram通知参数，跳过通知")
        return False
    
    try:
        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
        data = {
            "chat_id": tg_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            logger.info("Telegram通知发送成功")
            return True
        else:
            logger.error(f"Telegram通知发送失败，状态码: {response.status_code}")
            logger.error(f"响应内容: {response.text}")
            return False
    except Exception as e:
        logger.error(f"发送Telegram通知时发生错误: {str(e)}")
        return False
