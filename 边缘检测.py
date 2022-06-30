# canny 算法 通过求取 每个像素点周边图像像素变化的梯度，来确定这个点是不是边缘。   如果图像某个像素点的梯度值相差较大，这个点可能是个边缘点，
# 四个方向  左上，上， 右上，右
# 车道线边缘的梯度是非常大的

# 导入cv 模块
import cv2 as cv
import numpy as np

print(cv.__version__)
# 读取图片
img = cv.imread('lane.png')

# 显示图片
imshow = cv.imshow('read_img', img)
# 灰度处理
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edge_imge = cv.Canny(gray_img, 100, 150)

# 绘制多边形
pts = np.array([[0, 715], [1200, 715], [700, 380], [500, 380]])

cv.polylines(img, [pts], True, (255, 0, 0), 3)

# 显示图像
cv.imshow("ellipse", img)

# 获取一个和 原图一样大小的全黑的图像
mask = np.zeros_like(edge_imge)
print(mask.shape)
#  感兴趣的四个顶点的像素值  形成一个梯形的掩码
cv.fillPoly(mask, np.array([[[0, 715], [1200, 715], [700, 380], [500, 380]]]), color=255)
# 掩码操作
masked_img = cv.bitwise_and(edge_imge, mask)

cv.imshow('masked', masked_img)

cv.imshow('edge', edge_imge)

# 等待  0 无线等待， 具体数字，在具体数字达到后关闭
cv.waitKey(0)

# 保持一个好的习惯，用完之后释放内存
cv.destroyAllWindows()
