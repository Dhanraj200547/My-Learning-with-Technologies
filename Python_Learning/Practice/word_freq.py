s  = "A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs."

words = list(map(str,s.split()))
d = {}
for i in words:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for k,v in d.items():
    print(f" {k} : {v}")