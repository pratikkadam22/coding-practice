import os

final = {}
# roots = []
# dirss = []
filess = []

for root, dirs, files in os.walk("H:\PSU\practice\string contents"):
    # roots.append(root)
    # dirss.append(dirs)
    for f in files:
        filess.append(os.path.join(root,f))

for i in filess:
    with open(i) as f:
        if "pratik" in f.read():
            final[i] = True
        else:
            final[i] = False

print(final)