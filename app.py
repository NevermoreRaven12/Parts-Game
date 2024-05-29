import os
from PIL import Image, ImageTk
import random
import tkinter as tk
from tkinter import messagebox

# Função para selecionar uma imagem aleatória da pasta de imagens
def selecionar_imagem_aleatoria(actor_imgs):
    extensoes = ('.jpg', '.jpeg', '.png')
    arquivos = [f for f in os.listdir(actor_imgs) if f.lower().endswith(extensoes)]
    img_random = random.choice(arquivos)
    caminho_imagem = os.path.join(actor_imgs, img_random)
    return caminho_imagem, img_random

# Função para processar a imagem e obter o recorte
def processar_imagem(caminho_imagem):
    img = Image.open(caminho_imagem)
    img_resized = img.resize((400, 400))
    largura, altura = img_resized.size
    crop_size = (0, altura - 200, 200, altura)
    img_cropped = img_resized.crop(crop_size)
    return img_cropped

# Função para iniciar um novo jogo
def iniciar_novo_jogo():
    global resposta_correta, letras_reveladas, dicas_usadas
    entrada_texto.delete(0, 'end')
    letras_reveladas.clear()  # Limpar letras reveladas
    dica_label.config(text="")  # Limpar label de dica
    dicas_usadas = 0  # Reiniciar contador de dicas usadas
    
    # Selecionar uma nova imagem aleatória
    caminho_imagem, nome_imagem = selecionar_imagem_aleatoria(actor_imgs)
    
    # Processar a imagem e obter o recorte
    imagem_recortada = processar_imagem(caminho_imagem)
    
    # Atualizar resposta correta para a nova imagem
    resposta_correta = os.path.splitext(nome_imagem)[0]
    
    # Atualizar a exibição da imagem recortada
    imagem_recortada_tk = ImageTk.PhotoImage(imagem_recortada)
    label_recorte.configure(image=imagem_recortada_tk)
    label_recorte.image = imagem_recortada_tk
    
    # Atualizar a dica inicial
    dica_inicial = '_' * len(resposta_correta)
    dica_label.config(text=dica_inicial)

# Função para verificar a resposta inserida pelo jogador
def verificar_resposta(event=None):
    entrada = entrada_texto.get().strip()
    if entrada.lower() == resposta_correta.lower():
        messagebox.showinfo("Resultado", "Você acertou!")
        iniciar_novo_jogo()
    else:
        messagebox.showerror("Resultado", "Você errou. Tente novamente.")

# Função para revelar uma letra na dica
def dica():
    global letras_reveladas, dicas_usadas, resposta_correta
    if dicas_usadas < len(resposta_correta):
        # Selecionar uma letra ainda não revelada
        while True:
            indice = random.randint(0, len(resposta_correta) - 1)
            if indice not in letras_reveladas:
                letras_reveladas.add(indice)
                dicas_usadas += 1
                break
        # Mostrar a letra revelada no Label de dica
        dica = ''.join([resposta_correta[i] if i in letras_reveladas else '_' for i in range(len(resposta_correta))])
        dica_label.config(text=dica)
    else:
        messagebox.showinfo("Dicas Esgotadas", "Todas as letras já foram reveladas.")

# Função para mostrar a imagem recortada na interface gráfica
def mostrar_imagem_recortada(recorte, resposta):
    global letras_reveladas, dicas_usadas, resposta_correta
    resposta_correta = resposta
    
    janela = tk.Tk()
    janela.title('Jogo das Partes')
    
    # Configurar widgets da interface
    recorte_tk = ImageTk.PhotoImage(recorte)
    global label_recorte
    label_recorte = tk.Label(janela, image=recorte_tk)
    label_recorte.pack(expand=True)
    
    global entrada_texto
    entrada_texto = tk.Entry(janela, font=('Arial', 16))
    entrada_texto.pack(pady=10)
    
    botao_verificar = tk.Button(janela, text='Verificar', command=verificar_resposta, font=('Arial', 16))
    botao_verificar.pack(pady=10)
    
    global dica_label
    dica_label = tk.Label(janela, text="", font=('Arial', 16))
    dica_label.pack(pady=10)
    
    botao_dica = tk.Button(janela, text='Dica', command=dica, font=('Arial', 12))
    botao_dica.place(relx=1.0, rely=0.0, anchor='ne')
    
    janela.bind('<Return>', verificar_resposta)
    
    iniciar_novo_jogo()  # Iniciar o primeiro jogo ao abrir a janela
    
    janela.mainloop()

# Caminho para a pasta de imagens
actor_imgs = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\renamed_imgs"

# Variáveis globais para armazenar estado do jogo
letras_reveladas = set()
dicas_usadas = 0
resposta_correta = None

# Mostrar a imagem recortada na interface gráfica
caminho_imagem, nome_imagem = selecionar_imagem_aleatoria(actor_imgs)
imagem_recortada = processar_imagem(caminho_imagem)
mostrar_imagem_recortada(imagem_recortada, nome_imagem)
