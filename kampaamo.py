import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Service,ServiceTimetable,ServiceRegistration, HairdresserService, Feedback

app = create_app(os.getenv('HIUSMAGIA_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Service=Service, ServiceTimetable=ServiceTimetable, ServiceRegistration=ServiceRegistration,HairdresserService=HairdresserService, Feedback=Feedback)


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
