from collections import UserDict


class Record():

    def __init__(self, name, *args):
        self.name = Name(name)
        self.phone = Phone(args)

    def add_phone(self, key, *args):
        self.data[key] += Phone(args).value
        return self.data[key]

    def edit_phone(self, key, number, new_number):
        tmp = list(self.data[key])
        while number in tmp:
            idx = tmp.index(number)
            tmp[idx] = new_number
        self.data[key] = tuple(tmp)

    def del_phone(self, key, number):
        tmp = list(self.data[key])
        while number in tmp:
            idx = tmp.index(number)
            tmp.pop(idx)
        self.data[key] = tuple(tmp)


class Field:
    def __init__(self, _):
        self.value = _


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict, Record):

    def add_record(self, name, *args):
        record = Record(name, *args)
        self.data[record.name.value] = args
        return self.data

    def get_phones(self, *name):
        for elem in name:
            if elem:
                rez = self.data[elem]
                print(f"For {elem} finded phones: {rez}")


# Test working conditions for developed classes (add record, add phone, modificstions, del)
a = AddressBook()
a.add_record("Alex", 9878)
a.add_record("Toma", 111, 222)
print(a.data)
a.add_phone("Alex", 999999999, 666)
a.edit_phone("Alex", 9878, 10000000)
a.del_phone("Alex", 666)
print(a.data)
a.get_phones("Alex", "Toma", "")
