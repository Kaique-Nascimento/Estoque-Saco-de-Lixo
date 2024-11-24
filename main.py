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

apagar_image = PhotoImage(file=icone_apagar)
editar_image = PhotoImage(file=icone_editar)

# Conectar ao banco de dados
conectarBanco()

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
            for cliente in clientes:
                print(f"""Id: {cliente[0]}, Nome: {cliente[1]}, Endereço: {cliente[2]}, Telefone: {cliente[3]}
                {'=-' * 10}""")
            return True
    except Exception as e:
        print("DEU ERRO: " + str(e))
        return False
    finally:
        conn.close()
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
def tela():
    canvas.place(x = 0, y = 0)
    texto(30, 42,"Corno gay", "#000", 32)
    texto(44, 125, "porra do caralho", "#819830", 16)

    retangulo(83, 171, 353, 200,"#D9D9D9")
    texto(87, 177.5, "Cliente 2323", "#000", 16)
    imagem(canvas,83, 200, editar_image)
    imagem(canvas,83, 250, apagar_image)

    retangulo(83, 171+68, 353, 200+68,"#D9D9D9")
    texto(87, 177.5+68, "Cliente 2323", "#000", 16)

    retangulo(83, 239+68, 353, 268+68,"#D9D9D9")
    texto(87, 245.5+68, "Cliente 2323", "#000", 16)

    retangulo(83, 307+68, 353, 336+68,"#D9D9D9")
    texto(87, 313.5+68, "Cliente 2323", "#000", 16)
   

    canvas.create_text(
        404.0,
        525.0,
        anchor="nw",
        text="Cadastrar",
        fill="#000000",
        font=("ArialRoundedMTBold", 16 * -1)
    )

    canvas.create_rectangle(
        166.0,
        435.0,
        283.0,
        489.0,
        fill="#D9D9D9",
        outline="") #voltar

    canvas.create_rectangle(
        621.0,
        435.0,
        738.0,
        489.0,
        fill="#D9D9D9",
        outline="") #avançar

    canvas.create_text(
        647.0,
        452.0,
        anchor="nw",
        text="Avançar",
        fill="#000000",
        font=("ArialRoundedMTBold", 16 * -1)
    )

    canvas.create_text(
        201.0,
        452.0,
        anchor="nw",
        text="Voltar",
        fill="#000000",
        font=("ArialRoundedMTBold", 16 * -1)
    )




  



  




  

    canvas.create_rectangle(
        483.0,
        170.0,
        753.0,
        199.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        483.0,
        170.0,
        753.0,
        199.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        483.0,
        236.0,
        753.0,
        265.0,
        fill="#D9D9D9",
        outline="")
    
    canvas.create_rectangle(
        483.0,
        170.0,
        753.0,
        199.0,
        fill="#D9D9D9",
        outline="")


    canvas.create_rectangle(
        483.0,
        361.0,
        753.0,
        390.0,
        fill="#D9D9D9",
        outline="")



    canvas.create_rectangle(
        483.0,
        297.0,
        753.0,
        326.0,
        fill="#D9D9D9",
        outline="")

    window.resizable(False, False)
    window.mainloop()


carregaClientes()
tela()