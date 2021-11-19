from timeit import timeit

b = timeit("c.apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])",
                  setup='from __main__ import c', number=1)
