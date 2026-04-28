from datetime import datetime
class BorrowRecord:
    def __init__(self, record_id, member, book):
        self.record_id = record_id
        self.member = member
        self.book = book
        self.issue_date = datetime.now()
        self.due_date = self.issue_date 
        self.return_date = None
    def overdue_days(self):
        today = datetime.now()
        if self.return_date:
            return max(0, (self.return_date - self.due_date).days)
        else:
            return max(0, (today - self.due_date).days)
    def is_returned(self):
        return self.return_date is not None