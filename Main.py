from person import Person
from Dad import Dad
Tadej = Person(first_name="Tadej", last_name="Lorber", gender="Male",phone_num="85258552", birth="1990")
Miha = Person(first_name="Marko", last_name=" gkkakaka" , gender="Male", phone_num="85585255", birth="1980")

persons_array = [Tadej, Miha]

for p in persons_array:
    print "Name:"+ p.first_name
    print "Last name:"+ p.last_name
    print "Gender:"+ p.gender
    print p.ful_info()

dad = Dad ("Test" , "Test")
print " Oce:" + dad.full_name()

