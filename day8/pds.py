import pandas as pd 


# series holo 1 d column and dataframe holo 2d
#s = pd.Series([10,20,30,40,50])
#print(s)
'''
output: 
0    10
1    20
2    30
3    40
4    50
dtype: int64

output theke amra dekhte pai pandas custom index dey
'''

#marks = pd.Series([85,92,78],index = ["Math","English","Science"] )
##print(marks.mean()) # average


# DataFrame is like a dictonary
# data = {
#     "name": ["karim","rahim","rafiq"],
#     "age": [20,22,21],
#     "marks": [85,92,78]
# }

# df = pd.DataFrame(data)
# print(data)


# Series
# 1 d aray like obj that can hold data

# data = [1,2,3,4,5]
# series = pd.Series(data)
# print(series)

# creating series form dictonary 
# data = {'a':1,'b':2,'c':3} # defaulf index a,b,c
# print(pd.Series(data))

# data = [10,20,30]
# index = ['a','b','c']
# print(pd.Series(data,index=index))

#! dataframe

# create a dataframe from a dictonary

# data = {
#     'name':['diu','oggy','jack'],
#     'age': [25,35,45],
#     'city': ['dhaka','kumilla','tongi']
# }
# df = pd.DataFrame(data)
# print(df)
# print(type(df))

## create a df from list of dictonary
# data = [
#     {'name':'oggy','age':60,'city':'CN'},
#     {'name':'jack','age':65,'city':'CAN'},
#     {'name':'bob','age':60,'city':'CAAN'},
#     {'name':'oley','age':54,'city':'CCN'}
# ]

# df = pd.DataFrame(data)
# print(df)
# print(type(df))


# df = pd.read_csv() csv file read kore
# df.head() -top 5 record dey
# df.tail() last 5 record

## accessing data from df or csv file
# df['name] - sob nam dekha jabe
# df.loc[] - row index
# df.iloc[] - col index

## accessing specified element
# df.['name]

# iat - second second element


