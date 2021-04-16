import os
# 1.基本路径
base_path = os.path.dirname(__file__)

# 2.主机地址
host = "http://127.0.0.1:8000"

# 3.excel数据对应列
cell_config = {
    "path": 5,
    "method": 6,
    "headers": 7,
    "param_type": 8,
    "params": 9,
    "expect": 10,
    "is_run": 11,
    "result": 12,
    "desc": 13
}
