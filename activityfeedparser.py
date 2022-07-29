import re


string = input("Input xAPI-generated activity feed:")
repls_game = {"\"":"", ":":": "}
repls_name = {"\"":"", ":":": "}
repls_date = {"\"":"", "date:":"Date: ", "T":" | Time: "}
output = []

match_game = re.findall(r'\"vuiDisplayName...([\s\S]*?)\"', string, flags=re.IGNORECASE)
match_name = re.findall(r'\"achievementName...([\s\S]*?)\"', string, flags=re.IGNORECASE)
match_date = re.findall(r'\"date.{26}', string, flags=re.IGNORECASE)
if match_game or match_name or match_date:
    print("\nOUTPUT: \n")
    for i in match_game:
        for key, value in repls_game.items():
            i = i.replace(key, value)
        output.append("Game: \"" + i + "\"")

    n = 0    
    for i in match_name:
        for key, value in repls_name.items():
            i = i.replace(key, value)
        if(n <= len(output) - 1):
            output[n] = output[n] + " | Achievement Name: " + "\"" + i + "\""
        n += 1
    
    n = 0
    for i in match_date:
        for key, value in repls_date.items():
            i = i.replace(key, value)
        if(n <= len(output) - 1):
            output[n] = output[n] + " | " + i
        n += 1
print('\n'.join(output))
    