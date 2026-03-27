import html
import unicodedata
import openai

openai.api_key = ""
#TODO adding an .env think to be able to saftly use API Key with this public repo

# source IPA (HTML-escaped) for component extraction
#source_escape_compIPA = "zɔ.nənˌbʏ.mə"
source_escape_compIPA = "ˈʃtaʊ̯pˌzaʊ̯ɡɐ"
compIPA = html.unescape(source_escape_compIPA)

## TODO Unsecaping the HTML Stuff
#source_escape_ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
#ipa_list = [{'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonnegeel', 'IPA': 'ˈzɔ.nə.ɣeːl'}, {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}, {'Word': 'zonneplant', 'IPA': 'ˈzɔ.nə.ˌplɑnt'}, {'Word': 'zonnebloemknop', 'IPA': 'ˈzɔ.nə.bloːm.knɔp'}]
ipa_list = [ {'Word': 'stofzuiger', 'IPA': 'ˈstɔfˌzœyɣər'}, {'Word': 'zuigapparaat', 'IPA': 'ˈzœyɣˌʔɑpərɑt'}, {'Word': 'stofzuiger', 'IPA': 'ˈstɔfˌzœy̯ɣər'}, {'Word': 'stofzuigmachine', 'IPA': 'ˈstɔfˌzœyɣmɑˌʃinə'}, {'Word': 'vacuümreiniger', 'IPA': 'vɑˈkʏːmˌreːnəɣər'}, {'Word': 'automatische stofzuiger', 'IPA': 'ˌʔɔtɔˈmɑtɪʃə ˈstɔfˌzœyɣər'}, {'Word': 'handstofzuiger', 'IPA': 'ˈhɑntˌstɔfˌzœyɣər'}, {'Word': 'opzuiger', 'IPA': 'ˈɔpzœyɣər'}, {'Word': 'zuigborstel', 'IPA': 'ˈzœyɣˌbɔrsl̩'}, {'Word': 'stofzuigapparaat', 'IPA': 'ˈstɔfˌzœyɣˌʔɑpərɑt'}, {'Word': 'huisstofzuiger', 'IPA': 'ˈœysˌstɔfˌzœyɣər'}, {'Word': 'zuigzuiger', 'IPA': 'ˈzœyɣˌzœyɣər'}, {'Word': 'dweilzuiger', 'IPA': 'ˈdʋɛilˌzœyɣər'}, {'Word': 'zuigborsteltje', 'IPA': 'ˈzœyɣˌbɔrstəɫjə'}, {'Word': 'vloerzuiger', 'IPA': 'ˈvlurˌzœyɣər'}, {'Word': 'stofzuigketel', 'IPA': 'ˈstɔfˌzœyɣˌkətəl'}, {'Word': 'zuigset', 'IPA': 'ˈzœyɣsɛt'}, {'Word': 'zuigkop', 'IPA': 'ˈzœyɣkɔp'}, {'Word': 'stofzuigsysteem', 'IPA': 'ˈstɔfˌzœyɣsɪˌtem'}, {'Word': 'zuigmonden', 'IPA': 'ˈzœyɣmɔndən'} ]
ipa_test = {'Word': 'zonnebloem', 'IPA': 'ˈzɔ.nə.bloːm'}
# I added an synonym from GPT 5.1 into the output of the gpt 4.1 and i noticed that the single output of gpt 5.1 was better than the randomb 20 synonyms, which might mean we need to aösp care about how we promt it
n = len(ipa_list)
ipa_Scorelist = [[0] * n for _ in range(3)]
highest_score = 0

def Ipa_score(ipa_list):
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
