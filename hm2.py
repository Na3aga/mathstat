
#!/bin/python
import math, functools
from collections import Counter

def counted_elems(lst):
    return Counter(lst)

def histogramData(sparse_dict, step, min_el, max_el):
    # print([c for el, c in sparse_dict.items() if el <= (min_el+step)])
    counted = [{f'[{min_el};{min_el+step}]': sum([c for el,c in sparse_dict.items() if el <= (min_el+step)])}]
    print(counted)
    # print(sum([c for el, c in sparse_dict.items() if el <= (min_el + step)]))
    for i in range(min_el+2*step,max_el,step):
        counted.append({f'({i-step};{i}]': sum([c for el, c in sparse_dict.items() if ((el <=i) and (el > i-step))])})
    print(counted)
    return counted

m_func = lambda n: round(1+ 3.322*math.log10(n))
h_func = lambda lst: round((max(lst)-min(lst))/m_func(len(lst)))

def pretty_print_histogram(hist_lst):
    for i in hist_lst:
        print(i)

data  = [91, 95, 85, 85, 96, 87, 98, 92, 90, 89, 98, 97, 117, 88, 91, 119, 85, 77, 94, 89, 79, 108, 94, 112, 96, 93, 98, 112, 97, 88, 107, 95, 99, 101, 104, 81, 102, 117, 105, 104, 103, 107, 100, 85, 105, 112, 93, 92, 106, 108, 84, 113, 118, 98, 120, 94, 92, 85, 101, 108, 119, 96, 94, 92, 102, 109, 113, 99, 98, 115, 105, 86, 87, 92, 96, 89, 97, 115, 100, 99, 119, 97, 89, 99, 90, 79, 91, 103, 109, 108, 88, 91, 98, 99, 77, 72, 99, 84, 82, 96]

data.sort()
print(data)
print(f"{len(data)=}")
print(f"середнє арифм  = {sum(data)/len(data)}")
print(f"середнє арифм квадратів = {sum(list(map(lambda x: x*x,data)))/len(data)}")
print(f"медіана  = {(data[len(data)//2]+data[len(data)//2+1])/2 if len(data)%2 else data[(len(data)+1)//2]}")
h = h_func(data)
m = m_func(len(data))
print(f"{h=}")
print(f"{m=}")
print(f"{counted_elems(data)=}")
print(f"{counted_elems(data).items()=}")
print("Гістограма:")
pretty_print_histogram(histogramData(counted_elems(data), h, min(data), max(data)))
# histogramData(counted_elems(data), h, min(data), max(data))
rslt =
print(f"{histogramData(data,h(data))=}")