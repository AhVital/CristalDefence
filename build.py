#!/usr/bin/env python3
"""
Build script for CrystalDefence website.
Generates static HTML pages from Jinja2 templates for GitHub Pages.

Usage:
    pip install -r requirements.txt
    python build.py

This will generate HTML files in the docs/ directory ready for deployment.
"""

import os
import sys
from jinja2 import Environment, FileSystemLoader


def get_template_dir():
    """Get the template directory path."""
    return "src/templates"


def get_output_dir():
    """Get the output directory for generated HTML."""
    return "docs"


def create_environment(template_dir):
    """Create Jinja2 environment with template loader."""
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    return env


def generate_page(env, page_name, title, content_template):
    """Generate a single page HTML file."""
    template = env.get_template(content_template)
    html = template.render(title=title, page=page_name)
    
    output_dir = get_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, page_name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ Generated {output_dir}/{page_name}.html")


def copy_static_files(static_dir):
    """Copy static assets to output directory."""
    if os.path.exists(static_dir):
        css_path = os.path.join(static_dir, "style.css")
        if os.path.exists(css_path):
            dest_path = os.path.join(get_output_dir(), "style.css")
            with open(css_path, "r", encoding="utf-8") as src:
                content = src.read()
            with open(dest_path, "w", encoding="utf-8") as dst:
                dst.write(content)
            print(f"✅ Copied style.css")


def main():
    """Main build function."""
    template_dir = get_template_dir()
    
    # Check templates exist
    for tpl in ["base.html", "index.html", "products.html", "about.html"]:
        if not os.path.exists(os.path.join(template_dir, tpl)):
            print(f"❌ Missing template: {tpl}")
            sys.exit(1)
    
    print("🔨 Building CrystalDefence website...\n")
    
    env = create_environment(template_dir)
    
    generate_page(env, "index", 
                  "Пуленепробиваемые стекла для вашего спокойствия",
                  "index.html")
    
    generate_page(env, "products", "Каталог пуленепробиваемых стекол", 
                  "products.html")
    
    generate_page(env, "about", "О компании CrystalDefence", "about.html")
    
    copy_static_files("src/static")
    
    print("\n🎉 Build completed!")
    print(f"Generated pages in: {get_output_dir()}/")
    print("\nFor GitHub Pages:")
    print("  1. Upload contents of 'docs/' folder to repository root")
    print("  2. Ensure .nojekyll file exists (prevents GitHub from processing)")


if __name__ == "__main__":
    main()
