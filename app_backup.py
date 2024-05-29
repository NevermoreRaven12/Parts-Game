import os
from PIL import Image , ImageTk
import random
import tkinter as tk
from tkinter import messagebox


actor_imgs = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\renamed_imgs"

# Função principal do jogp

def select_random_img(actor_imgs):
    extensoes = ('.jpg', '.jpeg', '.png')
    arquivos = [f for f in os.listdir(actor_imgs) if f.lower().endswith(extensoes)]
    
    img_random = random.choice(arquivos)
    # Caminho completo da imagem
    caminho_imagem = os.path.join(actor_imgs, img_random)

    return caminho_imagem, img_random

# Função para processar a imagem

def process_img(caminho_imagem):
    img = Image.open(caminho_imagem)
    
    img_resized = img.resize((400, 400))
    
    largura, altura = img_resized.size
    
    crop_size = (0, altura - 200, 200, altura)
    
    img_cropped = img_resized.crop(crop_size)

    return img_cropped

# Função para iniciar um novo jogo

def iniciar_novo_jogo():
    global resposta_correta
    entrada_texto.delete(0, 'end')

    #Limpar letras reveladas e dicas usadas
    letras_reveladas = set()
    dicas_usadas = 0

    #Selecionar uma nova imagem aleatória
    caminho_imagem, nome_imagem = select_random_img(actor_imgs)

    #Processar a imagem e obter o recorte
    imagem_recortada = process_img(caminho_imagem)

    #Atualizar a resposta correta
    global resposta_correta
    resposta_correta = os.path.splitext(nome_imagem)[0]

    #Atualizar a exibição da imagem recortada e da dica
    imagem_recortada_tk = ImageTk.PhotoImage(imagem_recortada)
    label_recorte.configure(image=imagem_recortada_tk)
    label_recorte.image = imagem_recortada_tk
    
    dica_inicial = '_' * len(resposta_correta)
    dica_label.configure(text=dica_inicial)

# Função para verificar a resposta

def verificar_resposta(event=None):
    entrada = entrada_texto.get().strip()
    resposta_formatada = resposta_correta.lower().strip().replace('_', ' ')
    if entrada.lower() == resposta_formatada:
        messagebox.showinfo("Você acertou!")
        iniciar_novo_jogo()
    else:
        messagebox.showerror("Você errou, tente novamente.")

# Função de dica
def dica():
    global dicas_usadas
    if dicas_usadas < len(resposta_correta):
        # Selecionar uma letra ainda não revelada
        while True:
            indice = random.randint(0, len(resposta_correta) -1)
            if indice not in letras_reveladas:
                letras_reveladas.add(indice)
                dicas_usadas += 1
                break
        #Mostrar a letra revelada no Entry
        dica = ''.join([resposta_correta[i] if i in letras_reveladas else '_' for i in range(len(resposta_correta))])
        dica_label.config(text=dica)
    else:
        messagebox.showinfo("Todas as letras já foram reveladas")

def mostrar_imagem_recortada(recorte, reposta_correta):
    janela = tk.Tk()
    janela.title('Jogo das partes')
    # Converter para o formato tkinter
    recorte_tk = ImageTk.PhotoImage(recorte)
    # Criar Labels para exibir as imagens
    global label_recorte

    label_recorte = tk.Label(janela, image=recorte_tk)
    label_recorte.pack(expand=True)

    # Criar a entrada de texto
    global entrada_texto
    entrada_texto = tk.Entry(janela, font=('Arial', 16))
    entrada_texto.pack(pady=10)
    
    # Botão para verificar a resposta
    botao_verificar = tk.Button(janela, text='Chute', command=verificar_resposta, font=('Arial', 16))
    botao_verificar.pack(pady=10)
    
    # Label para a dica
    global dica_label
    dica_label = tk.Label(janela, text="_" * len(resposta_correta), font=('Arial', 16))
    dica_label.pack(pady=10)

    #Botão para revelar letras de dicas
    botao_dica = tk.Button(janela, text='Dica', command=dica, font=('Arial', 12))
    botao_dica.place(relx=1.0, rely=0.0, anchor='ne')
    
    # Permitir que a tecla enter verifique a resposta
    janela.bind('<Return>', verificar_resposta)
    
    # Iniciar o loop
    janela.mainloop()

actor_imgs = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\renamed_imgs"

letras_reveladas = set()
dicas_usadas = 0

# Selecionar a imagem aleatório
caminho_imagem, nome_imagem = select_random_img(actor_imgs)
# Processar a imagem
imagem_recortada = process_img(caminho_imagem)
# Mostrar a imagem recortada
resposta_correta = None

mostrar_imagem_recortada(imagem_recortada, resposta_correta)






