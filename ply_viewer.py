from plyfile import PlyData

plydata = PlyData.read('D:\Glossy-GS\output\dataset\point_cloud\iteration_7000\point_cloud.ply')

print("Properties in the PLY file:")
for property in plydata.elements[0].properties:
    print(property.name)
