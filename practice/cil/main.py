from practice.cil import utils
from practice.cil.utils import display
from practice.cil.processing import invert as inv, merge as mrg

img1 = utils.read_image('img1')
img2 = utils.read_image('img2')
logo = utils.read_image('codeit_logo')

inverted_img1 = utils.invert(img1)
inverted_img2 = utils.invert(img2)
inverted_logo = inv(logo)
merged_img = mrg(logo, inverted_logo)

print('원본 이미지')
print('\nimage1:')
display(img1)
print('\nimage2:')
display(img2)

print('\n색상 반전된 이미지')
print('\nimage1:')
display(inverted_img1)
print('\nimage2:')
display(inverted_img2)

print('원본 이미지:')
display(logo)
print('\n색상 반전 이미지:')
display(inverted_logo)
print('\n합성 이미지:')
display(merged_img)

# 채점 코드
print()
print('cil' in dir())
print('display' in dir())