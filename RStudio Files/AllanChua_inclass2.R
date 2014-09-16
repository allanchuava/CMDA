#allan Chua
#in class assignment 2
#1)
load('exampleData.rData')
summary(custdata)

summary(custdata$is.employed) # 328 people did not enter data for employment
summary(custdata$income)# the max income is 615,000! wow thats an outlier
summary(custdata$age)# the highest age is 146! wow that is old!

summary(custdata$state.of.res) # the majority live in california
summary(custdata$custid)# the min and max are very far apart
summary(custdata$sex)# majority is male 56%
summary(custdata$is.employed)#majority is employed, a couple have no information
summary(custdata$martial.stat)#majority are married
summary(custdata$health.ins)#most have insurance, no data is missing
summary(custdata$housing.type)# split between homeowner with morgage, and rented
summary(custdata$recent.move)#most have not moved, 56 with no data
summary(custdata$num.vehicles)#wow the max is 6 cars owned!
summary(custdata$age.normalized)# the minimum is negative
summary(custdata$gp)# pretty evenly spread out
summary(custdata$Median.Income)#pretty evenly spread out
summary(custdata$income.norm)#the minimum income is negative
summary(custdata$income.lt.30k)#majority make more thank 30k
summary(custdata$age.range)#majority are from 25-65

#2)
#ucicar
#the variable buying is all the same at 432
#same with maintanence
#same with doors at 432
#persons is the same 576
#so is lug boot and safety
#rating is different majority is uncacc

#3)
load('credit.RData')
summary(d)
#there are more females 210 that are divored, married or separated, compared to males 92
#most of the men are single compared to women
#most German loans don't need a co-applicant or guarantor since there are 907 loans with out those

install.packages("hexbin")
library(hexbin)
library(ggplot2)

#extract a subset of the dataset with reasonable values for the two 
#variables
custdata2 <- subset(custdata,
                    (custdata$age > 0 & custdata$age < 100
                     & custdata$income > 0))

#get a numerical summary of the relationship between the two
cor(custdata2$age, custdata2$income) #weak negative relationship
#gplot.hexbin(custdata2$age, y)

x <- custdata$age
y <- custdata$income
bin<-hexbin(x, y, xbins=50) 
plot(bin, main="Age vs Income Hexbin")

#this hexbin plot shows the density of the points in a more efficent way than a scatterplot
#This is a better way to visualize the data

ggplot(custdata2, aes(x=num.vehicles,y=income)) +
  geom_point() +
  ylim(0,200000) +
  theme_bw() +
  ggtitle("Scatterplot of income vs number of vehicles")

?geom_point

#Using a scatterplot to visualize the number of vechilces and income but it only show it in rows
#the higher the income the more vehicles you will have generally

custdata3 <- subset(custdata,
                     (custdata$age > 0 & custdata$age < 100
                      & custdata$income > 0 & custdata$income < 30000))


ggplot(custdata3) +
geom_bar(aes(x=recent.move), fill = "yellow") +
  theme_bw() +
  ggtitle("Vertical Bar recent move")

# for recent move, generally they make more than 30k a year, that is why it's false