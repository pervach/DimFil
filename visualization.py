
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self):
        self.plots = []

    def add_histogram(self, df, column, bins=10):
        plt.figure()
        sns.histplot(df[column], bins=bins, kde=True)
        self.plots.append(plt.gcf())

    def add_line_plot(self, df, x, y):
        plt.figure()
        sns.lineplot(data=df, x=x, y=y)
        self.plots.append(plt.gcf())

    def add_scatter_plot(self, df, x, y):
        plt.figure()
        sns.scatterplot(data=df, x=x, y=y)
        self.plots.append(plt.gcf())

    def remove_plot(self, index):
        if 0 <= index < len(self.plots):
            self.plots.pop(index)

    def show_all(self):
        for fig in self.plots:
            fig.show()
