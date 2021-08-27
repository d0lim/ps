# 일단 태그로 싸여진 놈들을 인식해야 함
# 솔직히 DFA 마렵긴 한데


s = input()


splitted = []
temp = {"isTag": False, "value": ""}
length = len(s)
# 일단, 태그와 가운데의 문자열을 분리해서 리스트 안에 저장한다
for i, c in enumerate(s):
    # 태그 시작
    if c == "<":
        # 일단 앞에 담아뒀던 애들이 있는지 확인
        if len(temp["value"]) != 0:
            # 담아뒀던 애들 있으면 먼저 담아주기
            splitted.append(temp)
            temp = {"isTag": False, "value": ""}
        temp["isTag"] = True
        temp["value"] = "<"
    # 태그 종료
    elif c == ">":
        temp["value"] += ">"
        # 스플릿 배열에 저장
        splitted.append(temp)
        # temp 초기화
        temp = {"isTag": False, "value": ""}
    else:
        temp["value"] += c
        # 만약에 문자열이 끝이라면?
        if i == length - 1:
            # 담아주고 끝
            splitted.append(temp)

result = ""

for item in splitted:
    if item["isTag"] == False:
        val = item["value"]
        rev = []
        for v in val.split():
            rev.append(v[::-1])
        item["value"] = " ".join(rev)

    result += item["value"]

print(result)