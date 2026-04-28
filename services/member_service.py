class MemberService:
    def __init__(self):
        self.members = {}
    def add_member(self, member):
        self.members[member.member_id] = member
    def get_member(self, member_id):
        return self.members.get(member_id)
    def list_members(self):
        return self.members.values()