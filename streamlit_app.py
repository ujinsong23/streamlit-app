import streamlit as st
import os
import re

# st.set_page_config(layout="wide")

OPTIONS = [
        {
            "models": {
                "m1_16fps": "videos/9sec/m1_16fps_newtest-8k/step-8000",
            },
            "step": 8000,
            "video_length": 9,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes"
        },
        {
            "models": {
                "attn": "videos/9sec/attn_newtest/step-2400",
            },
            "step": 2400,
            "video_length": 9,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes"
        },
        {
            "models": {
                "mamba": "videos/3sec/mamba2_newtest/step-8000",
                "attn": "videos/3sec/attn_newtest/step-8000",
                "m1": "videos/3sec/m1_newtest/step-8000",
                # "m2": "videos/3sec/m2_newtest/step-8000"
            },
            "step": 8000,
            "video_length": 3,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes, duplicate characters"
        },
        {
            "models": {
                "mamba": "videos/3sec/mamba2_newtest/step-6000",
                "attn": "videos/3sec/attn_newtest/step-6000",
                "m1": "videos/3sec/m1_newtest/step-6000",
                "m2": "videos/3sec/m2_newtest/step-6000"
            },
            "step": 6000,
            "video_length": 3,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes, duplicate characters"
        },
        {
            "models": {
                "attn": "videos/3sec/attn_newtest/step-4000",
                "mamba": "videos/3sec/mamba2_newtest/step-4000",
                "m1": "videos/3sec/m1_newtest/step-4000",
                "m2": "videos/3sec/m2_newtest/step-4000"
            },
            "step": 4000,
            "video_length": 3,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes"
        },
        {
            "models": {
                "mamba": "videos/3sec/mamba2_newtest/step-2500",
                "m2": "videos/3sec/m2_newtest/step-2500"
            },
            "step": 2500,
            "video_length": 3,
            "neg_prompt": "motion blur, distorted faces, abnormal eyes"
        }
    ]

def verify_model_dict(model_dict):
    for model_path in model_dict["models"].values():
        if not os.path.exists(model_path):
            print(f"Model path {model_path} does not exist")
            return False
        if not f"{model_dict["video_length"]}s" in model_path:
            print(f"Model path {model_path} does not match video length {model_dict["video_length"]}s")
            return False
        if not f"step-{model_dict["step"]}" in model_path:
            print(f"Model path {model_path} does not match step {model_dict["step"]}")
            return False
    
    return True
        

def stringify_model_names(model_dict):
    string = f"[{model_dict["video_length"]}s-{model_dict["step"]}step] "
    string+= " vs. ".join(model_dict["models"].keys())
    return string

def show_selected_comparison(model_dict):
    st.markdown(f"negative_prompt={model_dict["neg_prompt"]}")

    upload_folder_dict = model_dict["models"]
    
    for video_id in range(16):
        st.subheader(f"Sample #{video_id}")
        if len(upload_folder_dict)<4:
            cols = st.columns(len(upload_folder_dict))
            for col, (title, folder) in zip(cols, upload_folder_dict.items()):
                video_path = os.path.join(folder, f"{video_id:03d}-00.mp4")
                if os.path.exists(video_path):
                    col.caption(f"{title}")
                    col.video(video_path)
        else:
            cols = st.columns(2)
            for i, (title, folder) in enumerate(upload_folder_dict.items()):
                video_path = os.path.join(folder, f"{video_id:03d}-00.mp4")
                if os.path.exists(video_path):
                    with cols[i % 2]:
                        st.caption(f"{title}")
                        st.video(video_path)
                
        with open(video_path.replace("-00.mp4", ".txt")) as f:
            caption = f.read()
        st.write(caption)
        st.write("")

if __name__ == "__main__":
    """
    streamlit run streamlit_app.py 
    """

    options = {
        stringify_model_names(model_dict): model_dict for model_dict in OPTIONS if verify_model_dict(model_dict)
    }

    opt = st.selectbox(
        "Choose the comparison",
        tuple(options.keys())
    )

    show_selected_comparison(options[opt])