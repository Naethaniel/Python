def sun_angle(time):
    split = time.split(':')
    mins = int(split[0]) * 60 + int(split[1])

    #under 06:00 or over 18:00
    if mins < 360 or mins > 1080:
        return 'I don\'t see the sun!'
    return mins * 0.25 - 90

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert sun_angle("07:00") == 15
    # assert sun_angle("01:23") == "I don't see the sun!"
    # # print("Coding complete? Click 'Check' to earn cool rewards!")