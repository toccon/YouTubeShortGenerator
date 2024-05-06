# YoutubeShortGenerator

Welcome to YoutubeShortGenerator, a Python project designed to automate the creation of YouTube short videos. This tool leverages the MoviePy library for video editing and Google Text-to-Speech (gTTS) for text to speech conversion. 

## Dependencies

- **MoviePy 1.0.3**: MoviePy is a Python library for video editing, which is used in this project for generating looping background videos. You can install it via pip:
  ```
  pip install moviepy==1.0.3
  ```

- **gTTS (Google Text-to-Speech)**: gTTS is a Python library and CLI tool to interface with Google Translate's text-to-speech API. It's used here for generating audio from text for captions. Install it via pip:
  ```
  pip install gTTS
  ```

## About

The primary purpose of this project is to automate the creation of YouTube short videos. It generates looping background videos and adds captions using MoviePy and Google Text-to-Speech respectively.

## Example Project: Word of the Day (WOTD)

In the provided example project "Word of the Day" (WOTD), the code generates YouTube short videos based on data from spreadsheets. Each spreadsheet contains a word in English, its translation into another language, and an example sentence. These spreadsheets are located in the `spreadsheets` directory.

The process is as follows:

1. The code reads the spreadsheet data.
2. For each row in the spreadsheet, a YouTube short video is generated.
3. The generated videos can be found in the `staging` directory.

## Usage

To use this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/YoutubeShortGenerator.git
   ```

2. Install dependencies:
   ```
   pip install moviepy==1.0.3 gTTS
   ```

3. Run the script with your specific configuration or use the provided example project as a template.

4. Customize the project according to your needs and data.

## Contribution

Contributions are welcome! Feel free to fork this repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvement, please open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
