from DSproject import *
a = {"product": [], "item": [],"Quant":[] ,"price": []}

b = list(a.values())

na = b[0]

it= b[1]

qu=b[2]

pr = b[3]


print("\n-----WELCOME VISHAL.VJ DEPARTMENTAL STORE-----")
def itemshow():
    d = list(vj)
    print(d)
    for x in d:
        print(x)

def buyitem():

    d = list(vj)
    print(d)

    for x in d:
        print(x)

    w = input("Enter the item you want: ")
    w=w.upper()
    print(vj[w])

    for x in vj[w]:
        print(x, ":", vj[w][x])

    item= input("Enter item: ")
    item=item.capitalize()
    if item in vj[w]:
        l = input(f"how many {item} you want: ")

    for h in vj[w].keys():
        j = (vj[w][h])
        if h == vj[w]:
            print("The prize for", item, "is", j)
    amount = int(j) * int(l)
    print(f"Total amount of {item} Rs : {amount}")

    na.append(w)
    it.append(item)
    qu.append(l)
    pr.append(amount)
    s=sum(pr)



    print("\n\n------------------GROCERY LIST------------------")
    print("------------------------------------------------")
    print("  PRODUCT    ITEM     QUANTITY    Rs.")
    for i in range(len(na)):
        print( '\t',na[i],'\t',it[i],'\t\t',qu[i],'\t\t',pr[i])
    print("\nTOTAL AMOUNT(Rs): ", s)
def product():
    while True:
        try:
            print("\n1.VIEW ITEM\n2.BUY ITEM\n3.EXIT")
            choise = int(input("\nEnter what do you want: \n"))
        except ValueError:
            print("Enter correct item")

        else:
            if choise == 1:
                itemshow()
                print("------------------------------------------------")
            elif choise == 2:
                print("------------------------------------------------")
                buyitem()
                print("------------------------------------------------")
                while True:
                    try:
                        print("\n\n1.Add more item\n2.EXIT")
                        pro = int(input("You want to add more item: "))
                    except ValueError:
                        continue
                    else:
                        if pro == 1:
                            print("------------------------------------------------")
                            buyitem()
                            print("------------------------------------------------")
                        else:

                            print("\n\n\n--THANKYOU--")
                            quit()


            else:
                print("EXIT......")
                quit()

product()







