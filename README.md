# PDF Summarizer

PDFSummarizer is a web application that allows users to summarize PDF files by either uploading the file or by providing the URL of the file 🔍📄. The application integrates with Sci-Hub to fetch the PDF file and uses OpenAI API to provide high-quality summarization 🤖💬.

**Please note that this repository is a work in progress and  is  not yet complete.**

## Features
- PDF file upload or URL input for summarization 📎💻
- Integrates with OpenAI API to provide high-quality summarization 🤖💬

## Requirements
- Python 3.x 🐍
- Django 3.x 💻
- OpenAI API key 🔑

## Installation
To install the Django PDFSummarizer, follow these steps:
1. Clone the repository to your local machine using `git clone https://github.com/yinonh/PDFSummarizer.git` 📥
2. Navigate to the project directory using `cd PDFSummarizer` 🗂️
3. Create a virtual environment using `python -m venv myenv` and activate it using `source myenv/bin/activate` on Linux or `myenv\Scripts\activate` on Windows 💻
4. Install the required packages using `pip install -r requirements.txt` 📦
5. Add your OpenAI API key to the environment variables or to the local_settings.py file 🔒
6. Run the development server using `python manage.py runserver` 🚀

## Usage
To use the Django PDFSummarizer, follow these steps:
1. Input either the PDF file or the URL of the file on Sci-Hub 📎💻
2. Wait for the file to be summarized 🕐
3. View the summarized text 📝

## Example
![Django PDFSummarizer in action](https://s9.gifyu.com/images/video2123212380-_online-video-cutter.com_.gif)


#### Summary of my CV:
![enter image description here](https://imgur.com/lf2nwM0.png)

#### Summary [this](https://www.mdpi.com/2673-2688/1/2/9) article:
![enter image description here](https://imgur.com/baMCPnc.png)

## Contribution
Contributions to the Django PDFSummarizer are always welcome! If you have a bugfix, improvement, or new feature, please create a pull request or open an issue 🤝.
**Please note that this repository is a work in progress.**

## License
Django PDFSummarizer is licensed under the [MIT license](https://opensource.org/licenses/MIT) 📄.
