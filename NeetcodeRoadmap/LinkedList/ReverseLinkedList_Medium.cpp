struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        if(!head)
            return head;

        ListNode* prevNode = nullptr;
        ListNode* currNode = head;
        ListNode* nextNode = head->next;

        while(nextNode)
        {
            currNode->next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
            nextNode = nextNode->next;
        }

        currNode->next = prevNode;
        return currNode;
    }   
};

int main()
{
    return 0;
}