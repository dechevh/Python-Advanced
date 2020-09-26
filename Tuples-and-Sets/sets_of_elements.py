n_len, m_len = map(int, input().split())

n = set()
m = set()

for _ in range(n_len):
    number = int(input())
    n.add(number)

for _ in range(m_len):
    number = int(input())
    m.add(number)

intersection = n & m

for n in intersection:
    print(n)
