struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* current = nullptr;
        ListNode* l3 = nullptr; 
        int carry = 0;
        int value = 0;


        while (l1 || l2 || carry)
        {
            value = 0;
            value += l1 ? l1->val + carry : carry;
            value += l2 ? l2->val : 0;
            carry = value/10;
            value = value%10;

            if (!current)
            {
                current = new ListNode(value);
                l3 = current;
            }
            else
            {
                current->next = new ListNode(value);
                current = current->next;
            }
                        
            l1 = l1? l1->next : nullptr;
            l2 = l2? l2->next : nullptr;
        }   

        return l3;
    }
};