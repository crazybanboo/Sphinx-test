# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# 项目信息
project = '我的项目文档'
copyright = '2024, Your Name'
author = 'Your Name'
release = '1.0.0'

# 基本配置
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser'
]

# 语言设置
language = 'zh_CN'

# HTML输出配置
html_theme = 'sphinx_rtd_theme'

# Markdown支持配置
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
