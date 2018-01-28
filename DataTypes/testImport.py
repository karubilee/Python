from PIL import ImageFilter,Image
import requests
r = requests.get('https://www.baidu.com')
print(r.status_code)





im = Image.open('soee.png')
w,h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放50%
# im.thumbnail((w//2, h//2))
# im.save('thumbnail.jpg', 'jpeg')


im = Image.open('soee.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png', 'png')
