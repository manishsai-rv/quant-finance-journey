import random
import matplotlib.pyplot as plt
import statistics
results=[]
success_rates=[]
for experiment in range(10000):
    balance=1000
    wins=0
    losses=0
    for trade in range(100):
        x=random.random()
        if x<0.60:
            wins+=1
            balance*=1.02
        else:
            losses+=1 
            balance*=0.99 
    results.append(balance)
thresholds = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]    
def count_successes(results,threshold):
    successful = 0
    for result in results:
        if result>=threshold:
            successful+=1
    return successful
for threshold in thresholds:
    successful=count_successes(results,threshold)
    success_rate=(successful / 10000)*100
    success_rates.append(success_rate)
print("Target($)    Success Rate")
for threshold, rate in zip(thresholds, success_rates):
    print(threshold,'       ',rate)
average_balance=sum(results)/len(results)   #To calculate the average.
below_start = 0
#Probability of finishing below the initial balance.
for result in results:
    if result<1000:
        below_start+=1
# Line Graph Section
print("Loading... Graph")
print(thresholds)
print(success_rates)
plt.plot(thresholds,success_rates)
plt.xlabel("Target Balance ($)")
plt.ylabel("Success Rate (%)")
plt.title("Success Rate vs Target Balance")
plt.show()
#Histogram Section
plt.hist(results)
plt.xlabel("Final Balance ($)")
plt.ylabel("Number of Experiments")
plt.title("Distribution of Final Balances")
plt.show()
print()
print(len(results))
print("Wins: ",wins)
print("Losses: ",losses)
print("Final balance: ",balance)
print("Average final balance:", average_balance)
#To know the maximum and minimum final balance observed.
print("Lowest final balance observed: ",min(results))
print("Highest final balance observed: ",max(results))
#To calculate the median final balance.
median_balance = statistics.median(results)
print("Median final balance:", median_balance)
#To compare Median and average final balance.
if average_balance>median_balance:
    print("The distribution is right skewed.")#Most outcomes are concentrated toward the lower/middle side, while a smaller number of unusually high outcomes create a long tail to the right.
#Standard Deviation (Tells us roughly how spread out the outcomes are around the range.)
print("Standard Deviation:", statistics.stdev(results))
print("Experiments below $1000:", below_start)