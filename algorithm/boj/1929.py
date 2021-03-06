M, N = map(int, input().split())

def is_prime(num):
	if num <= 1:
		return False

	i = 2
	while i * i <= num:
		if num % i == 0:
			return False
		i += 1

	return True

if __name__=="__main__":
	for i in range(M, N+1):
		if is_prime(i):
			print(i)
