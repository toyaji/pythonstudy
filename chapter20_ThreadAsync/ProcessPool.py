#  맵리듀스와 비슷하게 프로세스 풀을 생성해서 진행하는 방법

import os
import multiprocessing
import hashlib

# 매겨변수 설정
buffsize = 8192   # 읽기 버터 사이즈
poolsize = 2      # 일꾼 수

def compute_digest(filename):
    try:
        f = open(filename, 'rb')
    except IOError:
        return None
    digest = hashlib.sha512()
    while True:
        chunk = f.read(buffsize)
        if not chunk: break
        digest.update(chunk)
    f.close()
    return filename, digest.digest()

def build_digest_map(topdir):
    digest_pool = multiprocessing.Pool(poolsize)
    allfiles = (os.path.join(path, name)
                for path, dirs, files in os.walk(topdir)
                for name in files)
    digest_map = dict(digest_pool.imap_unordered(compute_digest, allfiles, 20))
    digest_pool.close()
    return digest_map

if __name__ == '__main__':
    digest_map = build_digest_map("../Datacamp")
    print(len(digest_map))