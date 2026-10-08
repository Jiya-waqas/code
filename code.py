import pandas as pd 
import matplotlib.pyplot as plt

c_merge ['population_growth'] = (
    c_merge['population_y']= c_merge['population_x']
)

c_merge.head()

c_merge = c_merge.reset_index()

names = [
    'china',
    'india',
    'united states',
    'indonesia',
    'brazil',
    'pakistan',
    'bangladesh',
    'nigeria',
    'philiipines',
    'mexico'
]

pop_grow = c_merge ['populaion_growth'] / 10**6
plt.figure( figsize =(15,9))
plt.bar(names, pop_growth, width=0.6)

plt.xlabel('country')
plt.ylable('population_growth(Millions)')
plt.title(
    Top 10 counteries with the biggest population growth from 1952 - 2007
)

plt.xticks(rotation=45)

for x,y in zip(names,pop_growth):
    label = "{:.2f}".format(y)

    plt.annotate(
        lable,
        (x.y),
        textcoords= "offset"
    )