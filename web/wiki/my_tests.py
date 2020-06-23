import re
import os
import os.path

def build_bridge(path, start_page, end_page):
    def open_page(path, page):
        with open(os.path.join(path, page), encoding = "utf-8") as file:
            links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
            list_ref = set()
            for f in links:
                if os.path.exists(f) and f != page:
                    list_ref.add(f)
            return list_ref

    curr = 0
    D = {}
    Prev = {start_page: None}
    D[start_page] = 0
    Q = [start_page]
    visit = []
    while Q:
        w = Q.pop(0)

        if w == end_page:
            curr = end_page
            break

        if w not in visit:
            visit.append(w)
            for v in open_page(path, w):

                if not D.get(v):
                    Prev[v] = w
                    D[v] = D[w] + 1
                    Q.append(v)
    Ans = []

    while curr is not None:
        Ans.append(curr)
        curr = Prev[curr]
        if curr == start_page:
            Ans.append(curr)
            break

    return Ans[::-1]

print(build_bridge('', 'Stone_Age', 'Stone_Age'))
