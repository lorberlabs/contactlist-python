class Dad(object):
    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
       return self.first_name + self.last_name #ali return "%s s%" %(self.first_name, self.last_name)

class Son(Dad):
    toy = ""

    def __init__(self,first_name,last_name, toy):
        Dad.__init__(self,first_name, last_name)
        self.toy = toy
