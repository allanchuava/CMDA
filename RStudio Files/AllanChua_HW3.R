#Allan Chua
#HW 3

athletes = read.table("OlympicAthletes_0.csv", sep = ",", head = T)

summary(athletes$Gold.Medals)
summary(athletes$Silver.Medals)
summary(athletes$Bronze.Medals)
summary(athletes$Age)
summary(athletes$Total.Medals)
summary(athletes$Country)
summary(athletes$Closing.Ceremony.Date)
summary(athletes$Sport)
summary(athletes$Athlete)
summary(athletes$Year)

#there is no missing data, however there are outliers such as
#michael phelps who won over 22 gold medals at the games
#while some countries got none

plot(athletes$Country, athletes$Total.Medals)
# The plot shows the relationship between athlete home country and number of medals won
# The counties that won the most medals at the games were the United States


sportcounts = table(athletes$Sport)
barplot(sportcounts)
# The chart shows how many athletes were in each of the sports
# most were in swimming

agecounts = table(athletes$Age)
barplot(agecounts)
# the chart shows the number of athletes at each age
# most athletes are in their 20s, second was late 30s


# Since no data was missing or outliers or issues were present
# no data transformations had to be made on this data set
