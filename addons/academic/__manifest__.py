{
    "name": "Academic Information System v.1.0",
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
        Custom addons for education
        """,
    "data": [
        "wizard/create_attendee.xml",
        "security/groups.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "course.xml",
        "session.xml",
        "attendee.xml",
        "partner.xml",
        "reports/session.xml",
        "dashboard.xml",
    ],# data data yang akan di insert ke database jika addons ini di install
    "installable": True, # apakah addons ini bisa di install atau tidak
    "auto_install": False, # apakah addons ini akan di install secara otomatis
    "application": True, # apakah addons ini merupakan aplikasi atau tidak
}