# Bags, Queues, and Stacks

**许多基础数据类型** 都和对象的集合有关。而在一开始，我们会接触到背包（ Bag ）、队列（ Queue ）和栈（ Stack ）。这三种类型都非常基础并且应用广泛。

这里我们不会把注意力放在如何实现这三种基础类型，而是理解这种基础数据类型的 API。

### Bags

背包是一种不支持从中删除元素的集合数据类型 —— 它的目的就是帮助用例收集元素并迭代遍历所有收集到的元素。

- API

| class Bag(object) | Item |
|-------------------|------|
| Bag() | 创建一个空背包 |
| add(item) | 添加一个元素 |
| isEmpty() | 背包中是否为空 |
| size() | 背包中的元素数量 |

- 应用场景

使用 Bag 的 API，用例可以将元素添加进背包并且根据需要随时使用 `foreach` 语句访问所有的元素。用例可以是栈或是队列，但使用 Bag 可以说明元素的处理顺序并不重要。

例如计算标准输入中所有值的平均值和样本标准差。

### Queues

队列是一种基于先进先出（ FIFO ）策略的集合类型。在应用程序中使用队列的主要原因是在用集合保存元素的同时保存它们的相对顺序，是它们入列和出列顺序相同。

值得一提的是，尽管 python 的 `list` 类型可以实现队列，但在 python 的官方文档中，使用 [`collections.dequeue`](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues) 实现队列的，原因是在出列的时候， `list` 类型会更慢一点，因为 `list` 类型是在 `pop(0)` 的时候会把数组中的元素都向左移一位。

- API

| class Queue(object) | Item |
|---------------------|------|
| Queue() | 创建空队列 |
| enqueue(item) | 添加一个元素 |
| dequeue() | 删除最早添加的元素 |
| isEmpty() | 队列是否为空 |
| size() | 队列中的元素数量 |

- 应用场景

按照任务产生的顺序完成他们的策略，优先服务等待最久的人。

### Stacks

栈是一种基于后进先出（ LIFO ）策略的集合类型。在应用程序中使用栈迭代器的一个典型原因是在用集合保存元素的同时颠倒他们的相对顺序。在计算机领域，栈具有基础而深远的影响。

- API

| class Stack(object) | Item |
|---------------------|------|
| Stack() | 创建一个空栈 |
| push(item) | 添加一个元素 |
| pop() | 删除最近添加的元素 |
| isEmpty() | 队列是否为空 |
| size() | 队列中的元素数量 |

- 应用场景

如在上网冲浪的时候，每当点击超链接浏览一个新页面，浏览器在显示页面的同事也会把它压入栈，当点击回退访问之前的页面的时候，旧的页面就会从栈弹出。

另外一个双栈计算器的例子，见 [Evaluate.py](Evaluate.py)。


# Linked lists

链表是集合类的抽象数据类型实现中表示数据的合适选择。

> 定义：链表是一种递归的数据结构，它或者为空，或者是指向一个结点（ node ）的引用，该结点含有一个泛型的元素和一个指向另一条链表的引用。

### 结点记录

实现链表之前，我们用一个类来定义结点的抽象数据类型。

```python
class _Node(object):

    def __init__(self):
        self.item = None
        self.next = None
```

### 构造链表

- 实例化结点类
- 将每个结点的 item 域设置为所需的值
- 使用 next 域来构造链表

```python
first = _Node()
first.item = 'to'

second = _Node()
second.item = 'be'
first.next = second

third = _Node()
third.item = 'or'
second.next = third
```
![linked list](http://algs4.cs.princeton.edu/13stacks/images/linked-list.png)


### 插入结点，删除结点

- 插入节点
    - 表头，实例化结点类 newfirst 并将其指向 oldfirst
    - 表尾，实例化结点类并将上一个结点指向自身

- 删除结点
    - 表头，将自己指向自己，即 first = first.next
    - 表尾，遍历到最后，并将指向 last 的连接改为 null

![Add-linked-list](http://algs4.cs.princeton.edu/13stacks/images/linked-list-insert-front.png)

# 算法分析

# union-find 算法
