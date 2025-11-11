txt = input()
match txt:
    case "one":
        print(1)
    case "two":
        print(2)
    case "three":
        print(3)
    case _:
        print("default")
