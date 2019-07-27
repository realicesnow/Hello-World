def disp( lines ):
    for idx, val in enumerate(lines):
        print("{0:<3}{1}".format(idx, val), end="")