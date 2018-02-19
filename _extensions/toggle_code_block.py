from docutils import nodes
from sphinx.directives.code import CodeBlock

HTML = """
<script>
    function toggle(id) {{
        var element = document.getElementById(id);
        if (element.style.display == "block")
            element.style.display = "none"
        else
            element.style.display = "block"  
    }}
</script>

<p><a href="javascript:toggle('{id}')">{label}</a></p>
<div id="{id}" style="display: {display}">{content}</div>
<p></p>
"""


class toggle_code_block(nodes.General, nodes.FixedTextElement):
    pass


class ToggleCodeBlockDirective(CodeBlock):
    has_content = True

    option_spec = {
        'label': str,
        'hidden': bool,
    }

    def run(self):
        content = '\n'.join(self.content)
        block = toggle_code_block(content, content)
        block['hidden'] = self.options.get('display', True)
        block['label'] = self.options.get('label', 'Toggle')
        block['language'] = self.arguments[0]
        block['linenos'] = 'linenos' in self.options
        block.line = self.lineno
        return [block]


def html(self, node):
    try:
        self.visit_literal_block(node)
    except nodes.SkipNode:
        pass

    self.body[-1] = HTML.format(
        id=node.get('label').lower().replace(' ', '-'),
        display='none' if node.get('hidden') else 'block',
        label=node.get('label'),
        content=self.body[-1],
    )

    raise nodes.SkipNode


def latex(self, node):
    self.visit_literal_block(node)


def text(self, node):
    self.visit_literal_block(node)

def depart(self, node):
    pass

def setup(app):
    app.add_directive('toggle-code-block', ToggleCodeBlockDirective)
    app.add_node(toggle_code_block,
         html=[html, depart],
         latex=[latex, depart],
         text=[text, depart]
    )
    return {'version': '1.0'}
