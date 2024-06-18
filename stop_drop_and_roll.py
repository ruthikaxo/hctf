import pwn

pwn_activate = pwn.remote("83.136.252.167", 53961)

pwn_activate.sendlineafter("(y/n)", 'y')


pwn_activate.recvlines(1)
    
curr_event = pwn_activate.recvlinesS(1)[0]
event_arr = list(curr_event.split(', '))

while True:
    len_event_arr = len(event_arr)
    # print("Length of array is ->" +str(len_event_arr))

    response = ""
    
    for event in range(len_event_arr):
        if event > 0 and event < len_event_arr:
            response += "-"
        if event_arr[event] == "GORGE":
            response += "STOP"
        if event_arr[event] == "PHREAK":
            response += "DROP"
        if event_arr[event] == "FIRE":
            response += "ROLL"
    
    print("The response is ->", response)
    pwn_activate.sendline(response)

    print("loading...")
    
    pwn_activate.recvuntil('? ')
    
    event_arr = pwn_activate.recvlinesS(1)[0].split(', ')
    print("current event is-> ", event_arr)

    if event_arr[0].count('HTB') > 0:
        print(event_arr[0])
        print("HTB found, exiting...")
        break

    
