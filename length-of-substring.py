

def lengthOfSubString(s: str):
    print(s)
    max, long_check = 0, 0
    for i in range(1, len(s)+1):
        for j in range(i+1, len(s) + 1):
            check_str = s[i:j]
            print(f"check-str-#{check_str}--i-#{i}--j-#{j}")
            str_cnt = s.count(check_str)
            str_len = len(check_str)
            if str_cnt > 1:
                print(f"compare--check_str-#{check_str}--max--#{max}--longcheck#{long_check}--str_len--#{str_len}--strcnt#{str_cnt}")
                if long_check < str_cnt:
                    print("#####TRUE#####")
                    long_check = str_cnt
                    max = str_len
                    print(f"long-#{str_len}")
                # else:
                #     long_check, max = ma, longest

    print(f"max: {max}")
    return max
print(lengthOfSubString("zxyzxyz"))
