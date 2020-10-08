from time import *

print("30초 세보세요.")
start = time()
input("**************\n"
      "마음속으로 30초 센 후 엔터를 누르세요.\n"
      "**************")
print("{}초 지났습니다.".format(round(time() - start, 2)))