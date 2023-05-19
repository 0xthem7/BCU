fin = open("lab10/cities.txt", 'r')

line = fin.readline()
country_cmp = {}
while line != "":
    maxpop = 10000000
    maxcity = ""
    fields = line.split(';')
    city = fields[0]
    country = fields[1]
    # Exception
    try:
        population = int(fields[2])
    except:
        population = 0

    if country == "UK":
        if population < maxpop:
            maxpop = population
            country_cmp[city] = population
            line = fin.readline()
    line = fin.readline()

maxpop = max(country_cmp.values())
    
if maxpop == 10000000:
    print('No cities in input file.\n')
else:
    countries = country_cmp.keys()
    for city in countries:
        if country_cmp[city] == maxpop:
            x = city
    print(f"Largest city in UK  is {x} with {maxpop} population")
    
    