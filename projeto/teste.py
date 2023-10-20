import PySimpleGUI as sg


sg.theme('Reddit')   # Adiciona uma cor
# tudo que vc precisa para criar uma janela
layout =[           
            [sg.Text('Nome:'), sg.InputText(key='usuario',size=(15,0))],
            [sg.Text('Idade:'), sg.InputText(key='idade',size=(15,0))],
            [sg.Text('Pais:'), sg.InputText(key='pais',size=(15,0))],
            [sg.Button('Entrar')],
]

    # Criando a janela
window = sg.Window('Tela de Login').layout(layout)
    # Event Loop to process "events" and get the "values" of the inputs

eventos, valores = window.read()


while True:


    if eventos == sg.WINDOW_CLOSED: # Se o usuario clickar no X
        break
    if eventos == 'Entrar' :
        if valores['usuario'] == 'mateus' and valores['idade'] == 26 and valores['pais'] == 'brasil' :
            print('Bem vindo ao meu programa')

    
window.close()