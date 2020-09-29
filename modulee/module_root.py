import sys

print(sys.path)  # 모듈을 찾는 경로들의 리스트를 출력
"""
['C:\\Users\\user\\PycharmProjects\\study_Python\\modulee', 
'C:\\Users\\user\\PycharmProjects\\study_Python', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32', 
'C:\\Users\\user\\PycharmProjects\\study_Python\\venv', 
'C:\\Users\\user\\PycharmProjects\\study_Python\\venv\\lib\\site-packages']
"""
# 현재 파일과 상위 파일을 찾고 내부 함수, 외부 함수 순으로 찾음 (site-packages: 외부함수 저장)

sys.path.append('C:\\Users\\user\\Desktop')
# 리스트에 경로를 추가해 기존 경로 밖에 있는 모듈을 찾을 수 있음

print(sys.path)