import pandas
import numpy
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

pokemon = pandas.read_csv('pokemon.csv')
#Building a content based filtering system 
#Properties used are type,Legendary,canMegaEvolve
#Replacing boolean values with strings
pokemon['isLegendary']=pokemon['isLegendary'].replace(True,'Legendary')
pokemon['isLegendary']=pokemon['isLegendary'].replace(False,'notLegendary')
pokemon['hasMegaEvolution']=pokemon['hasMegaEvolution'].replace(True,'megaEvolve')
pokemon['hasMegaEvolution']=pokemon['hasMegaEvolution'].replace(False,'notMegaEvolve')
pokemon['Type_2']=pokemon['Type_2'].fillna('')

def createSoup(x):
    return ''.join(x['Type_1']) + ' ' + ''.join(x['Type_2'])+ ' ' +''.join(x['isLegendary'])+' '+''.join(x['hasMegaEvolution'])
    
pokemon['soup'] =pokemon.apply(createSoup,axis=1)

count = CountVectorizer(stop_words='english')
countMatrix =count.fit_transform(pokemon['soup'])

cosinSim = cosine_similarity(countMatrix,countMatrix)
indices = pandas.Series(pokemon.index,index=pokemon['Name']).drop_duplicates()
def getRecommendations(Name,cosinSim=cosinSim):
    idx = indices[Name]
    simScores = list(enumerate(cosinSim[idx]))
    simScores = sorted(simScores,key = lambda x:x[1],reverse=True)
    simScores = simScores[1:10]
    pokemonIndices = [i[0] for i in simScores]
    return pokemon['Name'].iloc[pokemonIndices]
print(getRecommendations('Rayquaza',cosinSim))