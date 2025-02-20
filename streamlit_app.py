import streamlit as st
import os


upload_folder_dict = {
    "3s-m1-4000step": "/home/yusu/new_home/code/y/generations/3sec/m1_newtest/step-4000",
    "3s-mamba-4000step": "/home/yusu/new_home/code/y/generations/3sec/mamba2_newtest/step-4000",

}

if __name__ == "__main__":
    """
    streamlit run streamlit_app.py 
    """

    model_names = list(upload_folder_dict.keys())
    st.title(" vs. ".join(model_names))

    for video_id in range(16):
        st.subheader(f"Sample #{video_id}")
        cols = st.columns(len(upload_folder_dict))
        for col, (title, folder) in zip(cols, upload_folder_dict.items()):
            video_path = os.path.join(folder, f"{video_id:03d}-00.mp4")
            if os.path.exists(video_path):
                col.caption(f"{title}")
                col.video(video_path)
        with open(video_path.replace("-00.mp4", ".txt")) as f:
            caption = f.read()
        st.write(caption)
        st.write("")