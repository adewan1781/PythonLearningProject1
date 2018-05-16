from com.inheritance1.MultiDerived import MultiDerived


def main():
    obj = MultiDerived("aaa")
    obj.pm()                        # method from second sub-child


if __name__ == '__main__':
    main()
