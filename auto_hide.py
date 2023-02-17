bl_info = {
    "name": "Auto Hide from Render",
    "author": "Your Name Here",
    "version": (1, 2),
    "blender": (2, 93, 0),
    "location": "View3D > Object > Auto Hide from Render",
    "description": "Automatically hide objects from render when hidden in viewport.",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}

import bpy


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


class AutoHideFromRenderPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    enable_addon: bpy.props.BoolProperty(
        name="Enable Add-on on Startup",
        default=True,
        description="Automatically enable the add-on on Blender startup"
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "enable_addon")


def register():
    bpy.utils.register_class(HideFromRender)
    bpy.utils.register_class(UnhideFromRender)
    bpy.utils.register_class(AutoHideFromRenderPreferences)
    bpy.app.handlers.depsgraph_update_pre.append(hide_render_callback)


def unregister():
    bpy.utils.unregister_class(HideFromRender)
    bpy.utils.unregister_class(UnhideFromRender)
    bpy.utils.unregister_class(AutoHideFromRenderPreferences)
    
    if hide_render_callback in bpy.app.handlers.depsgraph_update_pre:
        bpy.app.handlers.depsgraph_update_pre.remove(hide_render_callback)


if __name__ == "__main__":
    register()
