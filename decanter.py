import os

pasta_origem = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\imagens_atores"
pasta_destino = "C:\\Users\\Pedro\\Documents\\Projetos_Python\\jogo_partes\\renamed_imgs"

os.makedirs(pasta_destino, exist_ok=True)

for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith('.jpg' or '.png'):
        new_name = nome_arquivo.replace(' ', '_')
        caminho_antigo = os.path.join(pasta_origem, nome_arquivo)
        caminho_novo = os.path.join(pasta_destino, new_name)
        os.rename(caminho_antigo, caminho_novo)

        print(f'Renomeado: {caminho_antigo} -> {caminho_novo}')