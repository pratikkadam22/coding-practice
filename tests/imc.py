
def countArtifacts(artifacts, searched):
    completed, partial = 0, 0
    searched = searched.split()
    artifacts = artifacts.split(',')
    for artifact in artifacts:
        artifact = artifact.split(' ')
        x, y = artifact[0], artifact[1]

        # Calculating the area of artifact
        area = (ord(y[0]) - ord(x[0]) + 1) * (ord(y[1]) - ord(x[1]) + 1)

        found = 0
        for piece in searched:
            if (x[0] <= piece[0] and piece[0] <= y[0]) and (x[1] <= piece[1] and piece[1] <= y[1]):
                found += 1
        if found == area:
            completed += 1
        elif found > 0 and found < area:
            partial += 1
    return [completed, partial] 

artifacts = "1B 1C,2D 2F,4B 5B"
searched = "1B 1C 2E 2B 4B 5B"
print(countArtifacts(artifacts, searched))

# def countArtifacts(artifacts, searched):
#     completed, partial = 0, 0
#     artifacts = artifacts.split(',')
#     for i in range(len(artifacts)):
#         artifacts[i] = artifacts[i].split(' ')
#         x, y = artifacts[i][0], artifacts[i][1]

#         if x[0] != y[0] and x[1] != y[1]:
#             a = chr(ord(x[0]) + 1) + x[1]
#             b = x[0] + chr(ord(x[1]) + 1)
#             artifacts[i].insert(1, a)
#             artifacts[i].insert(2, b)

#         elif x[0] != y[0] and x[1] == y[1]:
#             if ord(y[0]) - ord(x[0]) == 2:
#                 a = chr(ord(x[0]) + 1) + x[1]
#                 artifacts[i].insert(1, a)
#             elif ord(y[0]) - ord(x[0]) == 3:
#                 a = chr(ord(x[0]) + 1) + x[1]
#                 b = chr(ord(x[0]) + 2) + x[1]
#                 artifacts[i].insert(1, a)
#                 artifacts[i].insert(2, b)

#         elif x[0] == y[0] and x[1] != y[1]:
#             if ord(y[1]) - ord(x[1]) == 2:
#                 a = x[0] + chr(ord(x[1]) + 1)
#                 artifacts[i].insert(1, a)
#             elif ord(y[1]) - ord(x[1]) == 3:
#                 a = x[0] + chr(ord(x[1]) + 1)
#                 b = x[0] + chr(ord(x[1]) + 2)
#                 artifacts[i].insert(1, a)
#                 artifacts[i].insert(2, b)
#     searched = searched.split()
#     for artifact in artifacts:
#         found = 0
#         for piece in searched:
#             if piece in artifact:
#                 found += 1
#         if found == len(artifact):
#             completed += 1
#         elif found > 0 and found < len(artifact):
#             partial += 1
#     print(searched)
#     return [completed, partial] 

# artifacts = "1A 1D,2D 2F,4B 5B"
# searched = "1A 1B 2E 2B 4B 5B"
# print(countArtifacts(artifacts, searched))