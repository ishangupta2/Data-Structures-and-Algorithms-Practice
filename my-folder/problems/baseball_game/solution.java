//import java.util.*
class Solution {
    public int calPoints(String[] operations) {
         Stack<Integer> stack = new Stack<Integer>();
        for(int i = 0; i < operations.length; i++) {
            if(operations[i].equals("C")) {
                stack.pop();
            }
            else if (operations[i].equals("D")) {
                stack.push(stack.peek()*2);
            }
            else if(operations[i].equals("+")) {
                int temp = stack.pop();
                int temp2 = stack.peek() + temp;
                stack.push(temp);
                stack.push(temp2);
            }
            else if(operations[i] instanceof String){
                stack.push(Integer.parseInt(operations[i]));
            }

        }
            int count = 0;
            while(!stack.isEmpty()) {
                count+=stack.pop();
            }
            return count;
    }
}