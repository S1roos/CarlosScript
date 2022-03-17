#Script to perform -carlos actions. These include:
#Limit Totals
#Clean Weights (Remove Zero-Weights)
#Normalize All
#Triangulate Mesh
#Apply Transforms
#Note that you should also have each mesh be less than ~50k tris each, but that's not something I can really automate.

#For this to work, simply select every object you'd like the script to work on and it'll go to town.

import bpy

for obj in bpy.context.selected_objects:
    #Set to object mode for first 2 actions
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
    #Clean Vertex Groups, only target deform groups
    bpy.ops.object.vertex_group_clean(group_select_mode='BONE_DEFORM')
    
    #Limit Totals to 4, only target deform groups
    bpy.ops.object.vertex_group_limit_total(group_select_mode='BONE_DEFORM', limit=4)
    
    #Set to weight paint mode for normalize action
    bpy.ops.object.mode_set(mode = 'WEIGHT_PAINT')
    
    #Normalize all weights, do NOT lock active and only target deform groups
    bpy.ops.object.vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)

    #Set to edit mode for triangulation
    bpy.ops.object.mode_set(mode = 'EDIT')
    
    #Triangulate mesh (make every model's vert count divisible by 4), using beauty methods
    bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')    

    #Delete loose verts, if you edited the model at all
    bpy.ops.mesh.delete_loose()
    
    #Swapping back to object mode to apply transforms
    bpy.ops.object.mode_set(mode = 'OBJECT')

    #And applying transforms. All done!
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    
    #Will output the names of all the meshes that were affected. Simply remove the comment before if you'd like to use.
    #print(obj.name + " done!")

    
