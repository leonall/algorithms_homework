# algorithms_homework

## 算法

### 排序

- [X] [冒泡法排序](sort/bubble_sort.py)
- [X] [快速排序](sort/quick_sort.py)

### 查找

- [X] [二分法查找](search/binary_search.py)
- [X] [firsh_occurance](search/first_occurance.py)

## 数据结构

### 数组

数组是我们在编程中最常用的数据结构之一，存放一组数据，有以下几个特点：

* 连续：顺序存储
* 定长：一旦定义后，长度不可变
* 支持随机访问：根据下标可直接访问到这个下标的元素，定位快 O(1)
* 头尾的删除插入很快 O(1)；中间任意位置的删除插入，后面的往前移动，效率 O(n)

- [X] [two_sum](array/two_sum.py)
- [X] [three_sum](array/three_sum.py)
- [X] [flatten](array/flatten.py)
- [X] [garage](array/garage.py)

### 链表

链表顺序存储数据，有以下几个特点：

* 内存不连续，前一个节点通过指针，指向后一个节点
* 不定长
* 不支持随机访问：无法根据下标去直接访问，必须从头一个一个往后面找。（线性阶）
* 头尾位置的删除插入 O(1)，中间位置，删除前需要顺序查找，效率 O(n)。

- [X] [单向链表 Python 实现](linkedlist/SingleLinkedList.md)
- [X] [双向链表 Python 实现](linkedlist/DoublyLinkedList.md)
- [X] [链表去重](linkedlist/remove_duplicates.py)
- [X] [两整数的加法](linkedlist/add_two_numbers.py)

### 栈

栈是“后进先出”为特点的数据结果

- [X] [用数组结构建立的栈](stack/stack.py)
- [X] [用链表结构建立的栈](stack/LinkedListStack.py)
- [X] [简化存储路径](stack/simplify_path.py)
- [X] [判断括号的使用是否正确](stack/valid_parenthesis.py)
