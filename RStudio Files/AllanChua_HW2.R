#Allan Chua
#HW2
getwd()

load('phsample.RData')
#The dataset provided by PDSR has information about workers like their age,
#employment class, education level, and sex

#2.12
#this code limits our desired subset of the data
#Subset of data rows matching detailed employment conditions
#we focus on the specific section of data
psub = subset(dpus,with(dpus,(PINCP>1000)&(ESR==1)&
                          (PINCP<=250000)&(PERNP>1000)&(PERNP<=250000)&
                          (WKHP>=40)&(AGEP>=20)&(AGEP<=50)&
                          (PWGTP1>0)&(COW %in% (1:7))&(SCHL %in% (1:24))))

#2.13
#this code limits our desired subset of the data
#Subset of data rows used for model training
#Subset of data rows used for model testing
psub$SEX = as.factor(ifelse(psub$SEX==1,'M','F'))
psub$SEX = relevel(psub$SEX,'M')
cowmap <- c("Employee of a private for-profit",
            "Private not-for-profit employee",
            "Local government employee",
            "State government employee",
            "Federal government employee",
            "Self-employed not incorporated",
            "Self-employed incorporated")
psub$Classofworker = as.factor(cowmap[psub$COW])
psub$Classofworker = relevel(psub$COW,cowmap[1])
schlmap = c(
  rep("no high school diploma",15),
  "Regular high school diploma","GED or alternative credential",
  "some college credit, no degree","some college credit, no degree",
  "Associate's degree","Bachelor's degree",
  "Master's degree",
  "Professional degree",
  "Doctorate degree")
psub$SCHL = as.factor(schlmap[psub$SCHL])
psub$SCHL = relevel(psub$SCHL,schlmap[1])
dtrain = subset(psub,ORIGRANDGROUP >= 500)
dtest = subset(psub,ORIGRANDGROUP < 500)

#2.14
#this code limits our desired subset of the data
#calculates the distribution of a category
> summary(dtrain$COW)


library(gdata)                   # load gdata package 
help(read.xls)                   # documentation 
mydata = read.xls("OlympicAthletes_0.xls")  # read from first sheet

athletes <- read.table('OlympicAthletes_0.txt', sep=',', header=T)
summary(athletes)
