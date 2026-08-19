
def pozzo_universale(i,g):
    if len(g[i]!=0):
        return False
    else:
        for x in range(1,len(g)+1):
            if g[x]



def main():
    # 6 è sicuramente un pozzo e un pozzo universale
    g = {
        1 : [6],
        2 : [6],
        3 : [6],
        4 : [6],
        5 : [6],
        6 : []
    }
    print(g)
    pozzo_universale(6,g)