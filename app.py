import streamlit as st

st.set_page_config(
    page_title="Interior AI Walkthrough",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Interior AI Walkthrough")

st.write(
    "Transform your interior render into a cinematic AI walkthrough."
)

st.divider()

# Upload image
uploaded_image = st.file_uploader(
    "🖼️ Upload your interior render",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:

    st.subheader("Your Interior")

    st.image(
        uploaded_image,
        width="stretch"
    )

    st.success("Image uploaded successfully! 🎉")

    st.divider()

    # Walkthrough settings
    st.subheader("🎬 Walkthrough Settings")

    col1, col2 = st.columns(2)

    with col1:

        camera = st.selectbox(
            "📷 Camera Movement",
            [
                "Slow cinematic forward movement",
                "Smooth room walkthrough",
                "Slow pan from left to right",
                "Slow pan from right to left",
                "Architectural showcase"
            ]
        )

        speed = st.selectbox(
            "⚡ Camera Speed",
            [
                "Very slow",
                "Slow",
                "Medium"
            ]
        )

    with col2:

        aspect_ratio = st.selectbox(
            "📐 Video Format",
            [
                "16:9 — YouTube / Website",
                "9:16 — Instagram / TikTok / Reels"
            ]
        )

        lighting = st.selectbox(
            "💡 Lighting Style",
            [
                "Natural daylight",
                "Warm evening lighting",
                "Bright architectural lighting",
                "Luxury cinematic lighting"
            ]
        )

    duration = st.selectbox(
        "⏱️ Video Duration",
        [
            "4 seconds",
            "6 seconds",
            "8 seconds"
        ]
    )

    instructions = st.text_area(
        "📝 Additional Instructions",
        placeholder="Example: Keep the furniture unchanged and create a smooth realistic camera movement."
    )

    st.divider()

    # AI Prompt Preview
    st.subheader("🧠 AI Walkthrough Prompt")

    generated_prompt = (
        f"Create a realistic cinematic interior walkthrough from the provided "
        f"architectural render. Use {camera.lower()} with a {speed.lower()} "
        f"camera movement. Use {lighting.lower()}. Preserve the existing "
        f"architecture, furniture, materials, colors, proportions, and "
        f"interior details. Keep the movement smooth and realistic. "
        f"Create the video in {aspect_ratio.split('—')[0].strip()} format "
        f"with a duration of {duration}."
    )

    if instructions:
        generated_prompt += f" Additional instructions: {instructions}"

    st.text_area(
        "Generated Prompt",
        value=generated_prompt,
        height=180
    )

    st.divider()
    
   # Generate button
if st.button(
    "🚶 Generate AI Walkthrough",
    type="primary",
    width="stretch"
):

    st.subheader("🎬 Walkthrough Request")

    st.write(f"**Camera:** {camera}")
    st.write(f"**Speed:** {speed}")
    st.write(f"**Format:** {aspect_ratio}")
    st.write(f"**Lighting:** {lighting}")
    st.write(f"**Duration:** {duration}")

    if instructions:
        st.write(f"**Instructions:** {instructions}")

    st.write("### 🧠 Final AI Prompt")

    st.code(
        generated_prompt,
        language="text"
    )

    st.success(
        "✅ Walkthrough settings prepared successfully!"
    )

    st.info(
        "🎬 Demo mode: no paid AI video generation is running yet."
    )
else:

    st.info(
        "👆 Upload an interior render above to begin."
    )