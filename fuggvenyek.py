def cigar_party(cigars, is_weekend):
    if is_weekend:
        
        return cigars >= 40
    else:
        
        return 40 <= cigars <= 60

def sorta_sum(a,b):
    osszeadas=a+b
    if 10<= osszeadas <=19:
        return 20
    else:
        return osszeadas