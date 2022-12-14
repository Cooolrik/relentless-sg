# relentless-sg - Persistent data scene graph. Copyright (c) 2022 Ulrik Lindahl
# Licensed under the MIT license https://github.com/Cooolrik/relentless-sg/blob/main/LICENSE

from EntitiesHelpers import *
from Versions import v1_0

v1_0.append(
    NewEntity(
        name = "SceneLayer", 
        
        dependencies = [ Dependency("NodeTransform", include_in_header = True),
                         Dependency("NodeGeometry", include_in_header = True) 
                         ],

        templates = [ Template("scene_graph", template = "DirectedGraph", types = ["item_ref"], flags = ["Acyclic","Rooted"]),
                      Template("nodes_name", template = "BidirectionalMap", types = ["item_ref","string"] ),
                      Template("nodes_transform", template = "ItemTable", types = ["item_ref","NodeTransform"] ),
                      Template("nodes_geometry", template = "ItemTable", types = ["item_ref","NodeGeometry"] ) 
                      ],

        variables = [ Variable("scene_graph" , "Graph"),
                      Variable("nodes_name" , "Nodes"),
                      Variable("nodes_transform" , "Transforms"),
                      Variable("nodes_geometry" , "Geometries") 
                      ],

        validations = [ ValidateAllKeysAreInTable("Graph","Nodes"),
                        ValidateAllKeysAreInTable("Transforms","Nodes"),
                        ValidateAllKeysAreInTable("Geometries","Nodes")
                        ]
        )
    )
