# 导入json和pandas库
import json
import pandas as pd
from pandas.io.json import json_normalize
# 读取文件并转换为数据框
df = json_normalize('data.json')




df = json_normalize('/staff/wangtiantong/nnU-Net/nnUNet/nnUNetFrame/dataset/nnUNet_preprocessed/Dataset002_Heart/nnUNetPlans.json')
# 将字典转换为数据框
df = pd.DataFrame(df)

# 将数据框转换为markdown格式的表格
md = df.to_markdown()

# 打印表格
print(md)
