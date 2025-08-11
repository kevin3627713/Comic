#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JM漫画下载邮件通知测试脚本
用于测试邮件发送功能是否正常工作
"""

import os
import sys
import json
import base64
import requests
import smtplib
import mimetypes
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import formataddr
from email import encoders

def create_test_files():
    """创建测试文件"""
    test_files = []
    
    # 创建测试文本文件
    test_txt = "test_manga.txt"
    with open(test_txt, 'w', encoding='utf-8') as f:
        f.write("JM漫画下载测试文件\n")
        f.write(f"创建时间: {datetime.now()}\n")
        f.write("这是一个测试附件文件。\n")
    test_files.append(test_txt)
    
    # 创建测试JSON文件
    test_json = "download_info.json"
    test_data = {
        "title": "测试漫画",
        "download_time": datetime.now().isoformat(),
        "file_count": 10,
        "total_size": "50MB",
        "format": ["jpg", "pdf"]
    }
    with open(test_json, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)
    test_files.append(test_json)
    
    return test_files

def test_notification_service(github_token, notification_repo, test_files):
    """测试通过notification-service发送邮件"""
    print("=== 测试notification-service发送方式 ===")
    
    def encode_file_to_base64(file_path):
        """将文件编码为base64字符串"""
        try:
            with open(file_path, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            print(f"编码文件失败: {e}")
            return None
    
    def get_content_type(file_path):
        """根据文件扩展名猜测MIME类型"""
        content_type, _ = mimetypes.guess_type(file_path)
        return content_type or 'application/octet-stream'
    
    # 准备附件
    attachments = []
    for file_path in test_files:
        if os.path.exists(file_path):
            filename = os.path.basename(file_path)
            encoded_content = encode_file_to_base64(file_path)
            if encoded_content:
                attachments.append({
                    "filename": filename,
                    "content": encoded_content,
                    "encoding": "base64",
                    "content_type": get_content_type(file_path)
                })
                print(f"准备附件: {filename}")
    
    # 构建请求payload
    payload = {
        "event_type": "send-notification",
        "client_payload": {
            "title": "JM漫画下载测试邮件",
            "content": "这是一个测试邮件，用于验证JM漫画下载完成后的邮件通知功能。\n\n如果您收到这封邮件，说明邮件通知功能工作正常。",
            "source": "jmcomic_test",
            "timestamp": datetime.now().isoformat(),
            "attachments": attachments
        }
    }
    
    # 发送请求
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}",
        "Content-Type": "application/json"
    }
    
    url = f"https://api.github.com/repos/{notification_repo}/dispatches"
    
    try:
        print(f"发送通知请求到: {url}")
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 204:
            print("✓ 通知请求发送成功")
            return True
        else:
            print(f"✗ 通知请求发送失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ 发送请求时发生错误: {e}")
        return False

def test_direct_smtp(smtp_config, test_files):
    """测试直接SMTP发送邮件"""
    print("=== 测试直接SMTP发送方式 ===")
    
    try:
        # 构建邮件
        message = MIMEMultipart()
        
        # 添加文本内容
        content = "这是一个测试邮件，用于验证JM漫画下载完成后的邮件通知功能。\n\n如果您收到这封邮件，说明邮件通知功能工作正常。"
        text_part = MIMEText(content, 'plain', 'utf-8')
        message.attach(text_part)
        
        # 添加附件
        for file_path in test_files:
            if os.path.exists(file_path):
                filename = os.path.basename(file_path)
                file_size = os.path.getsize(file_path)
                
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                
                # 猜测MIME类型
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = 'application/octet-stream'
                
                # 创建附件对象
                main_type, sub_type = content_type.split('/', 1)
                attachment_part = MIMEBase(main_type, sub_type)
                attachment_part.set_payload(file_data)
                encoders.encode_base64(attachment_part)
                
                # 设置附件头
                attachment_part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"'
                )
                
                message.attach(attachment_part)
                print(f"添加附件: {filename} ({file_size} bytes)")
        
        # 设置邮件头
        message['From'] = formataddr((Header(smtp_config['name'], 'utf-8').encode(), smtp_config['email']))
        message['To'] = formataddr((Header(smtp_config['name'], 'utf-8').encode(), smtp_config['email']))
        message['Subject'] = Header("JM漫画下载测试邮件", 'utf-8')
        
        # 发送邮件
        if smtp_config['ssl'].lower() == 'true':
            smtp_client = smtplib.SMTP_SSL(smtp_config['server'])
        else:
            smtp_client = smtplib.SMTP(smtp_config['server'])
        
        smtp_client.login(smtp_config['email'], smtp_config['password'])
        smtp_client.sendmail(smtp_config['email'], smtp_config['email'], message.as_string())
        smtp_client.close()
        
        print("✓ SMTP邮件发送成功")
        return True
        
    except Exception as e:
        print(f"✗ SMTP邮件发送失败: {str(e)}")
        return False

def cleanup_test_files(test_files):
    """清理测试文件"""
    print("清理测试文件...")
    for file_path in test_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"删除: {file_path}")

def main():
    """主函数"""
    print("JM漫画下载邮件通知测试脚本")
    print("=" * 50)
    
    # 创建测试文件
    print("创建测试文件...")
    test_files = create_test_files()
    
    try:
        # 获取配置
        github_token = os.environ.get('GITHUB_TOKEN', '')
        notification_repo = os.environ.get('NOTIFICATION_REPO', '')
        
        smtp_config = {
            'server': os.environ.get('SMTP_SERVER', ''),
            'ssl': os.environ.get('SMTP_SSL', 'true'),
            'email': os.environ.get('SMTP_EMAIL', ''),
            'password': os.environ.get('SMTP_PASSWORD', ''),
            'name': os.environ.get('SMTP_NAME', 'JM漫画下载服务')
        }
        
        success_count = 0
        total_tests = 0
        
        # 测试notification-service方式
        if github_token and notification_repo:
            total_tests += 1
            if test_notification_service(github_token, notification_repo, test_files):
                success_count += 1
        else:
            print("跳过notification-service测试（未配置GITHUB_TOKEN或NOTIFICATION_REPO）")
        
        # 测试直接SMTP方式
        if all([smtp_config['server'], smtp_config['email'], smtp_config['password']]):
            total_tests += 1
            if test_direct_smtp(smtp_config, test_files):
                success_count += 1
        else:
            print("跳过直接SMTP测试（未配置SMTP参数）")
        
        # 输出结果
        print("\n" + "=" * 50)
        print(f"测试完成: {success_count}/{total_tests} 成功")
        
        if total_tests == 0:
            print("错误: 没有配置任何发送方式")
            print("\n请设置以下环境变量之一：")
            print("方式1 - notification-service:")
            print("  GITHUB_TOKEN=your_token")
            print("  NOTIFICATION_REPO=username/repo")
            print("\n方式2 - 直接SMTP:")
            print("  SMTP_SERVER=smtp.gmail.com")
            print("  SMTP_EMAIL=your_email@gmail.com")
            print("  SMTP_PASSWORD=your_password")
            return 1
        
        if success_count == total_tests:
            print("✓ 所有测试通过，邮件通知功能正常")
            return 0
        else:
            print("✗ 部分测试失败，请检查配置")
            return 1
    
    finally:
        # 清理测试文件
        cleanup_test_files(test_files)

if __name__ == "__main__":
    sys.exit(main())