class WaitlistService:
    def __init__(self):
        self.waitlist = {}
    def add_to_waitlist(self, isbn, member):
        if isbn not in self.waitlist:
            self.waitlist[isbn] = []
        self.waitlist[isbn].append(member)
    def notify_next(self, isbn):
        if isbn in self.waitlist and self.waitlist[isbn]:
            m = self.waitlist[isbn].pop(0)
            print(f"Notify {m.name}: Book available")