from PIL import Image
import numpy as np
import rle_img as rleImg
import rle_txt as rleTxt
import BWT
import MTF
import AC
import HC
import side_funcs as sf
import compressors as comp
import conversions as conv
import LZ77

# file = open('tests/texts/MTF_RuText_enc.txt', 'rb')
# data = file.read(100)
# print(data)
def menu():
    path_in = {
        1: 'tests/texts/string.txt',
        2: 'tests/texts/RuText.txt',
        3: 'tests/texts/enwik7'
    }
    while 1:
        print("1. RLE\n2. BWT\n3. MTF\n4. AC\n5. HC\n6. SA-IS CHECK\n7. lZ77\n\n 0. exit")
        choice = int(input())

        if choice == 0:
            return 0
        elif choice == 1:
            print("1. text\n2. image\n\n  0. exit")
            choice = int(input())

            if choice == 0:
                return 0
            elif choice == 1:
                print("1. string\n2. RuText\n3. enwik7\n\n  0. exit")
                choice = int(input())

                path_enc = {
                    1: 'tests/texts/rle_string_enc.txt',
                    2: 'tests/texts/rle_RuText_enc.txt',
                    3: 'tests/texts/rle_enwik7_enc.txt'
                }

                path_dec = {
                    1: 'tests/texts/rle_string_dec.txt',
                    2: 'tests/texts/rle_RuText_dec.txt',
                    3: 'tests/texts/rle_enwik7_dec.txt'
                }

                rleTxt.rle_txt_enc(path_in[choice], path_enc[choice])
                rleTxt.rle_txt_dec(path_enc[choice], path_dec[choice])

            elif choice == 2:
                print("1. bw\n2. grayscale\n3. color\n\n  0. exit")
                choice = int(input())

                path_enc = {
                     1: 'tests/pics/rle_bw_enc.raw',
                     2: 'tests/pics/rle_grayscale_enc.raw',
                     3: 'tests/pics/rle_color_enc.raw'
                }

                path_dec = {
                     1: 'tests/pics/rle_bw_dec.raw',
                     2: 'tests/pics/rle_grayscale_dec.raw',
                     3: 'tests/pics/rle_color_dec.raw'
                }

                rleImg.rle_img_enc(path_in[choice], path_enc[choice])
                rleImg.rle_img_dec(path_enc[choice], path_dec[choice])
        elif choice == 2:
            print("1. naive\n2. file\n 0. exit")
            choice = int(input())

            if choice == 0:
                return 0

            elif choice == 1:
                in_str = 'ABACABA$'
                index, enc_data = BWT.bwt_naive_enc(in_str)
                BWT.bwt_naive_dec(enc_data, index)

            elif choice == 2:
                print("1. string\n2. RuText\n3. enwik7\n 0. exit")
                choice = int(input())

                path_enc = {
                    1: 'tests/texts/bwt_string_enc.txt',
                    2: 'tests/texts/bwt_RuText_enc.txt',
                    3: 'tests/texts/bwt_enwik7_enc.txt'
                }

                path_dec = {
                    1: 'tests/texts/bwt_string_dec.txt',
                    2: 'tests/texts/bwt_RuText_dec.txt',
                    3: 'tests/texts/bwt_enwik7_dec.txt'
                }
                # in_str, indices = BWT.bwt_enc('tests/pics/test1.png', 'tests/pics/aatest1_memee.raw')
                # BWT.bwt_dec('tests/pics/aatest1_memee.raw', indices, 'tests/pics/aatest1_memee_dec.raw')
                in_str, indices = BWT.bwt_enc(path_in[choice], path_enc[choice])
                BWT.bwt_dec(path_enc[choice], indices, path_dec[choice])

        elif choice == 3:
            print("1. string\n2. RuText\n3. enwik7\n 0. exit")
            choice = int(input())

            path_enc = {
                1: 'tests/texts/MTF_string_enc.txt',
                2: 'tests/texts/MTF_RuText_enc.txt',
                3: 'tests/texts/MTF_enwik7_enc.txt'
            }

            path_dec = {
                1: 'tests/texts/MTF_string_dec.txt',
                2: 'tests/texts/MTF_RuText_dec.txt',
                3: 'tests/texts/MTF_enwik7_dec.txt'
            }

            if choice == 0:
                return 0
            # MTF.Move_to_front('tests/pics/test1.png', 'tests/pics/test1_memee.raw')
            # MTF.decodeMtF('tests/pics/test1_memee.raw', 'tests/pics/test1_memee_dec.raw')
            MTF.mtf_enc(path_in[choice], path_enc[choice])
            MTF.mtf_dec(path_enc[choice], path_dec[choice])
        elif choice == 4:
            print("1. string\n2. RuText\n3. enwik7\n 0. exit")
            choice = int(input())

            path_enc = {
                1: 'tests/texts/AC_string_enc.txt',
                2: 'tests/texts/AC_RuText_enc.txt',
                3: 'tests/texts/AC_enwik7_enc.txt'
            }

            path_dec = {
                1: 'tests/texts/AC_string_dec.txt',
                2: 'tests/texts/AC_RuText_dec.txt',
                3: 'tests/texts/AC_enwik7_dec.txt'
            }
            AC.ac_enc(path_in[choice], path_enc[choice])
            AC.ac_dec(path_enc[choice], path_dec[choice])

        elif choice == 5:
            print("1. string\n2. RuText\n3. enwik7\n 0. exit")
            choice = int(input())

            path_enc = {
                1: 'tests/texts/HC_string_enc.txt',
                2: 'tests/texts/HC_RuText_enc.txt',
                3: 'tests/texts/HC_enwik7_enc.txt'
            }

            path_dec = {
                1: 'tests/texts/HC_string_dec.txt',
                2: 'tests/texts/HC_RuText_dec.txt',
                3: 'tests/texts/HC_enwik7_dec.txt'
            }
            HC.huffman_encode(path_in[choice], path_enc[choice])
            HC.huffman_decode(path_enc[choice], path_dec[choice])
        elif choice == 6:
            # print("1. string\n2. RuText\n3. enwik7\n 0. exit")
            # choice = int(input())
            #
            # path_in = {
            #     1: 'tests/texts/string.txt',
            #     2: 'tests/texts/RuText.txt',
            #     3: 'tests/texts/enwik7'
            # }
            #
            # path_enc = {
            #     1: 'tests/texts/SAIS_string_enc.txt',
            #     2: 'tests/texts/SAIS_RuText_enc.txt',
            #     3: 'tests/texts/SAIS_enwik7_enc.txt'
            # }
            #
            # path_dec = {
            #     1: 'tests/texts/SAIS_string_dec.txt',
            #     2: 'tests/texts/SAIS_RuText_dec.txt',
            #     3: 'tests/texts/SAIS_enwik7_dec.txt'
            # }
            sf.process_file('tests/texts/sa.txt', 'tests/texts/sa_hz.txt' )

        elif choice == 7:
            print("1. string\n2. RuText\n3. enwik7\n 0. exit")
            choice = int(input())

            path_in = {
                1: 'tests/texts/string.txt',
                2: 'tests/texts/RuText.txt',
                3: 'tests/texts/enwik7'
            }

            path_enc = {
                1: 'tests/texts/LZ77_string_enc.txt',
                2: 'tests/texts/LZ77_RuText_enc.txt',
                3: 'tests/texts/LZ77_enwik7_enc.txt'
            }

            path_dec = {
                1: 'tests/texts/LZ77_string_dec.txt',
                2: 'tests/texts/LZ77_RuText_dec.txt',
                3: 'tests/texts/LZ77_enwik7_dec.txt'
            }
            enc = LZ77.lz77_encode(path_in[choice], path_enc[choice])
            LZ77.lz77_decode(enc, path_dec[choice])
            # file = open('tests/texts/RuText.txt', 'r', encoding = 'utf-8')
            # data = file.read()
            # indices, huffman_codes, huffman_encoded = comp.compress(data)
            # comp.decompress(indices, huffman_codes, huffman_encoded)


menu()

#
# file = open('tests/texts/string.txt', 'r', encoding = 'utf-8')
# data = file.read()
#
#
# # ''' BWT + RLE '''
# # '''encode'''
# # data1, indices = comp.bwt_enc(data)
# # data2 = comp.rle_txt_enc(data1)
# # meow = ''.join(data2)
# #
# # file2 = open('bwtrle_enc.txt', 'w', encoding='utf-8')
# # file2.write(meow)
# #
# # '''decode'''
# # data1 = comp.rle_txt_dec(data2)
# # data = comp.bwt_dec(data1, indices)
# #
# # meow = ''.join(data)
# #
# # file2 = open('bwtrle_dec.txt', 'w', encoding='utf-8')
# # file2.write(meow)
#
#
#
# '''BWT + MTF + RLE'''
# data1, indices = comp.bwt_enc(data)
#
# meow1 = ''.join(data1)
#
# with open('bwtmtfrlebyte_enc.txt', 'w', encoding='utf-8') as file2:
#     file2.write(meow1)
#
# with open('bwtmtfrlebyte_enc.txt', 'rb') as file3:
#     data1 = file3.read()
#
# data2 = comp.mtf_enc(data1)
#
# meow = ''.join(map(chr, data2))
#
# with open('bwtmtf_enc.txt', 'w', encoding='utf-8') as file2:
#     file2.write(meow)
#
#
# path_in ='bwtmtf_enc.txt'
# path_out = 'bwtmtfrle_enc.txt'
# HC.huffman_encode(path_in, path_out)
#
# '''decode'''
# path_in ='bwtmtfrle_enc.txt'
# path_out = 'bwtmtfrleee_dec.txt'
#
# data2 = HC.huffman_decode(path_in, path_out)
# decoded_data = comp.mtf_dec(data2)
# data3 = comp.bwt_dec(data2, indices)
#
# meow = ''.join(data3)
#
# file2 = open('bwtmtfrle_dec.txt', 'w', encoding='utf-8')
# file2.write(meow)
#
# with open('mtf_decoded.txt', 'wb') as file5:
#     file5.write(bytes(decoded_data))


#BWT.average_repeating_length()
# BWT.average_repeating_length1()
# BWT.average_repeating_length2()
# BWT.average_repeating_length3()
