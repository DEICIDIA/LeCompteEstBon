objectif = -1
nb = [200,50,20,10,5]
operation = []
nbC = 0
def aux(objectif, plaques, operation):
        global nbC
        nbC = nbC + 1
        if len(plaques) <= 1:
            return False
        for i in range(0,len(plaques)-1):
            for j in range(i+1,len(plaques)):
                 nb1 = plaques[i]
                 nb2 = plaques[j]
                 plaques.pop(i)
                 plaques.pop(j-1)
                 if nb1 + nb2 == objectif:
                     operation.append(str(nb1)+"+"+str(nb2))
                     return True
                 else:
                    tmp = nb1 + nb2
                    plaques.insert(0,tmp)
                    if aux(objectif,plaques,operation) == True:
                        operation.insert(0,str(nb1) + "+" + str(nb2))
                        return True
                    else:
                        plaques.pop(0)
                 if nb1 * nb2 == objectif:
                     operation.append(str(nb1) + "*" + str(nb2))
                     return True
                 else:
                     tmp = nb1 * nb2
                     plaques.insert(0, tmp)
                     if aux(objectif, plaques, operation) == True:
                         operation.insert(0, str(nb1) + "*" + str(nb2))
                         return True
                     else:
                         plaques.pop(0)
                 if nb1 < nb2:
                     tmp = nb2 - nb1
                     plaques.insert(0, tmp)
                     if tmp == objectif:
                        operation.append(str(nb1) + "-" + str(nb2))
                        return True
                     if aux(objectif, plaques, operation) == True:
                        operation.insert(0, str(nb1) + "-" + str(nb2))
                        return True
                     else:
                        plaques.pop(0)
                 if nb1 > nb2:
                    tmp = nb1 - nb2
                    plaques.insert(0, tmp)
                    if tmp == objectif:
                        operation.append(str(nb1) + "-" + str(nb2))
                        return True
                    if aux(objectif, plaques, operation) == True:
                        operation.insert(0, str(nb1) + "-" + str(nb2))
                        return True
                    else:
                        plaques.pop(0)
                 if (nb1 > nb2) & (nb2 != 0) & (nb1 % nb2 == 0):
                    tmp = nb1 / nb2
                    plaques.insert(0, tmp)
                    if tmp == objectif:
                        operation.append(str(nb1) + "/" + str(nb2))
                        return True
                    else:
                        if aux(objectif, plaques, operation) == True:
                            operation.insert(0, str(nb1) + "-" + str(nb2))
                            return True
                        else:
                            plaques.pop(0)
                 if (nb1 < nb2) & (nb1 != 0) & (nb2 % nb1 == 0):
                    tmp = nb2 / nb1
                    plaques.insert(0, tmp)
                    if tmp == objectif:
                        operation.append(str(nb1) + "/" + str(nb2))
                        return True
                    else:
                        if aux(objectif, plaques, operation) == True:
                            operation.insert(0, str(nb1) + "-" + str(nb2))
                            return True
                        else:
                            plaques.pop(0)
                 plaques.insert(i,nb1)
                 plaques.insert(j,nb2)
        return False
if aux(objectif,nb,operation):
    print(operation)
    print("nbC :" ,nbC)
else:
    print("nikoumouk")
    print("nbC :" ,nbC)
