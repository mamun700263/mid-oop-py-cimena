class Star_Cinema:
    __hall_list=[]
    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)
    

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.__seats={}
        self.__show_list=[]#list of tuples
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)
        self.__seat_count=rows*cols


    def entry_show(self,id:int,movie_name,time:str):
        self.__show_list.append((id,movie_name,time))
        matrix=[]
        for i in range(self.__rows):
            col=[]
            for j in range(self.__cols):
                col.append(0)
            matrix.append(col)
        self.__seats[id]=matrix
        self.__id=id
    def book_seats(self,r,c,id):
        if self.__seat_count==0:
            print('sorry!! sir no more seat left ')
        else:
            if 0<r<=self.__rows and 0<c<=self.__cols :
                if self.__seats[id][r-1][c-1]!=1:
                    self.__seats[id][r-1][c-1]=1
                    self.__seat_count-=1
                    print(f'ticket booked row:{r} columc :{c}')
                else:
                    print(f'sorry sir !!! seat {r} {c} is already booked')
            else:
                print("invalid row column")
    
    def view_show_list(self):
        for i in self.__show_list:
            print(f'SHOW ID: {i[0]}  movie name: {i[1]}  time {i[2]}')
        
    def view_seats(self,id):
        print(f'{self.__seat_count } seats available')
        for i in self.__seats[id]:
            print(i)


#-------------------------------------------
#-------------------------------------------

h1=Hall(5,5,1)
# h2=Hall(8,8,2)
# h3=Hall(7,7,3)

h1.entry_show(101,"War","10:00 AM")
h1.entry_show(102,"TIGER","11:00 AM")
h1.entry_show(203,"PATHAN","07:00 AM")

# h2.entry_show(201,"TIGER","11:00 AM")
# h2.entry_show(202,"War","10:00 AM")
# h2.entry_show(203,"PATHAN","07:00 AM")

# h3.entry_show(301,"TIGER","11:00 AM")
# h3.entry_show(302,"PATHAN","07:00 AM")
# h3.entry_show(303,"War","10:00 AM")

print("Welcome to Star Cinema ")

def counetr():
    print('Select your Options: ')
    print('1.View show list of this day')
    print('2.view available seats ')
    print('3.book tickets ')
    print('4.Exit')
    return input('your option: ')


# h1.view_show_list()
chose =counetr()
choiceList=['1','2','3','4']
while True:
    print('-------------------------------------------')
    print('-------------------------------------------')
    if chose in choiceList:
        if chose=='1':
            h1.view_show_list()


        elif chose=='2':
            show_id=input("plz enter your show id ")
            if show_id.isdigit() and int(show_id) in h1._Hall__seats :
                h1.view_seats(int(show_id))
            else:
                print("invalid show id")


        elif chose=='3':
            show_id=input("plz enter your show id ")
            if show_id.isdigit() and int(show_id) in h1._Hall__seats:
                quantity_or_ticket=input("how many ticket do you want : ")
                if quantity_or_ticket.isdigit():
                    for j in range(int(quantity_or_ticket)):
                        r = input('enter row : ')
                        c = input('enter column : ')
                        if  (r.isdigit() and c.isdigit()):
                            h1.book_seats(int(r),int(c),int(show_id))
                        else:
                            print("invalid row or column")
                        
                else:
                    print("Invalid quantity ")
            else:
                print("invalid show id")



        elif chose=='4':
            print('Thank you ')
            break
        else:
            print("sorry invalid input :: try again ")

    else:
        print("sorry invalid input :: try again ")
    
    print('-------------------------------------------')
    print('-------------------------------------------')
    chose=counetr()




h1=Hall(5,5,1)
h2=Hall(2,3,4)




