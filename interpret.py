import pickle
import numpy as np
with open('para_wrong_prediction.pkl', 'rb') as f:
    wrong_prediction = pickle.load(f) # 단 한줄씩 읽어옴

with open('para_wrong_problem.pkl', 'rb') as f:
    wrong_problem = pickle.load(f) # 단 한줄씩 읽어옴

total_count = 0
in_content_count = 0
not_real_count = 0
real_indexes = []
not_real_indexes = []

for idx, problem in enumerate(wrong_problem[:340]):
    context = problem['context']
    answer = problem['answers']
    question = problem['question']
    prediction = wrong_prediction[idx]
    print("context", context)
    print("question", question)
    print("answer :", answer)
    print("model prediction :", prediction)
    print()


for idx, problem in enumerate(wrong_problem):
    context = problem['context']
    answer = problem['answers']
    for answer in answer['text']:
        if answer in wrong_prediction[idx]:
            not_real_indexes.append(idx)
            break
        elif wrong_prediction[idx] in answer:
            not_real_indexes.append(idx)
            break


real_indexes = [i for i in range(len(wrong_problem))]
for index in not_real_indexes:
    real_indexes.remove(index)


#print("total_count", total_count, "in_content_count", in_content_count, "not_real_count", not_real_count)
real_wrong_prediction = np.array(wrong_prediction)[real_indexes]
real_wrong_problem = np.array(wrong_problem)[real_indexes]

for idx, problem in enumerate(real_wrong_problem):
    context = problem['context']
    answer = problem['answers']
    print(context)
    print("question", problem['question'])
    print("answer", answer)
    print("my answer", real_wrong_prediction[idx])
    print()


In the United States, there has been a push to legalize importation of medications from Canada and other countries, in order to reduce consumer costs. While in most cases importation of prescription medications violates Food and Drug Administration (FDA) regulations and federal laws, enforcement is generally targeted at international drug suppliers, rather than consumers. There is no known case of any U.S. citizens buying Canadian drugs for personal use with a prescription, who has ever been charged by authorities.
question What is one country that has been suggested for importation of medicines for personal use with a prescription?
answer {'answer_start': [88, 88, 88], 'text': ['Canada', 'Canada', 'Canada']}
my answer United States
