from datetime import datetime
from models.borrow_record import BorrowRecord
class BorrowService:
    def __init__(self):
        self.records = {}
        self.counter = 1
    def issue_book(self, member, book, waitlist_service):
        if not member.can_borrow():
            print("Cannot borrow (limit/fine issue)")
            return
        if not book.is_available():
            print("Not available → added to waitlist")
            waitlist_service.add_to_waitlist(book.isbn, member)
            return
        record = BorrowRecord(self.counter, member, book)
        self.records[self.counter] = record
        self.counter += 1
        book.update_status("issued")
        member.borrowed_books.append(book)
        member.history.append(record)
        print(f"Issued | Record ID: {record.record_id}")
        print("Issue:", record.issue_date)
        print("Due:", record.due_date)
    def return_book(self, record_id, fine_service, waitlist_service):
        record = self.records.get(record_id)
        if not record:
            print("Invalid record")
            return
        if record.return_date:
            print("Already returned")
            return
        record.return_date = datetime.now()
        days = record.overdue_days()
        fine = fine_service.calculate_fine(days)
        if fine > 0:
            record.member.fines += fine
            print(f"Fine added: ₹{fine}")
        record.book.update_status("available")
        record.member.borrowed_books.remove(record.book)
        waitlist_service.notify_next(record.book.isbn)
        print(f"Returned: {record.book.title}")