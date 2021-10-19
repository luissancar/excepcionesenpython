def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("División por 0")
        return "error"
    except Exception:
        print("Error distion a división por 0")
        return "error"
    finally:
        print("Realizado")


def divide2(n1,n2):
    if n2 == 0:
        raise ZeroDivisionError("Error, división por 0")
    else:
        return n1,n2

print(divide(2,0))
print(divide(2,"ee"))


divide2(4,0)
