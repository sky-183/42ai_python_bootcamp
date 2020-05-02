# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/01 10:44:00 by vflander          #+#    #+#              #
#    Updated: 2020/05/01 10:44:00 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Documentation for 'the_bank' module
"""

from random import randrange


class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def is_valid(self) -> bool:
        """How do we define if a bank account is corrupted?
        • It has an even number of attributes.
        • It has an attribute starting with b.
        • It has no attribute starting with zip or addr.
        • It has no attribute name, id and value.
        :return:    True if account is valid
        """
        if len(self.__dict__) % 2 == 0:
            return False
        has_zip, has_addr = False, False
        for attr in self.__dict__.keys():
            if attr.startswith("b"):
                # print("FALSE: B")
                return False
            has_zip = attr.startswith("zip") or has_zip
            has_addr = attr.startswith("addr") or has_addr
        if not (has_addr or has_zip):
            # print("FALSE: ADDR/ZIP MISSING")
            return False
        has_name = "name" in self.__dict__.keys()
        has_id = "id" in self.__dict__.keys()
        has_value = "value" in self.__dict__.keys()
        if not (has_name and has_id and has_value):
            # print("FALSE: NAME/ID/VALUE MISSING")
            return False
        return True


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
        @origin:    int(id) or str(name) of the first account
        @dest:      int(id) or str(name) of the destination account
        @amount:    float(amount) amount to transfer
        @return     True if success, False if an error occured
        """
        origin = self.get_account(origin)
        dest = self.get_account(dest)
        if (origin is None) or (dest is None):
            return False
        if not origin.is_valid():
            # origin is not a valid account
            return False
        if not dest.is_valid():
            # dest is not a valid account
            return False
        if origin.value <= amount:
            return False
        # all is good, transferring funds now
        origin.transfer(-1 * amount)
        dest.transfer(amount)
        return True

    def get_account(self, account) -> Account:
        """Returns the account object by name or id (or None on error)
        :param account: int(id) or str(name) of the account
        :return: Account object or None
        """
        acc = None  # account object
        if issubclass(type(account), str):
            # ignoring the case when argument is valid intable str (like "42")
            for i in range(len(self.account)):
                try:
                    if self.account[i].name == account:
                        # cant just iterate by object, need to access
                        # the original objects, not copy, used in iteration
                        acc = self.account[i]
                        # Dont need to scan the whole list if we got it.
                        # But there may be another accounts with same name.
                        break
                except AttributeError:
                    # dont have 'name' attribute
                    pass
            # if we dont find that name in the list
        elif issubclass(type(account), int):
            try:
                acc = self.account[account]
            except IndexError:
                # account not found
                pass
        return acc

    def fix_account(self, account) -> bool:
        """
        Fixes the corrupted account, performing only automated fix, which can
        be done without user input:
        * rename values, starting with 'b' to 'fix_<oldname>'
        * add value 'fix_<random_num>' if number of values is even
        @account:   int(id) or str(name) of the account
        @return     True if success, False if an error occured
        """
        acc = self.get_account(account)
        if acc is None:
            return False
        for attr in acc.__dict__.keys():
            if attr.startswith("b"):
                new_name = "fix_" + attr
                acc.__dict__[new_name] = acc.__dict__.pop(attr)
        # 'while' instead of 'if' just in case we'll hit already existing field
        while len(acc.__dict__) % 2 == 0:
            name = "fix_" + str(randrange(10000))
            # acc.__dict__[name] = "this is a value, added by account fixer"
            # just another way of doing that, a bit cleaner
            setattr(acc, name, "this is a value, added by account fixer")
        return acc.is_valid()


if __name__ == "__main__":
    jane = Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31',
        info='None'
    )
    bank = Bank()
    bank.add(jane)
    print("fixing account with wrong name:")
    print(bank.fix_account("42"))  # False for bad acc name
    print("account before fixing:")
    print(bank.account[0].__dict__)
    print(bank.account[0].is_valid())  # False
    bank.fix_account("Smith Jane")
    # bank.fix_account(0)
    print("account after fixing:")  # True
    print(bank.account[0].__dict__)
    print(bank.account[0].is_valid())
    mike = Account(
        'Smith Mike',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31',
    )
    bank.add(mike)
    bank.fix_account(1)
    print("transferring:")
    bank.account[0].value = 1000
    print(bank.account[0].value, bank.account[1].value)
    print(bank.transfer(0, 1, 750))
    print(bank.account[0].value, bank.account[1].value)
