# 将列表数据分割为各个小列表,每个小列表内元素个数为n
# [p1,p2,p3,p4,p5,..] -> [[p1,p2,p3,p4],[p5,p6,p7,p8],...]
def split_list(l,n = 4):
    output = []
    for i in range(0,len(l),n):
        output.append(l[i:i+n])
    return output

# 对过长的文本进行简化，去除其中的符号以及两端的空格
def simplify(name):
    name = name.replace("."," ").replace(":"," ").replace("?"," ").replace(","," ").strip()
    if len(name) > 100:
        return name[:100]
    return name