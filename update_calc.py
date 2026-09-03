import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the project grid have 4 items
calc_project = '''          <article class="project-card reveal">
            <div class="project-visual visual-four" aria-hidden="true" style="background: linear-gradient(135deg, #10b981 0%, #047857 100%);">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <div class="project-content">
              <p class="project-type">Aplicación</p>
              <h3>Calculadora</h3>
              <p>Calculadora funcional desarrollada con Python, aplicando manejo de operaciones matemáticas y estructura de código clara.</p>
              <div class="project-tags">
                <span>Python</span>
                <span>Lógica</span>
                <span>App</span>
              </div>
              <a href="https://github.com/Uri46/Calculadora" target="_blank" class="btn btn-secondary" style="margin-top: 1rem; padding: 0.5rem 1rem; font-size: 0.9rem;">Ver en GitHub</a>
            </div>
          </article>
        </div>'''

html = html.replace('</article>\n        </div>', '</article>\n' + calc_project)

# Update the counter
html = re.sub(r'<strong data-counter="\d+">', '<strong data-counter="4">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
