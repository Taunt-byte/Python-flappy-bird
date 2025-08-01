import pygame
import random
import os

# Inicialização
pygame.init()
LARGURA, ALTURA = 400, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 150, 255)
VERDE = (0, 255, 0)

# Fonte
FONTE = pygame.font.SysFont('Arial', 32)
clock = pygame.time.Clock()
FPS = 60

# Arquivo de pontuações
SCORES_FILE = "scores.txt"

def carregar_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        return [int(linha.strip()) for linha in f.readlines() if linha.strip().isdigit()]

def salvar_score(score):
    scores = carregar_scores()
    scores.append(score)
    scores = sorted(scores, reverse=True)[:5]  # mantém só os 5 melhores
    with open(SCORES_FILE, "w") as f:
        for s in scores:
            f.write(str(s) + "\n")

def desenhar_texto(texto, tamanho, cor, x, y, centralizado=True):
    fonte = pygame.font.SysFont('Arial', tamanho)
    superficie = fonte.render(texto, True, cor)
    ret = superficie.get_rect()
    if centralizado:
        ret.center = (x, y)
    else:
        ret.topleft = (x, y)
    TELA.blit(superficie, ret)

def menu_inicial():
    esperando = True
    while esperando:
        TELA.fill(AZUL)
        desenhar_texto("Flappy Bird", 50, BRANCO, LARGURA // 2, ALTURA // 3)
        desenhar_texto("Pressione ESPAÇO para jogar", 25, BRANCO, LARGURA // 2, ALTURA // 2)

        # Mostrar ranking no menu
        scores = carregar_scores()
        desenhar_texto("TOP 5", 25, BRANCO, LARGURA // 2, ALTURA // 1.6)
        for i, score in enumerate(scores[:5]):
            desenhar_texto(f"{i+1}º - {score}", 22, BRANCO, LARGURA // 2, ALTURA // 1.6 + 30 + i*25)

        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando = False

def game_over(pontos):
    salvar_score(pontos)
    esperando = True
    while esperando:
        TELA.fill((0, 0, 0))
        desenhar_texto("Game Over", 50, BRANCO, LARGURA // 2, ALTURA // 5)
        desenhar_texto(f"Sua pontuação: {pontos}", 30, BRANCO, LARGURA // 2, ALTURA // 3)

        # Mostrar ranking
        scores = carregar_scores()
        desenhar_texto("Ranking TOP 5", 28, BRANCO, LARGURA // 2, ALTURA // 2.1)
        for i, score in enumerate(scores[:5]):
            desenhar_texto(f"{i+1}º - {score}", 24, BRANCO, LARGURA // 2, ALTURA // 2.1 + 30 + i*25)

        desenhar_texto("R - Reiniciar  |  ESC - Sair", 22, BRANCO, LARGURA // 2, ALTURA - 50)

        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    jogar()
                    esperando = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def jogar():
    # Variáveis do jogo
    bird_x = 50
    bird_y = ALTURA // 2
    bird_vel = 0
    gravidade = 0.5
    pulo = -8

    cano_largura = 70
    cano_altura = random.randint(100, 400)
    cano_espaco = 200
    cano_x = LARGURA
    vel_cano = 3
    pontos = 0

    rodando = True
    while rodando:
        clock.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bird_vel = pulo

        # Física
        bird_vel += gravidade
        bird_y += bird_vel

        # Canos
        cano_x -= vel_cano
        if cano_x + cano_largura < 0:
            cano_x = LARGURA
            cano_altura = random.randint(100, 400)
            pontos += 1

        # Colisão
        if bird_y > ALTURA or bird_y < 0:
            break
        if (cano_x < bird_x < cano_x + cano_largura) and not (cano_altura < bird_y < cano_altura + cano_espaco):
            break

        # Desenho
        TELA.fill(AZUL)
        pygame.draw.rect(TELA, VERDE, (cano_x, 0, cano_largura, cano_altura))
        pygame.draw.rect(TELA, VERDE, (cano_x, cano_altura + cano_espaco, cano_largura, ALTURA))
        pygame.draw.circle(TELA, BRANCO, (bird_x, int(bird_y)), 15)

        desenhar_texto(f"Pontos: {pontos}", 28, BRANCO, 10, 10, centralizado=False)

        pygame.display.update()

    game_over(pontos)

# Executar jogo
menu_inicial()
jogar()
