#import numpy as np
import open3d as o3d

# obj面片显示
textured_mesh= o3d.io.read_triangle_mesh('demo/kitti_000008/kitti_000008_points.obj')
print(textured_mesh)
textured_mesh.compute_vertex_normals()
textured_mesh1= o3d.io.read_triangle_mesh('demo/kitti_000008/kitti_000008_pred.obj')
print(textured_mesh1)
textured_mesh1.compute_vertex_normals()
o3d.visualization.draw_geometries([textured_mesh, textured_mesh1], window_name="Open3D")

# # obj顶点显示
# pcobj = o3d.geometry.PointCloud()
# pcobj.points = o3d.utility.Vector3dVector(textured_mesh.vertices)
# o3d.visualization.draw_geometries([pcobj], window_name="Open3D2")

# # obj顶点转array
# textured_pc =np.asarray(textured_mesh.vertices)
# print(textured_pc)
