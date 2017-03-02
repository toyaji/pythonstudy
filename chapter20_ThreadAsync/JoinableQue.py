# 큐를 이요해서 프로세스 사이에 통신 주고받는 멀티프로세싱 예시

import multiprocessing

def consumer(input_q):
    while True:
        item = input_q.get()
        # 항목을 처리함
        print(item)
        # 작업 완료 알림 - 요 부분이 조이너블 큐의 핵심
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)


if __name__ == '__main__':
    # 공유 프로세스 큐 생성
    q = multiprocessing.JoinableQueue()

    # 소비자 프로세스 실행
    cons_p = multiprocessing.Process(target=consumer, args=(q, ))
    cons_p.daemon = True
    cons_p.start()

    # 항목 생성
    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    # 모든 항목 처리시 까지 기다림 - 이거 없으면 소비자가 메인 프로그램 끝날때 그냥 끝내버림...
    # 큐에 있는 항목이 다 처리되는지 알 수 있도록 하기 위해서 joinableque 쓰는거임
    q.join()