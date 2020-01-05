## 利用pandas包进行数据分析时常见的操作有
1.创建对象: Series, DataFrame, DatetimeIndex
2.查看对象
3.选择
4.缺失值处理
5.相关操作
6.合并
7.分组和分段
8.轴转换和数据透视表
9.时间序列
10.导入和保存数据

## Create object
```
pd.Series([1,2,3,np.nan,6,8])

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
```

##
```
df3=pd.dataframe()
df3['min']=df.min()
df3['max']=df.max()
df3['std']=df.std()
```


## Modify column
```
  # 去掉温度后面的C
  df.loc[:, "column"]= df["column"].str.replace("C", "").astype('int32')
```

## Add column
1. 直接赋值
```
  # 计算温度差
  df.loc[:, "diff"]= df["a"]- df["b"]
```

2. apply(), axis = 1 for columns, axis = 0  for inex
```
  def get_type(df):
    df['col'] > 10:
      return 'A'
    return 'B'

  df.loc[:,"type"] = df.apply(get_type, axis=1)
```
3. df.assisn()
```
  df.assign(
    y_huashi= = labmda x: x['ywendu'] * 9 / 5 +32,
    b_huashi= = labmda x: x['bwendu'] * 9 / 5 +32
  )
```
4. 条件赋值
```
  df[df["bWendu]-df[''yWendu]>10, 'wencha']= "wencha_da"
```





## Reference
- https://github.com/peiss/ant-learn-pandas