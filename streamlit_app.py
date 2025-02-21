import streamlit as st
import os

OPTIONS = [
        # {
        #     "3s-m1-4000step": "videos/3sec/m1_newtest/step-4000",
        #     "3s-mamba-4000step": "videos/3sec/mamba2_newtest/step-4000" 
        # },
        {
            "3s-m2-2500step": "videos/3sec/m2_newtest/step-2500",
            "3s-mamba-2500step": "videos/3sec/mamba2_newtest/step-2500",
        },
        {
            "3s-m1-4000step": "videos/3sec/m1_newtest/step-4000",
            "3s-m2-4000step": "videos/3sec/m2_newtest/step-4000",
            "3s-mamba-4000step": "videos/3sec/mamba2_newtest/step-4000",
        }
    ]

def simplify_model_names(model_names):
    if len(model_names) < 3:
        return model_names
    else:
        return [model_name.split("-")[1] for model_name in model_names]

def show_selected_comparison(upload_folder_dict):
    st.caption(f"negative_prompt=motion blur, distorted faces, abnormal eyes")

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

if __name__ == "__main__":
    """
    streamlit run streamlit_app.py 
    """

    OPTIONS = {
        " vs. ".join(simplify_model_names(upload_folder_dict.keys())):upload_folder_dict for upload_folder_dict in OPTIONS
    }

    option = st.selectbox(
        "Choose the comparison",
        tuple(OPTIONS.keys())
    )

    show_selected_comparison(OPTIONS[option])