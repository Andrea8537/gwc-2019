# friend_ages = {"Anna" : 17, "Emma" : 17, "Tom" : 18}
# print(friend_ages)

# qlist=["What's your name", "What's you age"]


def takesurvey(q_list, a_list):
        anwer ={}
        for q in q_list:
            answer[q] = input(q)
        # print(answer)
        a_list.append(answer)
        # print(answers)

a=[]
q=["what's your name?", "what is your age?", "what's your favorite ice cream?", "What State do you live in", "What color is your hair"]
for i in range(5):
    takesurvey(q,a)
    print(answers)
    # anwers ={}
    # for q in questions:
    #     answer[q] = input(q)
    # print(answer)
    # answers.append (answer)
    # print(answers)
