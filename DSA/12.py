def pointer_to_string(s):
    ptr = id(s)
    print("String:", s)
    print("Memory Address (Pointer):", ptr)
    print("Accessed via Pointer:", s)
string = "Hello World"
pointer_to_string(string)
