library(readr)
marksheet <- read_csv("marksheet.csv")
View(marksheet)
#
mymatrix=matrix(1:9,nrow = 3,ncol = 3)
mydf=data.frame(mymatrix)
mydf

#
library(xlsx)
df <-data.frame(matrix(1:10))
write.xlsx(mydf,"output.xlsx")
write.csv(mydf,"output.csv")
#
library(rio)
export(mydf,"d1.xlsx")
###
#Greate matrix of 5 student score in three subjects,greate student score by uing function
#make suer the number yer get are int without decimal points
# Create a 3x3 matrix with predefined data
#my_matrix <-matrix( cells, nrow = 3, ncol = 3,byrow = TRUE,dimnames = list(rnames,cname))
#my_matrix
# Print the matrix
print(my_matrix)
#cells<-c(40,23,45,78,90,10,20,49,50)
cname<-c("Math","Phys","Bio")
rnames<-c("Ail","Badar","Saif")
Ail=rnorm(3,45,4)
Badar=rnorm(3,66,6)
Saif=rnorm(3,80,9)
studmatix=rbind(Ail,Badar,Saif)
studmatix
colnames(studmatix)<-c("Math","Phys","Bio")
#Toral
studmatix=cbind(studmatix,'Total'=rowSums(studmatix))
studmatix=cbind(studmatix,'percent'=(studmatix[,4]/300))
studmatix=rbind(studmatix,'Total'=colSums(studmatix))
studmatix=studmatix[-4,]
mydf=data.frame(studmatix)
mydf
export(mydf,"EX2.xlsx")
df<-edit(studmatix)
studmatix=edit(studmatix)
##
df= mtcars
str(df)
summay(df)
hist(df&mpg)
