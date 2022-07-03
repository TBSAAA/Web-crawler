

# 2797501328
# $2,797,501,328

str = "2797501328"
str_list = list(str)
final_list = []
length = len(str_list)
for i in range(1, length+1):
    final_list.append(str_list.pop(-1))
    if i % 3 == 0:
        final_list.append(",")
    if i == length:
        final_list.append("$")
final_list.reverse()
print("".join(final_list))

