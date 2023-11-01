from Question import Question

question_prompts=[
    "who is the pm of  india?\n (a) srujan\n (b)modi\n (c) yogi\n (d) draupathi\n",
    "who is the president of india?\n (a) srujan\n (b)modi\n (c) yogi\n (d) draupathi\n",
    "who is the cm of  up?\n (a) srujan\n (b)modi\n (c) yogi\n (d) draupathi\n"
]

questions=[
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"d"),
    Question(question_prompts[2],"c")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1

    print("you got "+str(score)+"/"+str(len(questions))+" correct")

run_test(questions)