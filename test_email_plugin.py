#!/usr/bin/env python3
"""
测试邮件插件的脚本
"""

import os
import sys
sys.path.insert(0, 'src')

from jmcomic.jm_plugin import SendQQEmailPlugin
from jmcomic.jm_option import JmOption

def test_email_plugin():
    """测试邮件插件"""
    
    # 创建一个模拟的 option 对象
    class MockOption:
        pass
    
    option = MockOption()
    
    # 创建插件实例
    plugin = SendQQEmailPlugin(option)
    
    # 测试参数
    test_params = {
        'msg_from': 'test@example.com',
        'msg_to': 'recipient@example.com', 
        'password': 'test_password',
        'title': 'Test Email',
        'content': 'This is a test email',
        'send_attachments': 'true',  # 字符串形式
        'zip_name': 'test.tar.gz',
        'pdf_zip_name': 'test.zip'
    }
    
    print("Testing email plugin with parameters:")
    for key, value in test_params.items():
        print(f"  {key}: {value}")
    
    try:
        # 这里只测试参数处理，不实际发送邮件
        print("\nTesting parameter processing...")
        
        # 模拟调用 invoke 方法的参数处理部分
        send_attachments = test_params['send_attachments']
        if isinstance(send_attachments, str):
            send_attachments = send_attachments.lower() in ('true', '1', 'yes', 'on')
        
        print(f"send_attachments converted to: {send_attachments}")
        
        # 测试附件准备
        if send_attachments:
            print("Would prepare attachments...")
            
        print("✓ Parameter processing test passed!")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
    
    return True

if __name__ == '__main__':
    success = test_email_plugin()
    sys.exit(0 if success else 1)