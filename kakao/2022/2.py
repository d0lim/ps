from collections import defaultdict


def to_minutes(hhmm):
    hh, mm = map(int, hhmm.split(":"))
    return int(hh) * 60 + int(mm)


def calcul(fees, mins):
    default, default_fee, unit, unit_fee = fees
    if mins <= default:
        return default_fee

    res = default_fee
    mins -= default
    res += (mins // unit) * unit_fee
    res += unit_fee if mins % unit != 0 else 0

    return res


def solution(fees, records):
    answer = []

    m = defaultdict(list)
    for record in records:
        hhmm, car, action = record.split()
        m[car].append((action, to_minutes(hhmm)))

    for car, o in m.items():
        if o[-1][0] == "IN":
            m[car].append(("OUT", to_minutes("23:59")))

    for car, o in m.items():
        # print(car, o)
        i_t = 0
        o_t = 0
        for action, val in o:
            if action == "IN":
                i_t += val
            else:
                o_t += val
        answer.append((car, calcul(fees, o_t - i_t)))

    # print([(car, calcul(fees, o["OUT"] - o["IN"])) for car, o in m.items()])

    return list(map(lambda x: x[1], sorted(answer, key=lambda x: x[0])))


solution(
    [180, 5000, 10, 600],
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ],
)
