# 7.8
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)
# 7.9
surprise[-1] = surprise[-1].lower()
print(surprise)
surprise_last = surprise[-1]
print(surprise_last)
surprise_last_list = list(surprise_last)
print(surprise_last_list)
surprise_last_rev = []
for i in range(4,-1,-1):
      surprise_last_rev.append(f'{surprise_last_list[i]}')
print(surprise_last_rev)
surprise[-1] = ''.join(surprise_last_rev)
print(surprise)
surprise[-1] = surprise[-1].capitalize()
print(surprise)
