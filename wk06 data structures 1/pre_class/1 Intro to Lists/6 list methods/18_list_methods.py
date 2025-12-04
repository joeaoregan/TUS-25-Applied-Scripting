scores = [4, 0, 1, 5, 1]
print(f"{len(scores)=} {scores=}")

scores.append(5)
print(f"{len(scores)=} {scores=}")

scores.extend([5,2,1,3,3])
print(f"{len(scores)=} {scores=}")

scores.insert(1,3)
print(f"{len(scores)=} {scores=}")

scores.remove(5)
print(f"{len(scores)=} {scores=}")

scores.pop()
print(f"{len(scores)=} {scores=}")

scores.clear()
print(f"{len(scores)=} {scores=}")

scores = [4, 3, 0, 1, 5, 1, 5, 5, 2, 1, 3, 3]
print(scores.count(5))

print(scores.index(5))

scores.reverse()
print(f"{scores=}")

scores.sort()
print(f"{scores=}")

scores.sort(reverse=True)
print(f"{scores=}")