import os
import re

# Create directories
os.makedirs('img/proyectos', exist_ok=True)
os.makedirs('img/titulos', exist_ok=True)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace project visuals
html = html.replace('<div class="project-visual visual-one" aria-hidden="true">\n              <span></span>\n              <span></span>\n              <span></span>\n            </div>', '<div class="project-visual" aria-hidden="true" style="background-image: url(\'img/proyectos/laberinto.jpg\'); background-size: cover; background-position: center;"></div>')

html = html.replace('<div class="project-visual visual-two" aria-hidden="true">\n              <span></span>\n              <span></span>\n              <span></span>\n            </div>', '<div class="project-visual" aria-hidden="true" style="background-image: url(\'img/proyectos/tetris.jpg\'); background-size: cover; background-position: center;"></div>')

html = html.replace('<div class="project-visual visual-three" aria-hidden="true">\n              <span></span>\n              <span></span>\n              <span></span>\n            </div>', '<div class="project-visual" aria-hidden="true" style="background-image: url(\'img/proyectos/dataskins.jpg\'); background-size: cover; background-position: center;"></div>')

html = html.replace('<div class="project-visual visual-four" aria-hidden="true" style="background: linear-gradient(135deg, \n#10b981 0%, #047857 100%);">\n              <span></span>\n              <span></span>\n              <span></span>\n            </div>', '<div class="project-visual" aria-hidden="true" style="background-image: url(\'img/proyectos/calculadora.jpg\'); background-size: cover; background-position: center;"></div>')

html = html.replace('<div class="project-visual visual-four" aria-hidden="true" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%);">\n              <span></span>\n              <span></span>\n              <span></span>\n            </div>', '<div class="project-visual" aria-hidden="true" style="background-image: url(\'img/proyectos/calculadora.jpg\'); background-size: cover; background-position: center;"></div>')

# Add Navigation link for titulos
html = html.replace('<a href="#proyectos">Proyectos</a>', '<a href="#proyectos">Proyectos</a>\n          <a href="#titulos">Títulos</a>')

# Add Titulos section before Experiencia
titulos_section = '''      <section class="content-wrap section" id="titulos">
        <div class="section-heading reveal">
          <p class="eyebrow">Certificaciones</p>
          <h2>Títulos y Cursos.</h2>
        </div>
        <div class="carousel">
          <button class="carousel-btn prev">&#10094;</button>
          <div class="carousel-track-container">
            <ul class="carousel-track">
              <li class="carousel-slide current-slide">
                <img src="img/titulos/python.jpg" alt="Título Python">
                <h4>Python - Santander</h4>
              </li>
              <li class="carousel-slide">
                <img src="img/titulos/geminis.jpg" alt="Título Geminis">
                <h4>Geminis - Santander</h4>
              </li>
              <li class="carousel-slide">
                <img src="img/titulos/excel.jpg" alt="Título Excel">
                <h4>Excel - Santander</h4>
              </li>
            </ul>
          </div>
          <button class="carousel-btn next">&#10095;</button>
        </div>
      </section>\n\n'''

html = html.replace('<section class="section-band dark" id="experiencia">', titulos_section + '<section class="section-band dark" id="experiencia">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
