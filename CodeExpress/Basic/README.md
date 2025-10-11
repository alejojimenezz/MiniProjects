<h1>CodExpress — Nivel Básico (Fundamentos y Lógica)</h1>
<p><strong>Tiempo total:</strong> 3 horas · <strong>Objetivo:</strong> completar <u>7 u 8 mini-retos</u> y, si te alcanza, una <u>app integrada (código 1900)</u> que reutilice tu propio código.</p>

<h2>Flujo de trabajo (fork &amp; PR)</h2>
<ol>
  <li>Haz <em>fork</em> de este repo y clónalo.</li>
  <li>Usa un <strong>&lt;ALIAS&gt;</strong> sin espacios ni acentos (tu usuario de GitHub o <code>nombre-apellido</code> en minúsculas).</li>
  <li>Para cada mini-reto, crea un archivo con <strong>este formato exacto</strong>: <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code> (ej.: <code>1007_juana-saavedra_v1.py</code>).</li>
  <li>Si haces la app integrada, crea la carpeta <code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo ejecutar) y, si quieres, <code>requirements.txt</code> y <code>src/</code>.</li>
  <li>Sube tus cambios a tu fork y abre un Pull Request a <code>main</code> titulado: <strong>&lt;ALIAS&gt; — Entrega Nivel Básico</strong>.</li>
</ol>

<hr />

<h2>Códigos (Nivel Básico)</h2>
<ul>
  <li><strong>Mini-retos:</strong> 1001–1008 (elige 7 u 8).</li>
  <li><strong>App integrada:</strong> 1900 (<em>Math &amp; Logic Kit</em>).</li>
</ul>
<p><strong>Nombre de archivo obligatorio:</strong> <code>&lt;CODIGO_RETO&gt;_&lt;ALIAS&gt;_v&lt;N&gt;.&lt;ext&gt;</code></p>

<hr />

<h2>Mini-retos (entrega 7 u 8)</h2>
<p>Usa solo la librería estándar de Python. Al final de cada archivo agrega, en comentarios, <strong>3 pruebas</strong> (entrada → salida esperada). La salida se compara <strong>literalmente</strong> (cuida espacios y saltos de línea).</p>

<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Nombre</th>
      <th>Qué se espera (detalles clave)</th>
      <th>Entrada / Salida mínima</th>
      <th>Archivo</th>
      <th>Docs útiles</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1001</strong></td><td>Calculadora precisa</td><td>Implementa + − × ÷ con <u>redondeo comercial</u> a 2 decimales usando <code>decimal.Decimal</code> y <code>ROUND_HALF_UP</code>. División por cero: imprime <code>ERROR:DIV0</code>.</td><td>Entrada: <code>a op b</code> (ej.: <code>5.005 + 2</code>) · Salida: número a 2 decimales.</td><td><code>1001_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/decimal.html">decimal</a></td></tr>
    <tr><td><strong>1002</strong></td><td>Ecuación de 2º grado</td><td>Resuelve <code>ax^2+bx+c=0</code>. Si <code>a=0</code> → lineal. Imprime <code>delta=...</code>. Si Δ es cuadrado perfecto, raíces enteras exactas; si no, usa <code>Decimal</code> a 4 decimales (<code>ROUND_HALF_UP</code>). Si Δ&lt;0: <code>sin raices reales</code>.</td><td>Entrada: <code>a b c</code> · Salida: <code>delta=... r1=... r2=...</code> o <code>sin raices reales</code>.</td><td><code>1002_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/math.html">math</a> · <a href="https://docs.python.org/3/library/decimal.html">decimal</a></td></tr>
    <tr><td><strong>1003</strong></td><td>Adivina el número (semilla)</td><td>Juego 1..100 con pistas ↑/↓ y conteo de intentos. Debe aceptar <code>--seed=&lt;n&gt;</code> y usar <code>random.seed()</code> para reproducibilidad.</td><td>I/O en consola; terminar con <code>acertaste en N</code>.</td><td><code>1003_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/random.html">random</a> · <a href="https://docs.python.org/3/library/argparse.html">argparse</a></td></tr>
    <tr><td><strong>1004</strong></td><td>Conversor °C↔°F↔K (múltiples líneas)</td><td>Lee varias líneas desde stdin (hasta EOF). Soporta C/F/K. Si el resultado &lt; 0 K: <code>ERROR:ABSOLUTE_ZERO</code>. Redondea a 2 decimales con <code>Decimal</code>.</td><td>Cada línea: <code>valor unidad_origen unidad_destino</code> · Salida: una línea por conversión.</td><td><code>1004_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/tutorial/inputoutput.html">I/O</a> · <a href="https://docs.python.org/3/library/decimal.html">decimal</a></td></tr>
    <tr><td><strong>1005</strong></td><td>¿Es primo? (hasta 10<sup>6</sup>)</td><td>Imprime <code>primo</code> o <code>no primo</code>. 0, 1 y negativos → <code>no primo</code>. Optimiza cortando en <code>√n</code>.</td><td>Entrada: <code>n</code> · Salida: <code>primo</code>/<code>no primo</code>.</td><td><code>1005_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/math.html">math</a></td></tr>
    <tr><td><strong>1006</strong></td><td>Tabla de multiplicar “bonita”</td><td>Imprime la tabla de <code>N</code> del 1 al 10 alineada en columnas, sin espacios al final de línea.</td><td>Entrada: <code>N</code> · Salida: 10 líneas “<code>N x i = r</code>” alineadas.</td><td><code>1006_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/string.html#format-string-syntax">format strings</a></td></tr>
    <tr><td><strong>1007</strong></td><td>Palíndromos con acentos y signos</td><td>Ignora mayúsculas, espacios, signos y <u>acentos/diacríticos</u>. Normaliza con <code>unicodedata</code> (NFKD) y filtra marcas de combinación.</td><td>Entrada: una línea de texto · Salida: <code>si</code> / <code>no</code>.</td><td><code>1007_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/unicodedata.html">unicodedata</a></td></tr>
    <tr><td><strong>1008</strong></td><td>Simulador de dados (histograma)</td><td>Simula <code>N</code> lanzamientos (caras 1..6) y muestra frecuencias ordenadas 1→6. Acepta <code>--seed</code> para reproducibilidad.</td><td>Entrada: <code>N</code> (opcional <code>--seed</code>) · Salida: 6 líneas “<code>cara: conteo</code>”.</td><td><code>1008_&lt;ALIAS&gt;_v1.py</code></td><td><a href="https://docs.python.org/3/library/random.html">random</a> · <a href="https://docs.python.org/3/library/argparse.html">argparse</a></td></tr>
  </tbody>
</table>

<h3>Requisitos mínimos por mini-reto</h3>
<ul>
  <li><strong>E/S exacta</strong>: la comparación es literal.</li>
  <li><strong>3 pruebas</strong> (entrada → salida) en comentarios al final del archivo.</li>
  <li><strong>Solo librería estándar</strong> de Python.</li>
  <li><strong>Nomenclatura exacta</strong> del archivo. Nombre incorrecto: −5%.</li>
</ul>

<hr />

<h2>App integrada (1900) — Math &amp; Logic Kit</h2>
<table>
  <thead>
    <tr>
      <th>Código</th>
      <th>Debe reutilizar</th>
      <th>Qué agrega</th>
      <th>Entregables</th>
      <th>Puntaje máx.</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><strong>1900</strong></td><td>1001, 1002, 1003, 1005, 1006, 1007, 1008</td><td>Un <strong>menú en consola</strong> que llama tus funciones, manejo básico de errores y mensajes claros.</td><td>Carpeta <code>1900_&lt;ALIAS&gt;_app/</code> con <code>README.md</code> (cómo correr y qué módulos integra) y, si quieres, <code>src/</code>.</td><td><strong>140</strong></td></tr>
  </tbody>
</table>
<ul>
  <li>Reutiliza funciones: impórtalas desde tus archivos o muévalas a <code>src/utils.py</code>.</li>
  <li>Menú simple: opciones 1..7 y “salir”.</li>
</ul>

<hr />

<h2>Puntajes — Nivel Básico</h2>
<ul>
  <li><strong>Mini-reto (máx. 70 pts)</strong>: funciona (60%) · casos borde / 3 pruebas (20%) · código claro (10%) · defensa breve (10%).</li>
  <li><strong>App 1900 (máx. 140 pts)</strong>: integración (50%) · cohesión/reuso (20%) · manejo de errores (20%) · README (10%).</li>
</ul>

<hr />

<h2>Requisitos de precisión y reproducibilidad</h2>
<ul>
  <li><strong>Redondeo con <code>decimal</code> y <code>ROUND_HALF_UP</code></strong> (1001, 1002, 1004).</li>
  <li><strong>Semillas reproducibles</strong> y argumentos de línea (1003, 1008).</li>
  <li><strong>Normalización Unicode</strong> para acentos/diacríticos (1007).</li>
  <li><strong>Lectura múltiple hasta EOF</strong> y <strong>formato exacto</strong> de salida (1004, 1006).</li>
</ul>
<p>Durante la revisión se puede pedir una <strong>edición en vivo de 2 minutos</strong> (p. ej., ajustar un formato o añadir un caso borde).</p>

<hr />

<h2>Checklist final</h2>
<ul>
  <li>7 u 8 mini-retos con nombres correctos: <code>100x_&lt;ALIAS&gt;_vN.py</code>.</li>
  <li>3 pruebas en comentarios por archivo.</li>
  <li>Si hiciste la app: carpeta <code>1900_&lt;ALIAS&gt;_app/</code> + <code>README.md</code> + menú funcional.</li>
  <li>Pull Request: <code>&lt;ALIAS&gt; — Entrega Nivel Básico</code>.</li>
</ul>

<h2>Documentación de Python</h2>
<p><a href="https://docs.python.org/3/">Guía oficial</a> · <a href="https://docs.python.org/3/library/decimal.html">decimal</a> · <a href="https://docs.python.org/3/library/random.html">random</a> · <a href="https://docs.python.org/3/library/argparse.html">argparse</a> · <a href="https://docs.python.org/3/library/unicodedata.html">unicodedata</a> · <a href="https://docs.python.org/3/tutorial/inputoutput.html">I/O</a> · <a href="https://docs.python.org/3/library/string.html#format-string-syntax">format strings</a></p>

<h2>Dudas</h2>
<p>Abre un Issue titulado <code>Q-&lt;ALIAS&gt;: asunto</code>. ¡Éxitos! 🚀</p>
