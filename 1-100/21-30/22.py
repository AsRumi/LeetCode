cell = [1, 0, 0, 0, 0, 1, 0, 0]
temp = cell.copy()

i = 0
days = len(temp)
while(i<days):
    if(i==0):
        cell[i] = temp[i+1]^0
    elif(i==days-1):
        cell[i] = temp[i-1]^0
    else:
        cell[i] = temp[i-1]^temp[i+1]
    i+=1

print(" ".join([str(res) for res in cell]))