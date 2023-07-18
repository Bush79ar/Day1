#Day 1
x<-'r'
class(x)
x=c('r','t')
x1=c(3.5,34)
c(TRUE,FALSE)->X2
#
temp<-c(72,71,68,73,69,75,71)
temp
names(temp)=c('su','mo','tu','we','th','fr','sa')
temp[3:6]
#square temp 
temp**2
#Multiply by 4
temp*4
min(temp)
max(temp)
sum(temp)
temp[temp>50]
#
#number1=c(20,21,22,23,24,25)
#number2=c(50,51,52,53,54,55)
tempNO70= temp[temp<70 | temp>79]
tempNO70
temp['we']
mean(temp1)
temp1=temp[c('th','fr')]
temp1
#deleet values
temp <- temp[-which(names(temp) == 'th')]
temp
temp01=temp[!names(temp)%in%c('mo','fr')]
temp01
#what is tow to the power of five
result <- 2^5
result
#stock.prices
t=c(23,27,23,21,34)
t
names(t)=c('Mon','Tues','Wed','Thu','Fir')
t
#7mean
mean(t)
#8 creat vecter called over 23 consisting of logicals to the day where t was more then 23
t>23
#9
t[t>23]
#10
t[t==max(t)] # name and num
names(t[t==max(t)]) # name

####
y <- matrix(1:20,nrow=5,ncol=4)
y
cells <- c(1,26,24,68,34,55)
rnames<- c("R1","R2")
cname<- c("C1","C2",'C3')
mymatrix <-matrix(cells,nrow=2,ncol=3,byrow=TRUE,dimnames=list(rnames,cname))
mymatrix
mymatrix*4
mymatrix * mymatrix
colnames(mymatrix)<-cname
colnames
###
m1<- matrix(1:6,nrow=2,ncol=3)
m1
m2<- matrix(1:6,nrow=3,ncol=2)
m2
 
result <- m1 %*% m2
result
result[,2] # 2 colm
result[2,] # 2 rows

###
# Generate 30 random numbers between 0 and 1 using runif()
random_runif <- runif(30)
random_runif
random_runif <- runif(n=30,min=50,max=100)
is_int <- as.integer(random_runif)
is_int


# Generate 30 random numbers from a standard normal distribution using rnorm()
random_rnorm <- rnorm(30)
random_rnorm
# Create a list to store the two sets of random numbers
random_list <- list(runif=random_runif, rnorm=random_rnorm)
random_list
# Plot boxplots for the two distributions
boxplot(random_list, main="Boxplot of Random Numbers", col=c("lightblue", "lightgreen"), names=c("runif", "rnorm"))
#  "a" to unber
(msft<-c(20,30,'a',20))
msft1=as.numeric(msft)
msft1

#add col
























