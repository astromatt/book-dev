// Optional ``return``
def jobName = 'example'

job(jobName) {

}



// Variable function parameter length

def concat1 = { String... args -> args.join('') }
assert concat1('abc','def') == 'abcdef'

def concat2 = { String[] args -> args.join('') }
assert concat2('abc', 'def') == 'abcdef'

def multiConcat = { int n, String... args ->
    args.join('')*n
}
assert multiConcat(2, 'abc','def') == 'abcdefabcdef'