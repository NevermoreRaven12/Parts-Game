import os
from PIL import Image , ImageTk
import random
import tkinter as tk
from tkinter import messagebox
from app import select_random_img, process_img, verificar_resposta

def mostrar_imagem_recortada(recorte):
    janela = tk.Tk()
    janela.title('Jogo das partes')
    # Converter para o formato tkinter
    recorte_tk = ImageTk.PhotoImage(recorte)
    # Criar Labels para exibir as imagens

    label_recorte = tk.Label(janela, image=recorte_tk)
    label_recorte.pack(expand=True)

    # Criar a entrada de texto
    global entrada_texto
    entrada_texto = tk.Entry(janela, font=('Arial', 16))
    entrada_texto.pack(pady=10)
    # Botão para verificar a resposta
    botao_verificar = tk.Button(janela, text='Chute', command=verificar_resposta, font=('Arial', 16))
    # Permitir que a tecla enter verifique a resposta
    janela.bind('<Return>', verificar_resposta)
    # Iniciar o loop
    janela.mainloop()

actor_imgs = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\renamed_imgs"

# Selecionar a imagem aleatório
caminho_imagem, nome_imagem = select_random_img(actor_imgs)
# Processar a imagem
imagem_recortada = process_img(caminho_imagem)
# Mostrar a imagem recortada
mostrar_imagem_recortada(imagem_recortada)

resposta_correta = os.path.splitext(nome_imagem)[0]

