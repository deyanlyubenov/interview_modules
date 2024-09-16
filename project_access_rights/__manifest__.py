{
    'name': 'Project Access Rights',
    'version': '16.0.0.1',
    'depends': ['project'],
    'category': 'Services/Project',
    'author': 'Deyan Lyubenov',
    'description': """
        Adds a new user group for accessing project configuration and reports,
        without having full access to all projects.
    """,
    'data': [
        'security/project_security.xml',
        'security/project_ir_rules.xml',
        'security/ir.model.access.csv',
    ],
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': False,
}
