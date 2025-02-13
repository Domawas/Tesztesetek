import fuggvenyek  

def sorta_sum_teszt():
    print("1. teszteset")
    a:int = 3
    b:int = 5
    vart:int = 8
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

    print("2. teszteset")
    a:int = 7
    b:int = 8
    vart:int = 20
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

    print("3. teszteset")
    a:int = 10
    b:int = 10
    vart:int = 20
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

    print("4. teszteset")
    a:int = 0
    b:int = 9
    vart:int = 9
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

    print("5. teszteset")
    a:int = 15
    b:int = 5
    vart:int = 20
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

    print("6. teszteset")
    a:int = -5
    b:int = 15
    vart:int = 20
    kapott:int = fuggvenyek.sorta_sum(a, b)
    print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")

def sorta_sum_teszt2():
    a_lista = [3, 7, 10, 0, 15, -5]
    b_lista = [5, 8, 10, 9, 5, 15]
    vart_lista = [8, 20, 20, 9, 20, 20]

    for i in range(0, len(a_lista), 1):
        print(f"{i+1}. teszteset")
        a:int = a_lista[i]
        b:int = b_lista[i]
        vart:int = vart_lista[i]
        kapott:int = fuggvenyek.sorta_sum(a, b)
        print(f"a: {a} | b: {b} | várt: {vart} | kapott: {kapott} | eredmény: {vart == kapott}")


sorta_sum_teszt2()
