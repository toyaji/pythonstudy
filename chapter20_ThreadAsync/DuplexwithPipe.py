# 클라이언트 서버 컴퓨팅이나 원격 프로시저 등에 쓰이는 파이프를 이용한 멀티 프로세스

import multiprocessing

def adder(pipe):
    server_p, client_p = pipe
    client_p.close()
    while True:
        try:
            x, y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)
    print('Server done')

if __name__ == '__main__':
    (server_p, client_p) = multiprocessing.Pipe()
     # 서버 프로세스 생성
    adder_p = multiprocessing.Process(target=adder, args=((server_p, client_p), ))
    adder_p.start()

    # 클라이언트에서 서버 닫기
    server_p.close()

    # 서버에 요청 보내기
    client_p.send((3,4))
    print(client_p.recv())

    client_p.send(('Hello', 'World'))
    print(client_p.recv())

    # 끝으로 파이프 닫기
    client_p.close()

    adder_p.join()