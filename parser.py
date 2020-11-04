import json

print("Input the filename of the downloaded file (Make sure you include the file extension)")
filename = input(" > ")
f = open(filename, "r", encoding="utf8")
quizInfo = json.loads(f.read())

def deUnicode(inp_string):
    string = r'{}'.format(inp_string)
    for letter, i in zip(string, range(len(string))):
        try:
            if letter == "\\" and string[i + 1] == "u":
                print("Done")
                string = string[:i] + string[i + 6:]
        except:
            pass
    return string

allAns = {}
for question in quizInfo["data"]["quiz"]["info"]["questions"]:
    if question["type"] == "MCQ":
        #? Single answer
        if question["structure"]["options"][int(question["structure"]["answer"])]["text"] == "":
            #? Image answer
            answer = question["structure"]["options"][int(question["structure"]["answer"])]["media"][0]["url"]
        else:
            answer = question["structure"]["options"][int(question["structure"]["answer"])]["text"]
    elif question["type"] == "MSQ":
        #? Multiple answers
        answer = []
        for answerC in question["structure"]["answer"]:
            if question["structure"]["options"][int(answerC)]["text"] == "":
                answer.append(question["structure"]["options"][int(answerC)]["media"][0]["url"])
            else:
                answer.append(question["structure"]["options"][int(answerC)]["text"])

    questionStr = question["structure"]["query"]["text"].replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n")
    allAns[questionStr] = answer.replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "").replace("<br/>", "\n")

with open("answers.txt", "w") as f:
    for i in allAns.keys():
        f.write(f'QUESTION: {i}\n\nANSWER :{allAns[i]}\n\n\n')


# f = open("answers.txt", "w")
# f.write(str(json.dumps(allAns, sort_keys=True, indent=2)).replace("{", "").replace("}", "").encode("utf8").decode("unicode-escape"))
