import os
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

from application import create_app, db, register_blueprints
from application.models.tagger.models import Entity2Label, Relation2Label
from application.models.graph.schema_models import EntityClass, ObjectProperty, DataProperty


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
register_blueprints(app)
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, 
        Entity2Label=Entity2Label, 
        Relation2Label=Relation2Label,
        EntityClass=EntityClass,
        ObjectProperty=ObjectProperty,
        DataProperty=DataProperty)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(use_debugger=False, host='0.0.0.0'))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
   manager.run()
