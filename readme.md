Library Management System - Design a system to mangage books, members, borrowing , returns and fine calculation in a library.

I. USE CASE DETAILS:

1. Actors - Librarian , Library Memeber
2. Preconditions - Library datasbase is initialised with books. Member is registered with a valid Library Card ID.
3. Trigger - Member requests to borrow a book by ISBN or Title.
4. Main Flow: 
   (1) Member searches for a book. 
   (2) System Checks Availablity.
   (3) Librarian Processes borrow request 
   (4) System Records issue date and due date(14 days default).
   (5) Book Status updated to 'issued'
   (6) Member returns book.
   (7) System calculates fine is overdue.
   (8) Book status updated to Available.
5. Alternate Flow:
   (A1) Book not available -> System shows waitlist option.
   (A2) Member on waitlist -> Notify on availablity.
   (A3) Member has unpaid fine -> Block new borrowing until fine is cleared.
6. Post Conditions:
   Book marked as issued or returned . Transaction record saved . Fine calculated if applicable
7. Non Functional:
   Search should return result in under 1 second. support up to 10,000 books and 1,000 concurrent users. Fine calculation must be accurate to the day .

II. CLASS DESIGN

 1. Book - isbn, title , author, genre, status, quality [Methods- checkAvailabilty(),updateStatus()]
 2. Member - memberId, name, email, active borrows[], fines [Methods - borrowBook(),returnBook(),payFine()]
 3. BorrowRecord - recordId, memberId,isbn , IssueDate, dueDate , returnDate -[Methods -calculateFine(),isOverdue() ]
 4. Librarian - staffId, name - [Methods - issueBook(),processReturn(),addBook(),removeBook() ]
 5. FinePolicy - ratePerDay, maxFine, gracePeriod - [Methods-computeFine(daysOverdue) ]

III. FINE CALCULATION LOGIC:
   o Days - No Fine
   1-7 Days - Rs.2 per day
   8-15 Days - Rs.5 per day
   16+ Days - Rs.10 per day


OUTPUTS :
<img width="1177" height="592" alt="image" src="https://github.com/user-attachments/assets/5ba258ce-0c2a-49ba-b58c-cb95e3d258c6" />
<img width="1114" height="646" alt="image" src="https://github.com/user-attachments/assets/081fabcd-6223-4f06-87c8-20602e3be54f" />
<img width="1079" height="627" alt="image" src="https://github.com/user-attachments/assets/b1694f00-a7cd-4a26-8fe3-e702a9e530cb" />
<img width="1051" height="660" alt="image" src="https://github.com/user-attachments/assets/c4f72eb6-ed47-4822-8969-643b687aa538" /> 
<img width="1193" height="830" alt="image" src="https://github.com/user-attachments/assets/a1fb93c8-a6e5-49c6-b78f-b4c086e40efc" />
<img width="1340" height="709" alt="image" src="https://github.com/user-attachments/assets/a0cf80f7-bb72-4894-9aa3-7eba26eb7dcb" /> 






