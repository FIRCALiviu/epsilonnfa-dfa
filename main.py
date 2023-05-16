import classes
def main():
    filename=input("Please enter filename:\n")
    file = open(filename)

    g=classes.graf(file.readline().strip(),file.readline().split(),file.readline().split())

    lines=file.read().splitlines()
    for line in lines:
        g.add(*line.split())

    
    y=input("Do you want the graphical representation of the dfa? y/n")
    if y=='y' or y=='Y':
        v=classes.visualizer(g.get_dfa())
        v.show()
    else:
        print(g.get_dfa())
    y=input("\n\n\n\nDo you want another DFA? y/n (input a filename if yes)")
    if y=='y' or y=="Y":
        print("\033c",end='')
        main()
    else:
        print("\n\nYou are welcome\n\n")
if __name__=='__main__':
    main()
