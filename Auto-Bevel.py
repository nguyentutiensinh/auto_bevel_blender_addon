import bpy
bl_info = {
    "name": "Auto Bevel",
    "location": "View3D > Add > Mesh > Auto Bevel,",
    "description": "Auto Bevel vertex or edge",
    "author": "nguyendinhat",
    "version": (1,0),
    "blender": (3,6,3),
    "category": "Mesh",
}

class VIEW3D_OT_auto_bevel(bpy.types.Operator):
    bl_idname = "view3d.auto_bevel"
    bl_label = "Auto Bevel"
    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        toolSettings = bpy.context.tool_settings
        if toolSettings.mesh_select_mode[0]:
            bpy.ops.mesh.bevel('INVOKE_DEFAULT', affect='VERTICES')
        else:
            bpy.ops.mesh.bevel('INVOKE_DEFAULT')
        return {'FINISHED'}

def register():
    bpy.utils.register_class(VIEW3D_OT_auto_bevel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_OT_auto_bevel)

if __name__ == "__main__":
    register()