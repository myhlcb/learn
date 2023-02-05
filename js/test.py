import imageio
import os
from PIL import Image, ImageSequence
 
print(os.path.abspath('.'),1111)
# 自定义压缩尺寸 rp*rp
rp = 30
 
# 图片缓存空间
image_list = []
 
# 读取gif图片
path = os.path.join(os.path.abspath('.'),'归并.gif')
print(path,222222)
