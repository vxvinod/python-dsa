def get_val(val: int | str) -> bool:
    return "int" if isinstance(val, int) else "String"

def check_list(lst: list[int]):
    for val in lst:
        print(val)

print(get_val("hello"))
print(get_val("10"))
print(get_val(100))

check_list([1,2,3,"vinod"])