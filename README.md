# 📘 README

### _Assignment 6: Medians & Order Statistics + Elementary Data Structures_

## Project Overview

This project contains two major components:

1.  **Selection Algorithms**
    - **Deterministic Median of Medians** (worst-case linear time)
    - **Randomized Quickselect** (expected linear time)
2.  **Elementary Data Structures**
    - Custom implementations of **Arrays, Stacks, Queues, and Linked
      Lists** in Python.

The goal is to understand algorithmic performance, compare empirical
results, and examine the time/space trade-offs of essential data
structures.

## ▶️ How to Run the Code

1.  Ensure you are using **Python 3.9+**.

2.  Install required libraries (if any are used):

        pip install -r requirements.txt

3.  Navigate to the project directory:

        cd Assignment6

4.  Run the selection algorithms demo:

        python assignment_6_selection_algorithms.py

5.  Run data structure implementations:

        python assignment_6_data_structures.py

6.

## Summary of Findings

### **Selection Algorithms**

- Median of Medians maintained **O(n)** performance consistently.
- Randomized Quickselect was faster **on average** but may slow down
  with bad pivot choices.
- Both found the 5th smallest element (**6**) in the dataset.

### **Data Structures**

- Arrays provide **O(1)** access but **O(n)** insert/delete.
- Stacks and Queues offer stable **O(1)** operations.
- Linked Lists allow dynamic memory with **O(1)** insert/delete but
  **O(n)** search.

## Conclusion

This project shows how algorithmic and structural decisions impact
performance. Deterministic selection offers stability; randomized offers
speed. Choosing the right data structure is crucial for efficient
software engineering.
