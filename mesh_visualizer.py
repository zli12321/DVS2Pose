import numpy as np
import open3d as o3d
import os

# sphere_mesh = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
def rotate_around(vis, mesh):
    # We create a 3D rotation matrix from x,y,z rotations, the rotations need to be given in radians
    R = mesh.get_rotation_matrix_from_xyz((0, np.deg2rad(2), 0))
    # The rotation matrix is applied to the specified object - in our case the mesh. We can also specify the rotation pivot center
    mesh.rotate(R, center=(0, 0, 0))

    # We create a 3D rotation matrix for the sphere as well in the opposite direction
    R_sphere = sphere_mesh.get_rotation_matrix_from_xyz((0, np.deg2rad(-4), 0))
    # Apply it
    sphere_mesh.rotate(R_sphere, center=(0, 0, 0))
    # For the changes to be seen we need to update both the geometry that has been changed and to update the whole renderer connected to the visualizer
    vis.update_geometry(mesh)
    vis.update_geometry(sphere_mesh)
    vis.update_renderer()

# entries = os.listdir('result/vis')
# mesh_path = entries[1]
# def visualizing_mesh(mesh):
mesh_path = 'pose2mesh_mesh/training_mesh500.obj'

mesh = o3d.io.read_triangle_mesh(mesh_path,True)
vis = o3d.visualization.Visualizer()
vis.create_window(window_name='Angel Visualize', width=800, height=600)
vis.add_geometry(mesh)

sphere_mesh = o3d.geometry.TriangleMesh.create_sphere(radius=0.05)
sphere_mesh.compute_vertex_normals()
vis.add_geometry(sphere_mesh)
sphere_mesh.translate((1, 0, 0))

# vis.register_animation_callback(rotate_around)

vis.run()
vis.destroy_window()