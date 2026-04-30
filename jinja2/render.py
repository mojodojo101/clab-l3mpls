import json
import re
from jinja2 import Environment, FileSystemLoader

def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)



def render_ce_template(template_file, variables):
    for router in variables["ce_routers"]:
        # Setup Jinja environment
        env = Environment(loader=FileSystemLoader("."))
        env.filters['regex_replace'] = regex_replace
        template = env.get_template(template_file)
        print(router)
        hostname = list(router.keys())[0]
        # Render template with variables
        output = template.render({"router":router})
        with open(f"../config/{hostname}.cli", "w") as out_file:
            out_file.write(output)
    return 


def render_pe_template(template_file, variables):
    for router in variables["pe_routers"]:
        # Setup Jinja environment
        env = Environment(loader=FileSystemLoader("."))
        env.filters['regex_replace'] = regex_replace
        template = env.get_template(template_file)
        print(router)
        hostname = list(router.keys())[0]
        # Render template with variables
        output = template.render({"router":router})
        with open(f"../config/{hostname}.cli", "w") as out_file:
            out_file.write(output)
    return 

def render_p_template(template_file, variables):
    for router in variables["p_routers"]:
        # Setup Jinja environment
        env = Environment(loader=FileSystemLoader("."))
        env.filters['regex_replace'] = regex_replace
        template = env.get_template(template_file)
        print(router)
        hostname = list(router.keys())[0]
        # Render template with variables
        output = template.render({"router":router})
        with open(f"../config/{hostname}.cli", "w") as out_file:
            out_file.write(output)
    return 






if __name__ == "__main__":


    # Load variables from JSON
    with open("ce_vars.json", "r") as f:
        ce_variables = json.load(f)
    result = render_ce_template("ceXX.j2", ce_variables)
    with open("pe_vars.json", "r") as f:
        pe_variables = json.load(f)
    result = render_pe_template("peXX.j2", pe_variables)
    with open("p_vars.json", "r") as f:
        p_variables = json.load(f)
    result = render_p_template("pXX.j2", p_variables)
    print(result)
