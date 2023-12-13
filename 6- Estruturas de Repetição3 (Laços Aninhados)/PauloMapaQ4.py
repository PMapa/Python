mNacional=float(input('Meta nacional: R$ '))
vendasT=0
e=1

while vendasT<mNacional:
    estado=str(input(f'. Nome do estado {e}: '))
    mEstadual=float(input('. Meta estadual: R$ '))
    c=1
    vendasE=0
    
    while vendasE<mEstadual:
        venda=float(input(f'.. Vendas na cidade {c}: R$ '))
        vendasE+=venda
        c+=1
        
    print(f".. Meta no estado {estado} atingida, valor total: R$ {vendasE:.02f}.")
    vendasT+=vendasE
    e+=1
    
print(f"Meta nacional cumprida, valor total: R$ {vendasT:.02f}.")