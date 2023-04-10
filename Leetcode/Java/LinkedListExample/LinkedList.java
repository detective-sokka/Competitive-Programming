package LinkedListExample;
public class LinkedList {

    public int value;
    public LinkedList next;

    public LinkedList getNext() {
        return next;
    }
    public int getValue() {
        return value;
    }
    public void setNext(LinkedList next) {
        this.next = next;
    }
    public void setValue(int value) {
        this.value = value;
    }    
}