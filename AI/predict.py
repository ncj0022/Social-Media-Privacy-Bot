from preprocess_flask import *
import pickle
import json
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer


#Loads pickle matrices/models and uses the inputted tweet object [[text],[text]..] to be predicted
#Returns 
def predict_text(tweet_object, tweet_id):
    if tweet_object == [[]]:
        return  None
    tfid_path = os.getcwd() + "/pickle_dumps/tfid.pickle"
    svm_path = os.getcwd() + "/pickle_dumps/svm.pickle"
    naive_path = os.getcwd() + "/pickle_dumps/naive.pickle"

    tf_convert = pickle.load(open(tfid_path,'rb'))
    svm_model = pickle.load(open(svm_path,'rb'))
    naive_model = pickle.load(open(naive_path,'rb'))
    
    tweet_clean = preprocess(tweet_object)
    print(tweet_object)

    tweet_df = pd.DataFrame(tweet_clean,columns=['text'])
    print(tweet_df)
    input_tf = tf_convert.transform(tweet_df['text'])
    predictions_SVM = svm_model.predict(input_tf)
    predictions_NB = naive_model.predict(input_tf)

    print("Prediction NB:",predictions_NB)
    probability = naive_model.predict_proba(input_tf)
    print(probability)
    response = {}

    if len(tweet_object) > 1: #multiple tweets
        sums = 0
        temp = 0
        x = 0
        for item in range(0, len(tweet_object)):
            sums += int(predictions_NB[item])
            if x < probability[item][1]:
                x = probability[item][1]
                temp = tweet_id[item]
        spam_percentage = sums/len(tweet_object)

        response.update({
            'tweet': temp,
            'prediction': spam_percentage, #percentage
            'tweet_probability': x 
        })

    
    else: #single tweet
        for item in range(0, len(tweet_object)):
            tweet_text = tweet_id[item]
            prediction = predictions_SVM[item]
            tweet_probability = probability[item][int(prediction)]
            response.update({
                'tweet': tweet_text,
                'prediction': prediction,
                'probability': tweet_probability
            })

    
    return json.dumps(response)