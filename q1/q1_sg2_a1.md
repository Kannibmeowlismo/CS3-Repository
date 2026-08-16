CS 3 Portfolio
# Activity 1: Computational Thinking Exercise

Group Members:
- Kristielle Garcia
- Kzyra Gumabon
- Yazmin Mundo

## Main Problem: 
- The school canteen is always crowded by students due to slow process of serving.

## Sub-Problems:
1. The canteen has slow serving processes and is crowded.
2. Students take too long to order their food.
3. The cashier has to manually compute totals and give change.
4. There is no system to track which food items are running out.

## Defining Computational Thinking Approaches
Sub-Problem 1: The canteen has slow serving processes and is crowded.

CT Skill: Decomposition

Solution: Divide the canteen processes into smaller steps.

Sub-Problem 2: Students take too long to order their food.

CT Skill: Abstraction

Solution: Display a simple digital menu where it is easily seen and accessible for everyone, along with its prices so students already know their order before proceeding to pick their food.

Sub-Problem 3: The cashier has to manually compute totals and give change.

CT Skill: Algorithm

Solution: We suggest creating a program that will send the students’ order to the cashier, and automatically compute the total and their change.

Sub-Problem 4: There is no system to track which food items are running out.

CT Skill: Logical Thinking

Solution: Program a system where it monitors each food item, identifying whether it’s out of supply or not. Create an “alarm” which alerts the staff when it is running out. Also display the quantity of items sold and the remaining.

### Pseudocode

START
  
    CREATE order = empty list
    CREATE add = “NONE”
    CREATE total_price = 0
    
    REPEAT
        OUTPUT menu_items, price_ items
        INPUT student_order
  
        IF student_ order is available THE
           ADD student_order to order
           total_price = total price + order
        ELSE
           OUTPUT “Food item is unavailable. Please choose another item.”
        END IF
    
           INPUT “Do you want to choose another item?”
  
           UNTIL add = “NO”
                
           OUTPUT order, total_price
                
           END
