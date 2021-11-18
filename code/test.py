import timeit

b = timeit.timeit("a+=1;print(a)",setup='a=0')
print(b)