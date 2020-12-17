def ask_ok(prompt, retries=4, reminder="Please try again!"):
    """
    Input Sample Method, Run outside VSCode on REPL for Input Prompt
    """
    while True:
        ok = input(prompt)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


res = ask_ok("Enter I/p Value : ")
print(res)
