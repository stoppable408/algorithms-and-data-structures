from typing import Generator


#(sA + B) % M
def lcg(A=5, B=3,M=7,s=0) -> Generator[int, None, None]:
    while True:
        s = (A * s + B) % M
        yield s

for i in lcg():
    print(i)
