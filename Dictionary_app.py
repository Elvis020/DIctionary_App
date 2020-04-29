# import json
# help(json.load)
# data = json.load(open("/home/spacey/Projects_with_Python/App_1/2.2 data.json"))
# print(type(data))
# print(data["access"])
#Write a function that takes an input and returns a value
def translate(w):
    import json
    import difflib
    from difflib import get_close_matches
    data = json.load(open("/home/spacey/Projects_with_Python/App_1/2.2 data.json"))

    if w in data.keys():
        for n in iter(data[w]):
            print(n)
    else:
        similar_words = get_close_matches(w, data.keys())
        if len(similar_words) > 0:
            simi = input("""Do you mean "%s".Enter y if Yes or n if No: """ % similar_words[0]).upper()
            if simi == "Y":
                if len(data[similar_words[0]]) == 1:
                    for n in iter(data[similar_words[0]]):
                        print(n)
                else:
                    for n in iter(data[similar_words[0]]):
                        print(n)
                    # print(f"""{similar_words[0]}:{data[similar_words[0]]}""")
            else:
                print("The word " + "\"" + w + "\"" + " doesn't exist, please double check your spelling.")

word = input("Plaese enter a word: ").casefold()
output = translate(word)
# for n in range(output):
#     print(output)
# Note: The difflib libraray was used to find the similarity between words
# import json
# data = json.load(open("/home/spacey/Projects_with_Python/App_1/2.2 data.json"))
# # data.keys()
# import difflib
# from difflib import get_close_matches
# print(get_close_matches("rainn", data.keys()))
