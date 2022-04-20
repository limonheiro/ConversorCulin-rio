import PySimpleGUI as sg

sg.theme("graygraygray")
sg.set_options(font="Futura 10")

# https://www.sepac.com.br/blog/chefe-sepac/pesos-e-medidas-na-culinaria/
def grXicara(valor, peso):
	valor = (round(valor / peso, 2))
	return (
		str(valor) + f' Xicara{"s" if valor > 1 else ""}'
	)

def xrKilo(valor, peso):
	valor = (round(valor * peso, 2))
	return (
		str(valor / 1000 if valor >= 1000 else valor)
		+ f'{"kg" if valor >= 1000 else "g"}'
	)

def Conversão(valuesOutput, window):
	try:
		output_string = "Digite um número"
		entrada = float(valuesOutput[-1])
		match valuesOutput[-2]:
			case "-TAB_TRIGO-":
				match valuesOutput[0]:
					case "gramas para xicara":
						output_string = grXicara(valor=entrada,peso=120)
					case "xicara para gramas":
						output_string = xrKilo(valor=entrada, peso=120)
			case "-TAB_AÇUCAR-":
				match valuesOutput[1]:
					case "gramas para xicara":
						output_string = grXicara(valor=entrada,peso=180)
					case "xicara para gramas":
						output_string = xrKilo(valor=entrada, peso=180)
			case "-TAB_AGUA-":
				match valuesOutput[2]:
					case "ml para xicara":
						value = round(entrada / 250.0, 2)
						output_string = (
							str(value) + f' Xicara{"s" if value > 1 else ""}'
					)
					case "xicara para ml":
						value = round(entrada * 250.0, 2)
						output_string = (
							str(value / 1000 if value >= 1000 else value)
							+ f'{"l" if value >= 1000 else "ml"}'
						)
		window["-OUTPUT-"].update(output_string)
	except ValueError:
		window["-OUTPUT-"].update("Digite um valor")


layout01 = [
    [
        sg.Spin(
            ["gramas para xicara", "xicara para gramas"],
            key="-UNITS_TRIGO-",
            expand_x=True,
        )
    ]
]

layout02 = [
    [
        sg.Spin(
            ["gramas para xicara", "xicara para gramas"],
            key="-UNITS_AÇUCAR-",
            expand_x=True,
        )
    ],
]

layout03 = [
    [
		sg.Spin(
			["ml para xicara", "xicara para ml"], 
			key="-UNITS_AGUA-", 
			expand_x=True
		)
	],
]

tabGroup = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Trigo", layout01, key="-TAB_TRIGO-"),
                    sg.Tab("Açucar", layout02, key="-TAB_AÇUCAR-"),
                    sg.Tab("Água", layout03, key="-TAB_AGUA-"),
                ]
            ],
			expand_x =True,
			border_width=0,
			pad=((0,0),(0,0)),
			selected_background_color='#EEEEEE',
			tab_background_color ='#AAAAAA',
			background_color='#FFFFFF'#graygraygray == EEEEEE
        ),
    ]
	
]

layout = [
    tabGroup,
    [sg.Input(key="-INPUT_TRIGO-",background_color="white")],
    [sg.Text("Digite um valor", key="-OUTPUT-", background_color='white')],
]

window = sg.Window("Conversor", layout, element_padding=(1,1), background_color='white')

valueRadio = ""
timeout = 200
while True:
    event, values = window.read(timeout=timeout)

    if event == sg.WIN_CLOSED:
        print("GoodBye.")
        break
    #'gramas para xicara', 	'gramas para xicara', 	'ml para xicara', 	'-TAB_AGUA-', 	'250'
    #unidadeTrigo, 			unidadeAçucar,			 unidadeAgua, 		tabelaAtiva, 	entrada
    valuesOutput = [i for i in values.values()]
    Conversão(valuesOutput, window)

window.close()
