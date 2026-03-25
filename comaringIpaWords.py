import html
import unicodedata

# source IPA (HTML-escaped) for component extraction
source_escape_compIPA = "zɔ.nənˌbʏ.mə"
compIPA = html.unescape(source_escape_compIPA)

## TODO Unsecaping the HTML Stuff
source_escape_ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]

ipa_test = {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}
n = len(ipa_list)
ipa_Scorelist = [[0] * n for _ in range(3)]
highest_score = 0

def Ipa_score(ipa_list, compIPA):
    #i have the lenght of the IPA list
    z = ipa_test
    n = len(ipa_list)
    for index,item in enumerate(ipa_list):
        Word = item.get("Word", "")
        source_escape_IPA = item.get("IPA", "")
        IPA = html.unescape(source_escape_IPA)

       # Score = sum( (1* len(compIPA) / len(Word)) for y in compIPA if y in IPA)
        sum_score = sum( (1) for y in compIPA if y in IPA)
        Score = sum_score / len(compIPA)
        ipa_Scorelist[2][index] = Score
        ipa_Scorelist[0][index] = Word
        ipa_Scorelist[1][index] = IPA

    # TODO now i need the highest score
    finalScore = ipa_Scorelist[2]
    highest_score = 0
    for i, ThisFinalScore in enumerate(finalScore): # Dont now why that works
        ThisFinalScore = finalScore[i] 
        if ThisFinalScore > highest_score:
            highest_score = ThisFinalScore
            thisIndex = i
    TheBestWord = ipa_Scorelist[0][thisIndex]
    return Word, IPA, ipa_Scorelist, highest_score, thisIndex, TheBestWord

print(Ipa_score(ipa_list))
