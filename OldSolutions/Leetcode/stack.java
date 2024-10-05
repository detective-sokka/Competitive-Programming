import java.util.Scanner;
import java.util.Stack;

import javax.sound.sampled.SourceDataLine;

class MyStack {    

    public static Integer peekStack(Stack<Integer> pStack) {

        return pStack.peek();
    }

    public static void main(String[] args) {
        
        Stack <Integer> stack = new Stack<>();
        Scanner scanner = new Scanner(System.in);

        while(true) {

            System.out.println("Hello there");
            System.out.println("Menu: \n1. Peek stack \n2. Push stack \n3. Pop stack \n4. Search stack\n*. Exit");
            System.out.print("Enter choice: ");
            
            int choice = scanner.nextInt();
            int element;            

            switch (choice) {
                case 1 -> {
                    try {

                        System.out.println("\nTop of stack is : " + stack.peek());                        

                    } catch (Exception e) {
                        
                        System.out.println("\nStack is empty");
                    }

                }
                case 2 -> {

                    System.out.print("\nElement to push: ");
                    
                    try {

                        element = scanner.nextInt();      
                        stack.push(element);                      

                    } catch (Exception e) {
                        
                        System.out.println("\nPlease enter a valid number ");
                    }                                         
                }
                case 3 -> {

                    try {

                        System.out.println("\n Popped element : " + stack.pop());

                    } catch (Exception e) {

                        System.out.println("\n Empty stack");
                    }
                }   
                case 4 -> {

                    System.out.print("Element to search: ");
                    element = scanner.nextInt();    
                    
                    int pos = stack.search(element);

                    if (pos == -1) {
                        
                        System.out.println("Element not found");

                    } else {

                        System.out.println("Element found in index : " + Integer.toString(pos));
                    }                    
                }

                default -> {
                    
                    return;
                }                
            }
        }
    }
}