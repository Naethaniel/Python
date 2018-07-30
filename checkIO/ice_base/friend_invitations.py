# With usage of properties
# class Friend:
#     def __init__(self, name):
#         self._name = name
#         self._invite = 'No party...'
#
#     @property
#     def invite(self):
#         return self._invite
#
#     @invite.setter
#     def invite(self, invite):
#         self._invite = invite
#
#
# class Party:
#     def __init__(self, place):
#         self._place = place
#         self._friends = []
#
#     def add_friend(self, friend):
#         self._friends.append(friend)
#
#     def send_invites(self, date):
#         invite = '{}: {}'.format(self._place, date)
#         for friend in self._friends:
#             friend.invite = invite
#
#     def del_friend(self, friend):
#         self._friends.remove(friend)


class Friend:
    def __init__(self, name):
            self._name = name
            self._invite = 'No party...'

    def set_invite(self, invite):
        self._invite = invite

    def show_invite(self):
        invite = self._invite
        return invite


class Party:
    def __init__(self, place):
        self._place = place
        self._friends = []

    def add_friend(self, friend):
        self._friends.append(friend)

    def send_invites(self, date):
        invite = '{}: {}'.format(self._place, date)
        for friend in self._friends:
            friend.set_invite(invite)

    def del_friend(self, friend):
        self._friends.remove(friend)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
