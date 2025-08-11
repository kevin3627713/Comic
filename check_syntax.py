#!/usr/bin/env python3
"""
检查 Python 文件语法
"""

import ast
import sys

def check_syntax(filename):
    """检查文件语法"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        ast.parse(source)
        print(f"✓ {filename} syntax is valid")
        return True
        
    except SyntaxError as e:
        print(f"✗ Syntax error in {filename}:")
        print(f"  Line {e.lineno}: {e.text}")
        print(f"  {' ' * (e.offset - 1)}^")
        print(f"  {e.msg}")
        return False
    except Exception as e:
        print(f"✗ Error checking {filename}: {e}")
        return False

if __name__ == '__main__':
    files_to_check = [
        'src/jmcomic/jm_plugin.py',
        'assets/option/option_workflow_download.yml',
        'assets/option/option_workflow_download_with_pdf.yml',
        '.github/workflows/download_dispatch.yml'
    ]
    
    all_good = True
    for filename in files_to_check:
        if filename.endswith('.py'):
            if not check_syntax(filename):
                all_good = False
        else:
            print(f"⚠ Skipping non-Python file: {filename}")
    
    sys.exit(0 if all_good else 1)