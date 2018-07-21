import pandas   #Pandas for dataframe manipulations
class Pokemon:
    pokemon = pandas.read_csv('pokemon.csv')    #Reading csv
    
    def simpleReccomendation():
        pokemon['popularity'] = ((7*pokemon['Attack']) + (5*pokemon['Defense']) + (6*pokemon['Speed'])-(9*pokemon['Catch_Rate'])) #Weighted Popularity
        pokemon = pokemon.sort_values('popularity',ascending=False) #Sorting
        pokemon = pokemon.drop('popularity',axis=1) #Dropping popularity
