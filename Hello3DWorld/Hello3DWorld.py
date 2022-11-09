bl_info = {
    "name": "Hello 3D World!",
    "description": "Say hello world... in 3D!",
    "author": "M. Scott Lassiter",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),
    "location": "Properties",
    "warning": "Don't forget to delete the default cube!",
    "doc_url": "www.GraphicArtQuest.com",
    "tracker_url": "https://github.com/GraphicArtQuest/Tutorials/issues",
    "support": "COMMUNITY",
    "category": "Mesh"
}

import bpy
import os


thisPath = os.path.abspath('Hello3DWorld.py')
bpy.app.debug_wm = False
 
class CustomPanel(bpy.types.Panel):
    bl_label = "Hello 3D World"
    bl_idname = "OBJECT_PT_HelloPanel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Hello There")

class ButtonOperator(bpy.types.Operator):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOL_PROPS'
    bl_idname = "sayhello.addtext"
    bl_label = "Say Hello!"
    bl_category = "Tools"

    def execute(self, context):
        bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    
        txt = bpy.context.active_object

        txt.data.body = 'Hello 3D World!'
        txt.modifiers.new('Make it chonky', 'SOLIDIFY')
        txt.modifiers.get('Make it chonky').thickness = -0.25

        print('Complete!')

        return {'FINISHED'}
 
def register():
    bpy.utils.register_class(CustomPanel)
    bpy.utils.register_class(ButtonOperator)
    print("Hello 3D World!")

def unregister():
    bpy.utils.unregister_class(CustomPanel)
    bpy.utils.unregister_class(ButtonOperator)
    print("Goodbye 3D World!")
