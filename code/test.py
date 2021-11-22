from timeit import timeit

# data = "credits"
# s = "s = pd.DataFrame(np.concatenate(credits['keywords'])).value_counts()"
# b = timeit(s, setup='from __main__ import pd,np,'+data, number=1)

timeit('a.append(i)', setup='a=[];i=0')
