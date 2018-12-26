from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as graph

data = dict()
for user_num in list(dataset.keys()):
    for county, country_list in (dataset[user_num]).items():
        if user_num in data:
            data[user_num] += sum(country_list)
        else:
            data[user_num] = sum(country_list)

print(data)

diagram = graph.bar(
    x = list(data.keys()),
    y = list(data.values())
)

figure = graph.Figure(data = [diagram])
plotly.ofline.plot(figure, filename = 'user costs.html')