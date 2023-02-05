import cohere
from cohere.classify import Example
import numpy as np 
from sklearn import metrics 

co = cohere.Client('fZf3vVCtJkS69wYLEJWyr8WGRUupRJ4NnMSUwL0e') # This is your trial API key

def rheaModel():
  """
  response = co.classify(  
    model='<model>',  
    inputs=inputs)
  """ 
  response = co.classify(
  model='48112639-5bee-4b80-8f70-1f5f60b645fe-ft',
  inputs=["I'm gonna kill myself.", "Today was really boring."]) # add more examples, here we should add parsed user data from social media accounts

  ys = [] 
  preds = [] 
  flag = 0 

  for line in response: 
    if line.prediction == "suicide": 
      ys.append(1) 
      flag = 1 
    else: 
      ys.append(0) 
    preds.append(line.confidence) 

  y = np.array(ys)  
  pred = np.array(preds) 

  fpr, tpr, thresholds = metrics.roc_curve(y, pred)

  auc = metrics.auc(fpr, tpr) 

  return auc, flag 

print(rheaModel()) 