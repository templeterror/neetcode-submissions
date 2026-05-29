/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode p = list1;
        ListNode q = list2;
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while ((p != null) && (q != null)) {
            if (p.val == q.val) {
                tail.next = q;
                q = q.next;
            } else if (p.val < q.val) {
                tail.next = p;
                p = p.next;
            } else if (p.val > q.val) {
                tail.next = q;
                q = q.next;
            }
            tail = tail.next;
        }

        if (p != null) tail.next = p; else if (q != null) tail.next = q;
        return dummy.next;
    }
}