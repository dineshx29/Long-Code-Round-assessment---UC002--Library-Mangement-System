class FineService:
    def calculate_fine(self, days):
        if days <= 0:
            return 0
        elif days <= 7:
            return days * 2
        elif days <= 15:
            return days * 5
        else:
            return days * 10