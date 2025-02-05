# SPE11 Geometry Files


## SPE11-C (`make_spe11c.py`)

This is a generator script for producing the geometry of the SPE11 variant C. It makes use of the Python API of `gmsh`, and thus,
you need to have `python` and the `gmsh` Python package available. The latter can simply be installed via `pip` with
`pip install gmsh`.

The script takes the `spe11b.geo` file and rotates and extrudes the geometry according to the description of variant C. After
successful execution, the script produces the file `spe11c.geo` (and `spe11c.brep`, which is included internally).
The script also takes a runtime argument `mesh-size` that controls the mesh size to be used at all points of the resulting geometry:

```bash
# generates spe11c.geo with a characteristic mesh size of 250m to be used around all points
python3 make_spe11c_geo.py --mesh-size 250
```


## Structured grid generation (`make_structured_mesh.py`)

__Important__: for the variants A & B, keep in mind that the geometries are defined in the x-y plane instead of the x-z plane
used in the description. See the above sections for more details.

If you need a structured mesh for your simulator, you may use this script to generate a `.msh` file containing a structured mesh
including the facies indices that all elements of the mesh belong to. The script takes the SPE variant and the resolution as
runtime arguments. That is, to generate structured meshes for all three variants, you can use the script in the following way:

```bash
# generate a 200x200 mesh for variant A in the file spe11a_structured.msh
python3 make_structured_mesh.py --variant A -nx 200 -ny 200
# generate a 200x200 mesh for variant B in the file spe11b_structured.msh
python3 make_structured_mesh.py --variant B -nx 200 -ny 200
# generate a 200x200x200 mesh for variant C in the file spe11c_structured.msh
python3 make_structured_mesh.py --variant C -nx 200 -ny 200 -nz 200
```

Note that this script also requires the Python API of `gmsh`. Furthermore, passing the flag `--remove-cells-in-facies-7` creates
mesh files in which the cells in all regions of facies 7 are removed.

