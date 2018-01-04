// Simple class declaration
class Person {
    String name
    int age
    def fetchAge = { age }
}

def p = new Person(name:'Jessica', age:42)



class Person {
    String name
    String toString() { name }
}
def sam = new Person(name:'Sam')

// Create a GString with lazy evaluation of "sam"
def gs = "Name: ${-> sam}"