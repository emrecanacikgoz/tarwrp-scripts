# tarwrp-scripts

* `tarwrp_extract_numbers.py`: extracts the numeric fields of calvin data files in current directory and prints them to stdout in tab separated format. The fields are given below. Only file-id(1), actions(7), rel_actions_world(7), rel_actions_gripper(7), robot_obs(15) are printed (37 columns). 

## tarwrp-files

* episode_XXXXXXX.npz: Each frame is represented in a file named episode_idnum.npz, consecutive idnums indicate consecutive frames (with the exception of episode transitions I guess). Other files indicating the contents: 
* ep_start_end_ids.npy indicates the start and end idnums of segments in that particular directory.
* ep_lens.npy indicates the lengths of segments given by ep_start_end_ids.npy.
* statistics.yaml gives basic stats for numeric variables.


## tarwrp-data

A summary of all data (including images) in episode_XXXXXXX.npz files (each represents a single 1/15 sec frame):

```
# julia> for f in data[:files]; println(f, "\t", summary(get(data, f))); end
# actions	7-element Vector{Float64}
# rel_actions_world	7-element Vector{Float64}
# rel_actions_gripper	7-element Vector{Float64}
# robot_obs	15-element Vector{Float64}
```

## tarwrp-tsv-fields

The fields in the output of calvin_extract_numbers.py is as follows:

00. idnum
01. actions/x (tcp (tool center point) position (3): x,y,z in absolute world coordinates)
02. actions/y
03. actions/z
04. actions/a (tcp orientation (3): euler angles a,b,c in absolute world coordinates)
05. actions/b
06. actions/c
07. actions/g (gripper_action (1): binary close=-1, open=1)
08. rel_actions_world/x (tcp position (3): x,y,z in relative world coordinates normalized and clipped to (-1, 1) with scaling factor 50)
09. rel_actions_world/y
10. rel_actions_world/z
11. rel_actions_world/a (tcp orientation (3): euler angles a,b,c in relative world coordinates normalized and clipped to (-1, 1) with scaling factor 20)
12. rel_actions_world/b
13. rel_actions_world/c
14. rel_actions_world/g (gripper_action (1): binary close=-1, open=1)
15. rel_actions_gripper/x (tcp position (3): x,y,z in relative world coordinates normalized and clipped to (-1, 1) with scaling factor 50)
16. rel_actions_gripper/y
17. rel_actions_gripper/z
18. rel_actions_gripper/a (tcp orientation (3): euler angles a,b,c in relative world coordinates normalized and clipped to (-1, 1) with scaling factor 20)
19. rel_actions_gripper/b
20. rel_actions_gripper/c
21. rel_actions_gripper/g (gripper_action (1): binary close=-1, open=1)
22. robot_obs/x (tcp position (3): x,y,z in world coordinates)
23. robot_obs/y
24. robot_obs/z
25. robot_obs/a (tcp orientation (3): euler angles a,b,c in world coordinates)
26. robot_obs/b
27. robot_obs/c
28. robot_obs/w (gripper opening width (1): in meters)
29. robot_obs/j1 (arm_joint_states (7): in rad)
30. robot_obs/j2
31. robot_obs/j3
32. robot_obs/j4
33. robot_obs/j5
34. robot_obs/j6
35. robot_obs/j7
36. robot_obs/g (gripper_action (1): binary close = -1, open = 1)

## calvin-annotation-statistics
- 486,178 `episode_XXXXXXX.npz` files.
- All annotated episodes are 64 timesteps.
- There are 3605 episodes.
- There are 3605 * (64+1) = 234,325 annotated `episode_XXXXXXX.npz` files.
- 55 tasks in total.

![alt text](https://github.com/emrecanacikgoz/tarwrp-scripts/figs/hist.png)

```
{'open_drawer': 20020, 'close_drawer': 15210, 'lift_yellow_block': 12480, 'move_slide_left': 11570, 'lift_purple_block': 11440, 'lift_pink_block': 10985, 'push_yellow_block_left': 6500, 'place_yellow_table': 5655, 'place_purple_drawer_top': 5525, 'place_yellow_drawer_top': 5460, 'turn_off_blue_led': 5395, 'turn_on_green_led': 5265, 'place_yellow_drawer': 5070, 'turn_on_blue_led': 5070, 'turn_on_red_led': 4940, 'place_pink_drawer_top': 4940, 'turn_off_green_led': 4615, 'place_purple_box': 4615, 'place_pink_table': 4550, 'place_pink_drawer': 4225, 'place_purple_table': 4225, 'rotate_yellow_block_right': 4225, 'turn_off_red_led': 4160, 'push_purple_block_left': 4160, 'rotate_purple_block_right': 4160, 'place_yellow_box': 4030, 'place_purple_drawer': 3835, 'place_yellow_left_cabinet': 3705, 'place_pink_box': 3510, 'rotate_pink_block_right': 3510, 'place_purple_left_cabinet': 3445, 'place_pink_right_cabinet': 3445, 'place_pink_left_cabinet': 3185, 'push_yellow_block_right': 3120, 'rotate_yellow_block_left': 2600, 'push_pink_block_left': 2405, 'place_yellow_right_cabinet': 2405, 'place_purple_right_cabinet': 2405, 'push_purple_block_right': 2145, 'rotate_purple_block_left': 2015, 'push_pink_block_right': 1950, 'stack_purple_on_yellow': 1820, 'rotate_pink_block_left': 1625, 'unstack_purple_block': 1560, 'unstack_yellow_block': 1300, 'stack_yellow_on_pink': 1040, 'stack_purple_on_pink': 1040, 'unstack_pink_block': 780, 'stack_yellow_on_purple': 715, 'push_pink_block_in_drawer': 715, 'stack_pink_on_yellow': 455, 'push_purple_block_in_drawer': 455, 'stack_pink_on_purple': 390, 'push_yellow_block_in_drawer': 195, 'stack_yellow_on_': 65}
```
