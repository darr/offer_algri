# 规则

 - 所有算法都在语言允许的范围内尽力做到行数最短。算法行数尽量控制在十行左右，一般算法行数不会超过20行，个别算法行数会超过20行。


# 滑动窗口的最大值
 - 题目描述
 - 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。



# 算法
 - 没有借助额外的数据结构或者内存。
 - 时间复杂度O(N)。
 - 这个算法最短python 行