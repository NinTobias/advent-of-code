def get_code(sample):
    start = [0, 1]
    const = start
    for char in sample:
        if char == "L":
            check = [start[0]-1,start[1]]
            if check not in [[0,2], [-1,1], [0,1], [1,1], [-2,0], [-1,0], [0,0], [1,0], [2,0], [-1,-1], [0,-1], [1,-1], [0,-2]]:
                pass
            else:
                start = [start[0]-1,start[1]]

        elif char == "R":
            check = [start[0]+1,start[1]]
            if check not in [[0,2], [-1,1], [0,1], [1,1], [-2,0], [-1,0], [0,0], [1,0], [2,0], [-1,-1], [0,-1], [1,-1], [0,-2]]:
                pass
            else:
                start = [start[0]+1,start[1]]
            
        elif char == "D":
            check = [start[0],start[1]-1]
            if check not in [[0,2], [-1,1], [0,1], [1,1], [-2,0], [-1,0], [0,0], [1,0], [2,0], [-1,-1], [0,-1], [1,-1], [0,-2]]:
                pass
            else:
                start = [start[0],start[1]-1]

        elif char == "U":
            check = [start[0],start[1]+1]
            if check not in [[0,2], [-1,1], [0,1], [1,1], [-2,0], [-1,0], [0,0], [1,0], [2,0], [-1,-1], [0,-1], [1,-1], [0,-2]]:
                pass
            else:
                start = [start[0],start[1]+1]
    print("const:", const, "start:", start)

get_code("RUDLLUDRRDRRLRURRULRLRDUDLRRLRDDUDRDLRRLLRURRDDLRLLRRURULRUULDUDUULDULDLRLRDLRDLRUURLDRLUDRRDDDRDRRRDDLLLRRLULLRRDDUDULRDRDUURLDLRULULUDLLDRUDUURRUDLLRDRLRRUUUDLDUDRRULLDURRDUDDLRURDLDRLULDDURRLULLRDDDRLURLULDLRUDLURDURRUDULDUUDLLLDDDUUURRRDLLDURRDLULRULULLRDURULLURDRLLRUUDDRRUDRDRRRURUUDLDDRLDRURULDDLLULULURDLDLDULLRLRDLLUUDDUDUDDDDRURLUDUDDDRRUDDLUDULLRDLDLURDDUURDLRLUUDRRULLRDLDDDLDULDUDRDUUULULDULUDLULRLRUULLDURLDULDRDLLDULLLULRLRD")


