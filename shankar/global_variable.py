x=10

def test_global_variable():
    x=20
    print(x)

test_global_variable()
print(x)

def test_global_variable2():
    global x
    x=30
    print(x)

test_global_variable2()
print(x)