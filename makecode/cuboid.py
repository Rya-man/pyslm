import numpy as np
from stl import mesh

def create_cuboid(width, height, depth, filename='cuboid.stl'):
    # Define the 8 vertices of the cuboid
    vertices = np.array([
        [0, 0, 0],  # Bottom-front-left
        [width, 0, 0],  # Bottom-front-right
        [width, depth, 0],  # Bottom-back-right
        [0, depth, 0],  # Bottom-back-left
        [0, 0, height],  # Top-front-left
        [width, 0, height],  # Top-front-right
        [width, depth, height],  # Top-back-right
        [0, depth, height]  # Top-back-left
    ])

    # Define the 12 triangles (2 triangles per rectangular face)
    faces = np.array([
        # Bottom face
        [0, 3, 1],
        [1, 3, 2],
        
        # Top face
        [4, 5, 7],
        [5, 6, 7],
        
        # Front face
        [0, 1, 4],
        [1, 5, 4],
        
        # Back face
        [2, 3, 6],
        [3, 7, 6],
        
        # Left face
        [0, 4, 3],
        [3, 4, 7],
        
        # Right face
        [1, 2, 5],
        [2, 6, 5]
    ])

    # Create the mesh
    cuboid_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    for i, face in enumerate(faces):
        for j in range(3):
            cuboid_mesh.vectors[i][j] = vertices[face[j], :]

    # Save the mesh to file
    cuboid_mesh.save(filename)
    print(f"Cuboid saved to {filename}")

# Example: Create a cuboid with width=10, height=20, depth=15
print("Enter the x y and z values for the cuboid")
x = float(input())
y= float(input())
z = float(input())
create_cuboid(x,y,z,"../models/cuboid.stl")

