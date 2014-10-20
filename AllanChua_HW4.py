# Allan Chua
# HW4

# 1) Create a new ipython notebook .

# 2) Discuss with your team and decide if you would like to use the same data set for your final 
#project. You can stay with it or you can find a new one. Data can come from a csv file, a text file, 
#or a JSON object. 

# 3) Import your data set to pandas. Re-create any reshaping operations you did in R for homework 
get_ipython().magic(u'pylab inline')
import pandas
import pylab
import pickle
import matplotlib as mp
import matplotlib.pyplot as plt

olympics = pd.read_excel('OlympicAthletes.xlsx', encoding = 'utf-8')

#2. If your dataset is new, provide a short data manual as a separate pdf.
#not new, its a olympic medal data for many countries

# 4) Get numerical summaries for all your variables. 
olympics.describe()

# 5) Comment on and perform any needed treatment for missing values.
olympics['Athlete'] = olympics['Athlete'].replace(np.nan, "Missing")
#replaces empty athletes with missing

# 6) Comment on and perform any needed data transformations.
# no data transformations needed

# 7) Get three visualizations that you consider meaningful.

# 1, histogram for atheletes home country 
pl.xlabel("Country")
pl.ylabel("Frequency")
pl.title("Olympic Athlete Countries: Histogram")
pl.hist(olympics['Country'])
pl.show()

# 2, bar chart for number of gold medals won by selected countries
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

# 3 a scatterplot for the number of sports vs the country
plt.title("Sport vs. Country : Scatterplot")
plt.xlabel("Sport")
plt.ylabel("Country")
plt.scatter(olympics['Sport'], olympics['Country'])
plt.savefig('scatter1.png') 

#8) Save your data as a pickle. 
olympics.to_pickle('olympics_pickle')

#9) Update your project repository on Git with the pickled file. Include a comment of what you did 
#in the description of the commit.

#10) Download your HW4 notebook as .py, and upload it to Dropbox and GitHub.