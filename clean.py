import os
import os.path as osp

root_dir = "/home/yusu/new_home/code/y/streamlit-app/videos/9sec/m1_test/step-3600"

inner_folder = osp.join(root_dir, os.listdir(root_dir)[0])
for rank in range(8):
    for prompt in range(2):
        mp4_file = osp.join(inner_folder, f"rank-{rank}/prompt-{prompt}/000000.mp4")
        text_file = osp.join(inner_folder, f"rank-{rank}/prompt-{prompt}/prompt.txt")
        assert osp.exists(mp4_file), f"mp4_file {mp4_file} does not exist"
        assert osp.exists(text_file), f"text_file {text_file} does not exist"
        new_mp4_file = osp.join(root_dir, f"{prompt*8+rank:03d}-00.mp4")
        new_text_file = osp.join(root_dir, f"{prompt*8+rank:03d}.txt")

        # print(f"{osp.basename(mp4_file)} {osp.basename(new_mp4_file)}")
        # print(f"{osp.basename(text_file)} {osp.basename(new_text_file)}")

        os.rename(mp4_file, new_mp4_file)
        os.rename(text_file, new_text_file)