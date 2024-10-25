#include <unordered_map>

class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {

        if (!head)
        {
            return nullptr;
        }

        std::unordered_map<Node*, Node*> nodesMap;
        Node* copyHead = new Node(head->val);
        Node* copyCurrent = copyHead;
        nodesMap[head] = copyHead;
        
        Node* current = head->next;        

        // Create a deep copy minus the random pointers
        while (current)
        {
            copyCurrent->next = new Node(current->val);
            copyCurrent = copyCurrent->next;

            nodesMap[current] = copyCurrent;
            current = current->next;
        }

        // Update the deep copy's random pointers
        copyCurrent = copyHead;
        current = head;

        while (current)
        {
            copyCurrent->random = nodesMap[current->random];
            current = current->next;
            copyCurrent = copyCurrent->next;
        }

        return copyHead;
    }
};

int main()
{
    return 0;
}