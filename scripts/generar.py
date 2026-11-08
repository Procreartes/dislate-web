#!/usr/bin/env python3
"""Genera la web de Dislate Producciones (dislateproducciones.com).

Uso:  python3 scripts/generar.py
Datos editables (Gestor de webs del portal o a mano): data/proyectos.json, data/servicios.json, data/portada.json
No edites los .html a mano: se sobrescriben.
"""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from web import RAIZ, Sitio, ICO, esc, datos, mailto, imagen, portada_foto  # noqa: E402

CORREO = "hola@dislateproducciones.com"

S = Sitio(
    nombre="Dislate Producciones", nombre_corto="Dislate",
    dominio="https://dislateproducciones.com",
    titular="Dislate Producciones SL", nif="B22534796",
    domicilio="Hoya de Parrado, 4 · 35017 Las Palmas de Gran Canaria",
    correo=CORREO, correo_datos="protecciondatos@dislateproducciones.com",
    objeto="Esta web informa sobre Dislate Producciones SL, sus servicios de producción de eventos y espectáculos, sus proyectos y la forma de contactar.",
    color_tema="#ff0000", color_fondo="#f3f0e8",
    precarga=["archivo-black-latin-400-normal.woff2", "inter-tight-latin-400-normal.woff2"],
    menu=[("/#hacemos", "Qué hacemos"), ("/#proyectos", "Proyectos"), ("/#contacto", "Contacto")],
    marca='<img src="/img/logo-rojo.png" width="36" height="43" alt=""><span class="marca-txt">Dislate <i>Producciones</i></span>',
    pie_html='''<div class="pie-arriba">
      <div><img class="pie-logo" src="/img/logo-blanco.png" width="90" height="108" alt="Dislate Producciones" loading="lazy">
      <p>Productora de eventos, festivales y espectáculos · Gran Canaria</p>
      <p class="pie-grupo">Una empresa de Grupo Livon</p></div>
      <div><p><a href="mailto:hola@dislateproducciones.com">hola@dislateproducciones.com</a></p>
      <p>Hoya de Parrado, 4 · Las Palmas de Gran Canaria</p></div>
    </div>''',
    credito_fotos=False,
)

PROYECTOS = datos("proyectos.json", [])
SERVICIOS = datos("servicios.json", [])


def inicio():
    hero = portada_foto("escenario", "Escenario de un festival iluminado en rojo y azul frente al público")
    servicios = "".join(
        f'<li class="aparece"><h3>{esc(s.get("titulo"))}</h3><p>{esc(s.get("texto"))}</p></li>' for s in SERVICIOS)
    filas = ""
    for i, p in enumerate(PROYECTOS, 1):
        img = imagen(p.get("imagen"), p.get("imagen_alt") or p.get("titulo"), "(min-width: 900px) 420px, 92vw", "fila-foto")
        enlace = (p.get("enlace") or "").strip()
        color = p.get("color") or "#333333"
        tag = "a" if enlace.startswith("https://") else "div"
        attrs = f' href="{esc(enlace)}" rel="noopener"' if tag == "a" else ""
        meta = " · ".join(esc(x) for x in [p.get("tipo"), p.get("lugar"), p.get("anio")] if x)
        filas += f'''<li class="fila aparece" style="--c:{esc(color)}">
      <{tag} class="fila-enlace"{attrs}>
        <span class="fila-n" aria-hidden="true">{i:02d}</span>
        <span class="fila-titulo">{esc(p.get("titulo"))}</span>
        <span class="fila-meta">{meta}</span>
        <span class="fila-texto">{esc(p.get("texto"))}</span>
        <span class="fila-visual" aria-hidden="{"false" if img else "true"}">{img or '<span class="fila-bloque"></span>'}</span>
      </{tag}></li>'''
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Organization", "name": "Dislate Producciones SL",
        "alternateName": "Dislate", "url": S.dominio + "/", "email": CORREO, "taxID": "B22534796",
        "description": "Productora de eventos, festivales y espectáculos en Canarias.", "areaServed": "Canarias",
        "address": {"@type": "PostalAddress", "streetAddress": "Hoya de Parrado, 4", "postalCode": "35017",
                    "addressLocality": "Las Palmas de Gran Canaria", "addressCountry": "ES"},
    }, ensure_ascii=False)

    cuerpo = f'''<section class="portada">
  <div class="contenedor portada-grid">
    <h1 class="portada-logo"><img src="/img/logo-rojo.png" width="600" height="719" alt="Dislate"><span class="visualmente-oculto">Dislate Producciones</span></h1>
    <div class="portada-txt">
      <p class="antetitulo">Productora de eventos · Gran Canaria</p>
      <p class="lema">Un dislate es un <em>disparate</em>.<br>Nosotros lo convertimos en <span>evento</span>.</p>
      <p class="entradilla">Festivales, ferias, giras y espectáculos en todo el archipiélago: de la idea al último foco apagado.</p>
      <div class="botones">
        <a class="boton boton-rojo" href="#contacto">Contar un proyecto {ICO["flecha"]}</a>
        <a class="boton boton-linea" href="#proyectos">Ver proyectos</a>
      </div>
    </div>
  </div>
  <div class="franja-foto">{hero}</div>
</section>

<section class="seccion" id="hacemos" aria-labelledby="t-hacemos">
  <div class="contenedor hacemos-grid">
    <div class="hacemos-cab"><p class="antetitulo">Qué hacemos</p><h2 id="t-hacemos">Todo lo que pasa <em>antes</em> de que se enciendan las luces</h2></div>
    <ol class="servicios">{servicios}</ol>
  </div>
</section>

<section class="seccion seccion-oscura" id="proyectos" aria-labelledby="t-proyectos">
  <div class="contenedor">
    <div class="cabecera-seccion"><p class="antetitulo">Índice de proyectos</p><h2 id="t-proyectos">Disparates <em>cumplidos</em></h2></div>
    <ol class="indice">{filas}</ol>
  </div>
</section>

<section class="seccion contacto" id="contacto" aria-labelledby="t-contacto">
  <div class="contenedor contacto-grid aparece">
    <div><p class="antetitulo">Contacto</p><h2 id="t-contacto">¿Tienen un <em>dislate</em> entre manos?</h2>
    <p class="entradilla">Cuéntennos qué quieren montar, dónde y cuándo. Ayuntamientos, cabildos, marcas, artistas o promotores: les respondemos con una propuesta.</p></div>
    <a class="contacto-correo" href="{mailto(CORREO, "Proyecto para Dislate")}">{ICO["mail"]}<span>{CORREO}</span></a>
  </div>
</section>'''
    return S.pagina("Dislate Producciones · Productora de eventos, festivales y espectáculos en Gran Canaria",
                    "Productora de eventos en Gran Canaria: festivales, ferias y stands, giras y espectáculos, producción técnica y comunicación en todo el archipiélago.",
                    "/", cuerpo, actual="", ld=ld)


def main():
    css = (RAIZ / "css/base.css").read_text(encoding="utf-8") + "\n" + (RAIZ / "css/tema.css").read_text(encoding="utf-8")
    S.escribir("css/estilos.css", css)
    S.publicar({"index.html": inicio()})


if __name__ == "__main__":
    main()
