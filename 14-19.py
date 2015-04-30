choice = ['Italy', 'Holland', 'Germany', 'Spain', 'England', 'Japan']

for country in choice:
    if country == 'Japan':
        print '%s is not in Eurpoe' %(country)
        break
    print 'Go to', country
else:
    print 'All the country is in Europe'

