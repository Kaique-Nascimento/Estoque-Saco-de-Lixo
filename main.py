import sqlite3 as bd
from conexao import conectarBanco
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / "img"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path
print(ASSETS_PATH)

#ver o pq ele nao ta pegando a imagem



window = Tk()

window.geometry("886x580")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 580,
    width = 886,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
#ver o pq ele nao ta pegando as imagens
icone_apagar = relative_to_assets("apagar.png")
icone_editar = relative_to_assets("editar.png")

editar_image = PhotoImage(file=icone_editar).subsample(10, 10)
apagar_image = PhotoImage(file=icone_apagar).subsample(10, 10)

# Conectar ao banco de dados
conectarBanco()
        
def texto(x, y, texto, cor, tamanho):
    canvas.create_text(
    x,
    y,
    anchor="nw",
    text=texto,
    fill=cor,
    font=("ArialRoundedMTBold", tamanho * -1)
)
    
def retangulo(x1, y1, x2, y2,cor):
    canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill=cor,
            outline="")
    
def imagem(canvas, x, y,nome):
    canvas.create_image(x, y, image=nome)

def cadastrarSaco(descricao, preco, quantidade):
    try:
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()
        
        dadosSaco = (descricao, preco, quantidade)
        
        inserirSaco = """
        INSERT INTO tb02_saco (tb02_descricao, tb02_preco, tb02_quantidade)
        VALUES (?,?,?)"""
        
        cursor.execute(inserirSaco, dadosSaco)
        conn.commit()
        print(f"Saco '{descricao}' cadastrado com sucesso!")
        
    except Exception as e:
        print("Erro ao cadastrar saco: " + str(e))
        
    finally:
        conn.close()

def cadastrarCliente(nome, endereco, telefone):
    try:
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()
        
        dadosCliente = (nome, endereco, telefone)
        
        inserirCliente = """
        INSERT INTO tb01_cliente (tb01_nome, tb01_endereco, tb01_telefone)
        VALUES (?,?,?)"""
        
        cursor.execute(inserirCliente, dadosCliente)
        conn.commit()
        print(f"Cliente '{nome}' cadastrado com sucesso!")
        
    except Exception as e:
        print("Erro ao cadastrar cliente: " + str(e))
        
    finally:
        conn.close()

def inserirDadosExemplo():
    cadastrarCliente('Eduardo', 'Rua Sei la 434', '+55 11 12345-6789')
    cadastrarCliente('Julia', 'Rua caguei no mato, 1234', '1194059284')
    cadastrarCliente('Antonio Abelardo da silva', 'Rua mato dentro', '+213123123')
    cadastrarSaco('Pia', 40.00, 5)
    cadastrarSaco('20 Litros', 45.00, 5)
    cadastrarSaco('40 Litros', 50.00, 5)
    cadastrarSaco('60 Litros (NORMAL)', 55.00, 5)
    cadastrarSaco('60 Litros (GROSSO)', 60.00, 5)
    cadastrarSaco('100 Litros (NORMAL)', 70.00, 5)
    cadastrarSaco('100 Litros (GROSSO)', 80.00, 5)
    cadastrarSaco('100 Litros (REFORÇADO)', 100.00, 5)
    cadastrarSaco('200 Litros', 75.00, 5)

def carregaClientes():
    try:
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()

        # Verificando se há clientes no banco de dados
        print("Carregando clientes...")
        carregaClientes = "SELECT * FROM tb01_cliente"
        cursor.execute(carregaClientes)
        clientes = cursor.fetchall()

        # Verificando se há clientes cadastrados
        if not clientes:
            print("Não há dados cadastrados!")
            input("Pressione qualquer tecla para continuar...")
            return False
        else:
            # Exibe os dados de cada cliente
            valorY = 171
            valorY2 = 200
            valorTextoY = 177.5
            valorIconeY = 185
            informacoes = ""
            contador = 0  # Contador para controlar quantos clientes foram processados
            for cliente in clientes:
                # Esquerdo
                retangulo(83, valorY, 353, valorY2, "#D9D9D9")
                texto(87, valorTextoY, cliente[1], "#000", 16)
                button_editar = Button(window, image=editar_image, cursor="hand2")
                canvas.create_window(300, valorIconeY, window=button_editar)
                button_apagar = Button(window, image=apagar_image, cursor="hand2")
                canvas.create_window(340, valorIconeY, window=button_apagar)
                
                # Atualizando as coordenadas para o próximo cliente
                valorY += 68
                valorY2 += 68
                valorTextoY += 68
                valorIconeY += 68
                contador += 1

                # Verificando se já exibimos 5 clientes (esquerdo)
                if contador == 5:
                    # Resetando os valores para o lado direito e reiniciando o contador
                    contador = 0
                    valorY = 171
                    valorY2 = 200
                    valorTextoY = 177.5
                    valorIconeY = 185

                    # Direito (começa a exibir clientes no lado direito)
                    retangulo(513, valorY, 783, valorY2, "#D9D9D9")
                    texto(517, valorTextoY, cliente[1], "#000", 16)
                    button_editar = Button(window, image=editar_image, cursor="hand2")
                    canvas.create_window(730, valorIconeY, window=button_editar)
                    button_apagar = Button(window, image=apagar_image, cursor="hand2")
                    canvas.create_window(770, valorIconeY, window=button_apagar)
                    
                    # Atualizando as coordenadas para o próximo cliente no lado direito
                    valorY += 68
                    valorY2 += 68
                    valorTextoY += 68
                    valorIconeY += 68
                    contador += 1

                # Quando o contador atingir 10, paramos de adicionar mais informações
                if contador == 10:
                    break  # Interrompe o loop após o cliente 10

                
            return True
    except Exception as e:
        print("DEU ERRO: " + str(e))
        return False
    finally:
        conn.close()
def criar_botao(x1, y1, x2, y2, texto, comando):
    # Cria um botão no canvas
    button = Button(window, text=texto, command=comando, width=10, height=2, bg="#D9D9D9", font=("ArialRoundedMTBold", 16))
    canvas.create_window((x1 + x2) / 2, (y1 + y2) / 2, window=button)
def comando_voltar():
    print("Voltar clicado!")

def comando_cadastrar():
    print("Cadastrar clicado!")

def comando_avancar():
    print("Avançar clicado!")
def tela():
    canvas.place(x = 0, y = 0)
    texto(30, 42,"Corno gay", "#000", 32)
    texto(44, 125, "porra do caralho", "#819830", 16)

    # Botão "Voltar"
    criar_botao(150.0, 435.0 + 70, 267.0, 489.0 + 70, "Anterior", comando_voltar)

    # Botão "Cadastrar"
    criar_botao(150.0 + 250, 435.0 + 70, 267.0 + 250, 489.0 + 70, "Cadastrar", comando_cadastrar)

    # Botão "Avançar
    criar_botao(150.0 + 250 + 250, 435.0 + 70, 267.0 + 250 + 250, 489.0 + 70, "Avançar", comando_avancar)









  



  











    window.resizable(False, False)
    window.mainloop()


carregaClientes()
tela()