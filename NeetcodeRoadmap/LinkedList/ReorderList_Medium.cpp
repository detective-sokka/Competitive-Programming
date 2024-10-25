struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    void reorderList(ListNode* head) {

        if(!head->next)
            return;
        
        ListNode* midPoint = getListMidPoint(head);

        ListNode *second = midPoint->next;
        midPoint->next = nullptr;

        second = reverseLinkedList(second);

        joinListsAlternatively(head, second);
    }  

    ListNode* getListMidPoint(ListNode* head){
        // Find the midpoint of the list
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow;
    }

    ListNode* reverseLinkedList(ListNode* head)
    {
        if(!head->next)
            return head;

        // Reverse the 2nd half
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = head->next;

        while (curr)
        {
            curr->next = prev;
            prev = curr;
            curr = next;
            next = next ? next->next : nullptr;
        }

        return prev;
    }

    void joinListsAlternatively(ListNode* first, ListNode* second)
    {
        // Join the two lists alternatively
        ListNode* tempFirst = nullptr;
        ListNode* tempSecond = nullptr;

        while(second)
        {
            // Store next as temp values
            tempFirst = first->next;
            tempSecond = second->next;

            first->next = second;
            second->next = tempFirst;

            first = tempFirst;
            second = tempSecond;
        }
    } 
};

int main()
{
    return 0;
}