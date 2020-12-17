while True:  # Infinite Loop Breaks with Ctrl+C
    num = int(input("Enter an Integer : "))
    if num < 0:
        print("Negative")
    elif num == 0:
        print("Zero")
    elif num > 0 and num < 10:
        print("Marginally Positive")
    else:
        print("Hugely Positive")
