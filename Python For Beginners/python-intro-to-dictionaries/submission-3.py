from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    return {name:age}


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict = {}
    for i, word in enumerate(words):
        my_dict[word] = i
    return my_dict



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))



# Bạn có thể nhớ quy tắc này:
# - chỉ cần value → for word in words
# - chỉ cần index hoặc truy cập bằng index → for i in range(len(words))
# - cần cả index + value → for i, word in enumerate(words)
# Trong bài của bạn, enumerate() là lựa chọn tốt nhất.



# Vi index(word) phai tim lai vi tri cua word trong moi vong lap, Python phải search từ đầu list để tìm word

# enumerate() helps loop through a list and take index and value at the same time
