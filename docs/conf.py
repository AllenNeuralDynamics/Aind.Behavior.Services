# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import glob
import logging
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))
import subprocess

import aind_behavior_services

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("sphinx_build.log")],
)
logger = logging.getLogger(__name__)
SOURCE_ROOT = "https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/tree/main/src/"


project = "AIND Behavior Services"
copyright = "2025, Allen Institute for Neural Dynamics"
author = "Bruno Cruz"
release = aind_behavior_services.__version__

logger.info(f"Building documentation for {project} version {release}")

# -- Generate api docs --
logger.info("Generating API docs...")
try:
    subprocess.run(
        [
            "sphinx-apidoc",
            "-o",
            "./api",
            "../src/aind_behavior_services",
            "-d",
            "4",
            "--tocfile",
            "api",
            "--remove-old",
            "-t",
            "./_templates-f",
        ],
        check=True,
    )
    logger.info("API docs generated successfully")
except subprocess.CalledProcessError as e:
    logger.error(f"Failed to generate API docs: {e}")
    raise


# -- Generate jsons --------------------------------------------------------------
logger.info("Generating JSON schemas...")
json_root_path = os.path.abspath("../src/schemas")
json_files = glob.glob(os.path.join(json_root_path, "*.json"))
rst_target_path = os.path.abspath("./json_schemas")

logger.info(f"Found {len(json_files)} JSON schema files")

leaf_template = """
{json_file_name}
----------------------------------------------------

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.Services/main/src/schemas/{json_file_name}.json>`_

.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.Services/main/src/schemas/{json_file_name}.json
   :lift_definitions:
   :auto_reference:

"""

os.makedirs(rst_target_path, exist_ok=True)

for json_file in json_files:
    json_file_name = os.path.basename(json_file)
    rst_file_path = os.path.join(rst_target_path, f"{json_file_name.replace('.json', '')}.rst")
    logger.debug(f"Processing {json_file_name} -> {rst_file_path}")

    try:
        with open(rst_file_path, "w") as f:
            f.write(leaf_template.format(json_file_name=json_file_name.replace(".json", "")))
        logger.debug(f"Successfully wrote {rst_file_path}")
    except Exception as e:
        logger.error(f"Failed to write {rst_file_path}: {e}")
        raise

logger.info("JSON schema documentation generated successfully")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx-jsonschema",
    "sphinx_jinja",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.linkcode",
    "sphinx_mdinclude",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx_copybutton",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True
autodoc_typehints = "description"

autodoc_pydantic_settings_show_json = False
autodoc_pydantic_model_show_json = True
autodoc_pydantic_model_show_field_summary = True
autodoc_pydantic_model_show_config_summary = True
autodoc_pydantic_model_undoc_members = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_title = "AIND Behavior Services"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "light_logo": "light-logo.svg",
    "dark_logo": "dark-logo.svg",
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# -- Options for linkcode extension ---------------------------------------


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None
    filename = info["module"].replace(".", "/")
    return f"{SOURCE_ROOT}/{filename}.py"
