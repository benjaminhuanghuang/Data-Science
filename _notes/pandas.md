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