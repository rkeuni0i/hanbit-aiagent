def fibonacci(n):
    """첫 번째 항이 1인 피보나치 수열의 첫 n개 항을 반환합니다."""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    fib_seq = [1, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


if __name__ == "__main__":
    n = 10
    result = fibonacci(n)
    print(f"피보나치 수열 (처음 {n}개 항): {result}")
