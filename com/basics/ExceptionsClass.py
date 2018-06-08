class ExceptionsClass:

    def show(self):
        try:
            name='sunder'
            x=10/0
        except Exception:
            print("exception caused")
        except ArithmeticError:
            print("exception with no name")
        else:
            print("no exception")
        finally:
            print("I will always gets executed")

        raise NameError("This is deliberate")
        print("I will not be printed")


if __name__ == '__main__':
    obj = ExceptionsClass()
    obj.show()
