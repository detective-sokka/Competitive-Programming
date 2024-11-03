struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {        
        
        if(!head || (!head->next))
            return nullptr;
        
        ListNode* slow = head;
        ListNode* fast = head;

        while(slow && fast && fast->next && fast->next->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* temp = nullptr;

        if(!fast->next)
        {
            fast = slow;
            slow = head;
            while(slow->next != fast)
                slow = slow->next;
        }
        
        temp = slow->next;
        slow->next = temp->next;
        temp->next = nullptr;
        return head;
    }
};

int main()
{
    return 0;
}