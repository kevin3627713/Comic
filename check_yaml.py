#!/usr/bin/env python3
"""
检查 YAML 文件语法
"""

import yaml
import sys

def check_yaml_syntax(filename):
    """检查 YAML 文件语法"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✓ {filename} YAML syntax is valid")
        return True
        
    except yaml.YAMLError as e:
        print(f"✗ YAML error in {filename}:")
        print(f"  {e}")
        return False
    except Exception as e:
        print(f"✗ Error checking {filename}: {e}")
        return False

if __name__ == '__main__':
    yaml_files = [
        'assets/option/option_workflow_download.yml',
        'assets/option/option_workflow_download_with_pdf.yml',
        '.github/workflows/download_dispatch.yml'
    ]
    
    all_good = True
    for filename in yaml_files:
        if not check_yaml_syntax(filename):
            all_good = False
    
    sys.exit(0 if all_good else 1)