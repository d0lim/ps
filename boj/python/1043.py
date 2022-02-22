import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
who_knows = list(map(int, sys.stdin.readline().rstrip().split()))[1:]

result = 0
parties = []
for _ in range(M):
    parties.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])

people = [False for _ in range(N + 1)]
for who_know in who_knows:
    people[who_know] = True
    party_who_know = list(
        filter(lambda party: True if who_know in party else False, parties)
    )
    parties = list(filter(lambda party: False if who_know in party else True, parties))
    if len(parties) == 0:
        break
    for party in party_who_know:
        for person in party:
            if not people[person]:
                people[person] = True
                who_knows.append(person)

print(len(parties))
