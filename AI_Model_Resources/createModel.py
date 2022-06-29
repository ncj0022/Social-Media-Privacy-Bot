from preprocess import *
import pandas as pd
import sklearn
import pickle
from sklearn import preprocessing
from sklearn import naive_bayes,svm,linear_model
from sklearn.model_selection import GridSearchCV,train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

def link_to_bool(temp):
    if not temp:
        return False
    else:
        return True

def best_parameters_test(parameters,train_tf,test_tf,y_train,y_test,model_choice):

    scores = ['precision', 'recall']

    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print()

        clf = GridSearchCV(
            model_choice, parameters, scoring='%s_macro' % score
        )
        clf.fit(train_tf, y_train)

        print("Best parameters set found on development set:")
        print()
        print(clf.best_params_)
        print()
        print("Grid scores on development set:")
        print()
        means = clf.cv_results_['mean_test_score']
        stds = clf.cv_results_['std_test_score']
        for mean, std, params in zip(means, stds, clf.cv_results_['params']):
            print("%0.3f (+/-%0.03f) for %r"
                % (mean, std * 2, params))
        print()

        print("Detailed classification report:")
        print()
        print("The model is trained on the full development set.")
        print("The scores are computed on the full evaluation set.")
        print()
        y_true, y_pred = y_test, clf.predict(test_tf)
        print(classification_report(y_true, y_pred))
        print()

def main():
    tfid_path = "AI/pickle_dumps/tfid.pickle"
    naive_path = "AI/pickle_dumps/naive.pickle"
    svm_path = "AI/pickle_dumps/svm.pickle"

    tweet_data = preprocess()

    df = pd.DataFrame(tweet_data, columns=['text','links','emojis','labels'])
    #print(df.head())

    x_train, x_test, y_train, y_test = train_test_split(df['text'],df['labels'],test_size=0.2)

    
    #models = pd.DataFrame(columns=['models','model_object','score'])
      
    #      
    # Term frequency inverse document frequency: convert text to numerical format 
    # other ways: count vectorizering and ngrams
    tf_vect = TfidfVectorizer()
    tf_vect.fit(df['text'])

    pickle.dump(tf_vect,open(tfid_path,'wb'))
    tf_pickle = pickle.load(open(tfid_path,'rb'))
    train_tf = tf_pickle.transform(x_train)
    test_tf = tf_pickle.transform(x_test)

    # NAIVE BAYES
    Naive = naive_bayes.MultinomialNB()
    Naive.fit(train_tf,y_train)# predict the labels on validation dataset
    pickle.dump(Naive,open(naive_path,'wb'))
    naive_pickle = pickle.load(open(naive_path,'rb'))
    predictions_NB = naive_pickle.predict(test_tf)# Use accuracy_score function to get the accuracy
    print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, y_test)*100)
    print("Prediction for [0]:",predictions_NB[0])
    print("test x value:",x_test.head(1))
    print("test y value:",y_test.head(1))

    

    # Classifier - Algorithm - SVM
    # fit the training dataset on the classifier
    SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
    SVM.fit(train_tf,y_train)# predict the labels on validation dataset
    pickle.dump(SVM,open(svm_path,'wb'))
    svm_pickle = pickle.load(open(svm_path,'rb'))
    predictions_SVM = svm_pickle.predict(test_tf)# Use accuracy_score function to get the accuracy
    print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, y_test)*100)
    print(predictions_SVM[0])
    
    # #SVM gridsearch
    # parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]}, {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
    # best_parameters_test(parameters,train_tf,test_tf,y_train,y_test,svm.SVC())

    # #Naive Bayes gridsearch
    # parameters = {}
    # best_parameters_test(parameters,train_tf,test_tf,y_train,y_test,naive_bayes.MultinomialNB())


if __name__ == "__main__":
    main()