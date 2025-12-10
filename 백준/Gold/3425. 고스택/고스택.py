import sys
input = sys.stdin.readline

LIMIT = 10**9

# 문제 정의에 맞춘 나눗셈/나머지
# a: 피제수(나눠지는 수), b: 제수(나누는 수)
def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    q = abs(a) // abs(b)
    if (a < 0) ^ (b < 0):  # 음수가 딱 하나이면 몫은 음수
        q = -q
    return q

def safe_mod(a, b):
    if b == 0:
        raise ZeroDivisionError
    r = abs(a) % abs(b)
    if a < 0:              # 나머지의 부호는 피제수(a)와 같음
        r = -r
    return r

def run_program(cmds, start_value):
    st = [start_value]
    try:
        for op in cmds:
            code = op[0]
            if code == 'NUM':
                st.append(op[1])
            elif code == 'POP':
                if not st: return "ERROR"
                st.pop()
            elif code == 'INV':
                if not st: return "ERROR"
                st[-1] = -st[-1]
            elif code == 'DUP':
                if not st: return "ERROR"
                st.append(st[-1])
            elif code == 'SWP':
                if len(st) < 2: return "ERROR"
                st[-1], st[-2] = st[-2], st[-1]
            elif code in ('ADD', 'SUB', 'MUL', 'DIV', 'MOD'):
                if len(st) < 2: return "ERROR"
                a = st.pop()   # 첫 번째(맨 위)
                b = st.pop()   # 두 번째
                if code == 'ADD':
                    res = b + a
                elif code == 'SUB':
                    res = b - a
                elif code == 'MUL':
                    res = b * a
                elif code == 'DIV':
                    res = safe_div(b, a)   # b div a
                else:  # 'MOD'
                    res = safe_mod(b, a)   # b mod a
                if abs(res) > LIMIT:
                    return "ERROR"
                st.append(res)
            else:
                # 정의되지 않은 명령은 없음
                return "ERROR"
        # 프로그램 종료 후 스택에 값이 정확히 하나여야 함
        if len(st) != 1:
            return "ERROR"
        return st[0]
    except ZeroDivisionError:
        return "ERROR"
    except Exception:
        # 혹시 모를 예외는 모두 에러 처리
        return "ERROR"

def main():
    while True:
        # 프로그램 한 개 읽기 (빈 줄 무시)
        cmds = []
        while True:
            line = input()
            if not line:
                return
            line = line.strip()
            if line == '':
                continue
            if line == 'QUIT':
                return
            if line == 'END':
                break
            parts = line.split()
            if parts[0] == 'NUM':
                x = int(parts[1])
                cmds.append(('NUM', x))
            else:
                cmds.append((parts[0],))

        # 실행 횟수
        n_line = input().strip()
        while n_line == '':
            n_line = input().strip()
        N = int(n_line)

        # N개의 입력값 실행
        outputs = []
        for _ in range(N):
            v_line = input().strip()
            while v_line == '':
                v_line = input().strip()
            v = int(v_line)
            out = run_program(cmds, v)
            outputs.append(out)

        # 출력
        for out in outputs:
            print(out)
        print()  # 각 프로그램 사이에 빈 줄

if __name__ == "__main__":
    main()
