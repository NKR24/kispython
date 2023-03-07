import re


def decode_bits(hex_str, fields_str):
    fields = re.findall(r'(\w+)\((\d+)(?:, (\d+))?\)', fields_str)
    num = int(hex_str, 16)

    values = []
    for field in fields:
        name = field[0]
        start = int(field[1])
        end = int(field[2]) if field[2] else start

        mask = ((1 << (end - start + 1)) - 1) << start
        value = (num & mask) >> start

        values.append((name, str(value)))

    return values


def main(hex_str):
    fields_str = 'B1(0, 7), B2(8, 14), B3(15, 16), B4(17), B5(18, 23), B6(24, 25)'
    return decode_bits(hex_str, fields_str)
