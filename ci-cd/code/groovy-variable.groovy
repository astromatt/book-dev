// Variable declaration
String x
def o


// You can also use implicit declaration
x = 1
println x

x = new java.util.Date()
println x

x = -3.1499392
println x

x = false
println x

x = "Hi"
println x

def (a, b, c) = [10, 20, 'foo']

def nums = [1, 3, 5]
def a, b, c
(a, b, c) = nums


// String literals
def username = 'Jenkins'
echo 'Hello Mr. ${username}'
echo "I said, Hello Mr. ${username}"


// Multi line strings
def viewspec = '''
    //depot/Tools/build/... //jryan_car/Tools/build/...
    //depot/commonlibraries/utils/... //jryan_car/commonlibraries/utils/...
    //depot/helloworld/... //jryan_car/helloworld/...
'''