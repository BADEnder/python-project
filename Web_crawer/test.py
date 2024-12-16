import pandas 

dfs = pandas.read_html('https://rate.bot.com.tw/xrt')

print(type(dfs[0]))