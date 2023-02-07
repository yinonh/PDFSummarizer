from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from . import SciHub
import PyPDF2
import re
import os
import dotenv
import openai
import requests

dotenv_file = os.path.join('.', ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


def summarize():
    pdf_text = ''
    try:
        # Open the pdf file in binary mode
        with open("files/file.pdf", "rb") as file:
            # Create pdf reader object
            pdf_reader = PyPDF2.PdfReader(file)
            # Get the document info
            pdf_info = pdf_reader.metadata
            # Get the title from the info

            # Iterate through each page
            for page in range(len(pdf_reader.pages)):
                # Get the page object
                pdf_page = pdf_reader.pages[page]
                # Extract the text from the page
                text = pdf_page.extract_text()
                # Print the text
                pdf_text += text

        match = re.findall("\n[1-9 \.]*[A-Z][a-z]*\n", pdf_text)

        pdf_dict = {}
        if match:
            pdf_dict[match[0]] = pdf_text[:pdf_text.find(match[0])]
        else:
            pdf_dict['\nAll the text\n'] = pdf_text

        for i in range(len(match) - 1):
            start = pdf_text.find(match[i])
            end = pdf_text.find(match[i + 1])
            pdf_dict[match[i]] = pdf_text[start:end]

        openai.api_key = os.environ['OPENAI_SECRET_KEY']
        result = '' if pdf_info.title is None else pdf_info.title
        for i in pdf_dict:
            try:
                resopnse = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="summarize this:" + pdf_dict[i][:4096],
                    temperature=0.2,
                    max_tokens=100,
                )["choices"][0]["text"]
                result += i + resopnse
            except TypeError:
                continue
    except:
        return "Error accrued"

    return result

def uploadFile(request):
    try:
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        fs.save("files/file.pdf", file)
    except Exception:
        return False

    return True

def downloadFile(url):
    try:
        pdfFile = SciHub.SciHub()
        pdfFile.download(url, path='files/file.pdf')
    except Exception:
        return False
    return True


def mainFunc(request):
    s = ''
    if request.method == 'POST':
        if request.POST.get('isLocal'):
            validFile = uploadFile(request)
        else:
            validFile = downloadFile(request.POST.get('textInput'))
        if validFile:
            try:
                s = summarize()
                os.remove("files/file.pdf")
            except:
                s = "Error"
        else:
            return "File invalid"
    return render(request, 'homePage.html', {'summarize': s})
