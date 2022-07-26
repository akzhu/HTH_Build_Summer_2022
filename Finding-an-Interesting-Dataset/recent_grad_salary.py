import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

recent_grad_salary = pandas.read_csv("recent-grads.csv")

print(recent_grad_salary)
