from xml.dom.minidom import Document

from django.http import HttpResponse
import plotly.graph_objs as go
import plotly.offline as opy
import pandas as pd
import plotly.io as pio
import math
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UploadedFile
import os
import uuid
from datetime import datetime
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect



# def get_unique_filename(filename):
#     timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#     basename, ext = os.path.splitext(filename)
#     new_filename = f'{basename}_{timestamp}{ext}'
#     return new_filename

# @csrf_exempt
# def upload_file(request):
#     if request.method == 'POST':
#         for file in request.FILES.getlist('file'):
#             # Generate a unique file name
#             #new_filename = get_unique_filename(file.name)
#             # Save the file to the database
#             UploadedFile.objects.create( uploaded_text_files=file)
#     return render(request, 'django1stapp\\upload_pour1.html')




# @csrf_exempt
# def upload_file(request):
#     if request.method == 'POST':
#         new_filename = request.POST.get('new_filename')
#         for file in request.FILES.getlist('file'):
#             # Check if a file with the same name already exists
#             existing_file = UploadedFile.objects.filter(uploaded_text_files__contains=new_filename)
#             if existing_file:
#                 existing_file.delete()
#             # Rename the file
#             file.name = new_filename
#             # Save the file to the database
#             UploadedFile.objects.create(uploaded_text_files=file)
#     return render(request, 'django1stapp\\upload_pour1.html')



from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         # Get the uploaded file and the desired new file name
#         uploaded_file = request.FILES['file']
#         new_file_name = request.POST['new_file_name']
#
#         # Check if a file with this name already exists in the database
#         existing_file = UploadedFile.objects.filter(file_name=new_file_name).first()
#
#         if existing_file:
#             # If the file already exists, delete the old file and replace it with the new one
#             existing_file.uploaded_text_files.delete()
#
#         # Generate a unique file name and save the file to the database
#         unique_file_name = slugify(new_file_name)
#         UploadedFile.objects.create(uploaded_text_files=uploaded_file, file_name=unique_file_name)
#
#         return HttpResponse('File uploaded successfully.')
#     else:
#         return render(request, 'django1stapp\\upload_pour1.html')

#
from django.shortcuts import render, redirect
from .forms import UploadFileForm_Pour1,UploadFileForm_Pour2
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            request.session['user'] = username
            return redirect (admin_page)
        elif username == 'customer' and password == 'customer':
            request.session['user'] = username
            return redirect(customer_page)
        else:
            return render(request, 'django1stapp\\login.html', {'error': 'Invalid login credentials'})
    return render(request, 'django1stapp\\login.html')


def admin_page(request):
    if 'user' in request.session and request.session['user'] == 'admin':
        return render(request, 'django1stapp\\admin_page.html', {'username': request.session['user']})
    else:
        return redirect(login)


def customer_page(request):
    if 'user' in request.session and request.session['user'] == 'customer':
        return render(request, 'django1stapp\\customer_page.html', {'username': request.session['user']})
    else:
        return redirect(login)


# def home(request):
#     return render(request, 'django1stapp\\home.html')

from django.contrib import messages
def upload_file_pour1(request):
    #success = False
    if request.method == 'POST':
        form = UploadFileForm_Pour1(request.POST, request.FILES)
        if form.is_valid():
            names = [form.cleaned_data.get('name{}'.format(i)) for i in range(1, 9)]
            files = [form.cleaned_data.get('file{}'.format(i)) for i in range(1, 9)]
            for name, file in zip(names, files):
                if file:
                    # check if an UploadedFile object with this name already exists
                    uploaded_file, created = UploadedFile.objects.get_or_create(name=name)
                    if not created:
                        # if an UploadedFile object already exists, delete the old file
                        uploaded_file.file.delete()
                    # save the new file to the UploadedFile object
                    uploaded_file.file.save(name, file)

            #success = True

            #return redirect(upload_file)
    else:
        form = UploadFileForm_Pour1()
    return render(request, 'django1stapp\\upload_pour1.html', {'form': form})

def upload_file_pour2(request):
    #success = False
    if request.method == 'POST':
        form = UploadFileForm_Pour2(request.POST, request.FILES)
        if form.is_valid():
            names = [form.cleaned_data.get('name{}'.format(i)) for i in range(1, 7)]
            files = [form.cleaned_data.get('file{}'.format(i)) for i in range(1, 7)]
            for name, file in zip(names, files):
                if file:
                    # check if an UploadedFile object with this name already exists
                    uploaded_file, created = UploadedFile.objects.get_or_create(name=name)
                    if not created:
                        # if an UploadedFile object already exists, delete the old file
                        uploaded_file.file.delete()
                    # save the new file to the UploadedFile object
                    uploaded_file.file.save(name, file)

            #success = True

            #return redirect(upload_file)
    else:
        form = UploadFileForm_Pour2()
    return render(request, 'django1stapp\\upload_pour2.html', {'form': form})

def pour1(request):
    # Get the names of the 8 files
    file_names = ["R1 Core", "R2 Core", "R2 Top", "R3 Core", "R3 Top", "R4 Core", "R4 Top", "R5 Core"]

    # Get the file objects from the database
    file_objs = [UploadedFile.objects.get(name=name) for name in file_names]

    # Get the file contents
    file_contents = []
    file_names = []
    for file_obj in file_objs:
        file_names.append(file_obj.name)
        file_contents.append(file_obj.file.read())

    # Perform calculations on the file contents
    for file_name, file_content in zip(file_names, file_contents):
        # Display the name of the file
        print(file_name)
        #print(file_contents)

        # Perform calculations on file_content
    for i, file_content in enumerate(file_contents):
        file_path = os.path.join("D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt", file_names[i] + ".txt")
        with open(file_path, "w") as f:
            f.write(file_content.decode())

    dfs = []
    max_cum_hrs = 0
    file_names = ['R1 Core', 'R2 Core', 'R2 Top', 'R3 Core', 'R3 Top','R4 Core','R4 Top','R5 Core']
    location = "D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt"


    #for i in range(1, 9):
    for file_name in (file_names):
        file_path = f"{location}\\{file_name}.txt"

        #print(file_path)

        df = pd.read_csv(file_path, delim_whitespace=True, header=None,
                         names=['SR.NO.', 'DATE', 'TIME', 'TEMPERATURE', 'BATTERY'])
        # Calculate the TIME(SEC) column using the formula

        df['TIME(SEC)'] = df['TIME'].apply(lambda x: pd.Timedelta(x).seconds)

        # Calculate the ABS TIME(SEC) column using the formula
        time_sec = df['TIME(SEC)'].values
        abs_time_sec = [0]
        for j in range(1, len(time_sec)):
            if time_sec[j] >= time_sec[j - 1]:
                abs_time_sec.append(time_sec[j] - time_sec[j - 1])
            else:
                abs_time_sec.append(24 * 3600 - (time_sec[j - 1]))
        df['ABS TIME(SEC)'] = abs_time_sec

        # Calculate the ABS TIME(HRS) column using the formula
        df['ABS TIME(HRS)'] = df['ABS TIME(SEC)'] / 3600

        # Calculate the CUM(HRS) column using the formula
        cum_hrs = [0]
        for j in range(1, len(df)):
            cum_hrs.append(df.at[j, 'ABS TIME(HRS)'] + cum_hrs[j - 1])
        df['CUM(HRS)'] = cum_hrs

        # Calculate the TTF column using the formula
        df['TTF'] = df['ABS TIME(HRS)'] * df['TEMPERATURE']

        # Calculate the CUM TTF column using the formula
        cum_ttf = [0]
        for i in range(1, len(df)):
            cum_ttf.append(df.at[i, 'TTF'] + cum_ttf[i - 1])
        df['CUM TTF'] = cum_ttf

        if df['CUM(HRS)'].max() > max_cum_hrs:
            max_cum_hrs = df['CUM(HRS)'].max()

        # Format the ABS TIME(HRS), CUM(HRS), TTF and CUM TTF columns as floats with two decimal places
        df['ABS TIME(HRS)'] = round(df['ABS TIME(HRS)'], 2)
        df['CUM(HRS)'] = round(df['CUM(HRS)'], 2)
        df['TTF'] = round(df['TTF'], 2)
        df['CUM TTF'] = round(df['CUM TTF'], 2)

        # Append the DataFrame to the list
        dfs.append(df)
        with pd.ExcelWriter('D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt\\output_file_pour1.xlsx') as writer:

            for i, df in enumerate(dfs):


                    df.to_excel(writer, sheet_name=f"Sheet{i+1}", index=False)

        # Create a list of traces for the plot
    traces_temperature = []
    traces_cumttf = []

    layout_temperature = go.Layout(title='Hours vs Temperature',
                                   xaxis=dict(title='Hours', tickmode='linear', dtick=6,
                                              range=[0, math.ceil(max_cum_hrs / 6) * 6]),
                                   yaxis=dict(title='Temperature (°C)', dtick=10), height=650)

    layout_cumttf = go.Layout(title='Hours vs TTF',
                              xaxis=dict(title='Hours', dtick=6, range=[0, math.ceil(max_cum_hrs / 6) * 6]),
                              yaxis=dict(title='TTF', range=[0, df['CUM TTF']]), height=650)



    # Create the figure
    ms = ['R1 Core', 'R2 Core', 'R2 Top', 'R3 Core', 'R3 Top','R4 Core','R4 Top','R5 Core']

    if request.method == 'POST':
        selected_sheets = request.POST.getlist('selected_sheets')
    #     print(selected_sheets)

        for i, Core in enumerate(ms):
            if Core in selected_sheets:
                dfs = pd.read_excel('D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt\\output_file_pour1.xlsx', sheet_name=f"Sheet{i+1}")
                #print()
                # Add a trace for the current DataFrame
                trace = go.Scatter(x=dfs['CUM(HRS)'], y=dfs['TEMPERATURE'], mode='lines', name=Core,
                                   customdata=dfs['CUM(HRS)'],
                                   hovertemplate='Cumulative Hours: %{customdata:.2f}<br>Temperature: %{y:.2f}')
                traces_temperature.append(trace)

                tracettf = go.Scatter(x=dfs['CUM(HRS)'], y=dfs['CUM TTF'], mode='lines', name=Core,
                                      customdata=dfs['CUM(HRS)'],
                                      hovertemplate='Cumulative Hours: %{customdata:.2f}<br>TTF: %{y:.2f}')
                traces_cumttf.append(tracettf)

        if not selected_sheets:
            print("No sheets selected")


    fig = go.Figure(data=traces_temperature, layout=layout_temperature)
    fig2 = go.Figure(data=traces_cumttf, layout=layout_cumttf)



    plot_div1 = opy.plot(fig, auto_open=False, output_type='div')
    plot_div2 = opy.plot(fig2, auto_open=False, output_type='div')

    return render(request, 'django1stapp\\pour1.html', {'div1': plot_div1, 'div2': plot_div2})
def pour2(request):
    # Get the names of the 8 files
    file_names = ["R6 Top", "R6 Core", "R6 Bottom", "R7 Top", "R7 Core", "R7 Bottom"]

    # Get the file objects from the database
    file_objs = [UploadedFile.objects.get(name=name) for name in file_names]

    # Get the file contents
    file_contents = []
    file_names = []
    for file_obj in file_objs:
        file_names.append(file_obj.name)
        file_contents.append(file_obj.file.read())

    # Perform calculations on the file contents
    for file_name, file_content in zip(file_names, file_contents):
        # Display the name of the file
        print(file_name)
        #print(file_contents)

        # Perform calculations on file_content
    for i, file_content in enumerate(file_contents):
        file_path = os.path.join("D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt", file_names[i] + ".txt")
        with open(file_path, "w") as f:
            f.write(file_content.decode())

    dfs = []
    max_cum_hrs = 0
    file_names = ["R6 Top", "R6 Core", "R6 Bottom", "R7 Top", "R7 Core", "R7 Bottom"]
    location = "D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt"


    #for i in range(1, 9):
    for file_name in (file_names):
        file_path = f"{location}\\{file_name}.txt"

        #print(file_path)

        df = pd.read_csv(file_path, delim_whitespace=True, header=None,
                         names=['SR.NO.', 'DATE', 'TIME', 'TEMPERATURE', 'BATTERY'])
        # Calculate the TIME(SEC) column using the formula

        df['TIME(SEC)'] = df['TIME'].apply(lambda x: pd.Timedelta(x).seconds)

        # Calculate the ABS TIME(SEC) column using the formula
        time_sec = df['TIME(SEC)'].values
        abs_time_sec = [0]
        for j in range(1, len(time_sec)):
            if time_sec[j] >= time_sec[j - 1]:
                abs_time_sec.append(time_sec[j] - time_sec[j - 1])
            else:
                abs_time_sec.append(24 * 3600 - (time_sec[j - 1]))
        df['ABS TIME(SEC)'] = abs_time_sec

        # Calculate the ABS TIME(HRS) column using the formula
        df['ABS TIME(HRS)'] = df['ABS TIME(SEC)'] / 3600

        # Calculate the CUM(HRS) column using the formula
        cum_hrs = [0]
        for j in range(1, len(df)):
            cum_hrs.append(df.at[j, 'ABS TIME(HRS)'] + cum_hrs[j - 1])
        df['CUM(HRS)'] = cum_hrs

        # Calculate the TTF column using the formula
        df['TTF'] = df['ABS TIME(HRS)'] * df['TEMPERATURE']

        # Calculate the CUM TTF column using the formula
        cum_ttf = [0]
        for i in range(1, len(df)):
            cum_ttf.append(df.at[i, 'TTF'] + cum_ttf[i - 1])
        df['CUM TTF'] = cum_ttf

        if df['CUM(HRS)'].max() > max_cum_hrs:
            max_cum_hrs = df['CUM(HRS)'].max()

        # Format the ABS TIME(HRS), CUM(HRS), TTF and CUM TTF columns as floats with two decimal places
        df['ABS TIME(HRS)'] = round(df['ABS TIME(HRS)'], 2)
        df['CUM(HRS)'] = round(df['CUM(HRS)'], 2)
        df['TTF'] = round(df['TTF'], 2)
        df['CUM TTF'] = round(df['CUM TTF'], 2)

        # Append the DataFrame to the list
        dfs.append(df)
        with pd.ExcelWriter('D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt\\output_file_pour2.xlsx') as writer:

            for i, df in enumerate(dfs):


                    df.to_excel(writer, sheet_name=f"Sheet{i+1}", index=False)

        # Create a list of traces for the plot
    traces_temperature = []
    traces_cumttf = []

    layout_temperature = go.Layout(title='Hours vs Temperature',
                                   xaxis=dict(title='Hours', tickmode='linear', dtick=6,
                                              range=[0, math.ceil(max_cum_hrs / 6) * 6]),
                                   yaxis=dict(title='Temperature (°C)', dtick=10), height=650)

    layout_cumttf = go.Layout(title='Hours vs TTF',
                              xaxis=dict(title='Hours', dtick=6, range=[0, math.ceil(max_cum_hrs / 6) * 6]),
                              yaxis=dict(title='TTF', range=[0, df['CUM TTF']]), height=650)



    # Create the figure
    ms = ["R6 Top", "R6 Core", "R6 Bottom", "R7 Top", "R7 Core", "R7 Bottom"]

    if request.method == 'POST':
        selected_sheets = request.POST.getlist('selected_sheets')
    #     print(selected_sheets)

        for i, Core in enumerate(ms):
            if Core in selected_sheets:
                dfs = pd.read_excel('D:\\Naval_Malpani\\DJANGO_PYTHON\\mysite\\media\\database_txt\\output_file_pour2.xlsx', sheet_name=f"Sheet{i+1}")
                #print()
                # Add a trace for the current DataFrame
                trace = go.Scatter(x=dfs['CUM(HRS)'], y=dfs['TEMPERATURE'], mode='lines', name=Core,
                                   customdata=dfs['CUM(HRS)'],
                                   hovertemplate='Cumulative Hours: %{customdata:.2f}<br>Temperature: %{y:.2f}')
                traces_temperature.append(trace)

                tracettf = go.Scatter(x=dfs['CUM(HRS)'], y=dfs['CUM TTF'], mode='lines', name=Core,
                                      customdata=dfs['CUM(HRS)'],
                                      hovertemplate='Cumulative Hours: %{customdata:.2f}<br>TTF: %{y:.2f}')
                traces_cumttf.append(tracettf)

        if not selected_sheets:
            print("No sheets selected")


    fig = go.Figure(data=traces_temperature, layout=layout_temperature)
    fig2 = go.Figure(data=traces_cumttf, layout=layout_cumttf)



    plot_div1 = opy.plot(fig, auto_open=False, output_type='div')
    plot_div2 = opy.plot(fig2, auto_open=False, output_type='div')

    return render(request, 'django1stapp\\pour2.html', {'div1': plot_div1, 'div2': plot_div2})