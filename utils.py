""" 
从形如T. Hofmann. Probabilistic latent semantic indexing. 
Proceedings of the Twenty-Second Annual International SIGIR Conference, 1999.
长文本中获取参考文献的名称，便于后面进行查询
"""
def simplify_name(name):
    s = name.split(".")[2:]
    for line in s:
        s2 = line.split(" ")[1:]
        if "," in line:
            continue 
        elif len(s2)<=2:
            continue
        elif min([len(w) for w in s2])<2 and len(s2)<4:
            continue
        else:
            return line