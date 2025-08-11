#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JMComic 漫画下载脚本
功能：下载完整本后转为PDF，保存到指定目录
"""

import jmcomic

def download_manga(album_id):
    """
    下载指定ID的漫画本子
    
    Args:
        album_id: 本子ID，例如 '422866'
    """
    try:
        # 创建配置对象
        option = jmcomic.create_option_by_file('option.yml')
        
        print(f"开始下载本子 {album_id}...")
        print("配置信息：")
        print("- 客户端：移动端API")
        print("- 下载路径：D:/文档/DOWNLOADS/漫画/")
        print("- PDF输出：D:/文档/DOWNLOADS/漫画/PDF/")
        print("- 自动转换为PDF")
        print("-" * 50)
        
        # 使用配置下载本子
        jmcomic.download_album(album_id, option)
        
        print(f"本子 {album_id} 下载完成！")
        print("图片已保存到：D:/文档/DOWNLOADS/漫画/")
        print("PDF已生成到：D:/文档/DOWNLOADS/漫画/PDF/")
        
    except Exception as e:
        print(f"下载失败：{e}")
        print("请检查：")
        print("1. 网络连接是否正常")
        print("2. 本子ID是否正确")
        print("3. 是否已安装 img2pdf 依赖：pip install img2pdf")

if __name__ == "__main__":
    # 示例：下载本子291605
    # 你可以修改这个ID为你想要下载的本子ID
    album_id = "291605"
    
    # 如果你想下载多个本子，可以使用循环
    # album_ids = ["422866", "123456", "789012"]
    # for album_id in album_ids:
    #     download_manga(album_id)
    
    download_manga(album_id)