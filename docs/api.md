# API 文档

(api-reference)=
## API 参考

```{image} _static/example.png
:alt: 示例图片
:width: 400px
:align: center
```

这里是项目的API文档。您可以在这里详细描述：

- 模块接口
- 函数说明
- 类定义
- 方法说明

### 示例API

```python
def example_function(param1: str, param2: int = 0) -> bool:
    """示例函数
    
    Args:
        param1 (str): 第一个参数说明
        param2 (int, optional): 第二个参数说明. 默认值为 0
        
    Returns:
        bool: 返回值说明
    """
    return True
```

## 使用示例

您可以这样使用上述API：

```python
result = example_function("test", 42)
print(result)  # 输出: True
```

```{note}
更多API文档正在完善中...
``` 