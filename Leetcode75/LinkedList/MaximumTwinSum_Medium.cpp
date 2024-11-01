struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution 
{
public:

    ListNode* reverseLinkedList(ListNode* head)
    {
        if ((!head) || (!head->next))
            return head;

        ListNode* node = nullptr;
        ListNode* nextNode = head;        
        ListNode* temp = nullptr;
        
        while (nextNode)
        {
            temp = nextNode->next;
            nextNode->next = node;
            node = nextNode;
            nextNode = temp;
        }

        return node;
    }
    
    int pairSum(ListNode* head) 
    {
        // Count the number of nodes 
        ListNode* slowPointer = head;
        ListNode* fastPointer = head;

        while (fastPointer->next && fastPointer->next->next)
        {
            slowPointer = slowPointer->next;
            fastPointer = fastPointer->next->next;
        }
                
        ListNode *twinList = reverseLinkedList(slowPointer->next);        
        slowPointer->next = nullptr;
        ListNode* listNode = head;
        int maximumSum = 0;

        while(listNode && twinList) 
        {
            maximumSum = maximumSum < listNode->val + twinList->val ? listNode->val + twinList->val : maximumSum;

            listNode = listNode->next;
            twinList = twinList->next;
        }

        return maximumSum;
    }
};

int main()
{
    return 0;
}