#!/usr/bin/python3

max_pos = 2048*640
pos = 0
chunk_size = 516
chunk_pos = 0

with open("mtd0.bin", "rb") as ecc:
    with open("mtd0_strip.bin", "wb") as strip:
        while pos < max_pos:
            read_size = chunk_size
            #print(ecc.tell())
            if chunk_pos == 3:
                read_size += 48
                e = ecc.read(read_size)
                strip.write(e[0:500])
                strip.write(e[537:549])
                chunk_pos = 0
            else:
                e = ecc.read(read_size)
                strip.write(e[0:512])
                chunk_pos += 1

            pos += read_size

