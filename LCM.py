# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# x = range(1, 21)
# not_primes = []
# primes = []
# for i in x:
# 	if i % 2 == 0 or i % 3 == 0:
# 		# print("Number is not Prime")
# 		not_primes.append(i)
# 	else:
# 		# print("Number is Prime")
# 		primes.append(i)
# print("Not Prime List: ", not_primes)
# print("Prime List: ", primes)
Num = 8
for i in range(1, Num+1):
	if (Num%i == 0):
		print(i)