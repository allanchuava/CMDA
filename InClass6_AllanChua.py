# Allan Chua
# Inclass 6_1

# 1) Download data from Scholar/Resources/Data/Ch06.
# done

# 2) Create a new ipython notebook, Inclass6_1.
# done

# 3) Import work_tab, work_comma, and last two 
#observations from stress2_1 file as pandas 
#DataFrames. If needed, manage data to display in 
#correct format as a pandas Data Frame
import pandas
import numpy
import json
import requests
table1 = pd.read_csv('work_comma.csv')
table1
table2 = pd.read_table('work_tab.txt')
table2
table3 = pd.read_table('stress2_1.txt', 
table3
	skiprows = 19, header = None, sep = '\s+')


# 4) Use the github API to create a pandas data frame with 
#4 columns from the returned results. 
r = requests.get('https://api.github.com/events')
t = r.json()

dframe = pandas.DataFrame(t, numpy.random.randn(, 4))
dframe

# 5) Save the DF from part 4 as a pickle. Load the pickle.
dframe.to_pickle('dframe_pickle')
pandas.read_pickle('dframe_pickle')

# 6) Save the data in part 4 in HDF5 format. Access it.
store = pandas.HDFStore('apidata.h5')
store = ['dframe'] = dframe
store['dframe']

##############################################################
# Inclass6_2
import xlrd
import datetime
# 1) Import your project data using one of the read_csv or read_table methods for 
#pandas.
olympics = pandas.read_excel('OlympicAthletes.xlsx', encoding = 'utf-8')

# 2) Describe your dataframe using.describe() method.
olympics.describe()

# 3) Choose one numeric variable and transform it into categorical, with 3-5 
# categories. 
year_bins = [2000, 2002, 2004, 2006, 2008, 2010]
olympics['year_categorical'] = pandas.cut(olympics['Year'], year_bins)
year_categorical = olympics['year_categorical']

# 4) Get the frequencies for the categorical variable created in part 3.
pandas.value_counts(year_categorical)

#5) Create an additional variable using mapping and using the categorical variable 
#from part 3. Your map dictionary should have two elements.
season = {'(2000, 2004]': 'summer_games', '(2002, 2006]' : 'winter_games'}
olympics['season'] = olympics['year_categorical'].map(season)

#6) Rename two columns in your data using .rename.
olympics = olympics.rename(columns = {'year_categorical' : 'year range', 'season' : 'year group'})

#7) Extract a 50% training set using cut random permutations of rows (eg. If you 
#have 101 rows in your dataframe, a 50% training set will have about 51 rows).
s1 = numpy.random.permutation(len(olympics))
t1 = s1[0 : (len(s1)/2)]
t1 = olympics.take(t1)

#8) Extract a second 50% training set.
s2 = np.random.permutation(len(olympics))
t2 = s2[0 : (len(s2))/2]
t2 = olympics.take(t2)

#9) Combine the two training sets into a third dataframe.
t = t1.append(t2)
t_total = len(t)

#10) Get rid of duplicate rows by using: dataframe_name.drop_duplicates(). What 
#percentage of the rows you have left?
t = t.drop_duplicates()
t_short = len(t)
#percentage is t_short divided by t_total, which is about 70 percent