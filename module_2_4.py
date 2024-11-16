numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = True

for i_num in numbers[1:]:
    for j_num in numbers[1:]:
       if i_num % j_num == 0 and i_num != j_num:
          is_prime = False
          if is_prime is False:
              not_primes.append(i_num)
              break
       if i_num % j_num == 0 and i_num == j_num:
           is_prime = True
           if is_prime is True:
               primes.append(i_num)
               break

print(f'Список: {numbers}')
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')


