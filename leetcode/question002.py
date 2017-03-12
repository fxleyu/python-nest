from listNode import ListNode
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryNum = 0
        work1 = l1
        work2 = l2
        preResult = ListNode(0)
        temp =  preResult
        while work1 != None or work2 != None:
            if work1 != None :
                carryNum += work1.val
                work1 = work1.next
            if work2 != None :
                carryNum += work2.val
                work2 = work2.next
            temp.next = ListNode(carryNum % 10)
            temp = temp.next
            if carryNum > 9 :
                carryNum = 1
            else :
                carryNum = 0

        if carryNum > 0 :
            temp.next = ListNode(1)

        return preResult.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    print result.val, result.next.val, result.next.next.val
