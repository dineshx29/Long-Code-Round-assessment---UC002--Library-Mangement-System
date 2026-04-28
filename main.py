from controllers.library_controller import LibraryController
from models.book import Book
from models.member import Member
controller = LibraryController()
print("---REC LIBRARY---")
print("*** SELECT ROLE ***")
print("1. Librarian")
print("2. Member")
role = input("Enter choice: ")
if role == "1":
    print("Logged in as LIBRARIAN")
    while True:
        print("\n**** LIBRARIAN MENU ****")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Add Member")
        print("5. View Members")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. View Member History")
        print("9. Exit")
        ch = input("Choice: ")
        if ch == "1":
            controller.book_service.add_book(Book(input("ISBN: "), input("Title: "),input("Author: "), input("Genre: ")))
        elif ch == "2":
            for b in controller.book_service.list_books():
                print(b.isbn, b.title, b.status)
        elif ch == "3":
            key = input("Search (ISBN/Title/Author): ")
            res = controller.book_service.search_books(key)
            for b in res:
                print(b.isbn, b.title, b.author, b.status)
        elif ch == "4":
            controller.member_service.add_member(
                Member(int(input("ID: ")), input("Name: "), input("Email: ")))
        elif ch == "5":
            for m in controller.member_service.list_members():
                print(m.member_id, m.name, "Fine:", m.fines)
        elif ch == "6":
            m = controller.member_service.get_member(int(input("Member ID: ")))
            b = controller.book_service.get_book(input("ISBN: "))
            if m and b:
                controller.borrow_service.issue_book(
                    m, b, controller.waitlist_service)
            else:
                print("Invalid member/book")
        elif ch == "7":
            controller.borrow_service.return_book(
                int(input("Record ID: ")),
                controller.fine_service,
                controller.waitlist_service)
        elif ch == "8":
            mid = int(input("Member ID: "))
            m = controller.member_service.get_member(mid)
            if m:
                for r in m.history:
                    print("\nRecord:", r.record_id)
                    print("Book:", r.book.title)
                    print("Issued:", r.issue_date)
                    print("Due:", r.due_date)
                    print("Returned:", r.return_date)
                    d = r.overdue_days()
                    f = controller.fine_service.calculate_fine(d)
                    print("Fine till now:", f)
        elif ch == "9":
            break
elif role == "2":
    print("Logged in as MEMBER")
    mid = int(input("Enter your Member ID: "))
    member = controller.member_service.get_member(mid)
    if not member:
        print("Member not found")
        exit()
    while True:
        print("\n**** MEMBER MENU ****")
        print("1. View Books")
        print("2. Search Book")
        print("3. View My History")
        print("4. View My Fine")
        print("5. Pay Fine")
        print("6. Exit")
        ch = input("Choice: ")
        if ch == "1":
            for b in controller.book_service.list_books():
                print(b.isbn, b.title, b.status)
        elif ch == "2":
            key = input("Search: ")
            res = controller.book_service.search_books(key)
            for b in res:
                print(b.isbn, b.title, b.author, b.status)
        elif ch == "3":
            for r in member.history:
                print("\nRecord:", r.record_id)
                print("Book:", r.book.title)
                print("Issued:", r.issue_date)
                print("Due:", r.due_date)
                print("Returned:", r.return_date)
                d = r.overdue_days()
                f = controller.fine_service.calculate_fine(d)
                print("Fine till now:", f)
        elif ch == "4":
            print("Total Fine:", member.fines)
        elif ch == "5":
            amt = int(input("Amount: "))
            member.pay_fine(amt)
            print("Remaining fine:", member.fines)
        elif ch == "6":
            break
else:
    print("Invalid role selected")