class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #print("hello world")
        
        l1=list1
        l2=list2
        
        
        dummy=ListNode()
        curr=dummy
        
        #print("current list")
        #print_list(curr)
        
        while l1 and l2:
            
            if l1.val > l2.val:
                #print("l1 was greater")
                curr.next=l2
                curr=curr.next
                l2=l2.next
                
                #print_list(dummy.next)
            elif l2.val > l1.val:
                #print("l2 was greater")
                curr.next=l1
                curr=curr.next
                
                l1=l1.next
                
                
                #print_list(dummy.next)
            else:
                #print("they were the same")
                curr.next=l1
                curr=curr.next
                l1=l1.next
                
                
                #print_list(dummy.next)
                
        if l1==None:
            curr.next=l2
        elif l2 == None:
            curr.next=l1
            
            
        #print_list(dummy.next)
        return dummy.next