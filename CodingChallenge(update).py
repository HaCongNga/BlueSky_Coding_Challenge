#List of dictionaries
ls_dict = []
import json
f = open('py_challange_input.json')
data = json.load(f)
#function to return the list of dictionaries
def create_matches_dictionary() :
  cricket_access = data['Cricket']
  for cricket_data in cricket_access :
    formats_access = cricket_data['formats']
    for formats_data in formats_access :
        regions_access = formats_data['regions']
        for regions_data in regions_access :
            regionName = regions_data['name']
            matches_access = regions_data['matches']
            for match in matches_access :
                match_dict = {'match_id':match['id'], 
                'livestream_provider':match['streaming']['liveStream']['provider'],
                'winner of the match':match['results']['winner'],
                'httplink of match':match['httpLink'],
                'region name':regionName, 
                'team1 & team2 playing in the match': match['team1'] == match['team2'],
                'isInternational':match['isInternational'],
                'resultsWithheld':match['results']['resultsWithheld'],
                'team1' : match['team1'], 'team2' : match['team2'],
                'points' : match['results']['points']
                }
                ls_dict.append(match_dict)
    return ls_dict
#print(create_match_dictionary())
# Q1: How many international matches took place
matches_dic = create_matches_dictionary()
# Count varible for International Matches
countInternational = 0
for match in matches_dic :
    if match['isInternational'] == True :
        countInternational = countInternational + 1
print("The number of international matches is :" , end = " ")
print(countInternational)
#Q3 : Percentage of matches played in north, south, central
countNorth = 0
countSouth = 0
countCentral = 0
numberOfMatches = len(matches_dic)
for match in matches_dic :
    if match['region name'] == "north" :
        countNorth = countNorth + 1
    elif match['region name'] == "south" :
        countSouth = countSouth + 1
    elif match['region name'] == "central" :
        countCentral = countCentral + 1
print("The Percentage (%) of matches played in north, south, central (respectively) is ")
print(countNorth/numberOfMatches * 100, end = " ")
print(countSouth/numberOfMatches * 100, end = " ")
print(countCentral/numberOfMatches * 100)
#Q4: How many results are withheld ? Form DataFrame.
import pandas as pd
countWithheldMatches = 0
dataFrameOfWithheld = []
for match in matches_dic :
    if match['resultsWithheld'] == True :
        list = {'match_id': match['match_id'], 'teams' : match['team1'] + " vs " + match['team2']}
        dataFrameOfWithheld.append(list)
        countWithheldMatches = countWithheldMatches + 1
print("The number of matches with Withdrew result is : " , end = " ")
print(countWithheldMatches)
print("The DataFrame of Withdrew-result matches :")
df = pd.DataFrame(dataFrameOfWithheld)
print(df)
#Q2 : Which team has scored the most points overall?
Points = [0] * 14
for i in range(1, len(Points)) :
    for match in matches_dic :
        if match['winner of the match'] == "T" + str(i+1) :
            Points[i] = Points[i] + match['points']
print('The team has scored the most points overall is : T', end = "")
print(Points.index(max(Points)) + 1)

f.close()
#def get_match_infos
