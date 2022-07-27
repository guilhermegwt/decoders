cod_msg = input("Message to encode/decode:\n")
msgspl = list(cod_msg)
alph_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alph_lower = [x.lower() for x in alph_upper]
lst = []
dec_msg = ""

for l in msgspl:
    if l in alph_upper or l in alph_lower:
        if l.isupper() == True:
            lttindex = alph_upper.index(l)
            lttrot13 = lttindex - 13
            lst.append(alph_upper[lttrot13])
        elif l.isupper() == False:
            lttindex = alph_lower.index(l)
            lttrot13 = lttindex - 13
            lst.append(alph_lower[lttrot13])
    else:
        lst.append(l)

dec_msg = "".join(lst)

print(dec_msg)
