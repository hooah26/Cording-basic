import re

p = re.compile("06.5")
# p = re.compile("^menu")
# p = re.compile("06$")
# m = p.match("cafe")
# search는 문자열내 모두 비교를 하지만 첫번째 해당 검색 매칭에서 있으면 하나만 값리턴.   match는 첫번째 글자부터 맞아야한다.
m = p.search("class menu 0695 z0615  k06115")

if m:
    print("매칭성공")
    print(m.span())
    print(m.group())
else:
    print("매칭실패") 