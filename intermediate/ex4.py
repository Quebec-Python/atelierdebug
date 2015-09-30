def weird(s):
    print(s)

    for ii in range(len(s)):
        for jj in range(ii, len(s)+1):
            print(ii, jj)

        return

if __name__=="__main__":
   ss="acaacb"
   weird(ss)