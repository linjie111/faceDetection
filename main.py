#导入cv 模块
import cv2 as cv

#读取图片
img = cv.imread('img.png')

# 灰度处理

gray_img  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 显示灰度
cv.imshow('gray',gray_img)

# 保存灰度图片
cv.imwrite('gray_youban.png',gray_img)

#显示图片
cv.imshow('read_img',img)

#等待  0 无线等待， 具体数字，在具体数字达到后关闭
cv.waitKey(0)

#保持一个好的习惯，用完之后释放内存
cv.destroyAllWindows()

