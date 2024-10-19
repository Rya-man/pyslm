import numpy as np
from stl import mesh

def create_rectangular_plane_stl(width: float, height: float, filename: str):
    # Define the 4 vertices of the rectangle
    vertices = np.array([
        [0, 0, 0],         # Vertex 1
        [width, 0, 0],     # Vertex 2
        [width, height, 0],# Vertex 3
        [0, height, 0],    # Vertex 4
    ])

    # Define 2 faces (2 triangles) to represent the rectangular plane
    faces = np.array([
        [0, 1, 2],  # Triangle 1
        [0, 2, 3],  # Triangle 2
    ])

    # Create the mesh object
    plane_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

    # Populate the mesh with the vertices and faces
    for i, face in enumerate(faces):
        for j in range(3):
            plane_mesh.vectors[i][j] = vertices[face[j], :]

    # Write to an STL file
    plane_mesh.save(filename)
    print(f"STL file saved as: {filename}")

# Example usage:
create_rectangular_plane_stl(width=10, height=5, filename='../models/rectangular_plane.stl')

