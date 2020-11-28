from PIL import Image , ImageFilter

path = "/Users/aelleek/Documents/Programming/Study/Python/OpenCV4Ex/data/lena.jpg"

# im = Image.open(path)
# size = (64,64)
#
# im.thumbnail(size)
#
# print(im.size)
#
# im.show()
#
# outpath = "/Users/aelleek/Documents/Programming/Study/Python/OpenCV4Ex/data/pillow_thumbname_lena.jpg"
#
# im.save(outpath)


## ex2

im = Image.open(path)

img2 = im.resize(800,800)     # ㅅㅏ이즈 변경
# img2 = im.crop((100,100,350,350))     # 이미지 일정부분 잘라내기
# img2 = im.rotate(90)    # 이미지 회전
# img2 = im.filter(ImageFilter.BLUR)  // 이미지 필터.. 뿌얘진다


img2.show()



## ex3
#
# im = Image.open(path)

