# 📌 Copy List with Random Pointer

This repository contains a Python implementation of the **Copy List with Random Pointer** problem (also known as *Deep Copy of a Linked List*).

---

## 📝 Problem Statement

A linked list of length `n` is given, where each node contains an additional **random pointer**, which could point to any node in the list, or `null`.

Construct a **deep copy** of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointers of the new nodes should point to new nodes in the copied list.

Return the head of the copied linked list.

### Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

---

## 🚀 Approach

We use the **interweaving nodes method** to achieve **O(n) time** and **O(1) space**:

1. **Interleave copy nodes** into the original list:
   ```
   Original: A → B → C
   Interleaved: A → A' → B → B' → C → C'
   ```
2. **Set random pointers** of copied nodes using:
   ```
   if A.random = C → then A'.random = A.random.next (C')
   ```
3. **Detach lists**: restore original list and extract copied list.

---

## 🧩 Complexity
- **Time:** O(n) (three passes over the list)  
- **Space:** O(1) (no extra hashmap, only pointers)

---

## 📂 Project Structure
```
copy-random-list/
│── README.md
│── copy_random_list.py   # main solution
└── tests/
    └── test_copy_random_list.py   # unit tests (optional)
```

---

## ▶️ Usage

### Run the example
```bash
python copy_random_list.py
```

### Sample Output
```
Original list:
Node(val=1, random=3)
Node(val=2, random=1)
Node(val=3, random=2)

Copied list:
Node(val=1, random=3)
Node(val=2, random=1)
Node(val=3, random=2)
```

---

## ✅ Example Input/Output

### Input
Linked list:
```
1 → 2 → 3
random pointers: 1 → 3, 2 → 1, 3 → 2
```

### Output
A deep copy with same structure, but all nodes are **newly created**:
```
1' → 2' → 3'
random pointers: 1' → 3', 2' → 1', 3' → 2'
```

---

## 🔮 Future Enhancements
- Add unit tests with `pytest`
- Add visualization of list and random pointers
- Extend to generic data structures with random references

---

👨‍💻 Author: *Your Name*  
📌 Problem Reference: [LeetCode 138 – Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
