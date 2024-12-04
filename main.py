import sqlite3 as bd
from conexao import conectarBanco
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *


OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / "img"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path
print(ASSETS_PATH)
contador_inicial = 1
contador_final = 15
window = Tk()

# Obter as dimensões da tela
screen_width = window.winfo_screenwidth()  # Largura da tela
screen_height = window.winfo_screenheight()  # Altura da tela

# Ajustando a geometria da janela para ocupar toda a tela
window.geometry(f"{screen_width}x{screen_height}+0+0")  # Tamanho igual à tela

# Configurando o canvas para preencher toda a janela
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=screen_height,  # Altura igual à altura da tela
    width=screen_width,     # Largura igual à largura da tela
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.pack(fill="both", expand=True)  # Isso faz o canvas se expandir para ocupar todo o espaço disponível

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

def quebrar_nome(nome, largura_maxima=280):
    # Função para quebrar o nome em várias linhas, baseado na largura máxima da janela
    palavras = nome.split()  # Dividir o nome em palavras
    linhas = []  # Armazenar as linhas de texto
    linha_atual = ""  # Começar com uma linha vazia

    for palavra in palavras:
        # Se adicionar a palavra ultrapassar a largura máxima, cria uma nova linha
        if len(linha_atual + " " + palavra) > largura_maxima:
            linhas.append(linha_atual.strip())  # Adiciona a linha atual à lista de linhas
            linha_atual = palavra  # Começa uma nova linha com a palavra atual
        else:
            linha_atual += " " + palavra  # Adiciona a palavra à linha atual

    if linha_atual:
        linhas.append(linha_atual.strip())  # Adiciona a última linha

    return linhas
def nomeClienteBanco(id):  
    try:
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()
        query = "SELECT tb01_nome FROM tb01_cliente WHERE tb01_id = ?"
        cursor.execute(query, (id,))
        nome_cliente = cursor.fetchone()
        
        if nome_cliente:
            return nome_cliente[0] 
        else:
            return None  
        
    except Exception as e:
        print("DEU ERRO: " + str(e))
        return None  
    finally:
        conn.close()

def editarCliente(id):
    print("Editando cliente com ID:", id)
    
def apagarCliente(id):
    window3 = Toplevel() 
    window3.geometry("300x150")  
    window3.configure(bg="#FFFFFF") 

    # Centralizando a janela
    screen_width = window3.winfo_screenwidth()  
    screen_height = window3.winfo_screenheight()  

    window_width = 300 
    window_height = 180  

    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    window3.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    canvas2 = Canvas(window3, bg="#FFFFFF", height=150, width=300, bd=0, highlightthickness=0)
    canvas2.pack() 

    try:
        conn = bd.connect('tb_saco.db') 
        cursor = conn.cursor()  
        
        cursor.execute("DELETE FROM tb01_cliente WHERE tb01_id = ?", (id,))
        conn.commit()
        
        canvas2.create_text(150, 80, text="Cliente apagado com sucesso", font=("Arial", 14), fill="#000")
        button_ok = Button(window3, text="Ok", command=lambda: window3.destroy(), width=8, height=2)
        button_ok.place(x=110, y=135)  
        carregaClientes()

    except Exception as e:
        print("Deu erro: " + str(e))

    finally:
        if conn:
            conn.close()


def telaApagarCliente(id):
    print("Apagar cliente com ID:", id)
    # Criando a janela de confirmação
    window2 = Toplevel() 
    window2.geometry("300x150")  
    window2.configure(bg="#FFFFFF") 

# Centralizando a janela
    screen_width = window2.winfo_screenwidth()  # Largura da tela
    screen_height = window2.winfo_screenheight()  # Altura da tela

    window_width = 300  # Largura da janela
    window_height = 180  # Altura da janela

    # Calculando a posição para centralizar
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)

    # Definindo a posição da janela
    window2.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    canvas2 = Canvas(window2, bg="#FFFFFF", height=150, width=300, bd=0, highlightthickness=0)
    canvas2.pack() 
    nome_cliente = nomeClienteBanco(id)
    canvas2.create_text(150, 50, text=f"Deseja apagar?", font=("Arial", 16), fill="#000")
    linhas_nome = quebrar_nome(nome_cliente)
    y_pos = 80  
    for linha in linhas_nome:
        canvas2.create_text(150, y_pos, text=linha, font=("Arial", 14), fill="#000")
        y_pos += 20  

    def confirmar():
        window2.destroy()
        apagarCliente(id)
    def cancelar():
        window2.destroy()
    
    button_confirmar = Button(window2, text="Sim", command=confirmar, width=8, height=2)
    button_confirmar.place(x=75, y=135)  

    button_cancelar = Button(window2, text="Não", command=cancelar, width=8, height=2)
    button_cancelar.place(x=180, y=135)  

    window2.mainloop()
def carregaClientes():
    try:
        conn = bd.connect('tb_saco.db')
        cursor = conn.cursor()

        # Verificando se há clientes no banco de dados
        print("Carregando clientes...")

        # Carregar a quantidade mínima e máxima de ids
        carregaContadoresSQL = "SELECT MIN(tb01_id), MAX(tb01_id) FROM tb01_cliente;"
        cursor.execute(carregaContadoresSQL)
        contadores = cursor.fetchall()
        
        # Exibindo valores de MIN e MAX do ID
        for contadore in contadores:
            print(f"Min tb01_id: {contadore[0]}, Max tb01_id: {contadore[1]}")
        
        # Consulta SQL para carregar os clientes no intervalo de IDs
        carregaClientesSQL = "SELECT * FROM tb01_cliente ORDER BY tb01_nome ASC"
        print(f"Consultando IDs entre {contador_inicial} e {contador_final}...")

        # Executando a consulta com os parâmetros contador_inicial e contador_final
        cursor.execute(carregaClientesSQL)
        clientes = cursor.fetchall()

        if not clientes:
            print("Não há dados cadastrados!")
            input("Pressione qualquer tecla para continuar...")
            return False
        else:
            # Inicializando as variáveis de posição para desenhar os clientes
            valorY = 171
            valorY2 = 200
            valorTextoY = 177.5
            valorIconeY = 185
            contador = 0

            # Número de colunas (3 colunas)
            colunas = 3

            for cliente in clientes:
                # Calculando a coluna onde o cliente vai ficar (0, 1, 2)
                coluna = contador % colunas  # Modulo para distribuir os clientes em 3 colunas

                # Lógica para determinar a posição X de acordo com a coluna
                if coluna == 0:
                    posX = 83  # Primeira coluna (esquerda)
                elif coluna == 1:
                    posX = 513  # Segunda coluna (centro)
                else:
                    posX = 903  # Terceira coluna (direita)

                # Exibindo o cliente
                retangulo(posX, valorY, posX + 270, valorY2, "#D9D9D9")  # A largura foi ajustada para todas as colunas
                texto(posX + 4, valorTextoY, cliente[1], "#000", 16)  # Ajuste conforme o índice da coluna para o nome do cliente

                # Atualizando a posição para o próximo cliente
                valorY += 68
                valorY2 += 68
                valorTextoY += 68
                valorIconeY += 68

                # Quando 5 clientes foram exibidos, resetamos o valorY para a próxima linha
                if (contador + 1) % 5 == 0:
                    valorY = 171
                    valorY2 = 200
                    valorTextoY = 177.5
                    valorIconeY = 185

                contador += 1

                # Limite de 15 clientes
                if contador >= 15:
                    break  # Interrompe o loop após 15 clientes

            return True
    except Exception as e:
        print("DEU ERRO: " + str(e))
        return False
    finally:
        conn.close()

def criar_botao(x1, y1, x2, y2, texto, comando):
    button = Button(window, text=texto, command=comando, width=10, height=2, bg="#D9D9D9", font=("ArialRoundedMTBold", 16))
    canvas.create_window((x1 + x2) / 2, (y1 + y2) / 2, window=button)

def comando_voltar():
    global contador_inicial, contador_final
    print("Voltar clicado!")
    contador_inicial -= 15
    contador_final = contador_inicial + 14  # Ajustado para que o intervalo seja correto
    if contador_final <= 0:
        contador_final = 1  # Garantir que o contador_final não seja negativo
    print(contador_inicial, contador_final)
    carregaClientes()

def comando_cadastrar():
    
    print("Cadastrar clicado!")
def comando_avancar():
    global contador_inicial, contador_final
    print("Avançar clicado!")
    contador_inicial += 15
    contador_final = contador_inicial + 14  # Ajustado para que o intervalo seja correto
    print(contador_inicial, contador_final)
    carregaClientes()

def tela():
    canvas.place(x = 0, y = 0)
    texto(30, 42,"Sistema de estoque saco de lixo", "#000", 32)
    screen_width = window.winfo_screenwidth()  
    screen_height = window.winfo_screenheight()  

    botao_height = 70
    y_botoes = screen_height - botao_height - 80  

    largura_espaco = 40  
    criar_botao(largura_espaco, y_botoes, largura_espaco + 117, y_botoes + botao_height, "Anterior", comando_voltar)

    # Botão "Cadastrar" - centralizado
    largura_centralizada = (screen_width - 117) / 2  # 117 é a largura do botão
    criar_botao(largura_centralizada, y_botoes, largura_centralizada + 117, y_botoes + botao_height, "Cadastrar", comando_cadastrar)

    # Botão "Avançar" - ajustado para ficar um pouco afastado da borda direita
    largura_direita = screen_width - 157  # 157 é a largura do botão + margem
    criar_botao(largura_direita, y_botoes, largura_direita + 117, y_botoes + botao_height, "Avançar", comando_avancar)
    

    window.resizable(False, False)
    carregaClientes()

    window.mainloop()


tela()