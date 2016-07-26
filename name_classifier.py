import numpy as np
import nltk
from nltk.tag.perceptron import PerceptronTagger
from sklearn.preprocessing import label_binarize
from sklearn.naive_bayes import MultinominalNB
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from matplotlib.pyplot import pyplot as plt

tagger = PerceptronTagger()
name_tag = []
non_name_tag = []
full_names = []
non_names = []

with open('full_names.txt') as infile:
    full_names = infile.read().splitlines()

with open('non_names.txt') as infile:
    non_names = infile.read().splitlines()

for x in full_names:
    tags = nltk.ne_chunk(tagger.tag(x.split())).pos()
    name_tag.append(tags[0][0][1]+' '+tags[0][1]+' '+tags[1][0][1]+' '+tags[1][1])

for x in non_names:
    tags = nltk.ne_chunk(tagger.tag(x.split())).pos()
    non_name_tag.append(tags[0][0][1]+' '+tags[0][1]+' '+tags[1][0][1]+' '+tags[1][1])

name_tag = [w.split() for w in name_tag]
non_name_tag = [w.split() for w in non_name_tag]

train_data = np.vstack((np.array(name_tag), np.array(non_name_tag)))
train_f1 = label_binarize(train_data[:,0], classes=list(set(train_data[:,0])))
train_f2 = label_binarize(train_data[:,1], classes=list(set(train_data[:,1])))
train_f3 = label_binarize(train_data[:,2], classes=list(set(train_data[:,2])))
train_f4 = label_binarize(train_data[:,3], classes=list(set(train_data[:,3])))

train_features = np.hstack((train_f1, train_f2, train_f3, train_f4))
train_output = np.hstack((np.ones(len(name_tag)), np.zeros(len(non_name_tag))))
train_output = train_output.reshape(len(train_output),1)

def get_features(word):
	tags = nltk.ne_chunk(tagger.tag(word.split())).pos()
	return tags[0][0][1]+' '+tags[0][1]+' '+tags[1][0][1]+' '+tags[1][1]

test_names = ['Jun Wang', 'Nishant Dahad','Alison Cheung','Naomi Nguyen','Preembarrass Hippogryph', 'Fustellatrici Pazze Perugia e dintorni', 'Undercloth Reclothe', 'Chinese New Year', 'Thames River']

test_data = []
for name in test_names:
	test_data.append(get_features(name))

test_data = [w.split() for w in test_data]
test_data_np = np.array(test_data)
test_f1 = label_binarize(test_data_np[:,0], classes=list(set(train_data[:,0])))
test_f2 = label_binarize(test_data_np[:,1], classes=list(set(train_data[:,1])))
test_f3 = label_binarize(test_data_np[:,2], classes=list(set(train_data[:,2])))
test_f4 = label_binarize(test_data_np[:,3], classes=list(set(train_data[:,3])))

test_features = np.hstack((test_f1, test_f2, test_f3, test_f4))
test_output = np.hstack((np.ones(4), np.zeros(5)))

clr = MultinominalNB()
clr.fit(train_features, train_output)
predicted_output = clr.predict(test_features)

print "Precision score:", precision_score(test_output, predicted_output)
print "Recall score:", recall_score(test_output, predicted_output)
print "F1 score :", f1_score(test_output, predicted_output)
print "Area under curve :", roc_auc_score(predicted_output, test_output)

roc_score = roc_auc_score(test_output, predicted_output)
plt.title('Receiver Operating Characteristic curve')
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f'%roc_score)
plt.legend(loc='lower right')
plt.ylabel('True positive Rate')
plt.xlabel('False positive Rate')
plt.show()