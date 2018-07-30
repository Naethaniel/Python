s='fasdfvxvzvadadsavvvvv'
currPos = 0
sub = ''
startedAt = 0
flag = 0
answer = s[0]
while True:
    if currPos == len(s)-1:
        if len(answer) < len(sub):
            answer = sub
        break
    if s[currPos] <= s[currPos+1]:
        if flag == 0:
            startedAt = currPos
            sub = s[startedAt]
            flag = 1
        sub += s[currPos+1]
        currPos += 1
    elif s[currPos] > s[currPos+1]:
        if len(answer) < len(sub):
            answer = sub
        sub = ''
        startedAt += 1
        currPos = startedAt
        flag = 0
print('Longest substring in alphabetical order is: ' + answer)
