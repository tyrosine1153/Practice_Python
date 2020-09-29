# pip : 패키지 설치
# https://pypi.org/ 에서 원하는 라이브러리 주소를 복사해 터미널에 붙여넣기를 한다
# pip install beautifulsoup4
"""  # 설치한 라이브러리의 예제
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
"""
# 터미널에 pip list 를 쓰면 현재 다운받은 라이브러리들을 볼 수 있다
# pip show 라이브러리 이름 : 그 라이브러리의 정보를 보여줌
# pip install --upgrade-- 라이브러리 이름 : 라이브러리 업데이트
# pip uninstall 라이브러리 이름 : 라이브러리 삭제