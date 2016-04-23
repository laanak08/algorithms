def main():
    A,B,N = raw_input().split(" ")
    print T(A,B,N)
    
def T(A,B,N):
    if N == A:
        return A
    elif N == B:
        return B
    else:
        return T(A,B,(N-1)) + T(A,B,(N-2))
main()