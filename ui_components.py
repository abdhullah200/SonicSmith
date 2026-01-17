import streamlit as st


def render_header():
    """Render the application header"""
    st.markdown("""
        <div class="title-container">
            <div class="music-icon">🎵</div>
            <h1 class="main-title">AI Music Generator</h1>
            <p class="subtitle">Create beautiful music with the power of AI</p>
        </div>
    """, unsafe_allow_html=True)


def render_api_key_error():
    """Render error message for missing API keys"""
    st.error("⚠️ API keys not found! Please configure your `.env` file.")
    st.markdown("""
        **Create a `.env` file in your project root with:**
        ```
        OPENAI_API_KEY=your_openai_api_key_here
        MODELSLAB_API_KEY=your_modelslab_api_key_here
        ```
    """)


def render_prompt_input():
    """Render the prompt input section"""
    st.markdown("### 🎼 Describe Your Music")
    prompt = st.text_area(
        "Music Prompt",
        "Generate a 30 second uplifting classical piano piece with gentle strings, perfect for a peaceful morning",
        height=120,
        placeholder="Describe the music you want to create...",
        label_visibility="collapsed"
    )
    return prompt


def render_examples():
    """Render example prompts"""
    with st.expander("💡 Need inspiration? Try these examples"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Classical & Orchestral:**
            - Dramatic orchestral piece with timpani and brass
            - Gentle piano solo with emotional melody
            - Baroque harpsichord composition
            """)
        with col2:
            st.markdown("""
            **Modern & Electronic:**
            - Upbeat electronic dance track with synths
            - Ambient soundscape with ethereal pads
            - Lo-fi hip hop beat with jazzy elements
            """)


def render_success_message():
    """Render success message"""
    st.markdown("""
        <div class="success-message">
            ✨ Your music has been generated successfully! ✨
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render application footer"""
    st.markdown("""
        <div style="text-align: center; color: white; padding: 2rem 0; margin-top: 2rem;">
            <p style="opacity: 0.8;">Powered by ModelsLab & OpenAI</p>
        </div>
    """, unsafe_allow_html=True)


# ============================================
# FILE: app.py
# ============================================
import streamlit as st
from agno.utils.log import logger
from config import Config
from styles import get_custom_css
from agent_setup import create_music_agent
from music_generator import MusicGenerator
from ui_components import (
    render_header,
    render_api_key_error,
    render_prompt_input,
    render_examples,
    render_success_message,
    render_footer
)


def main():
    """Main application entry point"""
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Render header
    render_header()
    
    # Check API keys
    if not Config.validate():
        render_api_key_error()
        st.stop()
    
    # Main content card
    st.markdown('<div class="music-card">', unsafe_allow_html=True)
    
    # Render prompt input
    prompt = render_prompt_input()
    
    # Render examples
    render_examples()
    
    st.markdown('<div style="margin: 2rem 0;">', unsafe_allow_html=True)
    
    # Initialize agent and generator
    agent = create_music_agent()
    generator = MusicGenerator(agent)
    
    # Generate button
    if st.button("🎹 Generate Music"):
        if prompt.strip() == "":
            st.warning("⚠️ Please enter a prompt first.")
        else:
            with st.spinner("🎵 Creating your masterpiece..."):
                try:
                    # Generate music
                    music = generator.generate(prompt)
                    
                    if music.audio and len(music.audio) > 0:
                        url = music.audio[0].url
                        
                        # Download audio
                        audio_bytes, filename = generator.download_audio(url)
                        
                        # Display success message
                        render_success_message()
                        
                        # Play audio
                        st.audio(audio_bytes, format="audio/mp3")
                        
                        # Download button
                        st.download_button(
                            label="⬇️ Download Your Music",
                            data=audio_bytes,
                            file_name="generated_music.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.error("❌ No audio generated. Please try again with a different prompt.")
                
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")
                    logger.error(f"Streamlit app error: {e}")
    
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()
