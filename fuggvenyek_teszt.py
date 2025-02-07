import fuggvenyek
def cigar_party_teszt():
    print("1. teszteset")
    cigars:int=30
    is_weekend:bool=True
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")


    print("2. teszteset")
    cigars:int=40
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")


    print("3. teszteset")
    cigars:int=44,5
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")

    print("4. teszteset")
    cigars:int=60
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")

    print("5. teszteset")
    cigars:int=72
    is_weekend:bool=True
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")


    print("6. teszteset")
    cigars:int=30
    is_weekend:bool=False
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")

    print("7. teszteset")
    cigars:int=40
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")
    
    print("8. teszteset")
    cigars:int=48
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")

    print("9. teszteset")
    cigars:int=60
    is_weekend:bool=False
    vart:bool=True
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")


    print("10. teszteset")
    cigars:int=72
    is_weekend:bool=False
    vart:bool=False
    kapott:bool=fuggvenyek.cigar_party(cigars,is_weekend)
    print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")
   

def cigar_party_teszt2():
    cigars_lista=[30,40,44,60,72,30,40,44,60,72]
    is_weekend_lista=[True,True,True,True,True,False,False,False,False,False]
    vart_lista=[False,True,True,True,True,False,True,True,True,False]

    for i in range(0, len(cigars_lista),1):
        print(f"{i+1}. teszteset")
        cigars:int=cigars_lista[i]
        is_weekend:bool=is_weekend_lista[i]
        vart:bool=vart_lista[i]
        kapott:bool=fuggvenyek.cigar_party(cigars, is_weekend)
        print(f"cigaretta: {cigars} | hétvége: {is_weekend} | várt: {vart} | kapott: {kapott} | eredmény: {vart==kapott}")

cigar_party_teszt2()