import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('valid_answer_non_para.pkl', 'rb') as f:
    list_valid_answer = pickle.load(f) # 단 한줄씩 읽어옴


score_list = []
text_list = []
for valid_answer in list_valid_answer:
    scores = []
    texts = []
    for idx, data in enumerate(valid_answer):
        scores.append(data['score'])
        texts.append(data['text'])
    score_list.append(scores)
    text_list.append(texts)

peak_list = []
for scores in score_list:
    peaks = []
    for idx, score in enumerate(scores):
        if idx==0 or idx==len(scores)-1: # start, end point eliminate
            continue
        if scores[idx-1] < scores[idx] and scores[idx] > scores[idx+1]:
            peaks.append(idx)
    peak_list.append(peaks)

text_peak_list = []
score_peak_list = []
for i, peaks in enumerate(peak_list):
    text_peaks = []
    score_peaks = []
    for j, peak in enumerate(peaks):
        text_peaks.append(list_valid_answer[i][j]['text']) 
        score_peaks.append(list_valid_answer[i][j]['score']) 
    text_peak_list.append(text_peaks)
    score_peak_list.append(score_peaks)

'''
print("전체 score들의 mean", np.mean([np.mean(score_list[i]) for i in range(len(score_list))]))
print("peak score들의 mean", np.mean([np.mean(score_peak_list[i]) for i in range(len(score_peak_list))]))
print("전체 score들의 std", np.mean([np.std(score_list[i]) for i in range(len(score_list))]))
print("peak score들의 std", np.mean([np.std(score_peak_list[i]) for i in range(len(score_peak_list))]))
'''

# confidence 구하기

confidences = []
for score_peaks in score_peak_list:
    whole_score = sum(score_peaks)
    confidence = score_peaks[0] / whole_score
    confidences.append(confidence)
    #print("confidence", confidence) 
'''
with open('confidence_para.pkl','wb') as f:
    pickle.dump(confidences,f)
'''

for idx, scores in enumerate(score_list):
    print(confidences[idx])    
    plt.plot(score_list[idx])
    #plt.rc('xtick', labelsize=8)  # x축 눈금 폰트 크기 
    #plt.xticks(rotation=90)
    #plt.plot(scores)
    plt.show()
