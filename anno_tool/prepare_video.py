#!/usr/bin/env python3
import json
from collections import OrderedDict
from tqdm import tqdm
import numpy as np

annotations = json.load(open('../COIN.json', 'r'), object_pairs_hook=OrderedDict)

classes = [
    info['class']
    for k, info in annotations['database'].items()
]

indices = np.argsort(classes)

items = list(annotations['database'].items())

processed = []

for i, index in enumerate(indices):
    key, info = items[index]
    anno = info['annotation']

    fields = {}
    fields['video_name'] = key
    fields['video_class'] = info['class']
    print(info['class'])
    fields['cut_points'] = ""
    fields['checkpoint'] = 0
    fields['steps'] = len(anno)
    fields['action_ids'] = ','.join([a['id'] for a in anno])

    fields['state'] = 2 if fields['steps'] <= 3 else 0
    fields['train'] = info['subset'] == 'training'
    fields['prev_vid'] = i if i > 0 else 1

    processed.append(
        OrderedDict([
            ("model", "anno.video"),
            ("pk", i + 1),
            ("fields", fields)
        ])
    )


json.dump(processed, open('./anno/fixtures/COIN.json', 'w'))

# vim: ts=4 sw=4 sts=4 expandtab
