input_file = open("input_1.txt", "r")
full_input = input_file.read()
lines = full_input.split('\n')

l_list = []
r_list = []
for i in lines:
    if i != "":
        j = i.split("   ")
        l_list.append(j[0])
        r_list.append(j[1])
l_list = sorted(l_list)
r_list = sorted(r_list)
# task1 
dists = []
for i in range(len(l_list)):
    a = int(l_list[i])
    b = int(r_list[i])
    #print(str(a) + " | " + str(b))
    if a > b:
        dists.append(a-b)
    elif a < b:
        dists.append(b-a)

print(sum(dists))
