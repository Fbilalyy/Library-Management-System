books = [
    {"book_name": "a",
     "book_number": 3,
     "book_category": "a",
     "book_placement": "a",
     "book_author": "a",
     "book_publishment_year": 3,
     "is_book_taken": True,
     "people_id": 123
     },
    {"book_name": "b",
     "book_number": 4,
     "book_category": "b",
     "book_placement": "b",
     "book_author": "b",
     "book_publishment_year": 4,
     "is_book_taken": False,
     "people_id": ()
     },
    {"book_name": "c",
     "book_number": 5,
     "book_category": "c",
     "book_placement": "c",
     "book_author": "c",
     "book_publishment_year": 5,
     "is_book_taken": False,
     "people_id": ()
     }

]

books_name = set()
books_number = set()
books_category = set()
books_placement = set()
books_author = set()
books_publishment_year = set()

c_1 = ""
while c_1 != "-q":
    print("What would you want to do? (Write help for command list)")
    c_1 = input()
    if c_1 == "-a" or c_1 == "add book":
        input_add_book = input()
        add_book = input_add_book.split()
        if len(add_book) != 6:
            print("Can not add book to the system. Missing parameter(s).")
        else:
            book_name = add_book[0]
            book_number = add_book[1]
            book_category = add_book[2]
            book_placement = add_book[3]
            book_author = add_book[4]
            book_publishment_year = add_book[5]
            if not book_number.isdigit() or not book_publishment_year.isdigit():
                print("Can not add book to the system. Improper parameter(s).")
            elif book_name and book_number and book_category and book_placement and book_author and book_publishment_year:
                books_name.add(book_name)
                books_number.add(int(book_number))
                books_category.add(book_category)
                books_placement.add(book_placement)
                books_author.add(book_author)
                books_publishment_year.add(int(book_publishment_year))
                new_book = {"book_name": book_name,
                            "book_number": int(book_number),
                            "book_category": book_category,
                            "book_placement": book_placement,
                            "book_author": book_author,
                            "book_publishment_year": int(book_publishment_year),
                            "is_book_taken": False,
                            "people_id": ()
                            }
                books.append(new_book)
                print(book_name + " has been added to the system.")
    elif c_1 == "-f" or c_1 == "find book":
        input_find_book = input()
        find_book_d = input_find_book.split()
        find_book = find_book_d[0]
        if len(find_book) < 1:
            print("Can not find book. Missing parameter(s).")
        else:
            taken_book = False
            if find_book.isdigit():
                for book in books:
                    if book["book_number"] == int(find_book):
                        if book["is_book_taken"] == True:
                            print('does book taken', book["book_name"], book["book_number"], book["book_category"], book["book_placement"], book["book_author"], book["book_publishment_year"])
                            taken_book = True
                        elif book["is_book_taken"] == False:
                            print(book["book_name"], book["book_number"], book["book_category"], book["book_placement"], book["book_author"])
                            taken_book = True
                if not taken_book:
                    print("Can not find book. There is no book like this in this system.")
            else:
                for book in books:
                    if book["book_name"] == find_book:
                        if book["is_book_taken"] == True:
                            print('does book taken', book["book_name"], book["book_number"], book["book_category"], book["book_placement"], book["book_author"], book["book_publishment_year"])
                            taken_book = True
                        elif book["is_book_taken"] == False:
                            print(book["book_name"], book["book_number"], book["book_category"], book["book_placement"], book["book_author"])
                            taken_book = True
                if not taken_book:
                    print("Can not find book. There is no book like this in this system.")
    elif c_1 == "-la" or c_1 == "list an author’s books":
        list_authors_book = input()
        if len(list_authors_book) != 1:
            print("Can not list book(s). Missing parameter(s).")
        else:
            for book in books:
                if book["book_author"] == list_authors_book:
                    print(book["book_name"],book["book_number"])
                else:
                    print("There are no books by this author in this system.")
    elif c_1 == "-t" or c_1 == "take book":
        input_take_book = input()
        take_book_d = input_take_book.split()
        take_book = take_book_d[0]
        people_id = take_book_d[1]
        if len(take_book_d) < 2:
            print("Can not give book. Missing parameter(s).")
        else:
            for book in books:
                if take_book.isdigit():
                    if book["book_number"] == int(take_book):
                        if book["is_book_taken"] == True:
                            print("Can not give book. Someone has already taken it.")
                        elif book["is_book_taken"] == False:
                            book["people_id"] = people_id
                            book["is_book_taken"] = True
                            print(book["book_name"], "has given with no problem.")
                    else:
                        print("Can not give book. There is no book like this in this system.")


                else:
                    if book["book_name"] == take_book:
                        if book["is_book_taken"] == True:
                            print("Can not give book. Someone has already taken it.")
                        elif book["is_book_taken"] == False:
                            book["people_id"] = people_id
                            book["is_book_taken"] = True
                            print(book["book_name"], "has given with no problem.")
                    else:
                        print("Can not give book. There is no book like this in this system.")


    elif c_1 == "-r" or c_1 == "return book":
        input_return_book = input()
        return_book_d = input_return_book.split()
        return_book = return_book_d[0]
        if len(input_return_book) < 1:
            print("Can not return book(s). Missing parameter(s).")
        else:
            for book in books:
                if return_book.isdigit():
                    if book["book_number"] == int(return_book):
                        if book["is_book_taken"] == False:
                            print("Can not return book. It has not been taken by anyone.")
                        if book["is_book_taken"] == True:
                            print(book["book_name"],"has been returned.")
                    elif book["book_name"] == return_book:
                        if book["is_book_taken"] == False:
                            print("Can not return book. It has not been taken by anyone.")
                        elif book["is_book_taken"] == True:
                            print(book["book_name"], "has been returned.")
                    else:
                        print("Can not return book. There is no book like this in this system.")
    elif c_1 == "-l" or c_1 == "list books":
        if books == []:
            print("There are no books in the system.")
        else:
            for book in books:
                print(book["book_name"],book["book_number"])
    elif c_1 == "-lt" or c_1 == "list taken books":
        for book in books:
            if not book["is_book_taken"] == True:
                print("No one has taken books :(")

            elif book["is_book_taken"] == True:
                print(book["book_name"], book["book_number"], book["people_id"])
    elif c_1 == "-ly" or c_1 == "list books before/after year":
        input_list_ba_year = input()
        list_ba_year = input_list_ba_year.split()
        year = list_ba_year[0]
        before_or_after = list_ba_year[1]

        if len(list_ba_year) < 2:
            print("Can not list book(s). Missing parameter(s).")
        else:

            if not year.isdigit():
                print("Can not list book(s). Improper input.")
            else:

                if before_or_after == "before":
                    found_books = False
                    for book in books:
                        if book["book_publishment_year"] < int(year):
                            print(book["book_name"], book["book_number"])
                            found_books = True
                    if not found_books:
                        print("There are no books that is published", [before_or_after], [year], "in the system.")
                elif before_or_after == "after":
                    found_books = False
                    for book in books:
                        if book["book_publishment_year"] > int(year):
                            print(book["book_name"], book["book_number"])
                            found_books = True
                    if not found_books:
                        print("There are no books that is published", [before_or_after], [year], "in the system.")
                else:
                    print("Can not list book(s). Improper input.")

    elif c_1 == "-h" or c_1 == "help":
        print("add book \t | -a | \t adds a new book to the system")
        print("find book \t | -f | \t this command finds a book at the system")
        print("list an author’s books \t | -la | \t finds the books of an author which are in the system")
        print("take book \t | -t | \t give a book to someone")
        print("return book \t | -r | \t returns a book which have taken by someone")
        print("list books \t | -l | \t lists every book in the system")
        print("list taken books \t | -lt | \t lists every taken book in the system")
        print("list books before/after year \t | -ly | \t lists every book in the system with given dates")
        print("help \t | -h | \t prints all commands and their descriptions")
        print("quit \t | -q | \t quits program")
    elif c_1 == "":
        print()
    elif c_1 == "-q" or c_1 == "quit":
        print("See you later :)")
    else:
        print("You have entered a command that does not exist. Write ‘help’ to get to know commands.")























