#Feito por Andrei Ramos Lopes
#Github: https://github.com/Andreirl032/random-bible-verse-app
import PySimpleGUI as sg
import xml.etree.ElementTree as ET
from random import randrange
import webbrowser

bible_abbreviations = [
    "gn", "ex", "lv", "nm", "dt", "js", "jz", "rt", "1sm", "2sm", "1rs", "2rs",
    "1cr", "2cr", "ed", "ne", "et", "job", "sl", "pv", "ec", "ct", "is", "jr", "lm",
    "ez", "dn", "os", "jl", "am", "ob", "jn", "mq", "na", "hc", "sf", "ag", "zc",
    "ml", "mt", "mc", "lc", "jo", "at", "rm", "1co", "2co", "gl", "ef", "fp",
    "cl", "1ts", "2ts", "1tm", "2tm", "tt", "fm", "hb", "tg", "1pe", "2pe", "1jo",
    "2jo", "3jo", "jd", "ap"
]

chosen_bible_abbreviation = bible_abbreviations[randrange(0,len(bible_abbreviations)-1)]
tree = ET.parse(f'nvi/nvi-{chosen_bible_abbreviation}.xml')
root = tree.getroot()

number_of_chapters = len(root)
chapter_num=randrange(1,number_of_chapters)
chosen_chapter = root[chapter_num-1]
text=""
for i in range(0,len(chosen_chapter),1):
    text+=f"{i+1} {chosen_chapter[i].text}\n"

layout = [[sg.Text("TRECHO ALEATÓRIO DA BÍBLIA:")],
          [sg.Text(f"{root.attrib['name']}, capítulo {chapter_num}")],
          [sg.Text(f"Leia mais em https://www.bibliaonline.com.br/nvi/{chosen_bible_abbreviation}/{chapter_num}",font=(None,0),enable_events=True,key="-LINK-",text_color="orange")],
          [sg.Text(f"{text}")],]
window=sg.Window(title="App da Bíblia", layout=layout, margins=(25, 25),location=(0,0), keep_on_top=True,no_titlebar=False, resizable=True,icon="bible.ico",finalize=True)
window.maximize()
window["-LINK-"].set_cursor("hand2")
window["-LINK-"].Widget.bind("<Enter>", lambda _: window["-LINK-"].update(font=(None,0, "underline")))
window["-LINK-"].Widget.bind("<Leave>", lambda _: window["-LINK-"].update(font=(None, 0)))
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == "-LINK-":
        webbrowser.open(f"https://www.bibliaonline.com.br/nvi/{chosen_bible_abbreviation}/{chapter_num}")
        window.minimize()

window.close()
