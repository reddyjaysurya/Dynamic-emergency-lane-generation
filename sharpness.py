TP=0
TN=0
FP=0
FN=0
for i in range(len(X)):
    if(labels[i]==0):
        if(X[i][0]<14):
            TP=TP+1
    if(labels[i]==1):
        if(X[i][0]>14):
            TN=TN+1
    if(labels[i]==0):
        if(X[i][0]>14):
            FP=FP+1
    if(labels[i]==1):
        if(X[i][0]<14):
            FN=FN+1
print((TP+TN)/(FP+FN+TP+TN))