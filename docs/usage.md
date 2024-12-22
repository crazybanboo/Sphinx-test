# 使用指南

这是一个Markdown格式的文档示例。

(basic-usage)=
## 基本用法

您可以使用常见的Markdown语法：

- 列表项1
- 列表项2
- 列表项3

### 代码示例 
```python
print("Hello, World!")
```

## 文档引用示例

### 基本引用
- 引用介绍文档：{ref}`介绍`
- 引用带自定义文本：{ref}`点击查看介绍 <介绍>`

### 文件引用
- [查看介绍文档](intro.rst)
- [使用指南](usage.md)

### 章节引用
您还可以使用标题ID来引用特定章节：
{ref}`basic-usage`

```{note}
MyST-Parser支持多种引用语法，上面展示的是最常用的几种。
```
