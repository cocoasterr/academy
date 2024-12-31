{
    "name":"Hospital Management System",
    "version": "1.0",
    "depends": [
        "base",
        "board",
    ], #list addons yang dibutuhkan pada custom addons
    "author": "Idoo",
    "category": "Education",
    'license': 'LGPL-3', 
    "website": "https://www.idoo.com",# nama website jika publish
    "description": 
        """
        Hospital Management System
        """,
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patients.xml",
        ],# data data yang akan di insert ke database jika addons ini di install
    "installable": True, # apakah addons ini bisa di install atau tidak
    "auto_install": False, # apakah addons ini akan di install secara otomatis
    "application": True, # apakah addons ini merupakan aplikasi atau tidak   
}