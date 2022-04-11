# CarlosScript
Script to perform various mesh cleanup before attempting to export using Carlos' Smush Blender plugin. Includes:  
Limit Totals  
Clean Weights (Remove Zero-Weights)  
Normalize All  
Triangulate Mesh  
Apply Transforms  
All you need to do is open the file in Blender's scripting tab, select each mesh you'd like to affect, and run the script.
As of right now, it seems the for each function does not work. At least, it does not fix issues in crossmod. So, you'll need to select a mesh, run the script, and repeat for each mesh you need cleaned until I get some free time to fix it. Sorry about that! 
Keep in mind you need to have each mesh SELECTED, and they will also need Vertex Groups and an Armature in order for the script to not error.  
Feel free to ping/DM me at Siroos#8829 on Discord if there any any bugs/suggestions you have. 
