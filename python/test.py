arr = []
line = int(input("입력할 줄 갯수 입력: "))
cpu = []
finish = []

for i in range(line):
        num=0
        a = []

        for j in range(1000):
                num = int(input("숫자"))
                if num == -1:
                        break
                elif num != -1:
                        a.append(num)
        arr.append(a)

for r in arr: ## cpu 유휴시간 구하기
        cpu.extend(r[1::2])

for k in arr: ## cpu 유휴시간 구하기
        finish.extend(k[0::])

sum_cpu = sum(cpu)
sum_finish = sum(finish)

print(sum_cpu) 
print(sum_finish)
