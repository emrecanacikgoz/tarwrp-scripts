# cd /datasets/TARWRP/500k_all_tasks_dataset_15hz
# python tarwrp_extract_numbers.py > train.tsv

import numpy as np
import os
import re
import sys
from tqdm import tqdm

path = "/datasets/TARWRP/500k_all_tasks_dataset_15hz"

for f in tqdm(sorted(os.listdir(path))):
    m = re.match(r"episode_(\d{7})\.npz", f)
    if m is not None:
        idnum = m.group(1)
        data = np.load(path + "/" + f, allow_pickle=True, mmap_mode='r')
        actions = data.get("actions")  # 1-7(7)
        rel_actions_world = data.get("rel_actions_world")  # 8-14(7)
        rel_actions_gripper = data.get("rel_actions_gripper")  # 8-14(7)
        robot_obs = data.get("robot_obs")  # 15-29(15)
        print(idnum, end='\t')
        print(*np.concatenate((actions, rel_actions_world, rel_actions_gripper, robot_obs)), sep='\t')
