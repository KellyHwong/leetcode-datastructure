#include <queue>
using std::queue;

class MyStack {
 public:
  queue<int> queue1;
  queue<int> queue2;

  MyStack() {}

  void push(int x) {
    queue2.push(x);
    transport(queue1, queue2);
    transport(queue2, queue1);
  }

  int pop() {
    int r = queue1.front();
    queue1.pop();
    return r;
  }

  int top() {
    int r = queue1.front();
    return r;
  }

  bool empty() { return queue1.empty(); }

 private:
  void transport(queue<int> &queue1, queue<int> &queue2) {
    while (!queue1.empty()) {
      queue2.push(queue1.front());
      queue1.pop();
    }
  }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */