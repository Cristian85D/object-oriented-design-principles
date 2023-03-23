# Questions
How can something be open and closed at the same time?

# Open/Close
- Classes or objects and methods should be open for extension but close for modification, this means that when you 
develop your software application make sure that you write your classes or modules in a generic way so that whenever 
you feel the need to extend the behavior of the class or object, then you shouldn't have to change the class itself.
Rather, a simple extension of the class should help you build the new behavior.
- Example: when a developer has to create a class implementation by extending the abstract base class to implement 
the required behavior instead of changing the abstract class.

# Open for extension
- A software component(class, module, method) should be extendable to add a new feature or to add a new behavior to it.

# Close for modification
- New features getting added to the software component, should not have to modify existing code.

# Advantages
- Existing classes are not changed and hence the chances of regression are less.
- It also helps maintain backward compatibility for the previous code.

# Key takeaways
- Ease of adding new features
- Leads to minimal cost of developing and testing software
- Open Closed principle often requires decoupling which, in turn, automatically follows the Single Responsibility 
Principle.
