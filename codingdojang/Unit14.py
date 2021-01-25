korean, english, math, science = map(int,input().split())
if (korean>=0 and korean<=100) and (english>=0 and english<=100) and (math>=0 and math<=100) and (science>=0 and science<=100):
    if (korean+english+math+science)/4 >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")
