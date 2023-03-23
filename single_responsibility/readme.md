# Cohesion
Is the degree to which the various parts of a software component are related.

# Coupling
Is defined as the level of interdependency between various software component.

# Single responsibility
- Every software component(Can be a class, a method, or module) should have one and only one responsibility.
- Aim for high Cohesion
- Always recommends loose coupling.
- High coupling is an undesirable feature in software.
- Loose coupling helps attain better adherence to the Single Responsibility
- When we develop classes, it should cater(atender) to the given functionality well. If a class is taking care(se ocupa) 
of two functionalities, it is better to split them. It refers to functionality as a reason to change. 
For example, a class can undergo(sufrir) changes because of the difference in behavior expected from it, but if a 
class is getting changed for two reasons(basically, changes in two functionalities), then the class should be 
definitely split.

# Advantages
- Whenever there is a change in one functionality, this particular class needs to change, and nothing else.
- Aditionally, if a class has multiple functionalities, the dependent classes will have to undergo changes for 
multiple reasons, which gets avoided.