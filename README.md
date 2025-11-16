🍉 Watermelon Problem – Codeforces 4A
Python Solution + Tests
📌 Problem Summary

Pete and Billy want to split a watermelon of weight w into two parts such that each part has an even weight.

Your task is to print:

"YES" → if the watermelon can be split into two positive even integers

"NO" → otherwise

Input

A single integer w (1 ≤ w ≤ 100)

Output

"YES" or "NO"

✅ Example Inputs & Outputs
Input	Output	Explanation
8	YES	8 → 4 + 4 (both even)
3	NO	3 cannot be split into two even numbers
2	NO	2 → only 1+1, and 1 is not even
🧠 Solution Logic

A watermelon can be split into two even parts only if:

The weight is even

The weight is greater than 2

✔ Even ensures both parts could be even
✔ Greater than 2 ensures both parts are positive (since 2 → 1+1, invalid)

📂 Repository Structure
.
├── watermelon.py         # Main program
├── test_watermelon.py    # Pytest test cases
├── README.md             # Documentation

▶️ How to Run the Program

Run the script and enter a weight:

python3 watermelon.py


Example:

Enter watermelon weight: 8
YES

🧪 Running Tests

This project uses pytest.

To run all tests:

pytest


Expected result:

3 passed
