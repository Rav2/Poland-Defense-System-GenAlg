# dane dotyczace wojewodztw,
# pochodza z https://pl.wikipedia.org/wiki/Województwo
# spisane 25.11.2016

#might be useful
def get_regions():
    return {'zachodnio_pomorskie': zachodnio_pomorskie, 'lubuskie':lubuskie, 'dolnoslaskie':dolnoslaskie, #west
           'opolskie': opolskie, 'slaskie' : slaskie, 'malopolskie': malopolskie,#south
           'podkarpackie' : podkarpackie, 'lubelskie' : lubelskie, 'podlaskie' : podlaskie, #east
           'warminsko_mazurskie' : warminsko_mazurskie, 'pomorskie' : pomorskie, #north
           'mazowieckie': mazowieckie, 'kujawsko_pomorskie': kujawsko_pomorskie, 'wielkopolskie':wielkopolskie,
            'lodzkie': lodzkie, 'swietokrzyskie':swietokrzyskie #central
            }

zachodnio_pomorskie = {
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
kujawsko_pomorskie = {
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
lubelskie = {
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
lodzkie = {
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
malopolskie = {
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
mazowieckie = {
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
opolskie = {
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
podkarpackie = {
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
podlaskie = {
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
pomorskie = {
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
slaskie = {
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
swietokrzyskie = {
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
warminsko_mazurskie = {
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
wielkopolskie = {
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