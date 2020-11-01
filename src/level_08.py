import bz2
from typing import Tuple


def solution(bz2_username: bytes, bz2_password: bytes) -> Tuple[str, str]:
    un = bz2.decompress(bz2_username).decode("utf-8")
    pw = bz2.decompress(bz2_password).decode("utf-8")
    return un, pw


username, password = solution(
    bz2_username=b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084",
    bz2_password=b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
print(f"Username: {username}\nPassword: {password}")
