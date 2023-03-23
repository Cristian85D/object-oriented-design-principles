# Dependecy inversion
- High Level class should not depend on Low Level class. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.
- High level class and dependents class should be decoupled with an abstraction layer in between.

# Advantages
- The tight coupling of classes is no more prevalent and hence no complexity/rigidity in the system. 
- As there is a clear abstraction layer between dependent classes(provided by a hook or parameter), it's easy to deal 
with dependencies across classes in a better way.
