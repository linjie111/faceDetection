#导入cv 模块
import cv2 as cv

#读取图片
img = cv.imread('img.png')
# 坐标
x,y,w,h = 100,100,100,100
#绘制矩形

# 起始点， 宽， 高
cv.rectangle(img,(x,y),(x+50,y+h),color=(0,0,255),thickness=1)
#绘制原型
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)


#显示图片
cv.imshow('read_img',img)

#等待  0 无线等待， 具体数字，在具体数字达到后关闭
cv.waitKey(0)

#保持一个好的习惯，用完之后释放内存
cv.destroyAllWindows()



