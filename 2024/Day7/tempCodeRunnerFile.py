for o in op:
        s = p[0]
        for i in range(len(o)):
            if o[i] == "+":
                s += vals[i+1]
            else:
                s *= vals[i+1]

        if s == eq:
            return True