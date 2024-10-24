// Source: https://anj910.medium.com/leetcode-328-odd-even-linked-list-1110ade1735e

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        
        if (!head)
        {
            return head;
        }
        ListNode* oddHead = head;
        ListNode* oddNode = head;
        ListNode* evenHead = head->next;
        ListNode* evenNode = head->next;

        while(oddNode && evenNode && evenNode->next && oddNode -> next)
        {
            oddNode->next = evenNode->next;
            evenNode->next = evenNode->next->next;

            oddNode = oddNode->next;
            evenNode = evenNode->next;
        }

        oddNode->next = evenHead;
        return oddHead;
    }
};

int main()
{
    return 0;
}