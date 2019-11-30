def outer(a):
    def inner(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                print("Not all arguments are string")
                return

        for kwarg in kwargs.values():
            if not isinstance(kwarg, str):
                print("Not all arguments are string")
                return

        else:
            a(*args, **kwargs)
    return inner


@outer
def sayhi(str1, str2, str3):
    print(str1, str2, str3)


@outer
def sayhello(a, b, c):
    print(a, b, c)


@outer
def sayBye(name1, name2):
    print(name1, name2)


sayhi(str1="porsche", str2="yuva", str3="sam")
sayhello(1, "jim", "harry")
sayBye("ben", name2="ten")