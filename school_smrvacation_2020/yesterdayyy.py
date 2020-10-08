lyrics_f = open(r'Yesterday.txt', 'r')
cnt_Y = cnt_y = 0
while True:
    f_readline = lyrics_f.readline()
    if not f_readline:
        break
    if 'Yesterday' in f_readline:
        cnt_Y += 1
    if 'yesterday' in f_readline:
        cnt_y += 1
print(f"노래 가사 속 Yesterday 수 {cnt_Y}개")
print(f"노래 가사 속 yesterday 수 {cnt_y}개")
lyrics_f.close()
