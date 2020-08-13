给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        dummy = ListNode(0)
        current = dummy
        p,q = l1,l2
        while p or q:
            if p and q:
                value = p.val + q.val + flag
                if value >= 10:
                    flag = 1
                    newnode = ListNode(value - 10)
                else:
                    flag = 0
                    newnode = ListNode(value)

                current.next = newnode
                current = current.next
                p,q = p.next,q.next
            elif p:
                value = p.val + flag
                if value >= 10:
                    flag = 1
                    newnode = ListNode(value - 10)
                else:
                    flag = 0
                    newnode = ListNode(value)

                current.next = newnode
                current = current.next
                p = p.next
            else:
                value = q.val + flag
                if value >= 10:
                    flag = 1
                    newnode = ListNode(value - 10)
                else:
                    flag = 0
                    newnode = ListNode(value)

                current.next = newnode
                current = current.next
                q = q.next

        if flag == 1:
            newnode = ListNode(1)
            current.next = newnode
            return dummy.next
        else:
            return dummy.next

        return dummy.next
