import numpy as np
from keras.utils import to_categorical

# 示例类别标签
labels = [0, 1, 2, 3]

# 转换为 one-hot 编码
one_hot_labels = to_categorical(labels, num_classes=4)

print("原始标签:", labels)
print("One-hot 编码:", one_hot_labels)
