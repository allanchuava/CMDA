# Allan Chua
# Inclass 7_1

# 1) Create a new ipython notebook.
# done
get_ipython().magic(u'pylab inline')

import pandas
import numpy
import matplotlib as mp
import matplotlib.pyplot as plt
import scipy

#project data, the olypmics data set

olympics = pd.read_excel('OlympicAthletes.xlsx', encoding = 'utf-8')

# 2) Use the data for your project as a panda dataframe.
# done

# 3) For suitable variables, plot : 
# 1. a histogram;
pl.xlabel("Country")
pl.ylabel("Frequency")
pl.title("Olympic Athelete Countries: Histogram")
pl.hist(olympics['Country'])
plt.savefig('hist1.png') 

# 2. a density plot;
pl.xlabel("Country")
pl.ylabel("Frequency")
pl.title("Olympic Athlete Countries: Density Plot")
olympics['Country'].plot(kind='kde')
plt.savefig('kde1.png')


# 3. a bar chart; 
# bar chart for number of gold medals won by selected countries
gold = olympics['Gold Medals'] >= 1

usa = olympics.Country == "United States"
china = olympics.Country == "China"
russia = olympics.Country == "Russia"

usaGold = len(olympics[usa & gold])
chinaGold = len(olympics[china & gold])
russiaGold = len(olympics[russia & gold])

goldCountries = {'USA' : usaGold, 
'China': chinaGold,
'Russia': russiaGold}

countryDF = pd.DataFrame.from_dict([goldCountries])
countryDF = pd.DataFrame(countryDF.transpose())
countryDF.columns = ['Gold']

colors=['gold']
countryDF.plot(kind='bar', title="Medals", color=color)
plt.savefig('bar1.png') 

# 4. a horizontal stacked bar chart with categories summing to 1;
countryRel = countryDF.div(countryDF.sum(1).astype(float), axis=0)
colors=['gold']
countryRel.plot(kind='barh', stacked=True, title="Medals: Relative", color=colors)
plt.savefig('bar2.png') 

# 5. a scatterplot.
plt.title("Sport vs. Country : Scatterplot")
plt.xlabel("Sport")
plt.ylabel("Country")
plt.scatter(olympics['Sport'], olympics['Country'])
plt.savefig('scatter1.png') 

# 4) Save all figures as png in your working directory. Submit the pngs with your in 
# class assignment.
# done

#####################################################################
# InClass 7_2

#1. Create a new ipython notebook Inclass7_2.ipynb.
#done
get_ipython().magic(u'pylab inline')
import scipy
import pandas
import numpy
import matplotlib.pyplot as plt
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

#2. Download Medical.csv from scholar/Data and import it as a pandas dataframe. You will 
#train a linear classifier to separate diabetic subjects (all subjects included in the dataset 
#are diabetic) into two classes of health literacy (how much they know about health) based 
#on their age and measured average blood glucose.
#done

#3. Wrangle your data with pandas. Keep features “age” and “HgA1c”. Create target variable 
#literacy with levels 0=“low literacy” and 1= “high literacy” based on the dataframe’s
#variable “literacy” with levels “low” and “high”.
medical = pd.read_csv('Medical.csv')
medical.replace(to_replace='HIGH',value=1, inplace=True)
medical.replace(to_replace='LOW',value=0, inplace=True)

#4. Setup the numpy arrays X and y.
X = array(medical[['Age', 'HgA1C']])
y = array(medical['A Literacy Category'])

#5. Take a 75% training set and a 25% testing set using the scikit-learn capabilities.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

#6. Scale your features.
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#7. Train the classifier. Write out the classifier’s equation.
clif = SGDClassifier()
clif.fit(X_train, y_train)
print 'Classifier Equation: '
print str(clif.intercept_[0]) +' + (' + str(clif.coef_[0][0]) + ')* x1 +
 (' + str(clif.coef_[0][1]) + ')* x2 = 0'

#8. What is the classifier’s accuracy on the training data?
y_train_prediction = clif.predict(X_train)
metrics.accuracy_score(y_train, y_train_prediction)
#it was about 89 percent accuracy

#9. What is the classifier’s accuracy on the test set?
y_test_prediction = clf.predict(X_test)
metrics.accuracy_score(y_test, y_test_prediction)
# it was 100 percent

#10. What is the confusion matrix and what is the interpretation of each number in the 
#matrix?
m1 = metrics.confusion_matrix(y_train, y_train_prediction)
# the classifier predicted the wrong result: low:0 and high:4
# classifier predicted the right result: low:0 and high:33
m2 = metrics.confusion_matrix(y_test, y_test_prediction)
# classifier predicted 13 correct but had to low results, its not safe to count

#11. Comment on the quality of this classifier for this problem.
# the classifier was correct in identifying all of the literacy levels
# but there was missing low literacy scores so the data is not complete.
# There is no relationship between age and literacy level

##############################################################
# InClass 7_3
#1) Download the PCA notebook from Scholar 
#Resources/Assignments.
#done
get_ipython().magic(u'pylab inline')
import sklearn
import numpy
import scipy
import pandas
import matplotlib.pyplot as plt

#2) Run the code to get the principal components, and create the 
#scatterplot. Comment on what digits are easiest to separate 
#and which one might be easily confounded, using only the 
#information carried in the first two principal components.
from sklearn.datasets import load_digits
digits = load_digits()
print digits.keys()
digits.target_names
X_digits, y_digits = digits.data, digits.target
X_digits.shape
from sklearn.decomposition import PCA
estimator = PCA(n_components=10)
X_pca = estimator.fit_transform(X_digits)
X_pca.shape
X_pca
colors = ['gray', 'orange', 'cyan', 'lime', 'red', 
'white', 'yellow', 'purple', 'blue', 'black']
for i in xrange(len(colors)):
    px = X_pca[:, 0][y_digits == i]
    py = X_pca[:, 1][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

#3) Modify the scatterplot code to visualize the last two principal 
#components (8 and 9). Change the axes labels accordingly.
colors = ['gray', 'orange', 'cyan', 'lime', 'red', 
'white', 'yellow', 'purple', 'blue', 'black']
for i in xrange(len(colors)):
    px = X_pca[:, 8][y_digits == i]
    py = X_pca[:, 9][y_digits == i]
    plt.scatter(px, py, c=colors[i])
plt.legend(digits.target_names)
plt.xlabel('Ninth Principal Component')
plt.ylabel('Tenth Principal Component')

#4) Comment on the ability of this new visualization to distinguish 
#between images of digits. 
# Most of the data is focused toward the center of the plot (0,0)
# It doesn't give easy recognition digits as the say a scatterplot 
# or other visual

#5) Save your version of notebook with all your comments and 
#scatterplots and submit to Drop Box and GitHub, in addition to 
#placing the .py download in your overall InClass7 assignment. 