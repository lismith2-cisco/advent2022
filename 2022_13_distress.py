from itertools import zip_longest


class PacketData:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"PacketData(${self.data})"

    def __lt__(self, other):
        if isinstance(self.data, int):
            if isinstance(other.data, int):
                return self.data < other.data
            else:
                return PacketData([self.data]) < other
        else:
            if isinstance(other.data, int):
                return self < PacketData([other.data])
            else:
                for left, right in zip(self.data, other.data):
                    if PacketData(left) < PacketData(right):
                        return True
                    elif PacketData(left) != PacketData(right):
                        return False
                return len(self.data) < len(other.data)

    def __eq__(self, other):
        if isinstance(self.data, int):
            if isinstance(other.data, int):
                return self.data == other.data
            else:
                return PacketData([self.data]) == other
        else:
            if isinstance(other.data, int):
                return self == PacketData([other.data])
            else:
                for left, right in zip(self.data, other.data):
                    if PacketData(left) != PacketData(right):
                        return False
                return len(self.data) == len(other.data)


striplines = (line.strip() for line in open("2022_12_distress_input.txt"))
packets = [PacketData(eval(line)) for line in striplines if line] + \
    [PacketData([[2]]), PacketData([[6]])]
ordered_packets = sorted(packets)

print((ordered_packets.index(PacketData([[2]])) + 1)
      * (ordered_packets.index(PacketData([[6]])) + 1))
