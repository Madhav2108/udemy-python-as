import pandas as p
li=[1,2,3]
data1=p.DataFrame(li)
print(data1)
import pandas as p
l=[[1,2,3],[4,5,6]]
data1=p.DataFrame(l)
print(data1)
import pandas as p
l=[['Alex',10],['bob',12],['Clark',13]]
data1=p.DataFrame(l,columns=['NAME','AGE'])
print(data1)
import pandas as p
l=[['Alex',10],['bob',12],['Clark',13]]
data1=p.DataFrame(l,columns=['NAME','AGE'],dtype=float)
print(data1)
import pandas as p
d={'NAME':['Tom','Jack','Steve','Ricky'],'AGE':[28,34,29,42]}
data=p.DataFrame(d)
print(data)
import pandas as p
d={'NAME':['Tom','Jack','Steve','Ricky'],'AGE':[28,34,29,42]}
data=p.DataFrame(d,index=['rank1','rank2','rank3','rank4'])
print(data)
import pandas as p
d=[{'a':1,'b':2,'c':3},{'a':5,'b':10,'c':20}]
data=p.DataFrame(d)
print(data)
d=[{'a':1,'b':2,'c':3},{'a':5,'b':10,'c':20}]
data=p.DataFrame(d,index=['first','second'])
print(data)
import pandas as p
d=[{'a':1,'b':2,'c':3},{'a':5,'b':10,'c':20}]
data=p.DataFrame(d,index=['first','second'],columns=['a','b1'])
print(data)
data=p.DataFrame(d,index=['first','second'],columns=['a','b'])
print(data)
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data)
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data['one'])
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data)
data['three']=p.Series([10,20,30],index=['a','b','c'])
print(data)
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data)
data['three']=p.Series([10,20,30],index=['a','b','c'])
print(data)
data['four']=data['one']+data['three']
print(data)
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,2,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data)
data['three']=p.Series([10,20,30],index=['a','b','c'])
print(data)
data['four']=data['one']+data['three']
print(data)
data.pop('three')
print(data)
import pandas as p
d={'one':p.Series([1,2,3],index=['a','b','c']),'two':p.Series([1,9,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data.loc['b'])
import pandas as p
d={'one':p.Series([1,2,5],index=['a','b','c']),'two':p.Series([1,9,3,4],index=['a','b','c','d'])}
data=p.DataFrame(d)
print(data.iloc[2])
import pandas as p
d={'one':p.Series([1,2,5,6],index=['a','b','c','e']),
   'two':p.Series([1,9,3,4],index=['a','b','c','d'])
   }
data=p.DataFrame(d)
print(data[2:4])
import pandas as p
d1=p.DataFrame([[1,2],[3,4]],columns=['a','b'])
d2=p.DataFrame([[5,6],[7,8]],columns=['a','b'])
d1=d1.append(d2)
print(d1)
import pandas as p
d1=p.DataFrame([[1,2],[3,4]],columns=['a','b'])
d2=p.DataFrame([[5,6],[7,8]],columns=['a','b'])
d1=d1.append(d2)
print(d1)
d1=d1.drop(0)
print(d1)
import pandas as p
d={'one':p.Series([1,2,5],index=['a','b','c']),'two':p.Series([1,9,3],index=['a','b','c'])}
data=p.DataFrame(d)
print(data)
print("SUM : \n",data.sum())
print("MIN :\n",data.min())
print("MAX :\n",data.max())
print("MIN INDEX :\n",data.idxmin())
print("MAX INDEX :\n",data.idxmax())
print(data.describe())
import pandas as p
d={'one':p.Series([1,2,5],index=['a','b','c']),'two':p.Series([1,9,3],index=['a','b','c'])}
data=p.DataFrame(d)
print(data)
print("SUM : \n",data.sum())
print("MIN :\n",data.min())
print("MAX :\n",data.max())
print("MIN INDEX :\n",data.idxmin())
print("MAX INDEX :\n",data.idxmax())
print(data.describe())





