import pwn

pwn_activate = pwn.remote("94.237.49.212", "54725")

my_flag= ""
char = 0

while True:
    print("loading...")
    pwn_activate.sendlineafter("index:", str(char))
    pwn_activate.recvuntil(": ")
    # if pwn_activate.recvline().strip().decode("utf-8") == 'Index out of range!':
    #     stop = 'Index out of range!'
    char+=1
    curr_char = pwn_activate.recvline().strip().decode("utf-8")
    my_flag += curr_char
    if curr_char == "}":
        print("so i'm gonna go...")
        break
        

print(my_flag)