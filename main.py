from PySimpleGUI import *
from zipper_creator import make_archive

label1 = Text('Select file(s) to compress: ')

input_box1 = InputText(tooltip='Please select file(s) to compress.')
choose_button1 = FilesBrowse('Choose', key='files')

label2 = Text('Select destination folder: ')
input_box2 = InputText(tooltip='Please select folder to save the compressed files.')
choose_button2 = FolderBrowse('Choose', key='folder')

compress_button = Button('Compress')
output_label = Text(key='output', text_color='yellow')

window = Window('File Zipper', layout=[[label1, input_box1, choose_button1],
                                       [label2, input_box2, choose_button2],
                                       [compress_button, output_label]])


while True:
    event, values = window.read()
    print(event)
    print(values)
    filepath = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths=filepath, dest_dir=folder)
    window['output'].update(value='Compression Completed')
    break


window.close()
