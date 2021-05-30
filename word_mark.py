#get hsk gaoji word
with open('pinyin.txt',mode='r',encoding="utf-8") as f:
    lines = f.readlines()

full_word = []
for line in lines:
    full_word.append(line.split(",")[1])

#get hsk 6 ji word
with open('hsk6_word.txt',mode='r',encoding="utf-8") as f:
    lines = f.readlines()

hsk6_word = []
for line in lines:
    hsk6_word.append(line.split(",")[0])

#get compare text
with open('喂——出来！.txt',mode='r',encoding="utf-8") as f:
    full_text = f.read()

#get included word in text
detected = set()
for word in full_word:
    if word in full_text:
        detected = detected | {word}

detected_hsk6 = set()
for word in hsk6_word:
    if word in full_text:
        detected_hsk6 = detected_hsk6 | {word}

#output result
s = '\n'.join(detected)
with open('result_gaoji.txt',mode='w',encoding="utf-8") as f:
    f.write(s)

s = '\n'.join(detected_hsk6)
with open('result_hsk6.txt',mode='w',encoding="utf-8") as f:
    f.write(s)

total_detected = detected | detected_hsk6
s = '\n'.join(total_detected)
with open('result_total.txt',mode='w',encoding="utf-8") as f:
    f.write(s)