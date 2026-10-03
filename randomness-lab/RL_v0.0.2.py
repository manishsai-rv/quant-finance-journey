import random
import matplotlib.pyplot as plt
import statistics
initial_balance=float(input("Enter initial balance ($): "))
win_probability = float(input("Enter win probability (%): "))/100
win_return = float(input("Enter win return per trade (%): "))/100
loss_return = float(input("Enter loss return per trade (%) as magnitude of loss: "))/100 #loss_return is now the magnitude of the loss, not a negative return.
experiments=int(input("Enter number of experiments: "))
trades=int(input("Enter number of trades per experiment: "))
results=[]
success_rates=[]
for experiment in range(experiments):
    balance=initial_balance
    wins=0
    losses=0
    for trade in range(trades):
        x=random.random()
        if x<win_probability:
            wins+=1
            balance*=(1+win_return)
        else:
            losses+=1 
            balance*=(1-loss_return)
    results.append(balance)
print(len(results))
print("Wins in last experiment:", wins)
print("Losses in last experiment:", losses)
#Using an arithmetic progression to generate systematically spaced success thresholds.
thresholds = []
while True:
    difference = float(input("Enter threshold difference ($): "))
    if difference > 0:
        break
    print("Please enter a number greater than 0.")
threshold=initial_balance
#To find success rate
def count_successes(results,threshold):
    successful = 0
    for result in results:
        if result>=threshold:
            successful+=1
    return successful
# Calculate success rates until the probability reaches 0%.
while True:
    thresholds.append(threshold)
    successful=count_successes(results, threshold)
    success_rate=(successful / len(results)) * 100
    success_rates.append(success_rate)
    if success_rate==0:
        break
    threshold+=difference
#To draw a table
print("Target($)    Success Rate")
print('___________|_____________')
for threshold, rate in zip(thresholds, success_rates):
    print(threshold,'       ',rate)
average_balance=sum(results)/len(results)   #To calculate the average.
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
print("Final balance of last experiment: ",balance)
print("Average final balance:", average_balance)
#Find the maximum and minimum final balance observed.
print("Lowest final balance observed: ",min(results))
print("Highest final balance observed: ",max(results))
#Calculate the median final balance.
median_balance = statistics.median(results)
print("Median final balance:", median_balance)
#Compare Median and average final balance.
if average_balance>median_balance:
    print("The distribution is right-skewed, but please check the histogram for confirmation.")#Most outcomes are concentrated toward the lower/middle side, while a smaller number of unusually high outcomes create a long tail to the right.
#Standard Deviation measures the spread of final balances around the mean.
print("Standard Deviation:", statistics.stdev(results))
below_start = 0
#Count experiments that finish below the initial balance.
for result in results:
    if result<initial_balance:
        below_start+=1
#Probability of experiments that finish below the initial balance.
probability_below_start=(below_start/len(results))*100
print("Experiments below initial balance:", below_start)
print("Probability of experiments below initial balance:", probability_below_start)


