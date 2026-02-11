#Write a generator function that generates the first 10 even numbers.
def even():
    for i in range(2,21,2):
        yield i

for i in even():
    print(i)
        
