#중첩 if문 (nested if statement)
#if문 안에 it문이라는 뜻

num = int(input("숫자:"))

if num % 2 == 0:
    if num % 3 == 0:           #만약 여기쯤에서 pass 넣으면 그 코드는 무시
        print("6의 배수입니다.")
    else:
        print("짝수입니다.")
else:
    print("홀수입니다.")



