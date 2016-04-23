def main():
    A,B,N = raw_input().split(" ")
    print T(int(A),int(B),int(N))
    
def T(A,B,N):
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        return T(A,B,(N-1)) + T(A,B,(N-2))
main()