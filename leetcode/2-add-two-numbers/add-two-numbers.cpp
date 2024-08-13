/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

int restore_num(ListNode *);
ListNode *convert_to_linked_list(int);

class Solution {
 public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *ptr1 = l1;
    ListNode *ptr2 = l2;
    int carry_flag = 0;
    int sum = 0;
    ListNode head = ListNode(-1);
    ListNode *ptr = &head;

    do {
      int val1, val2;
      if (ptr1 != nullptr)
        val1 = ptr1->val;
      else
        val1 = 0;
      if (ptr2 != nullptr)
        val2 = ptr2->val;
      else
        val2 = 0;
      sum = val1 + val2 + carry_flag;
      carry_flag = sum / 10;
      ptr->next = new ListNode(sum % 10);
      ptr = ptr->next;
      if (ptr1 != nullptr) ptr1 = ptr1->next;
      if (ptr2 != nullptr) ptr2 = ptr2->next;
    } while (ptr1 != nullptr || ptr2 != nullptr || carry_flag != 0);

    return head.next;
  }

  ListNode *addTwoNumbersByRestore(ListNode *l1, ListNode *l2) {
    /**
     * 由于还原的数可能非常大（超过int的范围）
     * 故放弃这一方法
     */
    int num1 = restore_num(l1);
    int num2 = restore_num(l2);
    ListNode *head = convert_to_linked_list(num1 + num2);
    return head;
  }
};

int restore_num(ListNode *head) {
  int num = 0;
  int base = 1;
  ListNode *ptr = head;
  while (1) {
    num = num + ptr->val * base;
    base *= 10;
    ptr = ptr->next;
    if (ptr == nullptr) break;
    return num;
  }
}
ListNode *convert_to_linked_list(int num) {
  // 小端模式，低位在前
  ListNode *head = &ListNode(num % 10);
  int num = num / 10;
  ListNode *tail = head;
  while (1) {
    if (num == 0) break;
    tail->next = &ListNode(num % 10);
    num = num / 10;
    tail = tail->next;
  }
  return head;
}

int main(int argc, char **argv) {
  """
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
    请你将两个数相加，并以相同形式返回一个表示和的链表。
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    """

    l1 = [2, 4, 3];
  l2 = [ 5, 6, 4 ];
  head1 = build_linked_list(l1);  // 实际给的输入数据结构
  head2 = build_linked_list(l2);

  /*
    num1 = restore_num(head1)
    num2 = restore_num(head2)
    head = convert_to_linked_list(num1+num2)
    num = restore_num(head)
  */
  sol = Solution();
  sol.addTwoNumbers();
}