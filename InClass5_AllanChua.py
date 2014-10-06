# Allan Chua
# Inclass 5_1

# 1) Run ipython
# done

# 2) Import modules pandas, numpy and matplotlib
# done

# 3)  Select 5 commands from these modules. Find a way to look for these function using ? and wildcards
# 

pandas.*cat?
pandas.*ver*?
numpy.*ning*?
numpy.int*?
matplotlib.func_*?

# 4) Use all the short-cut commands
# done

# 5) Run all the magic commands.
# done

# 6)  Use your Inclass4_3, Part I and run snippets of code in iPython by copy-paste
# done

# 7)  Introspect magic command %xdel, function str.split, module re and matplotlib.pylab

%xdel 				#This deletes a variable. It tries to clear it from anywhere that
# IPython's machinery has references to it.
str.split			#Returns a list of the words in the string S, 
# using sep as the delimiter string.
matplitlib.pylab	#This is a procedural interface to
# the matplotlib object-oriented plotting library.


# 8)  Start pylab; build the plot on slide 10; do tab completion on numpy.;do introspection on 
# numpy.random; find the line about randn. What type of numbers does it generate?

numpy.random	Random number generation function
randn			Generates random numbers between 0-1
randn                Normally distributed values.

# 9) Find out what cumsum does.

cumsum		This returns the total sum of the elements along the given axis

# 10) How long does it take to generate 100 normally distributed random numbers? How about 
# 1000? How about 10,000?How did you find that out?(hint: run magic command timeit)


100   Random Numbers  is  100000 loops, best of 3: 5 µs per loop
1000  Random Numbers  is  10000 loops,  best of 3: 38.6 µs per loop
10000 Random Numbers  is  1000 loops,   best of 3: 379 µs per loop


# InClass5_2
##########################################################################

# 1) Create a new ipython notebook “Inclass5_2”
# done

# 2) Create two one-dimensional arrays with 5 elements of your choice. Display arrays’ shape and type.
group1 = [1, 2, 3, 4 ,5]
group2 = [6, 7, 8, 9 ,10]

array1 = np.array(group1)
array2 = np.array(group2)

array1.dtype
array1.shape

array2.dtype
array2.shape

# 3) Do element-wise summation for the two arrays. 

arraySum = array1 + array2
arraySum

# 4) Do element-wise product for the two arrays.

arrayProduct = array1 * array2
arrayProduct

# 5) Create a 6X6 identity matrix.
idenmatrix = eye(6)
idenmatrix

# 6) Replace all element on third row with value 5.
idenmatrix[2,] = 5
idenmatrix

# 7) Replace all elements that are not zero with value 6 using a boolean indexing and slicing.
idenmatrix[idenmatrix!=0] = 6

# 8) Create an empty 3 dimensional array, arr3 with shape (2,3,4), and elements of integer type. 
arr3 = np.empty((2,3,4))

# 9) Display its number of dimensions, shape and type of each element. 
arr3.dtype
arr3.shape
arr3.ndim

# 10) Give the second element on the third dimension, from the second group on the second dimension, 
# from the first group on the first dimension the value 5.
arr3[0,1,1] = 5

# 11) Generate an array of 20 uniformly distributed random numbers with values between 0 and 1.
randarray = rand(20)

# 12) Get the min, max, sum, mean, and standard deviation of the array in part 11.
randarray.min()
randarray.max()
randarray.sum()
randarray.mean()
randarray.std()

# 13) Replace all elements less than 0.5 with 0 and all elements larger than 0.5 with 1
# in the array from part 11 using “where” function.
randarray[randarray < 0.5] = 0
randarray[randarray > 0.5] = 1

# 14) Sort the array in part 11.
np.sort(randarray)

# 15) Find the unique values in the same array.
unique(randarray)

# 16) Save your ipython notebook and download it as .py. Open it with your editor (Notepad++ etc.) 
# and make sure that there are correct and complete comments delimiting all your code and output. 
# done


############################################################################
# InClass5_3

# 1) Go to quandl.com. Open an account. Go to the “Account Settings” and make note of your API Key
# done

# 2) Go to https://github.com/quandl/Python. Click on “Download ZIP”. Unzip folder and copy 
#“setup.py” and “Quandl” folders into your local folder where you run ipython. (EG: 
#C:\Users\Denisa)
# done

# 3) Create a new ipython notebook, In5_3. Import pandas module. Import Quandl module by 
#“import Quandl”. Since we already have the required NumPy and Pandas modules, it should 
#work for you.
import pandas as pd
import Quandl as ql

#4) Go to https://www.quandl.com/c/markets/bitcoin-data
# done

# 5) You will import data for Bitcoin exchange rates to USD on different venues: Bitstamp, Bitfinex 
#and LakeBTC. Go to:
#https://www.quandl.com/BCHARTS/BITSTAMPUSD
#Click on “Python” Library on the right. The code you need to use to import data will show up.
#Import only 2014 data to September30. Use your authentication key. Example code:
#bitstamp = Quandl.get("BITCOIN/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-
#30", authtoken="2_mykey_T")
#Import in separate DataFrames the data for Bitfinex and LakeBTC as well. 

bitStamp = ql.get("BCHARTS/BITSTAMPUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")
bitFinex = ql.get("BAVERAGE/USD_BITFINEX", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")
lakeBTC = ql.get("BCHARTS/LAKEUSD", trim_start="2014-01-01", trim_end="2014-09-30", authtoken="d2RqcjFpy3hu6apaVJrP")

# 6) View your three created pandas data frames using df_name.head(). What are the column 
#names? What is the frequency of data (daily/weekly/yearly Bitcoin prices)? Answer in comments
bitStamp.head()
## Column Names: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
## Frequency of Data: Daily
bitFinex.head()
## Column Names: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
## Frequency of Data: Daily
lakeBTC.head()
## Column Names: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
## Frequency of Data: Daily

# 7) Create three objects ind1, ind2, and ind3 containing the index of each of the created 
# dataframes.
ind1 = bitStamp.index
ind2 = bitFinex.index
ind3 = lakeBTC.index

# 8) Display ind1, ind2, ind3. How many elements are in each?
ind1
## 774 elements
ind2
## 332 elements
ind3
## 212 elements

# 9) Display the .values attribute of each of ind1, ind2, ind3. What type of object is being displayed 
# for each? What dtype is each element of the displayed object? Answer with comments.
ind1.values
## ind1 is A date of dtype: datetime64[ns]
ind2.values
## ind2 is A date of dtype: datetime64[ns]
ind3.values
## ind3 is A date of dtype: datetime64[ns]

# 10) Display the .columns attribute of each DataFrame. How many columns do we have in each?
bitStamp.columns
# there is 7 columns in the DataFrame
bitFinex.columns
# there is 7 columns in the DataFrame
lakeBTC.columns
# there is 7 columns in the DataFrame

# 11) Drop the variable showing BTC volume from each dataframe using the .drop method.
bitStamp.drop("Volume (BTC)", axis=1)
bitFinex.drop("Volume (BTC)", axis=1)
lakeBTC.drop("Volume (BTC)", axis=1)

# 12) Download your saved ipython notebook as .py, edit the content with your editor, add it to the 
# overall Inclass5 assignment marking it clearly as Part 5_3. 
#done

# 13) Upload your finalized Inclass 5 (containing the three parts from Mon, Wed and Frid) to Dropbox 
#and GitHub.
# done
