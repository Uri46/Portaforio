import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Name
html = re.sub(r'Hector Ta\u00f1o', 'Hector Uriel Fernandez Taño', html)
html = re.sub(r'Uriel', 'Hector Uriel Fernandez Taño', html)

# Fix encoding issue if any
html = html.replace('Hector Tao', 'Hector Uriel Fernandez Taño')

# Fix years of experience to 1
html = re.sub(r'<strong data-counter="4">', '<strong data-counter="1">', html)

# Replace Profile text
profile_old = r'<article class="text-panel reveal">.*?</article>'
profile_new = '''<article class="text-panel reveal">
            <p>
              Estudiante avanzado de la Tecnicatura Superior en Análisis de Sistemas, con base práctica en Python y desarrollo web. 
            </p>
            <p>
              Responsable, proactivo y con capacidad de aprendizaje continuo; busco dar mis primeros pasos profesionales aportando compromiso y trabajo en equipo.
            </p>
          </article>'''
html = re.sub(profile_old, profile_new, html, flags=re.DOTALL)

# Replace Experience with Education
exp_old = r'<section class="section-band dark" id="experiencia">.*?</section>'
exp_new = '''<section class="section-band dark" id="experiencia">
        <div class="content-wrap section">
          <div class="section-heading reveal">
            <p class="eyebrow">Formación</p>
            <h2>Educación y conocimientos técnicos.</h2>
          </div>
          <div class="timeline">
            <article class="timeline-item reveal">
              <span class="timeline-dot"></span>
              <div>
                <p>Marzo 2024 - Actualidad</p>
                <h3>Técnico Superior en Análisis de Sistemas</h3>
                <span>ISFT N° 179 Carlos Pellegrini. Formación en análisis, programación, bases de datos, y más.</span>
              </div>
            </article>
            <article class="timeline-item reveal">
              <span class="timeline-dot"></span>
              <div>
                <p>Marzo 2024 - Septiembre 2024</p>
                <h3>Técnico en Refrigeración</h3>
                <span>Ref Soluciones. Formación en instalación, diagnóstico y mantenimiento.</span>
              </div>
            </article>
            <article class="timeline-item reveal">
              <span class="timeline-dot"></span>
              <div>
                <p>2016 - 2022</p>
                <h3>Secundario Completo</h3>
                <span>Escuela Secundaria N° 1 "Manuel Belgrano".</span>
              </div>
            </article>
          </div>
        </div>
      </section>'''
html = re.sub(exp_old, exp_new, html, flags=re.DOTALL)

# Update Footer links
html = html.replace('<a href="#" aria-label="LinkedIn">LinkedIn</a>', '<a href="https://www.linkedin.com/in/hector-ta%C3%B1o-372715330/" target="_blank" aria-label="LinkedIn">LinkedIn</a>')
# Ensure github is there
html = html.replace('<a href="#" aria-label="GitHub">GitHub</a>', '<a href="https://github.com/Uri46" target="_blank" aria-label="GitHub">GitHub</a>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
