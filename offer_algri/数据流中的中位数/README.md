# 规则

 - 所有算法都在语言允许的范围内尽力做到行数最短。算法行数尽量控制在十行左右，一般算法行数不会超过20行，个别算法行数会超过20行。


# 数据流中的中位数
 - 题目描述
 - 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。



# 算法
 - 没有借助额外的数据结构或者内存。
 - 时间复杂度O(N)。
 - 这个算法最短python 行