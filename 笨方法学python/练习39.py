
states={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'NeW York':'NY',
    'Michigan':'MI'}



cities={
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'}



cities['NY']='new York'
cities['OR']='Portland'


print('-'*10)
print("NY State has:",cities['NY'])
print("OR State has:",cities['OR'])


print('-'*10)
print("Michigan's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is:",states['Florida'])


print('-'*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])


print('-'*10)
for state,abbrev in states.items():
    print("%s is abbreviated %s"%(state,abbrev))


print('-'*10)
for abbrev,city in cities.items():
    print("%s has the city %s"%(abbrev,city))


print('-'*10)
for state,abbrev in states.items():
    print("%s state is abbreviated %s and has city %s"%(state,abbrev,cities[abbrev]))


print('-'*10 )
state=states.get('Texas',None)


if not state:
    print("Sotty,no Texas.")


city=cities.get('TX','Does Not Exist')
print("The city for the state 'TX'is;%s"%city)




things=['a','b','c','d']
print(things[1])
things[1]='z'
print(things[1])
print(things)



