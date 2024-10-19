import vtk

def visualize_stl_with_vtk(filename: str):
    # Create a reader for the STL file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)

    # Create a mapper and actor for rendering
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Set up the renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(0.1, 0.1, 0.1)  # Background color dark gray

    # Start the visualization
    renderWindow.Render()
    renderWindowInteractor.Start()

# Example usage:
file = input("ENter the file name\t")
visualize_stl_with_vtk(file)

