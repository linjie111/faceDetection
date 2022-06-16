#导入cv 模块
import cv2 as cv

#读取图片
img = cv.imread('img.png')

#建立一个检测函数
def face_detect_demo():
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #调用opencv 中自带的人家已经训练好的分类器
    face_detect = cv.CascadeClassifier('C:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

    # 参数详解  图像，每次遍历后的缩放倍数，检测几次确定都有人脸才能确定，
    face = face_detect.detectMultiScale(gray,1.01,5,0,(300,300),)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=3)
    cv.imshow('result',img)
#显示图片
cv.imshow('read_img',img)
face_detect_demo()
#等待  0 无线等待， 具体数字，在具体数字达到后关闭

#等待键盘
while True:
    if ord(' ')== cv.waitKey(0):
        break
#cv.waitKey(0)


#保持一个好的习惯，用完之后释放内存
cv.destroyAllWindows()



