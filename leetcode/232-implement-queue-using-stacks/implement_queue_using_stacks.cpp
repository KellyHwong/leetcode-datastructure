#include <stack>
using std::stack;

class MyQueue {
 private:
  stack<int> inStack, outStack;
  void in2out() {
    while (!inStack.empty()) {
      outStack.push(inStack.top());
      inStack.pop();
    }
  }

 public:
 public:
  MyQueue() {}

  void push(int x) { inStack.push(x); }

  int pop() {
    if (outStack.empty()) {
      in2out();
    }
    int x = outStack.top();
    outStack.pop();
    return x;
  }

  int peek() {
    if (outStack.empty()) {
      in2out();
    }
    int x = outStack.top();
    return x;
  }

  bool empty() { return inStack.empty() && outStack.empty(); }
};