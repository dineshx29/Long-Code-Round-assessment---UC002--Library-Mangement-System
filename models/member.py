class Member:
    MAX_BORROW = 3
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.fines = 0
        self.borrowed_books = []
        self.history = []
    def can_borrow(self):
        return len(self.borrowed_books) < self.MAX_BORROW and self.fines == 0
    def pay_fine(self, amount):
        self.fines -= amount
        if self.fines < 0:
            self.fines = 0