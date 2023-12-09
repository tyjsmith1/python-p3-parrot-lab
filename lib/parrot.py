def parrot(command=None):
    default = "Squawk!"
    if command is None:
        print(default)
        return default
    else:
        print(command)
        return command
