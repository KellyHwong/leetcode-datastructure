## Subsets 子集（确切地说是幂集）

### 动态规划法
dp[i] means the subsets of length i.

For example,
input: [1,2,3,4]
dp[1] = [[1],[2],[3],[4]]

For dp[2], we can construct from [1]
对于dp[2]，用[1]组合起来
[1] 和 [2],[3],[4]组合，[2] 和 [3],[4]组合， 即总是和后面的组合，这符合人手写组合的习惯
对于dp[3]，用dp[2]和dp[1]组合起来
dp[2]这个时候就是dp[2] = [1,2], [1,3], [1,4], [2,3], [2,4], [3,4]，那么
[1,2] 组合 [3]和[4] 

有个组合次序的问题，[1,2,3,4]的dp[3]里，[1,2,3]可以由[1,2]组[3]而成，也可以由[1,3]组[2]而成
在上面的动态规划过程中，[1,2]组了[3]和[4]，[1，3]就只组[4]，不组[3]了
也就是说，每次生成的上一级的子集都是有顺序的，对于同一个生成的集合，下一级的子集里，前面的子集优先组合，后面的子集则组剩下的
dp[3] = [1,2,3],[1,2,4],[1,3,4]是怎么生成的呢，都去跟[1] [2] [3] [4]组合就行了，但是从[1,2]的位置看，只用遍历[3]开始的最小元素就行了
[1,2,3],[1,2,4]由[1,2]组合[3]和[4]而成，而对于[1,3]，[1,2,3]已经被组合成了，只组剩下的[4]，这样就避免了上一级子集重复生成的问题

### DFS法


### 二进制法
若 {\displaystyle S} S是有限集，有 {\displaystyle |S|=n} |S|=n个元素，那么 {\displaystyle S} S的幂集有 {\displaystyle |{\mathcal {P}}(S)|=2^{n}} |{\mathcal  {P}}(S)|=2^{n}个元素。（其实可以——事实上电脑就是这样做的——将 {\displaystyle {\mathcal {P}}(S)} {\mathcal  {P}}(S)的元素表示为n位二进制数；第n位表示包含或不含 {\displaystyle S} S的第n个元素。这样的数总共有 {\displaystyle 2^{n}} 2^{n}个。）——维基百科


## 参考
[https://leetcode.com/problems/subsets/discuss/329218/Python-DP](https://leetcode.com/problems/subsets/discuss/329218/Python-DP)
[维基：幂集](https://zh.wikipedia.org/wiki/%E5%86%AA%E9%9B%86)
[yisuang1186:Subsets](https://yisuang1186.gitbooks.io/-shuatibiji/subsets.html)