# 🖐️ Helping Hands – Sistema de Pedidos de Ajuda por Gestos

**Helping Hands** é uma solução inteligente que utiliza **visão computacional** com **Python + MediaPipe** para interpretar **gestos com as mãos** em ambientes de baixa iluminação — como durante **quedas de energia** — e ativar **alertas de emergência** automaticamente.

---

## 🚨 Problema

Durante apagões ou situações de emergência:
- Pessoas com **deficiência visual** ou com **dificuldade de locomoção** podem não conseguir pedir ajuda rapidamente.
- **Hospitais, centros de comando e residências** podem ficar vulneráveis.
- Sistemas de chamada por voz em locais ruidosos.

---

## 🎯 Objetivo

Criar um sistema que:
- **Reconheça gestos** com a mão via webcam.
- **Ative sons de alerta** diferentes para emergências específicas.
- **Acione uma lanterna de emergência** simulando iluminação por gestos.
- **Funcione mesmo com iluminação reduzida**, usando o processamento de imagem.

---

## 🧠 Como funciona

| Gesto Reconhecido | Ação Realizada                     |
|-------------------|------------------------------------|
| ✋ 5 dedos         | 🚨 Toca som de **Ajuda URGENTE**    |
| 🤟 3 dedos         | 🩺 Toca som de **Ajuda MÉDICA**     |
| ✌️ 1 dedos         | 💡 Ativa **lanterna de emergência** |
| ✊ 0 dedos         | 🔕 Cancela todos os alertas         |

---

## 🧰 Tecnologias utilizadas

- **Python 3.10**
- **MediaPipe** (detecção de mãos)
- **OpenCV** (visão computacional)
- **Pygame** (áudio)
- **Threading** (execução de sons simultâneos)
- **NumPy** (tela branca para lanterna)

---

## 📁 Estrutura de pastas
helpinghands/
- ├── main.py
- ├── sounds/
- │├── alert_urgente.wav
- │└── alerta_medico.wav


---

## ▶️ Como executar

1. Instale as dependências:

```bash
pip install opencv-python mediapipe pygame numpy
```

2. Execute o projeto:
```bash
python main.py
```

3. Use os gestos com a mão na frente da câmera conforme a tabela de gestos.


## 💡 Possíveis melhorias futuras
- Registro de alertas em banco de dados

- Integração com WhatsApp ou Telegram

- Detecção de mais de uma pessoa ao mesmo tempo

- Suporte a libras ou gestos personalizados

# 👥 Desenvolvedores
#### Deivison Pertel – RM 550803
#### Eduardo Akira Murata – RM 98713
#### Wesley Souza de Oliveira – RM 97874



