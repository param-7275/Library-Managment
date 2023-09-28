while True:
    a = input("Enter Your Name:")
    print("Welcome To ABC Library:")
    while True:
        def book():
            print("Press 1 For Show Books\nPress 2 For Issued Book\nPress 3 For Submit Book\nPress 4 For Exit")
        try:
            book()
            books = ["Rich Dad Poor Dad", "Lost Child", "My India", "The Holy Quran", "Wonderland"]
            while True:
                h = int(input("What You Want, Choose One Option: "))
                if h==1:
                    print(f"Book List:-",books)
                    book()

                elif h==2:
                    print(f"Book List:-",books)
#                     book()
                    g = input("which book you want to issue! Enter Book Name: ")
                    if g.upper or g.lower in books:
                        print("please take your book")
                        books.remove(g)
                    else:
                        print("sorry this book already issued")
                elif h==3:
                    u = input("enter book name: ")
                    books.append(u)
                elif h==4:
                    print("Thanks For Coming ABC Library\nVISIT AGAIN!\n")
                    break
                else:
                    print("Please Select Given Choice")
                    book()
                break  
        except:
            print("Character Not Allowed Please Enter Given Choices\n")
#             book()
        