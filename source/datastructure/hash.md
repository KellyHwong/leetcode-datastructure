### 散列算法

Python 的字典数据结构就是用散列实现的，那么它的内部结构是啥样的咧。
如黑皮《数据结构与算法分析》中论述，散列表就是一种键值映射，但是键值是可以冲突的。解决键值冲突，和优化散列表的大小，是散列算法的主要问题。
散列  算法的要素是表大小，散列函数，输出的散列值（即 hash 值），用 hash 值来索引/存入数据，不同键的 hash 值可以相同。

#### 分离链接法 Separate Chaining

一句话概括：分离链接法就是不改变表的大小，hash 值重复的就用链表存储此元素，缺点是申请新存储单元需要时间

#### 开放寻址法 Open Address Hashing

分离链接法是强行把相同 hash 的元素存到一起，而开放寻址法，说白了，就是这个位置被占了，我们按照一定的规则，找下一个位置。这个规则叫探测法。
i 表示 hash 次数，h_i(X)=(Hash(X) + F(i)) mod TableSize，F(i) 是发生第 i 次冲突的解决办法。

要有 F(0)=0，这（大概）是为了做 hash 判断，设定这个单元，表明冲突到这里了，就不要再继续试探了。

“因为所有的数据都要存到表里，所以开放地址散列法所需要的表空间要比分离链接法大”

这句话真是表义不明，难道不是所有数据存到表里？分离链接法本身空间固定，有冲突则是动态申请空间；而开放寻址法本身就是设计成比较稀疏的表，通过探测法解决冲突，同时期望冲突不要太多，所以开放寻址法需要的空间大。

“一般，开放定址散列法的装填因子应该低于\lambda=0.5”

##### 线形探测法

##### 平方探测法

##### 双散列

#### 再散列/再哈希

#### 参考资料

黑皮《数据结构与算法分析》
