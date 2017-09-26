class Person (object):
    first_name = ""
    last_name = ""
    gender = ""
    phone_num = ""
    birth = ""


    def __init__(self, first_name, last_name, gender, phone_num, birth):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_num = phone_num
        self.birth = birth
    def ful_name(self):
        return self.first_name + "" + self.last_name

    def ful_info(self):
        return self.first_name + " " + self.last_name + " " + self.gender + "," + self.phone_num + "," + self.birth


