with open("input.txt") as f: 
    Input = f.read()

num = ['one','two','three','four','five','six','seven','eight','nine']

mylist = Input.split('\n')
sum = 0
for i,v in enumerate(mylist):
    first = ""
    last = ""
    fidx = 100;
    lidx = -1;
    for i,char in enumerate(v):
        for idx,n in enumerate(num):
            midx = v.find(n,i)
            if midx == -1: continue 
            if midx <fidx:
                fidx = midx
                first = str(idx+1)
            if midx >lidx:
                lidx = midx
                last = str(idx+1)
        try:
            int(char)
        except: 
            continue  
        if i <fidx:
            fidx = i
            first = char
        if i >lidx:
            lidx = i
            last = char
                
    sum += int(first+last)
    print(first,last)
print(sum)