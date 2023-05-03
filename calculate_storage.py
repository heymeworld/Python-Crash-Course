파일 시스템의 블록 크기가 4096바이트인 경우, 이는 1바이트로만 구성된 파일이 여전히 4096바이트의 스토리지를 사용한다는 것을 의미합니다. 4097바이트로 구성된 파일은 4096*2=8192바이트의 스토리지를 사용합니다. 이를 유념하여 주어진 크기의 파일을 저장하는데 필요한 총 바이트 수를 계산하는 아래의 calculate_storage 함수의 공백을 채울 수 있습니까?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks+1)
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
