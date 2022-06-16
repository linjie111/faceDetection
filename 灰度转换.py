#导入cv 模块
import cv2 as cv

#读取图片
img = cv.imread('img.png')

#显示图片
cv.imshow('read_img',img)

#等待  0 无线等待， 具体数字，在具体数字达到后关闭
cv.waitKey(0)

#保持一个好的习惯，用完之后释放内存
cv.destroyAllWindows()



