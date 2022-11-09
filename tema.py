dict1={'disciplina':"L.Rom",'note':[8,8,4,4,4],'teza':6}
dict2={'disciplina':"Matematica",'note':[8,9,9,7,10,10,10],'teza':9}
dict3={'disciplina':"Limba Engleza",'note':[10,10,10,9],'teza':9}
def notaMedie(dictionar):
    media=sum(dictionar['note'])/len(dictionar['note'])
    return round((media+dictionar['teza'])/2,2)
media1=notaMedie(dict1)
media2=notaMedie(dict2)
media3=notaMedie(dict3)
print("Media la",dict1['disciplina'],"este:",media1)
print("Media la",dict2['disciplina'],"este:",media2)
print("Media la",dict3['disciplina'],"este:",media3)

lista_notelor=[media1,media2,media3]
lista_notelor_teza=[dict1['teza'],dict2['teza'],dict3['teza']]
lista_notelor_medii_fara_teza=[sum(dict1['note'])/len(dict1['note']),sum(dict2['note'])/len(dict2['note']),sum(dict3['note'])/len(dict3['note'])]
for nota in lista_notelor_teza:
    if nota <5:
        print("Restantier")
        exit()
for nota in lista_notelor_medii_fara_teza:
    if nota <5:
        print("Repetent")
        exit()

mediaTotala=sum(lista_notelor)/3
min=10
for nota in lista_notelor:
    if(nota<min):
        min=nota
if(min>=9 and mediaTotala>=9):
    print("Elev eminent")
elif(min>=8 and mediaTotala>=8):
    print("Elev proeminent")
elif(min>=5):
    print("Elev codas")
else:
    print("Elev repetent")
    

