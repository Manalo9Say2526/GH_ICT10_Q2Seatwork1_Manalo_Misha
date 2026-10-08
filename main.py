# input and display proccesing
from pyscript import display, document # type: ignore

def country_nickname(e): # initiating function 
    document.getElementById('output').innerHTML = " " # in order for the display not to overlap
    country = document.getElementById('Country').value # connects to ID input type and selected country

    countries = [ # list of countries
        'Philippines',
        'Vietnam',
        'Thailand',
        'Indonesia',
        'Malaysia',
        'Brunei',
        'Laos',
        'Timor-Leste',
        'Myanmar',
        'Singapore',
        'Cambodia'
    ]

    nicknames = ( # nickname tuples
        'Pearl of the Orient Seas',
        'Land of the Ascending Dragon',
        'Land of Smiles',
        'Emerald of the Equator',
        'Truly Asia',
        'Abode of Peace',
        'Land of a Million Elephants',
        'Land of the Rising Sun',
        'Golden Land',
        'Lion City',
        'Kingdom of Wonder'
    )
    
    

    display("Nickname: " + nicknames[countries.index(country)], target='output') # connecting tuple (nickname) and list (countries) to display, with indexing to determine or select the position of  the country and nickname
    



