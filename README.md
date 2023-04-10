# ✍️ Script Writer
This module is designed to convert text stories into video scripts using the YAML format and source appropriate footage to accompany the narration. It automates script formatting and optimization for video production. These scripts can be rendered with the [content-renderer](https://github.com/the-innovation-squad/content-renderer).

The project uses the OpenAI models to generate the video script and curates relevant footage based on the script content through:
- Pexels API
- Shutterstock API

## 📜 Example Input
To run this program place your input text in the `input/text.txt` file. The input text should be a story or a news article or any other text that you want to convert into a video script.

```text
In this example input for the Script Writer project, we'll explore the world of futuristic transportation. Imagine a world where flying cars, hyperloop trains, and autonomous vehicles seamlessly navigate through bustling cities. Cutting-edge technology and advanced engineering have revolutionized the way we commute, making travel faster, safer, and more environmentally friendly than ever before. Join us on this exciting journey to uncover how these innovations are shaping the future of transportation and redefining the limits of human mobility.
```

You'll also need an `input/settings.yml` file to specify the video settings. The settings file should be in the following format:

```yaml
footage_engine: "shutterstock" # one of ["shutterstock", "pexels"], default "pexels"
footage_engine_settings: # optional per engine settings, check the code in scripts/footage_engines/... for specifics & defaults
  aspect_ratio: "16_9"
script_style: "funny" # "informative" or "creative" or anything you'd like, default "informative"
max_content_length: 200 # max chacters in a scene's narration, default 200
max_timeline_entries: 3 # max number of scenes, default 3
```

## 🖨️ Example Output
```yaml
title: The Future of Transportation
timeline:
- clip: https://player.vimeo.com/external/408412129.hd.mp4?s=0dc8c5e810d75a1e02e8fc908cb199be129260d3&profile_id=170&oauth2_token_id=57447761
  content: Imagine a world where flying cars, hyperloop trains, and autonomous vehicles
    seamlessly navigate through bustling cities.
- clip: https://player.vimeo.com/external/459027612.hd.mp4?s=b9828da270ea0d1c4fdec819e73771b95d00645d&profile_id=170&oauth2_token_id=57447761
  content: Cutting-edge technology and advanced engineering have revolutionized the
    way we commute, making travel faster, safer, and more environmentally friendly
    than ever before.
- clip: https://player.vimeo.com/external/646926076.hd.mp4?s=9eb7baa241006d075bc1a25a0a82a09c4607553e&profile_id=175&oauth_token_id=57447761
  content: Join us on this exciting journey to uncover how these innovations are shaping
    the future of transportation and redefining the limits of human mobility.
```

## ⚙️ Setup and Installation

1. Clone the repository to your local machine.

2. Copy the `.env.sample` file, rename it to `.env`, and fill in the values:
	```bash
	cp .env.sample .env
	```

3. Install the required Python packages:
	```bash
	pip3 install -r requirements.txt
	```

### Environment Variables
- `OPENAI_API_KEY`: The API key for OpenAI, can be found at https://platform.openai.com/account/api-keys
- `PEXELS_API_KEY`: The API key for Pexels, can be found at https://www.pexels.com/api/new/
- `SHUTTERSTOCK_API_KEY`: The API key for Shutterstock, can be found at https://www.shutterstock.com/account/developers/apps

## 🚀 Running the App

1. To run the app, simply execute the following command:
	```bash
	python3 scripts/main.py
	```
	This will create a script video based on the input text and source the appropriate footage.

## 🔧 Available Arguments

| Short | Long      | Description                                   | Type           |
|-------|-----------|-----------------------------------------------|----------------|
| `-d`  | `--debug` | Enable debug mode, and skip script generation | Flag (boolean) |

## 📖 How the App Works
The app works in the following steps:

1. Read the input text from the input/text.txt file.

2. Generate the keyword script using OpenAI models or use a sample keyword script in debug mode.

3. Add relevant footage to the keyword script using the a video search API

4. Write the final script with footage information to the output/output.yml file.


Feel free to modify and enhance the README to better suit your project's needs.
