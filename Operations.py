import cv2 as cv

# Reading images
img=cv.imread('/home/varad/opencv/Image_processing/Resources/Photos/cat_large.jpg')
cv.imshow('cats',img)
cv.waitKey(0)

# Reading videos
capture=cv.VideoCapture('/home/varad/opencv/Image_processing/Resources/Videos/dog.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
