# SonicSmith

SonicSmith is a small, local web app that converts natural-language prompts into short AI-generated musical pieces. It provides an in-browser preview, playback controls, and downloadable audio exports.

## What this repo contains

- A Streamlit UI to enter prompts and preview generated audio
- An agent layer that talks to an AI provider to create music
- Utilities to download and serve generated audio

## Required environment variables

Create a local `.env` (DO NOT commit). The app expects the following variables (placeholders shown):

- `MODEL_PROVIDER` — which provider to use: `openai`, `google`, `anthropic`, or `groq`
- `OPENAI_API_KEY` — OpenAI API key (used when `MODEL_PROVIDER=openai`)
- `GOOGLE_API_KEY` — Google Gemini API key (used when `MODEL_PROVIDER=google`)
- `GROQ_API_KEY` — Groq API key (used when `MODEL_PROVIDER=groq`)
- `ANTHROPIC_API_KEY` — Anthropic API key (used when `MODEL_PROVIDER=anthropic`)
- `MODELSLAB_API_KEY` — ModelsLab API key used for music generation

A safe example file is provided as `.env.example`.

## Quick start

1. Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Copy the example and fill in your keys (do not add real keys to version control):

```bash
cp .env.example .env     # on Windows PowerShell: Copy-Item .env.example .env
# then edit .env and paste your keys
```

3. Run the app locally:

```bash
streamlit run app.py
```

4. In the UI select or configure the `MODEL_PROVIDER` and enter a prompt, then click Generate.

## Choosing a provider

Set `MODEL_PROVIDER` to the provider for which you have valid keys. Only supply the keys you will use; unused provider keys can be left blank in `.env`.

## Security & incidents

- Never commit `.env` or real API keys to git. Use `.env.example` to show variable names only.
- If API keys were committed or pushed, revoke and rotate them immediately.
- After rotating keys, update local `.env` and any deployed secrets stores (GitHub Actions Secrets, host platform env vars, etc.).

## Troubleshooting

- If generation fails, confirm your provider selection and that the relevant API key is valid and not rate-limited.
- Check the Streamlit logs in the terminal for stack traces.

<div align="center">
  
### 💜 Made with Love and Code by Abdullah Ariff

**If you found this project helpful, please consider giving it a ⭐ on GitHub!**

[![GitHub Stars](https://img.shields.io/github/stars/abdhullah200/SonicSmith?style=social)](https://github.com/abdhullah200/SonicSmith)
[![GitHub Forks](https://img.shields.io/github/forks/abdhullah200/SonicSmith?style=social)](https://github.com/abdhullah200/SonicSmith/fork)
[![GitHub Issues](https://img.shields.io/github/issues/abdhullah200/SonicSmith)](https://github.com/abdhullah200/SonicSmith/issues)

</div>


- Add an appropriate `LICENSE` file if you plan to publish the repository.

