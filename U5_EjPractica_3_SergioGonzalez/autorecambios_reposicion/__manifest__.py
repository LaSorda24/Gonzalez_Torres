# -*- coding: utf-8 -*-
{
    "name": "AutoRecambios Reposicion",
    "version": "18.0.1.0.0",
    "summary": "Gestion de solicitudes internas de reposicion de recambios",
    "description": """
Modulo para gestionar solicitudes internas de reposicion en AutoRecambios Medina.

Permite registrar necesidades de stock, calcular el coste estimado y
gestionar el flujo borrador -> confirmado -> finalizado.
""",
    "author": "Sergio Gonzalez",
    "category": "Inventory",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/reposicion_views.xml",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
