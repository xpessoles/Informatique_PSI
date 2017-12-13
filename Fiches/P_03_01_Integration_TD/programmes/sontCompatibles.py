def sontCompatibles(r1,r2):
    for i in range(len(r1)):
        if r1[i]=='1' and r2[i]=='1':
            return(False)
    return(True)