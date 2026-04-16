# Max Profit Optimization

## 1. Problem Overview

In this problem, I was required to determine the optimal combination of properties (Theatres, Pubs, and Commercial Parks) that maximizes total earnings within a given time limit **n**.

Each property:

- Takes a fixed amount of time to build
- Starts generating revenue after completion
- Cannot be built in parallel (only one construction at a time)

The goal is to maximize total earnings after **n units of time**.

---

## 2. Approach

I implemented a **brute-force optimization approach** to explore all possible combinations of buildings within the given time constraint.

### Steps:

1. Iterate through all possible counts of:

   * Theatres (T)
   * Pubs (P)
   * Commercial Parks (C)

2. For each combination:

   * Check if total build time ≤ n
   * Simulate construction sequentially (T → P → C)
   * Track when each building becomes operational

3. Compute profit:

   * Each building earns money for the remaining time after construction
   * Earnings depend on building type

4. Keep track of:

   * Maximum profit
   * Best combination (T, P, C)

---

## 3. Key Design Decisions

### 1. Sequential Construction Constraint

Since parallel construction is not allowed, I simulated builds in a fixed order:

* Theatres → Pubs → Commercial Parks

This ensures correctness while keeping implementation simple.

---

### 2. Profit Calculation Logic

For each building:

* Revenue = earning rate × (remaining time after completion)

This reflects the real-world constraint that buildings only generate income after they are completed.

---

### 3. Brute Force Strategy

Although brute force is not the most efficient approach, it guarantees:

* Correctness
* Simplicity
* Exhaustive exploration of all valid combinations

Given the input size is relatively small, this approach is acceptable.

---

## 4. Assumptions

* Only one building can be constructed at a time
* Buildings start generating revenue immediately after completion
* Land availability is not a constraint
* Build order is fixed (T → P → C) for simplicity

---

