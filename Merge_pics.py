import cv2
import numpy as np
import glob
import os

if not os.path.exists('./origin/'):
    os.mkdir('./origin/')
picture_path = './origin/*'
pic_list = glob.glob(picture_path) #用glob方法获取要合并的图片的集合

if pic_list:
    pic_list.sort(key=lambda x: int(x[9:-4])) #sort方法用来排序，因为本来会1,10,2,3这样排，x[9:-4]的意思是从第九个字符开始到倒数第四个字符结束，中间作为对比条件
    output = cv2.imread(pic_list.pop(0)) #pop方法返回第一张图片的地址，接着用imread方法获取
    print(output.shape)
    # index = 0
    # print(pic_list)

    for path in pic_list: #pic_list集合已经排除掉首张图片地址，避免重复合并
        # index += 1
        # base = osp.splitext(osp.basename(path))[0]
        # print(index, base)

        input = cv2.imread(path, cv2.IMREAD_COLOR) #imread方法循环获取剩下的图
        try:
            #横向：使用numpy的concatenate
            # output = np.concatenate((output,input),axis=0)
            #纵向：使用numpy的vstack
            output = np.vstack((output,input))
        except ValueError as identifier:
            print('错误是：',identifier) # 一般出错有可能是因为拼接的图片出现宽度不相同
            if output.shape[1] != input.shpae[1]:
                input = cv2.resize(input,(int(output.shape[1]),int(input.shape[0]*(output.shape[1]/input.shape[1]))),interpolation=cv2.INTER_CUBIC) #如果是宽度不同就等比例改变宽度
                output = np.vstack((output,input))
                print('更改后的：',input.shape)
            else:
                output = np.row_stack((output,input)) #还有一种情况就是通道不同，不是3通道的合并会出错，就进行单通道合并，我也不懂
    print(output.shape)
    cv2.imwrite('Merge.jpg',output) #保存合并好的图