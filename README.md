# Final-year-project

import torch

# 检查系统可用的GPU数量
device_count = torch.cuda.device_count()
print(f"可用GPU数量: {device_count}")

# 遍历所有GPU并打印详细信息
for i in range(device_count):
    print(f"\n---- GPU {i} 信息 ----")
    print(f"设备名称: {torch.cuda.get_device_name(i)}")
    prop = torch.cuda.get_device_properties(i)
    print(f"显存总量: {prop.total_memory / 1024**3:.2f} GB")
    print(f"计算能力: {prop.major}.{prop.minor}")  # CUDA核心版本
    print(f"多处理器数量: {prop.multi_processor_count}")
