# 파이프로 메시지 주고받는경우, 파이프는 기본적으로 양방향성 (duplex)

import multiprocessing

def consumer(pipe):
    # 파이프는 기본적으로 양끝의 커넥션을 담은 튜플을 반환함
    output_p, input_p = pipe
    # 파이프의 입력쪽을 닫아줌
    input_p.close()
    while True:
        try:
            # 보내진 객체 받는 부분
            item = output_p.recv()
        except EOFError:              # 더이상 데이터 없거나, 연결의 반대쪽이 닫힌 경우 해당 에러 일으킴
            break

        print(item)
    print('Consumer done')

def producer(seqeunce, input_p):
    for item in seqeunce:
        input_p.send(item)



if __name__ == '__main__':
    # 파이프 객체 생성
    (output_p, input_p) = multiprocessing.Pipe()

    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p),))
    cons_p.start()

    # 생성자 출력 파이프 닫기 (연결종료라는 말이 더 맞는듯?)
    output_p.close()

    """ 위에처럼 연결 막은 다음에 새로 프로세스 연결할려고 하면 에러남
    cons_p1 = multiprocessing.Process(target=consumer, args=((output_p, input_p),))
    cons_p1.start()
    """

    # 항목 생성
    sequence = [x for x in range(100)]
    producer(sequence, input_p)

    # 입력 파이프 닫기
    input_p.close()


    cons_p.join()