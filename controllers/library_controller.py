from services.book_service import BookService
from services.member_service import MemberService
from services.borrow_service import BorrowService
from services.fine_service import FineService
from services.waitlist_service import WaitlistService
class LibraryController:
    def __init__(self):
        self.book_service = BookService()
        self.member_service = MemberService()
        self.borrow_service = BorrowService()
        self.fine_service = FineService()
        self.waitlist_service = WaitlistService()