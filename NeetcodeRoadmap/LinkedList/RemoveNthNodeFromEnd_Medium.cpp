struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        // Count number of nodes in linked list
        ListNode* current = head;
        int count = 0;

        while (current)
        {
            count++;
            current = current->next;
        }
        // compute the position from beginning
        current = head;
        count -= n;

        if (count == 0) // if head node is to be removed
        {
            return head->next;
        }

        while (count > 1)
        {
            current = current->next;
            count--;
        }

        // remove node
        ListNode* removedNode = current->next;
        current->next = removedNode->next;
        removedNode->next = nullptr;

        return head;
    }
};

int main()
{
    return 0;
}