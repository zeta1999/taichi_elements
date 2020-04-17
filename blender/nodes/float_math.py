import bpy

from . import base


def get_res_value(socket):
    node = socket.node
    out = node.outputs['Result']
    val_1 = node.inputs['Float 1'].get_value()
    val_2 = node.inputs['Float 2'].get_value()
    mode = node.mode
    if mode == 'ADD':
        out.value = val_1 + val_2
    elif mode == 'SUBTRACT':
        out.value = val_1 - val_2
    elif mode == 'MULTIPLY':
        out.value = val_1 * val_2
    elif mode == 'DIVIDE':
        out.value = val_1 / val_2
    return out.value


class ElementsFloatMathNode(base.BaseNode):
    bl_idname = 'elements_float_math_node'
    bl_label = 'Float Math'

    category = base.CONVERTER
    get_value = {'Result': get_res_value, }
    items = [
        ('ADD', 'Add', ''),
        ('SUBTRACT', 'Subtract', ''),
        ('MULTIPLY', 'Multiply', ''),
        ('DIVIDE', 'Divide', '')
    ]
    mode: bpy.props.EnumProperty(items=items, name='Mode')

    def init(self, context):
        self.width = 200.0

        out = self.outputs.new('elements_float_socket', 'Result')
        out.text = 'Result'
        out.hide_value = True

        val_1 = self.inputs.new('elements_float_socket', 'Float 1')
        val_1.text = 'Float 1'

        val_2 = self.inputs.new('elements_float_socket', 'Float 2')
        val_2.text = 'Float 2'

    def draw_buttons(self, context, layout):
        layout.prop(self, 'mode')