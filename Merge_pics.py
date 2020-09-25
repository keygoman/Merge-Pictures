import cv2
import numpy as np
import glob
# import os.path as osp

picture_path = './origin/*'
pic_list = glob.glob(picture_path) #用glob方法获取要合并的图片的集合
output = cv2.imread(pic_list.pop(0)) #pop方法返回第一张图片的地址，接着用imread方法获取
print(output.shape)
# index = 0
# print(pic_list)

for path in pic_list: #pic_list集合已经排除掉首张图片地址，避免重复合并
    # index += 1
    # base = osp.splitext(osp.basename(path))[0]
    # print(index, base)

    input = cv2.imread(path, cv2.IMREAD_COLOR) #imread方法循环获取剩下的图
    #横向：使用numpy的concatenate
    # output = np.concatenate((output,input),axis=0)
    #纵向：使用numpy的vstack
    output = np.vstack((output,input))

print(output.shape)
cv2.imwrite('Merge.jpg',output) #保存合并好的图