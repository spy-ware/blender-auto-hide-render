import bpy
bl_info = {
    "name": "Auto Hide from Render",
    "author": "ChatGPT",
    "version": (1, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Object > Auto Hide from Render",
    "description": "Automatically hide objects from render when hidden in viewport.",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


class HideFromRender(bpy.types.Operator):
    """Hide From Render"""
    bl_idname = "object.hide_from_render"
    bl_label = "Hide from Render"

    def execute(self, context):
        obj = context.object
        obj.hide_render = True
        return {'FINISHED'}


class UnhideFromRender(bpy.types.Operator):
    """Unhide From Render"""
    bl_idname = "object.unhide_from_render"
    bl_label = "Unhide from Render"

    def execute(self, context):
        obj = context.object
        obj.hide_render = False
        return {'FINISHED'}


def hide_render_callback(scene, depsgraph):
    for obj in scene.objects:
        if obj.hide_get():
            obj.hide_render = True
        else:
            obj.hide_render = False


def register():
    bpy.utils.register_class(HideFromRender)
    bpy.utils.register_class(UnhideFromRender)
    bpy.app.handlers.depsgraph_update_pre.append(hide_render_callback)


def unregister():
    bpy.utils.unregister_class(HideFromRender)
    bpy.utils.unregister_class(UnhideFromRender)
    bpy.app.handlers.depsgraph_update_pre.remove(hide_render_callback)


if __name__ == "__main__":
    register()
