turtle0 = "ttttuuuurrrrttttlllleeee"
print(turtle0)
#ПЕРВЫЙ СПОСОБ!
t = turtle0[1]
u = turtle0[5]
r = turtle0[10]
l = turtle0[16]
e = turtle0[-1]
print(f"{t}{u}{r}{t}{l}{e}")
#ВТОРОЙ СПОСОБ!
turtle2 = "" + turtle0[0] + turtle0[5] + turtle0[10] + turtle0[0] + turtle0[16] + turtle0[-1]
print(turtle2)
#ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ!
num = 2+2
print(num==4)