#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JM漫画下载邮件通知使用示例
演示如何在本地环境中测试和使用邮件通知功能
"""

import os
import sys

def setup_environment_variables():
    """设置环境变量示例"""
    print("=== 环境变量配置示例 ===")
    print()
    
    print("方式1: 通过notification-service发送（推荐）")
    print("export GITHUB_TOKEN='your_github_personal_access_token'")
    print("export NOTIFICATION_REPO='your_username/notification-service'")
    print("export SMTP_SERVER='smtp.gmail.com'")
    print("export SMTP_SSL='true'")
    print("export SMTP_EMAIL='your_email@gmail.com'")
    print("export SMTP_PASSWORD='your_app_password'")
    print("export SMTP_NAME='JM漫画下载服务'")
    print()
    
    print("方式2: 直接SMTP发送")
    print("export SMTP_SERVER='smtp.gmail.com'")
    print("export SMTP_SSL='true'")
    print("export SMTP_EMAIL='your_email@gmail.com'")
    print("export SMTP_PASSWORD='your_app_password'")
    print("export SMTP_NAME='JM漫画下载服务'")
    print()

def check_current_config():
    """检查当前配置"""
    print("=== 当前配置检查 ===")
    
    # 检查notification-service配置
    github_token = os.environ.get('GITHUB_TOKEN', '')
    notification_repo = os.environ.get('NOTIFICATION_REPO', '')
    
    print("notification-service配置:")
    print(f"  GITHUB_TOKEN: {'✓ 已设置' if github_token else '✗ 未设置'}")
    print(f"  NOTIFICATION_REPO: {'✓ 已设置' if notification_repo else '✗ 未设置'}")
    
    # 检查SMTP配置
    smtp_server = os.environ.get('SMTP_SERVER', '')
    smtp_email = os.environ.get('SMTP_EMAIL', '')
    smtp_password = os.environ.get('SMTP_PASSWORD', '')
    
    print("\n直接SMTP配置:")
    print(f"  SMTP_SERVER: {'✓ 已设置' if smtp_server else '✗ 未设置'}")
    print(f"  SMTP_EMAIL: {'✓ 已设置' if smtp_email else '✗ 未设置'}")
    print(f"  SMTP_PASSWORD: {'✓ 已设置' if smtp_password else '✗ 未设置'}")
    print(f"  SMTP_SSL: {os.environ.get('SMTP_SSL', 'true')}")
    print(f"  SMTP_NAME: {os.environ.get('SMTP_NAME', 'JM漫画下载服务')}")
    
    # 判断可用的发送方式
    print("\n可用的发送方式:")
    if github_token and notification_repo:
        print("  ✓ notification-service方式")
    else:
        print("  ✗ notification-service方式（配置不完整）")
    
    if smtp_server and smtp_email and smtp_password:
        print("  ✓ 直接SMTP方式")
    else:
        print("  ✗ 直接SMTP方式（配置不完整）")
    
    print()

def gmail_setup_guide():
    """Gmail设置指南"""
    print("=== Gmail邮箱设置指南 ===")
    print()
    print("1. 开启两步验证:")
    print("   - 访问 https://myaccount.google.com/security")
    print("   - 开启「两步验证」")
    print()
    print("2. 生成应用专用密码:")
    print("   - 在两步验证页面，找到「应用专用密码」")
    print("   - 选择「邮件」和「其他设备」")
    print("   - 生成16位密码，用作SMTP_PASSWORD")
    print()
    print("3. 配置参数:")
    print("   SMTP_SERVER=smtp.gmail.com")
    print("   SMTP_SSL=true")
    print("   SMTP_EMAIL=your_email@gmail.com")
    print("   SMTP_PASSWORD=your_16_digit_app_password")
    print()

def qq_setup_guide():
    """QQ邮箱设置指南"""
    print("=== QQ邮箱设置指南 ===")
    print()
    print("1. 开启SMTP服务:")
    print("   - 登录QQ邮箱网页版")
    print("   - 设置 → 账户 → POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务")
    print("   - 开启「SMTP服务」")
    print()
    print("2. 获取授权码:")
    print("   - 点击「生成授权码」")
    print("   - 按提示发送短信")
    print("   - 获得16位授权码，用作SMTP_PASSWORD")
    print()
    print("3. 配置参数:")
    print("   SMTP_SERVER=smtp.qq.com")
    print("   SMTP_SSL=true")
    print("   SMTP_EMAIL=your_email@qq.com")
    print("   SMTP_PASSWORD=your_16_digit_authorization_code")
    print()

def run_test():
    """运行测试"""
    print("=== 运行邮件功能测试 ===")
    print()
    print("执行以下命令来测试邮件功能:")
    print("python test_email_notification.py")
    print()
    print("如果测试成功，您就可以在GitHub Actions中使用邮件通知功能了。")
    print()

def github_actions_usage():
    """GitHub Actions使用说明"""
    print("=== GitHub Actions使用说明 ===")
    print()
    print("1. 配置Secrets:")
    print("   - 进入GitHub仓库页面")
    print("   - Settings → Secrets and variables → Actions")
    print("   - 添加必要的secrets（参考上面的配置示例）")
    print()
    print("2. 运行工作流:")
    print("   - 进入Actions页面")
    print("   - 选择「下载JM本子并发送邮件 (dispatch)」")
    print("   - 点击「Run workflow」")
    print("   - 填入JM_ALBUM_IDS和其他参数")
    print("   - 点击「Run workflow」开始执行")
    print()
    print("3. 查看结果:")
    print("   - 在Actions页面查看运行日志")
    print("   - 检查邮箱是否收到附件邮件")
    print("   - 下载的文件也会上传到GitHub Artifacts")
    print()

def troubleshooting():
    """故障排除"""
    print("=== 常见问题排除 ===")
    print()
    print("1. 邮件发送失败:")
    print("   - 检查SMTP服务器地址是否正确")
    print("   - 确认邮箱用户名和密码/授权码是否正确")
    print("   - 验证是否开启了SMTP服务")
    print("   - 检查网络连接是否正常")
    print()
    print("2. 附件过大:")
    print("   - 系统会自动分割超过20MB的文件")
    print("   - 如果仍然失败，可能是邮件服务商限制")
    print("   - 建议使用支持大附件的邮件服务")
    print()
    print("3. GitHub Token权限不足:")
    print("   - 确保Token有repo权限")
    print("   - 检查NOTIFICATION_REPO格式是否正确（username/repo）")
    print()
    print("4. 调试方法:")
    print("   - 先运行本地测试脚本")
    print("   - 查看GitHub Actions详细日志")
    print("   - 检查邮箱垃圾邮件文件夹")
    print()

def main():
    """主函数"""
    print("JM漫画下载邮件通知使用指南")
    print("=" * 60)
    print()
    
    while True:
        print("请选择操作:")
        print("1. 查看环境变量配置示例")
        print("2. 检查当前配置")
        print("3. Gmail邮箱设置指南")
        print("4. QQ邮箱设置指南")
        print("5. 运行邮件功能测试")
        print("6. GitHub Actions使用说明")
        print("7. 常见问题排除")
        print("0. 退出")
        print()
        
        try:
            choice = input("请输入选项 (0-7): ").strip()
            print()
            
            if choice == '0':
                print("再见！")
                break
            elif choice == '1':
                setup_environment_variables()
            elif choice == '2':
                check_current_config()
            elif choice == '3':
                gmail_setup_guide()
            elif choice == '4':
                qq_setup_guide()
            elif choice == '5':
                run_test()
            elif choice == '6':
                github_actions_usage()
            elif choice == '7':
                troubleshooting()
            else:
                print("无效选项，请重新选择。")
            
            print()
            input("按回车键继续...")
            print()
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"发生错误: {e}")
            print()

if __name__ == "__main__":
    main()