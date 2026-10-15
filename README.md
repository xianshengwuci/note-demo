# 我的第一个笔记小工具

这是一个用 Python 和 Gradio 制作的本地网页小工具。输入一段笔记后，它会显示字符数和原文。

> 这是一个练习项目，不会调用 AI，也不需要 API Key。

## 功能

- 输入笔记文本
- 统计字符数
- 显示原文

字符数由 Python 的 `len()` 计算，空格和换行也会计入。

## 环境要求

- Python 3.13
- Gradio

## 安装 Gradio

Windows 命令提示符中运行：

```text
py -m pip install gradio
