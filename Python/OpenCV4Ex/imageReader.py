# import cv2
#
# imageFile = './data/lena.jpg'
#
# img = cv2.imread(imageFile)
#
# img2 = cv2.imread(imageFile, 0)
#
# cv2.imwrite('./data/TestLena.bmp', img)
#
# cv2.imwrite('./data/TestLena.png', img2)
#
# cv2.imwrite('./data/TestLena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
#
# cv2.imwrite('./data/TestLena2.jpg', img2, [cv2.IMWRITE_JPEG_QUALITY, 40])
#
# cv2.imshow('Lena color', img)
#
# cv2.imshow('Lena grayscale', img2)
#
# cv2.waitKey()
# cv2.destroyAllWindows()


import cv2
from matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgBGR = cv2.imread(imageFile) # cv2.IMREAD_COLOR
plt.axis('off')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB) # plot에 imgRGB를 그리고
plt.show( ) # plot에 그린 내용을 출력한다.




