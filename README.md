<h1 align="center">🏎️ Retro Car Racing</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyGame-000000?style=for-the-badge&logo=python&logoColor=white" />
</p>

<p align="center">
  Un juego de carreras 2D estilo retro, hecho con <b>Python</b> y <b>PyGame</b>, inspirado en el clásico<br/>
  "Brick Game Classic Car Race" de la Atari Tetris.
</p>

---

## 📖 Descripción

**Retro Car Racing** es un juego de carreras de autos 2D divertido y atractivo, creado con Python y la biblioteca PyGame. Los jugadores navegan su auto a través de tres carriles mientras evitan autos enemigos que aparecen desde la parte superior de la pantalla. El objetivo es sobrevivir el mayor tiempo posible sin chocar con ningún enemigo.

## 🎮 Capturas de pantalla

<table align="center">
  <tr>
    <td align="center" width="50%">
      <img src="screenshots/Captura%20de%20pantalla%202026-07-22%20191529.png" width="100%" alt="Menú principal" /><br/>
      <sub><b>Menú principal</b></sub>
    </td>
    <td align="center" width="50%">
      <img src="screenshots/Captura%20de%20pantalla%202026-07-22%20191629.png" width="100%" alt="Gameplay" /><br/>
      <sub><b>Elegir auto</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="screenshots/Captura%20de%20pantalla%202026-07-22%20191707.png" width="100%" alt="Gameplay avanzado" /><br/>
      <sub><b>Partida en progreso</b></sub>
    </td>
    <td align="center" width="50%">
      <img src="screenshots/Captura%20de%20pantalla%202026-07-22%20191721.png" width="100%" alt="Game Over" /><br/>
      <sub><b>Pantalla de Game Over</b></sub>
    </td>
  </tr>
</table>

## ✨ Características

- 🛣️ Tres carriles para que el jugador navegue.
- 🚗 Autos enemigos que aparecen y se mueven hacia abajo en la pantalla.
- 💥 Detección de colisiones entre el auto del jugador y los autos enemigos.
- 🖥️ Sistema de menú simple e intuitivo para iniciar y salir del juego.
- 🏁 Pantalla de Game Over con el puntaje obtenido.

## 🛠️ Instalación

Necesitas tener **Python** y **PyGame** instalados en tu máquina.

1. Clona el repositorio:

   ```bash
   git clone https://github.com/uimp3/Retro-Car-Racing.git
   cd Retro-Car-Racing
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecutar el juego

```bash
python src/main.py
```

## 🕹️ Controles

| Tecla | Acción |
|---|---|
| ⬅️ Flecha izquierda | Mover el auto al carril izquierdo |
| ➡️ Flecha derecha | Mover el auto al carril derecho |
| ⏎ Enter | Iniciar partida desde el menú |
| Esc | Salir del juego |

## 📁 Estructura del proyecto

```
Retro-Car-Racing/
├── images/          # Assets gráficos del juego (autos, pistas, fondos)
├── screenshots/      # Capturas de pantalla del juego
├── src/
│   ├── main.py       # Punto de entrada del juego
│   ├── game.py        # Lógica principal del juego
│   ├── menu.py         # Sistema de menú
│   └── enemy.py         # Lógica de los autos enemigos
├── requirements.txt
└── README.md
```

## 📚 Documentación y referencias

- [Documentación de PyGame](https://www.pygame.org/docs/)
- [Tutoriales y ejemplos de PyGame](https://www.pygame.org/wiki/tutorials)

---

<p align="center">Hecho con ❤️ por <a href="https://github.com/uimp3">Edwin Muñoz</a></p>
