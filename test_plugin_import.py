#!/usr/bin/env python3
"""
测试插件导入和参数
"""

import sys
import inspect
sys.path.insert(0, 'src')

try:
    from jmcomic.jm_plugin import SendQQEmailPlugin
    
    # 检查 invoke 方法的签名
    sig = inspect.signature(SendQQEmailPlugin.invoke)
    print("SendQQEmailPlugin.invoke signature:")
    print(f"  {sig}")
    
    # 检查参数
    params = list(sig.parameters.keys())
    print(f"\nParameters: {params}")
    
    # 检查是否有我们添加的参数
    expected_params = ['send_attachments', 'zip_name', 'pdf_zip_name']
    for param in expected_params:
        if param in params:
            print(f"✓ {param} parameter found")
        else:
            print(f"✗ {param} parameter missing")
    
    # 检查是否有 **kwargs
    if any(p.kind == inspect.Parameter.VAR_KEYWORD for p in sig.parameters.values()):
        print("✓ **kwargs found")
    else:
        print("✗ **kwargs missing")
        
    print("\n✓ Plugin import test passed!")
    
except Exception as e:
    print(f"✗ Plugin import test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)