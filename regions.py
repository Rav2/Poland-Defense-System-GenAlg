# data about polish regions
# from  https://pl.wikipedia.org/wiki/Wojewodztwo
# written down 25.11.2016


# might be useful
def get_regions():
    return {'zachodnio_pomorskie': zachodnio_pomorskie, 'lubuskie':lubuskie, 'dolnoslaskie':dolnoslaskie, #west
           'opolskie': opolskie, 'slaskie' : slaskie, 'malopolskie': malopolskie,#south
           'podkarpackie' : podkarpackie, 'lubelskie' : lubelskie, 'podlaskie' : podlaskie, #east
           'warminsko_mazurskie' : warminsko_mazurskie, 'pomorskie' : pomorskie, #north
           'mazowieckie': mazowieckie, 'kujawsko_pomorskie': kujawsko_pomorskie, 'wielkopolskie':wielkopolskie,
            'lodzkie': lodzkie, 'swietokrzyskie':swietokrzyskie #central
            }


def get_regions_list():
    return [zachodnio_pomorskie, lubuskie, dolnoslaskie, opolskie, slaskie, malopolskie, podkarpackie, lubelskie, podlaskie,
            warminsko_mazurskie, pomorskie, mazowieckie, kujawsko_pomorskie, wielkopolskie, lodzkie, swietokrzyskie]

# shows possible threat to Poland's safety, takes value 1, 2 or 3, where 1 is the lowest and 3 the highest
threat_coef = {'DE' : 1, 'CZ' : 1, 'SK' : 1, 'UA' : 2, 'BY' : 2, 'LT' : 1, 'RU' : 3}

zachodnio_pomorskie = {
                        'name' : 'zachodnio-pomorskie',
                        'weight' : 1,
                        'pop' : 1721405,
                        'area' : 22892.48, # km^2
                        'DE' : 188.9, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }
lubuskie = {
                        'name' : 'lubuskie',
                        'weight' : 1,
                        'pop' : 11023317,
                        'area' : 13987.89, # km^2
                        'DE' : 195.6, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }
dolnoslaskie = {
                        'name' : 'dolnoslaskie',
                        'weight' : 1,
                        'pop' : 2914362,
                        'area' : 19946.74, # km^2
                        'DE' : 76.0, #km
                        'CZ' : 410.8,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }

opolskie = {
                        'name' : 'opolskie',
                        'weight' : 1,
                        'pop' : 1010203,
                        'area' : 9411.87, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 192.4,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }


slaskie = {
                        'name' : 'slaskie',
                        'weight' : 1,
                        'pop' : 4615870,
                        'area' : 12333.09	, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 142.9,
                        'SK' : 85.3,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }

malopolskie = {
                        'name' : 'malopolskie',
                        'weight' : 1,
                        'pop' : 3354077,
                        'area' : 15182.79, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 301.6,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }

podkarpackie = {
                        'name' : 'podkarpackie',
                        'weight' : 1,
                        'pop' : 2129951,
                        'area' : 17845.76, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 134.0,
                        'UA' : 239.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }


lubelskie = {
                        'name' : 'lubelskie',
                        'weight' : 1,
                        'pop' : 2165651,
                        'area' : 25122.46, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 165.2,
                        'LT' : 0.0,
                        'RU' : 282.5
                    }



podlaskie = {
                        'name' : 'podlaskie',
                        'weight' : 1,
                        'pop' : 1198690,
                        'area' : 20187.02, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 236.3,
                        'LT' : 100.3,
                        'RU' : 0.0
                    }

warminsko_mazurskie = {
                        'name' : 'warminsko-mazurskie',
                        'weight' : 1,
                        'pop' : 1450697,
                        'area' : 24173.47	, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 208.3
                    }

pomorskie = {
                        'name' : 'pomorskie',
                        'weight' : 1,
                        'pop' : 2290070,
                        'area' : 18310.34, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.8
                    }

mazowieckie = {
                        'name' : 'mazowieckie',
                        'weight' : 3, #capital city
                        'pop' : 5301760,
                        'area' : 35558.47, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }






kujawsko_pomorskie = {
                        'name' : 'kujawsko-pomorskie',
                        'weight' : 1,
                        'pop' : 2096404,
                        'area' : 17971.34, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }

wielkopolskie = {
                        'name' : 'wielkopolskie',
                        'weight' : 1,
                        'pop' : 3462196,
                        'area' : 29826.50	, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }




lodzkie = {
                        'name' : 'lodzkie',
                        'weight' : 1,
                        'pop' : 2524651,
                        'area' : 18218.95, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }


swietokrzyskie = {
                        'name' : 'swietokrzyskie',
                        'weight' : 1,
                        'pop' : 1273995,
                        'area' : 11710.50	, # km^2
                        'DE' : 0.0, #km
                        'CZ' : 0.0,
                        'SK' : 0.0,
                        'UA' : 0.0,
                        'BY' : 0.0,
                        'LT' : 0.0,
                        'RU' : 0.0
                    }


