# 🐤 Flappy Bird em Python (com Pygame)

Este é um clone simples e funcional do clássico **Flappy Bird**, desenvolvido em **Python** utilizando a biblioteca **Pygame**.  
O projeto inclui:
- 🎮 Jogabilidade com física básica
- 📋 Menu inicial
- 💀 Tela de game over
- 🏆 Sistema de ranking com persistência (top 5 pontuações)

---

## 🎯 Objetivo do Jogo

Controle o pássaro pressionando a tecla `ESPAÇO` para voar entre os canos sem colidir. Cada par de canos ultrapassado aumenta sua pontuação em 1.

---

## 📷 Prévia

[![Veja o vídeo](https://img.youtube.com/vi/dF1forpMViw/0.jpg)](https://youtu.be/dF1forpMViw)


---

## ⚙️ Requisitos

- Python 3.6+
- Pygame

### Instalação do Pygame:
```bash
pip install pygame
````

---

## ▶️ Como Jogar

### Executar o jogo:

```bash
python main.py
```

### Controles:

* `ESPAÇO`: Faz o pássaro subir
* `R`: Reinicia o jogo após perder
* `ESC`: Sai do jogo

---

## 🏆 Ranking

As **5 maiores pontuações** são salvas no arquivo `scores.txt` e exibidas:

* no **menu inicial**
* na **tela de game over**

Você pode apagar o arquivo `scores.txt` para zerar o ranking.

---

## 📁 Estrutura do Projeto

```
flappy_bird/
│
├── flappy_bird.py        # Código principal do jogo
├── scores.txt            # (gerado automaticamente) armazena pontuações
└── README.md             # Este arquivo
```

---

## 💡 Possíveis Melhorias

* Adicionar sprites personalizados
* Incluir efeitos sonoros e música
* Registrar data/hora das pontuações no ranking
* Tela de pause
* Ajuste de dificuldade progressiva

---

## 📚 Tecnologias Utilizadas

* Python 🐍
* Pygame 🎮

---

## 📄 Licença

Este projeto é open-source e você pode usá-lo como quiser!
Sinta-se à vontade para modificar, contribuir ou adaptar.
