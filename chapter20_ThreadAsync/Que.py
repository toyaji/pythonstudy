# 더이상 생산되는 거 없어서 소비자에게 종료되야 한다고 알려주는 방법 예시

import multiprocessing

def consumer(input_q):
    while True:
        # timeout 옵션 주면 블락킹 되었을때 값 받을때가지 최대 기다릴 시간 설정함 - 해당 시간 넘어가면 에러 띄워줌
        item = input_q.get(timeout=3)
        if item is None:
            break
        print(item)
    print('Consumer done')

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)

if __name__ == '__main__':
    # 큐 생성
    q = multiprocessing.Queue()

    # 생성한 큐를 받는 프로세스 생성
    cons_p = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p.start()

    sequence = [x for x in range(100)]
    producer(sequence, q)

    # 큐에 표지를 추가하여 종료 알려줌
    q.put(None)

    # 큐가 비었는지 확인
    print(q.empty())

    # 큐를 닫아서 더이상 큐에 값이 못들어오게 함 - 이렇게 하면 타임아웃 셋팅 해놓으면 에러띄움
    q.close()

    # 현재 큐 사이즈 반환
    print(q.qsize())

    cons_p.join()